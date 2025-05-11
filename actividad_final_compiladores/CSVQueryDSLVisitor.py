# Generated from CSVQueryDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSVQueryDSLParser import CSVQueryDSLParser
else:
    from CSVQueryDSLParser import CSVQueryDSLParser

# This class defines a complete generic visitor for a parse tree produced by CSVQueryDSLParser.

class CSVQueryDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSVQueryDSLParser#prog.
    def visitProg(self, ctx:CSVQueryDSLParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#stat.
    def visitStat(self, ctx:CSVQueryDSLParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#loadStat.
    def visitLoadStat(self, ctx:CSVQueryDSLParser.LoadStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#filterStat.
    def visitFilterStat(self, ctx:CSVQueryDSLParser.FilterStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#filterExprList.
    def visitFilterExprList(self, ctx:CSVQueryDSLParser.FilterExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#filterExpr.
    def visitFilterExpr(self, ctx:CSVQueryDSLParser.FilterExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#aggregateStat.
    def visitAggregateStat(self, ctx:CSVQueryDSLParser.AggregateStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#aggregateFunction.
    def visitAggregateFunction(self, ctx:CSVQueryDSLParser.AggregateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#printStat.
    def visitPrintStat(self, ctx:CSVQueryDSLParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVQueryDSLParser#value.
    def visitValue(self, ctx:CSVQueryDSLParser.ValueContext):
        return self.visitChildren(ctx)



del CSVQueryDSLParser