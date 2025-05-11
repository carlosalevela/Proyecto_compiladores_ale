# Generated from CSVQueryDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSVQueryDSLParser import CSVQueryDSLParser
else:
    from CSVQueryDSLParser import CSVQueryDSLParser

# This class defines a complete listener for a parse tree produced by CSVQueryDSLParser.
class CSVQueryDSLListener(ParseTreeListener):

    # Enter a parse tree produced by CSVQueryDSLParser#prog.
    def enterProg(self, ctx:CSVQueryDSLParser.ProgContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#prog.
    def exitProg(self, ctx:CSVQueryDSLParser.ProgContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#stat.
    def enterStat(self, ctx:CSVQueryDSLParser.StatContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#stat.
    def exitStat(self, ctx:CSVQueryDSLParser.StatContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#loadStat.
    def enterLoadStat(self, ctx:CSVQueryDSLParser.LoadStatContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#loadStat.
    def exitLoadStat(self, ctx:CSVQueryDSLParser.LoadStatContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#filterStat.
    def enterFilterStat(self, ctx:CSVQueryDSLParser.FilterStatContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#filterStat.
    def exitFilterStat(self, ctx:CSVQueryDSLParser.FilterStatContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#filterExprList.
    def enterFilterExprList(self, ctx:CSVQueryDSLParser.FilterExprListContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#filterExprList.
    def exitFilterExprList(self, ctx:CSVQueryDSLParser.FilterExprListContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#filterExpr.
    def enterFilterExpr(self, ctx:CSVQueryDSLParser.FilterExprContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#filterExpr.
    def exitFilterExpr(self, ctx:CSVQueryDSLParser.FilterExprContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#aggregateStat.
    def enterAggregateStat(self, ctx:CSVQueryDSLParser.AggregateStatContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#aggregateStat.
    def exitAggregateStat(self, ctx:CSVQueryDSLParser.AggregateStatContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#aggregateFunction.
    def enterAggregateFunction(self, ctx:CSVQueryDSLParser.AggregateFunctionContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#aggregateFunction.
    def exitAggregateFunction(self, ctx:CSVQueryDSLParser.AggregateFunctionContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#printStat.
    def enterPrintStat(self, ctx:CSVQueryDSLParser.PrintStatContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#printStat.
    def exitPrintStat(self, ctx:CSVQueryDSLParser.PrintStatContext):
        pass


    # Enter a parse tree produced by CSVQueryDSLParser#value.
    def enterValue(self, ctx:CSVQueryDSLParser.ValueContext):
        pass

    # Exit a parse tree produced by CSVQueryDSLParser#value.
    def exitValue(self, ctx:CSVQueryDSLParser.ValueContext):
        pass



del CSVQueryDSLParser