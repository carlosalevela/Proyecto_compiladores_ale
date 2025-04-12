# Generated from Simple.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleParser import SimpleParser
else:
    from SimpleParser import SimpleParser

# This class defines a complete listener for a parse tree produced by SimpleParser.
class SimpleListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleParser#prog.
    def enterProg(self, ctx:SimpleParser.ProgContext):
        pass

    # Exit a parse tree produced by SimpleParser#prog.
    def exitProg(self, ctx:SimpleParser.ProgContext):
        pass


    # Enter a parse tree produced by SimpleParser#classDef.
    def enterClassDef(self, ctx:SimpleParser.ClassDefContext):
        pass

    # Exit a parse tree produced by SimpleParser#classDef.
    def exitClassDef(self, ctx:SimpleParser.ClassDefContext):
        pass


    # Enter a parse tree produced by SimpleParser#member.
    def enterMember(self, ctx:SimpleParser.MemberContext):
        pass

    # Exit a parse tree produced by SimpleParser#member.
    def exitMember(self, ctx:SimpleParser.MemberContext):
        pass


    # Enter a parse tree produced by SimpleParser#stat.
    def enterStat(self, ctx:SimpleParser.StatContext):
        pass

    # Exit a parse tree produced by SimpleParser#stat.
    def exitStat(self, ctx:SimpleParser.StatContext):
        pass


    # Enter a parse tree produced by SimpleParser#FuncCall.
    def enterFuncCall(self, ctx:SimpleParser.FuncCallContext):
        pass

    # Exit a parse tree produced by SimpleParser#FuncCall.
    def exitFuncCall(self, ctx:SimpleParser.FuncCallContext):
        pass


    # Enter a parse tree produced by SimpleParser#Var.
    def enterVar(self, ctx:SimpleParser.VarContext):
        pass

    # Exit a parse tree produced by SimpleParser#Var.
    def exitVar(self, ctx:SimpleParser.VarContext):
        pass


    # Enter a parse tree produced by SimpleParser#Parens.
    def enterParens(self, ctx:SimpleParser.ParensContext):
        pass

    # Exit a parse tree produced by SimpleParser#Parens.
    def exitParens(self, ctx:SimpleParser.ParensContext):
        pass


    # Enter a parse tree produced by SimpleParser#MultiDiv.
    def enterMultiDiv(self, ctx:SimpleParser.MultiDivContext):
        pass

    # Exit a parse tree produced by SimpleParser#MultiDiv.
    def exitMultiDiv(self, ctx:SimpleParser.MultiDivContext):
        pass


    # Enter a parse tree produced by SimpleParser#Int.
    def enterInt(self, ctx:SimpleParser.IntContext):
        pass

    # Exit a parse tree produced by SimpleParser#Int.
    def exitInt(self, ctx:SimpleParser.IntContext):
        pass


    # Enter a parse tree produced by SimpleParser#SumaResta.
    def enterSumaResta(self, ctx:SimpleParser.SumaRestaContext):
        pass

    # Exit a parse tree produced by SimpleParser#SumaResta.
    def exitSumaResta(self, ctx:SimpleParser.SumaRestaContext):
        pass



del SimpleParser