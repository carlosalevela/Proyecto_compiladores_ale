import csv
from CSVFilterVisitor import CSVFilterVisitor

class MyCSVVisitor(CSVFilterVisitor):
    def __init__(self):
        self.data = []
        self.filtered_data = []
        self.filename = ""
        self.filtros = []

    def visitLoadStat(self, ctx):
        self.filename = ctx.STRING().getText().replace('"', '')
        with open(self.filename, newline='') as f:
            self.data = list(csv.DictReader(f))
        self.filtered_data = self.data
        return None

    def visitFilterStat(self, ctx):
        column = ctx.STRING().getText().replace('"', '')
        op = ctx.OPERATOR().getText()
        value = float(ctx.NUMBER().getText())

        self.filtered_data = [
            row for row in self.filtered_data
            if eval(f"{float(row[column])} {op} {value}")
        ]
        return None

    def visitPrintStat(self, ctx):
        for row in self.filtered_data:
            print(row)
        return None

    def visitCountStat(self, ctx):
        column = ctx.STRING().getText().replace('"', '')
        op = ctx.OPERATOR().getText()
        value = float(ctx.NUMBER().getText())

        conteo = sum(
            1 for row in self.data
            if eval(f"{float(row[column])} {op} {value}")
        )

        print(f"👤 Personas con {column} {op} {value}: {conteo}")
        return None  # <-- Este estaba fuera de la función

    def visitCountBetweenStat(self, ctx):
        column = ctx.STRING().getText().replace('"', '')
        inferior = float(ctx.NUMBER(0).getText())
        superior = float(ctx.NUMBER(1).getText())

        self.filtered_data = [
            row for row in self.data
            if inferior <= float(row[column]) <= superior
        ]

        conteo = len(self.filtered_data)

        print(f"👤 Personas con {column} entre {inferior} y {superior}: {conteo}")
        return None
