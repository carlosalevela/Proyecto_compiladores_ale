from MiGramaticaVisitor import MiGramaticaVisitor
from MiGramaticaParser import MiGramaticaParser

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.memory = {}  # Tabla de símbolos

    def visitPrograma(self, ctx: MiGramaticaParser.ProgramaContext):
        print("Ejecutando el programa...")
        return self.visitChildren(ctx)

    def visitAssign(self, ctx: MiGramaticaParser.AsignacionContext):
        var_name = ctx.ID().getText()
        expr_value = self.visit(ctx.expresion())

    # Convertir el valor a entero si es posible
        if isinstance(expr_value, str) and expr_value.isdigit():
            expr_value = int(expr_value)

        self.memory[var_name] = expr_value  # Guardar el valor en memoria
        print(f"Asignando {var_name} = {expr_value}")
        return expr_value

    def visitForLoop(self, ctx: MiGramaticaParser.ForLoopContext):
        print("Ejecutando bucle FOR...")

    # Inicialización
        self.visit(ctx.asignacion(0))  # i = 0

    # Condición
        condicion = ctx.condicion()
    
        while self.visit(condicion):  # Mientras la condición sea verdadera
            for sentencia in ctx.sentencia():  # Ejecutar el cuerpo del for
                self.visit(sentencia)

        # Actualización de la variable del for
            self.visit(ctx.asignacion(1))  # i = i + 1

        # Recalcular la condición después de actualizar i
            condicion = ctx.condicion()

    def visitCondicion(self, ctx: MiGramaticaParser.CondicionContext):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.op.text

        if op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right

    def visitAddSub(self, ctx: MiGramaticaParser.ExpresionContext):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))

        # Asegurar que sean enteros
        left = int(left) if isinstance(left, str) and left.isdigit() else left
        right = int(right) if isinstance(right, str) and right.isdigit() else right

        return left + right if ctx.op.text == '+' else left - right

    def visitMulDiv(self, ctx: MiGramaticaParser.ExpresionContext):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))

        # Asegurar que sean enteros
        left = int(left) if isinstance(left, str) and left.isdigit() else left
        right = int(right) if isinstance(right, str) and right.isdigit() else right

        return left * right if ctx.op.text == '*' else left / right

    def visitInt(self, ctx: MiGramaticaParser.ExpresionContext):
        return int(ctx.INT().getText())

    def visitVariable(self, ctx: MiGramaticaParser.ExpresionContext):
        var_name = ctx.ID().getText()
        return self.memory.get(var_name, 0)  # Retorna 0 si la variable no está definida