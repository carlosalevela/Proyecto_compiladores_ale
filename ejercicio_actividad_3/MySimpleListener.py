from SimpleListener import SimpleListener

class MySimpleListener(SimpleListener):
    def enterClassDef(self, ctx):
        print(f"📦 Clase encontrada: {ctx.ID().getText()}")

    def enterMember(self, ctx):
        if len(ctx.children) == 3:
            print(f"   🧾 Variable: {ctx.ID().getText()}")
        else:
            print(f"   🔧 Método: {ctx.ID(0).getText()}({ctx.ID(1).getText()})")

    def enterStat(self, ctx):
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == "=":
            print(f"      📌 Asignación: {ctx.ID().getText()} = ...")
