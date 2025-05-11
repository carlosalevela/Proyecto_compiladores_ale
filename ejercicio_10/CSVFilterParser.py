# Generated from CSVFilter.g4 by ANTLR 4.13.2
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
        4,1,12,57,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,0,0,7,0,
        2,4,6,8,10,12,0,0,54,0,15,1,0,0,0,2,24,1,0,0,0,4,26,1,0,0,0,6,30,
        1,0,0,0,8,37,1,0,0,0,10,44,1,0,0,0,12,47,1,0,0,0,14,16,3,2,1,0,15,
        14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,
        0,19,25,3,4,2,0,20,25,3,6,3,0,21,25,3,8,4,0,22,25,3,10,5,0,23,25,
        3,12,6,0,24,19,1,0,0,0,24,20,1,0,0,0,24,21,1,0,0,0,24,22,1,0,0,0,
        24,23,1,0,0,0,25,3,1,0,0,0,26,27,5,1,0,0,27,28,5,10,0,0,28,29,5,
        2,0,0,29,5,1,0,0,0,30,31,5,3,0,0,31,32,5,4,0,0,32,33,5,10,0,0,33,
        34,5,9,0,0,34,35,5,11,0,0,35,36,5,2,0,0,36,7,1,0,0,0,37,38,5,5,0,
        0,38,39,5,4,0,0,39,40,5,10,0,0,40,41,5,9,0,0,41,42,5,11,0,0,42,43,
        5,2,0,0,43,9,1,0,0,0,44,45,5,6,0,0,45,46,5,2,0,0,46,11,1,0,0,0,47,
        48,5,5,0,0,48,49,5,4,0,0,49,50,5,10,0,0,50,51,5,7,0,0,51,52,5,11,
        0,0,52,53,5,8,0,0,53,54,5,11,0,0,54,55,5,2,0,0,55,13,1,0,0,0,2,17,
        24
    ]

class CSVFilterParser ( Parser ):

    grammarFileName = "CSVFilter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "';'", "'filter'", "'column'", 
                     "'count'", "'print'", "'between'", "'and'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "OPERATOR", "STRING", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_loadStat = 2
    RULE_filterStat = 3
    RULE_countStat = 4
    RULE_printStat = 5
    RULE_countBetweenStat = 6

    ruleNames =  [ "prog", "stat", "loadStat", "filterStat", "countStat", 
                   "printStat", "countBetweenStat" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    OPERATOR=9
    STRING=10
    NUMBER=11
    WS=12

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
                return self.getTypedRuleContexts(CSVFilterParser.StatContext)
            else:
                return self.getTypedRuleContext(CSVFilterParser.StatContext,i)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_prog

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

        localctx = CSVFilterParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.stat()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 106) != 0)):
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
            return self.getTypedRuleContext(CSVFilterParser.LoadStatContext,0)


        def filterStat(self):
            return self.getTypedRuleContext(CSVFilterParser.FilterStatContext,0)


        def countStat(self):
            return self.getTypedRuleContext(CSVFilterParser.CountStatContext,0)


        def printStat(self):
            return self.getTypedRuleContext(CSVFilterParser.PrintStatContext,0)


        def countBetweenStat(self):
            return self.getTypedRuleContext(CSVFilterParser.CountBetweenStatContext,0)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_stat

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

        localctx = CSVFilterParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.loadStat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.filterStat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.countStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 22
                self.printStat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 23
                self.countBetweenStat()
                pass


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
            return self.getToken(CSVFilterParser.STRING, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_loadStat

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

        localctx = CSVFilterParser.LoadStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(CSVFilterParser.T__0)
            self.state = 27
            self.match(CSVFilterParser.STRING)
            self.state = 28
            self.match(CSVFilterParser.T__1)
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

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def OPERATOR(self):
            return self.getToken(CSVFilterParser.OPERATOR, 0)

        def NUMBER(self):
            return self.getToken(CSVFilterParser.NUMBER, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_filterStat

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

        localctx = CSVFilterParser.FilterStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(CSVFilterParser.T__2)
            self.state = 31
            self.match(CSVFilterParser.T__3)
            self.state = 32
            self.match(CSVFilterParser.STRING)
            self.state = 33
            self.match(CSVFilterParser.OPERATOR)
            self.state = 34
            self.match(CSVFilterParser.NUMBER)
            self.state = 35
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CountStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def OPERATOR(self):
            return self.getToken(CSVFilterParser.OPERATOR, 0)

        def NUMBER(self):
            return self.getToken(CSVFilterParser.NUMBER, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_countStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCountStat" ):
                listener.enterCountStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCountStat" ):
                listener.exitCountStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCountStat" ):
                return visitor.visitCountStat(self)
            else:
                return visitor.visitChildren(self)




    def countStat(self):

        localctx = CSVFilterParser.CountStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_countStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(CSVFilterParser.T__4)
            self.state = 38
            self.match(CSVFilterParser.T__3)
            self.state = 39
            self.match(CSVFilterParser.STRING)
            self.state = 40
            self.match(CSVFilterParser.OPERATOR)
            self.state = 41
            self.match(CSVFilterParser.NUMBER)
            self.state = 42
            self.match(CSVFilterParser.T__1)
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
            return CSVFilterParser.RULE_printStat

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

        localctx = CSVFilterParser.PrintStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(CSVFilterParser.T__5)
            self.state = 45
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CountBetweenStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(CSVFilterParser.NUMBER)
            else:
                return self.getToken(CSVFilterParser.NUMBER, i)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_countBetweenStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCountBetweenStat" ):
                listener.enterCountBetweenStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCountBetweenStat" ):
                listener.exitCountBetweenStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCountBetweenStat" ):
                return visitor.visitCountBetweenStat(self)
            else:
                return visitor.visitChildren(self)




    def countBetweenStat(self):

        localctx = CSVFilterParser.CountBetweenStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_countBetweenStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(CSVFilterParser.T__4)
            self.state = 48
            self.match(CSVFilterParser.T__3)
            self.state = 49
            self.match(CSVFilterParser.STRING)
            self.state = 50
            self.match(CSVFilterParser.T__6)
            self.state = 51
            self.match(CSVFilterParser.NUMBER)
            self.state = 52
            self.match(CSVFilterParser.T__7)
            self.state = 53
            self.match(CSVFilterParser.NUMBER)
            self.state = 54
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





