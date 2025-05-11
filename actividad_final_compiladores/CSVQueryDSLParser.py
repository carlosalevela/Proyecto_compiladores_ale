# Generated from CSVQueryDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,
        43,8,4,10,4,12,4,46,9,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        1,6,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,
        18,0,2,1,0,6,8,1,0,12,13,60,0,21,1,0,0,0,2,29,1,0,0,0,4,31,1,0,0,
        0,6,35,1,0,0,0,8,39,1,0,0,0,10,47,1,0,0,0,12,52,1,0,0,0,14,58,1,
        0,0,0,16,60,1,0,0,0,18,63,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,
        23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,1,1,0,0,0,25,30,3,4,2,
        0,26,30,3,6,3,0,27,30,3,12,6,0,28,30,3,16,8,0,29,25,1,0,0,0,29,26,
        1,0,0,0,29,27,1,0,0,0,29,28,1,0,0,0,30,3,1,0,0,0,31,32,5,1,0,0,32,
        33,5,12,0,0,33,34,5,2,0,0,34,5,1,0,0,0,35,36,5,3,0,0,36,37,3,8,4,
        0,37,38,5,2,0,0,38,7,1,0,0,0,39,44,3,10,5,0,40,41,5,11,0,0,41,43,
        3,10,5,0,42,40,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,
        45,9,1,0,0,0,46,44,1,0,0,0,47,48,5,4,0,0,48,49,5,12,0,0,49,50,5,
        10,0,0,50,51,3,18,9,0,51,11,1,0,0,0,52,53,5,5,0,0,53,54,3,14,7,0,
        54,55,5,4,0,0,55,56,5,12,0,0,56,57,5,2,0,0,57,13,1,0,0,0,58,59,7,
        0,0,0,59,15,1,0,0,0,60,61,5,9,0,0,61,62,5,2,0,0,62,17,1,0,0,0,63,
        64,7,1,0,0,64,19,1,0,0,0,3,23,29,44
    ]

class CSVQueryDSLParser ( Parser ):

    grammarFileName = "CSVQueryDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "';'", "'filter'", "'column'", 
                     "'aggregate'", "'count'", "'sum'", "'average'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "OPERATOR", "LOGICAL_OP", 
                      "STRING", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_loadStat = 2
    RULE_filterStat = 3
    RULE_filterExprList = 4
    RULE_filterExpr = 5
    RULE_aggregateStat = 6
    RULE_aggregateFunction = 7
    RULE_printStat = 8
    RULE_value = 9

    ruleNames =  [ "prog", "stat", "loadStat", "filterStat", "filterExprList", 
                   "filterExpr", "aggregateStat", "aggregateFunction", "printStat", 
                   "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    OPERATOR=10
    LOGICAL_OP=11
    STRING=12
    NUMBER=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVQueryDSLParser.StatContext)
            else:
                return self.getTypedRuleContext(CSVQueryDSLParser.StatContext,i)


        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CSVQueryDSLParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.stat()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 554) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadStat(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.LoadStatContext,0)


        def filterStat(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.FilterStatContext,0)


        def aggregateStat(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.AggregateStatContext,0)


        def printStat(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.PrintStatContext,0)


        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = CSVQueryDSLParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.loadStat()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.filterStat()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.aggregateStat()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.printStat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CSVQueryDSLParser.STRING, 0)

        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_loadStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadStat" ):
                listener.enterLoadStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadStat" ):
                listener.exitLoadStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStat" ):
                return visitor.visitLoadStat(self)
            else:
                return visitor.visitChildren(self)




    def loadStat(self):

        localctx = CSVQueryDSLParser.LoadStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(CSVQueryDSLParser.T__0)
            self.state = 32
            self.match(CSVQueryDSLParser.STRING)
            self.state = 33
            self.match(CSVQueryDSLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filterExprList(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.FilterExprListContext,0)


        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_filterStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterStat" ):
                listener.enterFilterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterStat" ):
                listener.exitFilterStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterStat" ):
                return visitor.visitFilterStat(self)
            else:
                return visitor.visitChildren(self)




    def filterStat(self):

        localctx = CSVQueryDSLParser.FilterStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(CSVQueryDSLParser.T__2)
            self.state = 36
            self.filterExprList()
            self.state = 37
            self.match(CSVQueryDSLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filterExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVQueryDSLParser.FilterExprContext)
            else:
                return self.getTypedRuleContext(CSVQueryDSLParser.FilterExprContext,i)


        def LOGICAL_OP(self, i:int=None):
            if i is None:
                return self.getTokens(CSVQueryDSLParser.LOGICAL_OP)
            else:
                return self.getToken(CSVQueryDSLParser.LOGICAL_OP, i)

        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_filterExprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterExprList" ):
                listener.enterFilterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterExprList" ):
                listener.exitFilterExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterExprList" ):
                return visitor.visitFilterExprList(self)
            else:
                return visitor.visitChildren(self)




    def filterExprList(self):

        localctx = CSVQueryDSLParser.FilterExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_filterExprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.filterExpr()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 40
                self.match(CSVQueryDSLParser.LOGICAL_OP)
                self.state = 41
                self.filterExpr()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CSVQueryDSLParser.STRING, 0)

        def OPERATOR(self):
            return self.getToken(CSVQueryDSLParser.OPERATOR, 0)

        def value(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.ValueContext,0)


        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_filterExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterExpr" ):
                listener.enterFilterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterExpr" ):
                listener.exitFilterExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterExpr" ):
                return visitor.visitFilterExpr(self)
            else:
                return visitor.visitChildren(self)




    def filterExpr(self):

        localctx = CSVQueryDSLParser.FilterExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_filterExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(CSVQueryDSLParser.T__3)
            self.state = 48
            self.match(CSVQueryDSLParser.STRING)
            self.state = 49
            self.match(CSVQueryDSLParser.OPERATOR)
            self.state = 50
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggregateFunction(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.AggregateFunctionContext,0)


        def STRING(self):
            return self.getToken(CSVQueryDSLParser.STRING, 0)

        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_aggregateStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateStat" ):
                listener.enterAggregateStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateStat" ):
                listener.exitAggregateStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateStat" ):
                return visitor.visitAggregateStat(self)
            else:
                return visitor.visitChildren(self)




    def aggregateStat(self):

        localctx = CSVQueryDSLParser.AggregateStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_aggregateStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(CSVQueryDSLParser.T__4)
            self.state = 53
            self.aggregateFunction()
            self.state = 54
            self.match(CSVQueryDSLParser.T__3)
            self.state = 55
            self.match(CSVQueryDSLParser.STRING)
            self.state = 56
            self.match(CSVQueryDSLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_aggregateFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateFunction" ):
                listener.enterAggregateFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateFunction" ):
                listener.exitAggregateFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateFunction" ):
                return visitor.visitAggregateFunction(self)
            else:
                return visitor.visitChildren(self)




    def aggregateFunction(self):

        localctx = CSVQueryDSLParser.AggregateFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_aggregateFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_printStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStat" ):
                listener.enterPrintStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStat" ):
                listener.exitPrintStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)




    def printStat(self):

        localctx = CSVQueryDSLParser.PrintStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(CSVQueryDSLParser.T__8)
            self.state = 61
            self.match(CSVQueryDSLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CSVQueryDSLParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(CSVQueryDSLParser.STRING, 0)

        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = CSVQueryDSLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





