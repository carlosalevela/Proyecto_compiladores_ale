import csv
from CSVQueryDSLVisitor import CSVQueryDSLVisitor

class MyCSVVisitor(CSVQueryDSLVisitor):
    def __init__(self):
        self.filename = ""
        self.data = []
        self.filters = []  # Lista de funciones lambda compuestas
        self.aggregations = []  # Tuplas: ('count', 'columna')
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
        condition_fn = self.visit(ctx.filterExprList())
        self.filters.append(condition_fn)
        return None

    def visitFilterExprList(self, ctx):
        return self.visit(ctx.filterOrExpr())

    def visitFilterOrExpr(self, ctx):
        conditions = [self.visit(child) for child in ctx.filterAndExpr()]
        return lambda row: any(cond(row) for cond in conditions)

    def visitFilterAndExpr(self, ctx):
        conditions = [self.visit(child) for child in ctx.filterAtom()]
        return lambda row: all(cond(row) for cond in conditions)

    def visitFilterAtom(self, ctx):
        if ctx.filterExpr():
            return self.visit(ctx.filterExpr())
        else:
            return self.visit(ctx.filterOrExpr())

    def visitFilterExpr(self, ctx):
        column = ctx.STRING().getText().replace('"', '')
        operator = ctx.OPERATOR().getText()
        value_text = ctx.value().getText().strip('"')

        def condition(row, col=column, op=operator, val=value_text):
            left = row[col]
            try:
                left = float(left)
                val = float(val)
            except ValueError:
                pass  # mantener como string
            return eval(f"left {op} val")

        return condition

    def visitAggregateStat(self, ctx):
        func = ctx.aggregateFunction().getText()
        column = ctx.STRING().getText().replace('"', '')
        self.aggregations.append((func, column))
        return None

    def visitPrintStat(self, ctx):
        current_data = self.data

        if self.filters:
            current_data = [row for row in self.data if all(f(row) for f in self.filters)]

        self.filtered_data = current_data

        if not self.filtered_data:
            print("⚠️ No se encontraron resultados para los filtros aplicados.")

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

        if not self.aggregations:
            for row in self.filtered_data:
                print(row)

        # Resetear filtros y agregaciones para el siguiente script
        self.filters = []
        self.aggregations = []
        return None
