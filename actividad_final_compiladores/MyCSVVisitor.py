import csv
from CSVQueryDSLVisitor import CSVQueryDSLVisitor

class MyCSVVisitor(CSVQueryDSLVisitor):
    def __init__(self):
        self.filename = ""
        self.data = []
        self.filters = []  # lista de funciones lambda
        self.aggregations = []  # tuplas: ('count', 'column_name')
        self.filtered_data = []

    def visitLoadStat(self, ctx):
        self.filename = ctx.STRING().getText().replace('"', '')
        with open(self.filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            reader.fieldnames[0] = reader.fieldnames[0].lstrip('\ufeff')
            self.data = [dict((k.strip(), v) for k, v in row.items()) for row in reader]
            self.filtered_data = self.data.copy()

        print("✅ Columnas cargadas:", list(self.data[0].keys()))
        return None

    def visitFilterStat(self, ctx):
        for expr in ctx.filterExprList().children:
            if expr.getText() in ('AND', 'OR'):
                self.filters.append(expr.getText())
            elif expr.getText().startswith('column'):
                column = expr.STRING().getText().replace('"', '')
                op = expr.OPERATOR().getText()
                value_text = expr.value().getText().strip('"')

                def filter_fn(row, col=column, o=op, val=value_text):
                    left = row[col]
                    try:
                        left = float(left)
                        val = float(val)
                    except ValueError:
                        pass  # keep as string
                    return eval(f"left {o} val")

                self.filters.append(filter_fn)
        return None

    def visitAggregateStat(self, ctx):
        func = ctx.aggregateFunction().getText()
        column = ctx.STRING().getText().replace('"', '')
        self.aggregations.append((func, column))
        return None

    def visitPrintStat(self, ctx):
        # Aplicar filtros acumulados
        current_data = self.data

        # Construir lógica con AND/OR entre funciones
        temp = []
        op = None
        for item in self.filters:
            if callable(item):
                temp.append(item)
            elif item in ("AND", "OR"):
                op = item

        if len(temp) > 0:
            if op == "OR":
                current_data = [row for row in self.data if any(f(row) for f in temp)]
            else:  # default AND
                current_data = [row for row in self.data if all(f(row) for f in temp)]

        self.filtered_data = current_data

        if not self.filtered_data:
            print("⚠️ No se encontraron resultados para los filtros aplicados.")

        # Ejecutar agregaciones
        for func, col in self.aggregations:
            try:
                values = [float(row[col]) for row in self.filtered_data if row[col]]
            except ValueError:
                values = [row[col] for row in self.filtered_data if row[col]]

            if func == 'count':
                print(f"Conteo de {col}: {len(values)}")
            elif func == 'sum':
                print(f"Suma de {col}: {sum(values)}")
            elif func == 'average':
                avg = sum(values) / len(values) if values else 0
                print(f"Promedio de {col}: {avg:.2f}")

        # Si no hay agregaciones, imprime los registros filtrados
        if not self.aggregations:
            for row in self.filtered_data:
                print(row)

        # Resetear para el próximo script
        self.filters = []
        self.aggregations = []
        return None
