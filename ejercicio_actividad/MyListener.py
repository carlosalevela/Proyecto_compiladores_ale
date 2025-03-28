from MiGramaticaListener import MiGramaticaListener
from MiGramaticaParser import MiGramaticaParser

class MyListener(MiGramaticaListener):
    def exitForStatement(self, ctx: MiGramaticaParser.ForStatementContext):
        print("Detectado un bucle FOR.")

    def exitCondicionSimple(self, ctx: MiGramaticaParser.CondicionSimpleContext):
        print(f"Condición detectada: {ctx.getText()}")

    def exitAssign(self, ctx: MiGramaticaParser.AssignContext):
        print(f"Asignación detectada: {ctx.getText()}")
