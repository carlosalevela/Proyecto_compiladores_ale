// Generated from MiGramatica.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MiGramaticaLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.3", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SELECT=1, FROM=2, WHERE=3, STAR=4, COMMA=5, SEMI=6, GT=7, LT=8, EQ=9, 
		GE=10, LE=11, NE=12, IDENTIFIER=13, NUMBER=14, STRING=15, WS=16;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SELECT", "FROM", "WHERE", "STAR", "COMMA", "SEMI", "GT", "LT", "EQ", 
			"GE", "LE", "NE", "IDENTIFIER", "NUMBER", "STRING", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'SELECT'", "'FROM'", "'WHERE'", "'*'", "','", "';'", "'>'", "'<'", 
			"'='", "'>='", "'<='", "'!='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SELECT", "FROM", "WHERE", "STAR", "COMMA", "SEMI", "GT", "LT", 
			"EQ", "GE", "LE", "NE", "IDENTIFIER", "NUMBER", "STRING", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public MiGramaticaLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MiGramatica.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22n\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5"+
		"\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3"+
		"\r\3\r\3\r\3\16\3\16\7\16M\n\16\f\16\16\16P\13\16\3\17\6\17S\n\17\r\17"+
		"\16\17T\3\17\3\17\6\17Y\n\17\r\17\16\17Z\5\17]\n\17\3\20\3\20\7\20a\n"+
		"\20\f\20\16\20d\13\20\3\20\3\20\3\21\6\21i\n\21\r\21\16\21j\3\21\3\21"+
		"\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17"+
		"\35\20\37\21!\22\3\2\7\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\f\f\17\17"+
		"))\5\2\13\f\17\17\"\"\2s\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2"+
		"\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25"+
		"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2"+
		"\2\2\2!\3\2\2\2\3#\3\2\2\2\5*\3\2\2\2\7/\3\2\2\2\t\65\3\2\2\2\13\67\3"+
		"\2\2\2\r9\3\2\2\2\17;\3\2\2\2\21=\3\2\2\2\23?\3\2\2\2\25A\3\2\2\2\27D"+
		"\3\2\2\2\31G\3\2\2\2\33J\3\2\2\2\35R\3\2\2\2\37^\3\2\2\2!h\3\2\2\2#$\7"+
		"U\2\2$%\7G\2\2%&\7N\2\2&\'\7G\2\2\'(\7E\2\2()\7V\2\2)\4\3\2\2\2*+\7H\2"+
		"\2+,\7T\2\2,-\7Q\2\2-.\7O\2\2.\6\3\2\2\2/\60\7Y\2\2\60\61\7J\2\2\61\62"+
		"\7G\2\2\62\63\7T\2\2\63\64\7G\2\2\64\b\3\2\2\2\65\66\7,\2\2\66\n\3\2\2"+
		"\2\678\7.\2\28\f\3\2\2\29:\7=\2\2:\16\3\2\2\2;<\7@\2\2<\20\3\2\2\2=>\7"+
		">\2\2>\22\3\2\2\2?@\7?\2\2@\24\3\2\2\2AB\7@\2\2BC\7?\2\2C\26\3\2\2\2D"+
		"E\7>\2\2EF\7?\2\2F\30\3\2\2\2GH\7#\2\2HI\7?\2\2I\32\3\2\2\2JN\t\2\2\2"+
		"KM\t\3\2\2LK\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\34\3\2\2\2PN\3\2\2"+
		"\2QS\t\4\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\\\3\2\2\2VX\7\60"+
		"\2\2WY\t\4\2\2XW\3\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[]\3\2\2\2\\V\3"+
		"\2\2\2\\]\3\2\2\2]\36\3\2\2\2^b\7)\2\2_a\n\5\2\2`_\3\2\2\2ad\3\2\2\2b"+
		"`\3\2\2\2bc\3\2\2\2ce\3\2\2\2db\3\2\2\2ef\7)\2\2f \3\2\2\2gi\t\6\2\2h"+
		"g\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3\2\2\2kl\3\2\2\2lm\b\21\2\2m\"\3\2\2"+
		"\2\t\2NTZ\\bj\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}