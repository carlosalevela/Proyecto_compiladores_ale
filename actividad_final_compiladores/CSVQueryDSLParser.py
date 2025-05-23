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
        4,1,18,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,5,5,51,8,5,10,5,12,5,54,9,5,1,
        6,1,6,1,6,5,6,59,8,6,10,6,12,6,62,9,6,1,7,1,7,1,7,1,7,1,7,3,7,69,
        8,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,11,1,
        11,1,11,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,
        0,2,1,0,10,12,1,0,16,17,82,0,27,1,0,0,0,2,35,1,0,0,0,4,37,1,0,0,
        0,6,41,1,0,0,0,8,45,1,0,0,0,10,47,1,0,0,0,12,55,1,0,0,0,14,68,1,
        0,0,0,16,70,1,0,0,0,18,75,1,0,0,0,20,81,1,0,0,0,22,83,1,0,0,0,24,
        86,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,
        0,29,30,1,0,0,0,30,1,1,0,0,0,31,36,3,4,2,0,32,36,3,6,3,0,33,36,3,
        18,9,0,34,36,3,22,11,0,35,31,1,0,0,0,35,32,1,0,0,0,35,33,1,0,0,0,
        35,34,1,0,0,0,36,3,1,0,0,0,37,38,5,1,0,0,38,39,5,16,0,0,39,40,5,
        2,0,0,40,5,1,0,0,0,41,42,5,3,0,0,42,43,3,8,4,0,43,44,5,2,0,0,44,
        7,1,0,0,0,45,46,3,10,5,0,46,9,1,0,0,0,47,52,3,12,6,0,48,49,5,4,0,
        0,49,51,3,12,6,0,50,48,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,
        1,0,0,0,53,11,1,0,0,0,54,52,1,0,0,0,55,60,3,14,7,0,56,57,5,5,0,0,
        57,59,3,14,7,0,58,56,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,
        0,0,0,61,13,1,0,0,0,62,60,1,0,0,0,63,69,3,16,8,0,64,65,5,6,0,0,65,
        66,3,10,5,0,66,67,5,7,0,0,67,69,1,0,0,0,68,63,1,0,0,0,68,64,1,0,
        0,0,69,15,1,0,0,0,70,71,5,8,0,0,71,72,5,16,0,0,72,73,5,14,0,0,73,
        74,3,24,12,0,74,17,1,0,0,0,75,76,5,9,0,0,76,77,3,20,10,0,77,78,5,
        8,0,0,78,79,5,16,0,0,79,80,5,2,0,0,80,19,1,0,0,0,81,82,7,0,0,0,82,
        21,1,0,0,0,83,84,5,13,0,0,84,85,5,2,0,0,85,23,1,0,0,0,86,87,7,1,
        0,0,87,25,1,0,0,0,5,29,35,52,60,68
    ]

class CSVQueryDSLParser ( Parser ):

    grammarFileName = "CSVQueryDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "';'", "'filter'", "'OR'", "'AND'", 
                     "'('", "')'", "'column'", "'aggregate'", "'count'", 
                     "'sum'", "'average'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "OPERATOR", "LOGICAL_OP", 
                      "STRING", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_loadStat = 2
    RULE_filterStat = 3
    RULE_filterExprList = 4
    RULE_filterOrExpr = 5
    RULE_filterAndExpr = 6
    RULE_filterAtom = 7
    RULE_filterExpr = 8
    RULE_aggregateStat = 9
    RULE_aggregateFunction = 10
    RULE_printStat = 11
    RULE_value = 12

    ruleNames =  [ "prog", "stat", "loadStat", "filterStat", "filterExprList", 
                   "filterOrExpr", "filterAndExpr", "filterAtom", "filterExpr", 
                   "aggregateStat", "aggregateFunction", "printStat", "value" ]

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
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    OPERATOR=14
    LOGICAL_OP=15
    STRING=16
    NUMBER=17
    WS=18

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
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.stat()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8714) != 0)):
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
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.loadStat()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.filterStat()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.aggregateStat()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
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
            self.state = 37
            self.match(CSVQueryDSLParser.T__0)
            self.state = 38
            self.match(CSVQueryDSLParser.STRING)
            self.state = 39
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
            self.state = 41
            self.match(CSVQueryDSLParser.T__2)
            self.state = 42
            self.filterExprList()
            self.state = 43
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

        def filterOrExpr(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.FilterOrExprContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.filterOrExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterOrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filterAndExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVQueryDSLParser.FilterAndExprContext)
            else:
                return self.getTypedRuleContext(CSVQueryDSLParser.FilterAndExprContext,i)


        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_filterOrExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterOrExpr" ):
                listener.enterFilterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterOrExpr" ):
                listener.exitFilterOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterOrExpr" ):
                return visitor.visitFilterOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def filterOrExpr(self):

        localctx = CSVQueryDSLParser.FilterOrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_filterOrExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.filterAndExpr()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 48
                self.match(CSVQueryDSLParser.T__3)
                self.state = 49
                self.filterAndExpr()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterAndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filterAtom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVQueryDSLParser.FilterAtomContext)
            else:
                return self.getTypedRuleContext(CSVQueryDSLParser.FilterAtomContext,i)


        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_filterAndExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterAndExpr" ):
                listener.enterFilterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterAndExpr" ):
                listener.exitFilterAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterAndExpr" ):
                return visitor.visitFilterAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def filterAndExpr(self):

        localctx = CSVQueryDSLParser.FilterAndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_filterAndExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.filterAtom()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 56
                self.match(CSVQueryDSLParser.T__4)
                self.state = 57
                self.filterAtom()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filterExpr(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.FilterExprContext,0)


        def filterOrExpr(self):
            return self.getTypedRuleContext(CSVQueryDSLParser.FilterOrExprContext,0)


        def getRuleIndex(self):
            return CSVQueryDSLParser.RULE_filterAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterAtom" ):
                listener.enterFilterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterAtom" ):
                listener.exitFilterAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterAtom" ):
                return visitor.visitFilterAtom(self)
            else:
                return visitor.visitChildren(self)




    def filterAtom(self):

        localctx = CSVQueryDSLParser.FilterAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_filterAtom)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.filterExpr()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(CSVQueryDSLParser.T__5)
                self.state = 65
                self.filterOrExpr()
                self.state = 66
                self.match(CSVQueryDSLParser.T__6)
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
        self.enterRule(localctx, 16, self.RULE_filterExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(CSVQueryDSLParser.T__7)
            self.state = 71
            self.match(CSVQueryDSLParser.STRING)
            self.state = 72
            self.match(CSVQueryDSLParser.OPERATOR)
            self.state = 73
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
        self.enterRule(localctx, 18, self.RULE_aggregateStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(CSVQueryDSLParser.T__8)
            self.state = 76
            self.aggregateFunction()
            self.state = 77
            self.match(CSVQueryDSLParser.T__7)
            self.state = 78
            self.match(CSVQueryDSLParser.STRING)
            self.state = 79
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
        self.enterRule(localctx, 20, self.RULE_aggregateFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
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
        self.enterRule(localctx, 22, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(CSVQueryDSLParser.T__12)
            self.state = 84
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
        self.enterRule(localctx, 24, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
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





