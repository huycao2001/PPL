// Generated from c:\Users\Dell\Desktop\PPL_ass1\src\main\d96\parser\D96.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class D96Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		BREAK=1, CONTINUE=2, IF=3, ELSEIF=4, ELSE=5, FOREACH=6, ARRAY=7, IN=8, 
		BY=9, INT_TYPE=10, FLOAT_TYPE=11, BOOLEAN_TYPE=12, STRING_TYPE=13, NULL=14, 
		RETURN=15, ATTRIBUTE_TYPE=16, SELF=17, NEW=18, CLASS=19, IMMUTABLE=20, 
		MUTABLE=21, CONSTRUCTOR=22, DESTRUCTOR=23, DOLLAR_ID=24, ASSIGN=25, ADD=26, 
		SUB=27, MUL=28, DIV=29, MOD=30, NOT=31, AND=32, OR=33, STRCOMPARE=34, 
		CONCATE=35, EQUAL=36, NOTEQUAL=37, LARGER=38, SMALLER=39, LE=40, SE=41, 
		INT_LITERAL=42, BOOL_LITERAL=43, FLOAT_LITERAL=44, STRING_LITERAL=45, 
		BLOCK_COMMENT=46, LB=47, RB=48, LP=49, RP=50, LS=51, RS=52, COLON=53, 
		DOUBLEDOT=54, DOT=55, COMMA=56, SEMI_COLON=57, ID=58, WS=59, ERROR_CHAR=60, 
		UNCLOSE_STRING=61, ILLEGAL_ESCAPE=62;
	public static final int
		RULE_program = 0, RULE_class_declaration = 1, RULE_member = 2, RULE_attribute_declaration = 3, 
		RULE_testing = 4, RULE_primitive_type = 5, RULE_att_name = 6, RULE_method_declaration = 7, 
		RULE_parameter_decl = 8, RULE_constructor = 9, RULE_destructor = 10, RULE_block_statement = 11, 
		RULE_statement = 12, RULE_var_declare_statement = 13, RULE_assign_statement = 14, 
		RULE_if_statement = 15, RULE_for_statement = 16, RULE_return_statement = 17, 
		RULE_break_statement = 18, RULE_continue_statement = 19, RULE_expression = 20, 
		RULE_expression1 = 21, RULE_expression2 = 22, RULE_expression3 = 23, RULE_expression4 = 24, 
		RULE_expression5 = 25, RULE_operands = 26;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "class_declaration", "member", "attribute_declaration", "testing", 
			"primitive_type", "att_name", "method_declaration", "parameter_decl", 
			"constructor", "destructor", "block_statement", "statement", "var_declare_statement", 
			"assign_statement", "if_statement", "for_statement", "return_statement", 
			"break_statement", "continue_statement", "expression", "expression1", 
			"expression2", "expression3", "expression4", "expression5", "operands"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
			"'Array'", "'In'", "'By'", "'Int'", "'Float'", "'Boolean'", "'String'", 
			"'Null'", "'return'", null, "'Self'", "'New'", "'Class'", "'Val'", "'Var'", 
			"'Constructor'", "'Destructor'", null, "'='", "'+'", "'-'", "'*'", "'/'", 
			"'%'", "'!'", "'&&'", "'||'", "'==.'", "'+.'", "'=='", "'!='", "'>'", 
			"'<'", "'>='", "'<='", null, null, null, null, null, "'('", "')'", "'{'", 
			"'}'", "'['", "']'", "':'", "'..'", "'.'", "','", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "ARRAY", 
			"IN", "BY", "INT_TYPE", "FLOAT_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", 
			"NULL", "RETURN", "ATTRIBUTE_TYPE", "SELF", "NEW", "CLASS", "IMMUTABLE", 
			"MUTABLE", "CONSTRUCTOR", "DESTRUCTOR", "DOLLAR_ID", "ASSIGN", "ADD", 
			"SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "STRCOMPARE", "CONCATE", 
			"EQUAL", "NOTEQUAL", "LARGER", "SMALLER", "LE", "SE", "INT_LITERAL", 
			"BOOL_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", "BLOCK_COMMENT", "LB", 
			"RB", "LP", "RP", "LS", "RS", "COLON", "DOUBLEDOT", "DOT", "COMMA", "SEMI_COLON", 
			"ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE"
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

	@Override
	public String getGrammarFileName() { return "D96.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public D96Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(D96Parser.EOF, 0); }
		public List<Class_declarationContext> class_declaration() {
			return getRuleContexts(Class_declarationContext.class);
		}
		public Class_declarationContext class_declaration(int i) {
			return getRuleContext(Class_declarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(54);
				class_declaration();
				}
				}
				setState(57); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==CLASS );
			setState(59);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_declarationContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(D96Parser.CLASS, 0); }
		public List<TerminalNode> ID() { return getTokens(D96Parser.ID); }
		public TerminalNode ID(int i) {
			return getToken(D96Parser.ID, i);
		}
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public TerminalNode COLON() { return getToken(D96Parser.COLON, 0); }
		public List<MemberContext> member() {
			return getRuleContexts(MemberContext.class);
		}
		public MemberContext member(int i) {
			return getRuleContext(MemberContext.class,i);
		}
		public Class_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_declaration; }
	}

	public final Class_declarationContext class_declaration() throws RecognitionException {
		Class_declarationContext _localctx = new Class_declarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_class_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(CLASS);
			setState(62);
			match(ID);
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COLON) {
				{
				setState(63);
				match(COLON);
				setState(64);
				match(ID);
				}
			}

			setState(67);
			match(LP);
			setState(69); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(68);
				member();
				}
				}
				setState(71); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ATTRIBUTE_TYPE) | (1L << DOLLAR_ID) | (1L << ID))) != 0) );
			setState(73);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MemberContext extends ParserRuleContext {
		public Attribute_declarationContext attribute_declaration() {
			return getRuleContext(Attribute_declarationContext.class,0);
		}
		public Method_declarationContext method_declaration() {
			return getRuleContext(Method_declarationContext.class,0);
		}
		public MemberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_member; }
	}

	public final MemberContext member() throws RecognitionException {
		MemberContext _localctx = new MemberContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_member);
		try {
			setState(77);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ATTRIBUTE_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(75);
				attribute_declaration();
				}
				break;
			case DOLLAR_ID:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(76);
				method_declaration();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attribute_declarationContext extends ParserRuleContext {
		public TerminalNode ATTRIBUTE_TYPE() { return getToken(D96Parser.ATTRIBUTE_TYPE, 0); }
		public TestingContext testing() {
			return getRuleContext(TestingContext.class,0);
		}
		public TerminalNode SEMI_COLON() { return getToken(D96Parser.SEMI_COLON, 0); }
		public Attribute_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute_declaration; }
	}

	public final Attribute_declarationContext attribute_declaration() throws RecognitionException {
		Attribute_declarationContext _localctx = new Attribute_declarationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_attribute_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(ATTRIBUTE_TYPE);
			setState(80);
			testing();
			setState(81);
			match(SEMI_COLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TestingContext extends ParserRuleContext {
		public Att_nameContext att_name() {
			return getRuleContext(Att_nameContext.class,0);
		}
		public TerminalNode COLON() { return getToken(D96Parser.COLON, 0); }
		public Primitive_typeContext primitive_type() {
			return getRuleContext(Primitive_typeContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(D96Parser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(D96Parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(D96Parser.COMMA, i);
		}
		public TestingContext testing() {
			return getRuleContext(TestingContext.class,0);
		}
		public TestingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_testing; }
	}

	public final TestingContext testing() throws RecognitionException {
		TestingContext _localctx = new TestingContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_testing);
		int _la;
		try {
			setState(97);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(83);
				att_name();
				{
				setState(84);
				match(COLON);
				setState(85);
				primitive_type();
				setState(88);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGN) {
					{
					setState(86);
					match(ASSIGN);
					setState(87);
					expression();
					}
				}

				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				{
				setState(90);
				att_name();
				setState(91);
				match(COMMA);
				setState(92);
				testing();
				setState(95);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
				case 1:
					{
					setState(93);
					match(COMMA);
					setState(94);
					expression();
					}
					break;
				}
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Primitive_typeContext extends ParserRuleContext {
		public TerminalNode INT_TYPE() { return getToken(D96Parser.INT_TYPE, 0); }
		public TerminalNode FLOAT_TYPE() { return getToken(D96Parser.FLOAT_TYPE, 0); }
		public TerminalNode BOOLEAN_TYPE() { return getToken(D96Parser.BOOLEAN_TYPE, 0); }
		public TerminalNode STRING_TYPE() { return getToken(D96Parser.STRING_TYPE, 0); }
		public Primitive_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitive_type; }
	}

	public final Primitive_typeContext primitive_type() throws RecognitionException {
		Primitive_typeContext _localctx = new Primitive_typeContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_primitive_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT_TYPE) | (1L << FLOAT_TYPE) | (1L << BOOLEAN_TYPE) | (1L << STRING_TYPE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Att_nameContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode DOLLAR_ID() { return getToken(D96Parser.DOLLAR_ID, 0); }
		public Att_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_att_name; }
	}

	public final Att_nameContext att_name() throws RecognitionException {
		Att_nameContext _localctx = new Att_nameContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_att_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			_la = _input.LA(1);
			if ( !(_la==DOLLAR_ID || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_declarationContext extends ParserRuleContext {
		public Att_nameContext att_name() {
			return getRuleContext(Att_nameContext.class,0);
		}
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public Block_statementContext block_statement() {
			return getRuleContext(Block_statementContext.class,0);
		}
		public List<Parameter_declContext> parameter_decl() {
			return getRuleContexts(Parameter_declContext.class);
		}
		public Parameter_declContext parameter_decl(int i) {
			return getRuleContext(Parameter_declContext.class,i);
		}
		public List<TerminalNode> SEMI_COLON() { return getTokens(D96Parser.SEMI_COLON); }
		public TerminalNode SEMI_COLON(int i) {
			return getToken(D96Parser.SEMI_COLON, i);
		}
		public Method_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_declaration; }
	}

	public final Method_declarationContext method_declaration() throws RecognitionException {
		Method_declarationContext _localctx = new Method_declarationContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_method_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			att_name();
			setState(104);
			match(LB);
			setState(113);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(105);
				parameter_decl();
				setState(110);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==SEMI_COLON) {
					{
					{
					setState(106);
					match(SEMI_COLON);
					setState(107);
					parameter_decl();
					}
					}
					setState(112);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(115);
			match(RB);
			setState(116);
			block_statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Parameter_declContext extends ParserRuleContext {
		public TerminalNode COLON() { return getToken(D96Parser.COLON, 0); }
		public Primitive_typeContext primitive_type() {
			return getRuleContext(Primitive_typeContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(D96Parser.ID); }
		public TerminalNode ID(int i) {
			return getToken(D96Parser.ID, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(D96Parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(D96Parser.COMMA, i);
		}
		public Parameter_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter_decl; }
	}

	public final Parameter_declContext parameter_decl() throws RecognitionException {
		Parameter_declContext _localctx = new Parameter_declContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_parameter_decl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(118);
			match(ID);
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(119);
				match(COMMA);
				setState(120);
				match(ID);
				}
				}
				setState(125);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
			setState(126);
			match(COLON);
			setState(127);
			primitive_type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstructorContext extends ParserRuleContext {
		public TerminalNode CONSTRUCTOR() { return getToken(D96Parser.CONSTRUCTOR, 0); }
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public Block_statementContext block_statement() {
			return getRuleContext(Block_statementContext.class,0);
		}
		public List<Parameter_declContext> parameter_decl() {
			return getRuleContexts(Parameter_declContext.class);
		}
		public Parameter_declContext parameter_decl(int i) {
			return getRuleContext(Parameter_declContext.class,i);
		}
		public List<TerminalNode> SEMI_COLON() { return getTokens(D96Parser.SEMI_COLON); }
		public TerminalNode SEMI_COLON(int i) {
			return getToken(D96Parser.SEMI_COLON, i);
		}
		public ConstructorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constructor; }
	}

	public final ConstructorContext constructor() throws RecognitionException {
		ConstructorContext _localctx = new ConstructorContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_constructor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(CONSTRUCTOR);
			setState(130);
			match(LB);
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(131);
				parameter_decl();
				setState(136);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==SEMI_COLON) {
					{
					{
					setState(132);
					match(SEMI_COLON);
					setState(133);
					parameter_decl();
					}
					}
					setState(138);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(141);
			match(RB);
			setState(142);
			block_statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DestructorContext extends ParserRuleContext {
		public TerminalNode DESTRUCTOR() { return getToken(D96Parser.DESTRUCTOR, 0); }
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public Block_statementContext block_statement() {
			return getRuleContext(Block_statementContext.class,0);
		}
		public DestructorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_destructor; }
	}

	public final DestructorContext destructor() throws RecognitionException {
		DestructorContext _localctx = new DestructorContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_destructor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			match(DESTRUCTOR);
			setState(145);
			match(LB);
			setState(146);
			match(RB);
			setState(147);
			block_statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Block_statementContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public Block_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_statement; }
	}

	public final Block_statementContext block_statement() throws RecognitionException {
		Block_statementContext _localctx = new Block_statementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_block_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			match(LP);
			setState(153);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BREAK) | (1L << CONTINUE) | (1L << IF) | (1L << FOREACH) | (1L << RETURN) | (1L << ATTRIBUTE_TYPE) | (1L << NOT) | (1L << INT_LITERAL) | (1L << BOOL_LITERAL) | (1L << FLOAT_LITERAL) | (1L << STRING_LITERAL) | (1L << LB) | (1L << ID))) != 0)) {
				{
				{
				setState(150);
				statement();
				}
				}
				setState(155);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(156);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public Var_declare_statementContext var_declare_statement() {
			return getRuleContext(Var_declare_statementContext.class,0);
		}
		public Assign_statementContext assign_statement() {
			return getRuleContext(Assign_statementContext.class,0);
		}
		public If_statementContext if_statement() {
			return getRuleContext(If_statementContext.class,0);
		}
		public For_statementContext for_statement() {
			return getRuleContext(For_statementContext.class,0);
		}
		public Return_statementContext return_statement() {
			return getRuleContext(Return_statementContext.class,0);
		}
		public Break_statementContext break_statement() {
			return getRuleContext(Break_statementContext.class,0);
		}
		public Continue_statementContext continue_statement() {
			return getRuleContext(Continue_statementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_statement);
		try {
			setState(165);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ATTRIBUTE_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(158);
				var_declare_statement();
				}
				break;
			case NOT:
			case INT_LITERAL:
			case BOOL_LITERAL:
			case FLOAT_LITERAL:
			case STRING_LITERAL:
			case LB:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(159);
				assign_statement();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 3);
				{
				setState(160);
				if_statement();
				}
				break;
			case FOREACH:
				enterOuterAlt(_localctx, 4);
				{
				setState(161);
				for_statement();
				}
				break;
			case RETURN:
				enterOuterAlt(_localctx, 5);
				{
				setState(162);
				return_statement();
				}
				break;
			case BREAK:
				enterOuterAlt(_localctx, 6);
				{
				setState(163);
				break_statement();
				}
				break;
			case CONTINUE:
				enterOuterAlt(_localctx, 7);
				{
				setState(164);
				continue_statement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_declare_statementContext extends ParserRuleContext {
		public TerminalNode ATTRIBUTE_TYPE() { return getToken(D96Parser.ATTRIBUTE_TYPE, 0); }
		public List<TerminalNode> ID() { return getTokens(D96Parser.ID); }
		public TerminalNode ID(int i) {
			return getToken(D96Parser.ID, i);
		}
		public TerminalNode COLON() { return getToken(D96Parser.COLON, 0); }
		public Primitive_typeContext primitive_type() {
			return getRuleContext(Primitive_typeContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(D96Parser.ASSIGN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode SEMI_COLON() { return getToken(D96Parser.SEMI_COLON, 0); }
		public List<TerminalNode> COMMA() { return getTokens(D96Parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(D96Parser.COMMA, i);
		}
		public Var_declare_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_declare_statement; }
	}

	public final Var_declare_statementContext var_declare_statement() throws RecognitionException {
		Var_declare_statementContext _localctx = new Var_declare_statementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_var_declare_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(ATTRIBUTE_TYPE);
			setState(168);
			match(ID);
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(169);
				match(COMMA);
				setState(170);
				match(ID);
				}
				}
				setState(175);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(176);
			match(COLON);
			setState(177);
			primitive_type();
			setState(178);
			match(ASSIGN);
			setState(179);
			expression();
			setState(184);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(180);
				match(COMMA);
				setState(181);
				expression();
				}
				}
				setState(186);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(187);
			match(SEMI_COLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_statementContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode ASSIGN() { return getToken(D96Parser.ASSIGN, 0); }
		public TerminalNode SEMI_COLON() { return getToken(D96Parser.SEMI_COLON, 0); }
		public Assign_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_statement; }
	}

	public final Assign_statementContext assign_statement() throws RecognitionException {
		Assign_statementContext _localctx = new Assign_statementContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_assign_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(189);
			expression();
			setState(190);
			match(ASSIGN);
			setState(191);
			expression();
			setState(192);
			match(SEMI_COLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_statementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(D96Parser.IF, 0); }
		public List<TerminalNode> LB() { return getTokens(D96Parser.LB); }
		public TerminalNode LB(int i) {
			return getToken(D96Parser.LB, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> RB() { return getTokens(D96Parser.RB); }
		public TerminalNode RB(int i) {
			return getToken(D96Parser.RB, i);
		}
		public List<Block_statementContext> block_statement() {
			return getRuleContexts(Block_statementContext.class);
		}
		public Block_statementContext block_statement(int i) {
			return getRuleContext(Block_statementContext.class,i);
		}
		public List<TerminalNode> ELSEIF() { return getTokens(D96Parser.ELSEIF); }
		public TerminalNode ELSEIF(int i) {
			return getToken(D96Parser.ELSEIF, i);
		}
		public TerminalNode ELSE() { return getToken(D96Parser.ELSE, 0); }
		public If_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_statement; }
	}

	public final If_statementContext if_statement() throws RecognitionException {
		If_statementContext _localctx = new If_statementContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_if_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			match(IF);
			setState(195);
			match(LB);
			setState(196);
			expression();
			setState(197);
			match(RB);
			setState(198);
			block_statement();
			setState(207);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELSEIF) {
				{
				{
				setState(199);
				match(ELSEIF);
				setState(200);
				match(LB);
				setState(201);
				expression();
				setState(202);
				match(RB);
				setState(203);
				block_statement();
				}
				}
				setState(209);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(212);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(210);
				match(ELSE);
				setState(211);
				block_statement();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class For_statementContext extends ParserRuleContext {
		public TerminalNode FOREACH() { return getToken(D96Parser.FOREACH, 0); }
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode IN() { return getToken(D96Parser.IN, 0); }
		public List<TerminalNode> INT_LITERAL() { return getTokens(D96Parser.INT_LITERAL); }
		public TerminalNode INT_LITERAL(int i) {
			return getToken(D96Parser.INT_LITERAL, i);
		}
		public TerminalNode DOUBLEDOT() { return getToken(D96Parser.DOUBLEDOT, 0); }
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public Block_statementContext block_statement() {
			return getRuleContext(Block_statementContext.class,0);
		}
		public TerminalNode BY() { return getToken(D96Parser.BY, 0); }
		public For_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_statement; }
	}

	public final For_statementContext for_statement() throws RecognitionException {
		For_statementContext _localctx = new For_statementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_for_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			match(FOREACH);
			setState(215);
			match(LB);
			setState(216);
			match(ID);
			setState(217);
			match(IN);
			setState(218);
			match(INT_LITERAL);
			setState(219);
			match(DOUBLEDOT);
			setState(220);
			match(INT_LITERAL);
			setState(223);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BY) {
				{
				setState(221);
				match(BY);
				setState(222);
				match(INT_LITERAL);
				}
			}

			setState(225);
			match(RB);
			setState(226);
			block_statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_statementContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(D96Parser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI_COLON() { return getToken(D96Parser.SEMI_COLON, 0); }
		public Return_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_statement; }
	}

	public final Return_statementContext return_statement() throws RecognitionException {
		Return_statementContext _localctx = new Return_statementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_return_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			match(RETURN);
			setState(229);
			expression();
			setState(230);
			match(SEMI_COLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Break_statementContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(D96Parser.BREAK, 0); }
		public TerminalNode SEMI_COLON() { return getToken(D96Parser.SEMI_COLON, 0); }
		public Break_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_statement; }
	}

	public final Break_statementContext break_statement() throws RecognitionException {
		Break_statementContext _localctx = new Break_statementContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_break_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(BREAK);
			setState(233);
			match(SEMI_COLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Continue_statementContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(D96Parser.CONTINUE, 0); }
		public TerminalNode SEMI_COLON() { return getToken(D96Parser.SEMI_COLON, 0); }
		public Continue_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_statement; }
	}

	public final Continue_statementContext continue_statement() throws RecognitionException {
		Continue_statementContext _localctx = new Continue_statementContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_continue_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
			match(CONTINUE);
			setState(236);
			match(SEMI_COLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public List<Expression1Context> expression1() {
			return getRuleContexts(Expression1Context.class);
		}
		public Expression1Context expression1(int i) {
			return getRuleContext(Expression1Context.class,i);
		}
		public TerminalNode CONCATE() { return getToken(D96Parser.CONCATE, 0); }
		public TerminalNode STRCOMPARE() { return getToken(D96Parser.STRCOMPARE, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_expression);
		int _la;
		try {
			setState(243);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(238);
				expression1();
				setState(239);
				_la = _input.LA(1);
				if ( !(_la==STRCOMPARE || _la==CONCATE) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(240);
				expression1();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(242);
				expression1();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expression1Context extends ParserRuleContext {
		public List<Expression2Context> expression2() {
			return getRuleContexts(Expression2Context.class);
		}
		public Expression2Context expression2(int i) {
			return getRuleContext(Expression2Context.class,i);
		}
		public TerminalNode EQUAL() { return getToken(D96Parser.EQUAL, 0); }
		public TerminalNode NOTEQUAL() { return getToken(D96Parser.NOTEQUAL, 0); }
		public TerminalNode LARGER() { return getToken(D96Parser.LARGER, 0); }
		public TerminalNode SMALLER() { return getToken(D96Parser.SMALLER, 0); }
		public TerminalNode LE() { return getToken(D96Parser.LE, 0); }
		public TerminalNode SE() { return getToken(D96Parser.SE, 0); }
		public Expression1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression1; }
	}

	public final Expression1Context expression1() throws RecognitionException {
		Expression1Context _localctx = new Expression1Context(_ctx, getState());
		enterRule(_localctx, 42, RULE_expression1);
		int _la;
		try {
			setState(250);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(245);
				expression2(0);
				setState(246);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUAL) | (1L << NOTEQUAL) | (1L << LARGER) | (1L << SMALLER) | (1L << LE) | (1L << SE))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(247);
				expression2(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(249);
				expression2(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expression2Context extends ParserRuleContext {
		public Expression3Context expression3() {
			return getRuleContext(Expression3Context.class,0);
		}
		public Expression2Context expression2() {
			return getRuleContext(Expression2Context.class,0);
		}
		public TerminalNode OR() { return getToken(D96Parser.OR, 0); }
		public TerminalNode AND() { return getToken(D96Parser.AND, 0); }
		public Expression2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression2; }
	}

	public final Expression2Context expression2() throws RecognitionException {
		return expression2(0);
	}

	private Expression2Context expression2(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expression2Context _localctx = new Expression2Context(_ctx, _parentState);
		Expression2Context _prevctx = _localctx;
		int _startState = 44;
		enterRecursionRule(_localctx, 44, RULE_expression2, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(253);
			expression3(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(260);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression2Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression2);
					setState(255);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(256);
					_la = _input.LA(1);
					if ( !(_la==AND || _la==OR) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(257);
					expression3(0);
					}
					} 
				}
				setState(262);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expression3Context extends ParserRuleContext {
		public Expression4Context expression4() {
			return getRuleContext(Expression4Context.class,0);
		}
		public Expression3Context expression3() {
			return getRuleContext(Expression3Context.class,0);
		}
		public TerminalNode ADD() { return getToken(D96Parser.ADD, 0); }
		public TerminalNode SUB() { return getToken(D96Parser.SUB, 0); }
		public Expression3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression3; }
	}

	public final Expression3Context expression3() throws RecognitionException {
		return expression3(0);
	}

	private Expression3Context expression3(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expression3Context _localctx = new Expression3Context(_ctx, _parentState);
		Expression3Context _prevctx = _localctx;
		int _startState = 46;
		enterRecursionRule(_localctx, 46, RULE_expression3, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(264);
			expression4(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(271);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression3Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression3);
					setState(266);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(267);
					_la = _input.LA(1);
					if ( !(_la==ADD || _la==SUB) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(268);
					expression4(0);
					}
					} 
				}
				setState(273);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expression4Context extends ParserRuleContext {
		public Expression5Context expression5() {
			return getRuleContext(Expression5Context.class,0);
		}
		public Expression4Context expression4() {
			return getRuleContext(Expression4Context.class,0);
		}
		public TerminalNode MUL() { return getToken(D96Parser.MUL, 0); }
		public TerminalNode DIV() { return getToken(D96Parser.DIV, 0); }
		public TerminalNode MOD() { return getToken(D96Parser.MOD, 0); }
		public Expression4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression4; }
	}

	public final Expression4Context expression4() throws RecognitionException {
		return expression4(0);
	}

	private Expression4Context expression4(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expression4Context _localctx = new Expression4Context(_ctx, _parentState);
		Expression4Context _prevctx = _localctx;
		int _startState = 48;
		enterRecursionRule(_localctx, 48, RULE_expression4, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(275);
			expression5();
			}
			_ctx.stop = _input.LT(-1);
			setState(282);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression4Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression4);
					setState(277);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(278);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MUL) | (1L << DIV) | (1L << MOD))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(279);
					expression5();
					}
					} 
				}
				setState(284);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expression5Context extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(D96Parser.NOT, 0); }
		public Expression5Context expression5() {
			return getRuleContext(Expression5Context.class,0);
		}
		public OperandsContext operands() {
			return getRuleContext(OperandsContext.class,0);
		}
		public Expression5Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression5; }
	}

	public final Expression5Context expression5() throws RecognitionException {
		Expression5Context _localctx = new Expression5Context(_ctx, getState());
		enterRule(_localctx, 50, RULE_expression5);
		try {
			setState(288);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(285);
				match(NOT);
				setState(286);
				expression5();
				}
				break;
			case INT_LITERAL:
			case BOOL_LITERAL:
			case FLOAT_LITERAL:
			case STRING_LITERAL:
			case LB:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(287);
				operands();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OperandsContext extends ParserRuleContext {
		public TerminalNode STRING_LITERAL() { return getToken(D96Parser.STRING_LITERAL, 0); }
		public TerminalNode INT_LITERAL() { return getToken(D96Parser.INT_LITERAL, 0); }
		public TerminalNode FLOAT_LITERAL() { return getToken(D96Parser.FLOAT_LITERAL, 0); }
		public TerminalNode BOOL_LITERAL() { return getToken(D96Parser.BOOL_LITERAL, 0); }
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public OperandsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operands; }
	}

	public final OperandsContext operands() throws RecognitionException {
		OperandsContext _localctx = new OperandsContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_operands);
		int _la;
		try {
			setState(296);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_LITERAL:
			case BOOL_LITERAL:
			case FLOAT_LITERAL:
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(290);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT_LITERAL) | (1L << BOOL_LITERAL) | (1L << FLOAT_LITERAL) | (1L << STRING_LITERAL))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(291);
				match(ID);
				}
				break;
			case LB:
				enterOuterAlt(_localctx, 3);
				{
				{
				setState(292);
				match(LB);
				setState(293);
				expression();
				setState(294);
				match(RB);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 22:
			return expression2_sempred((Expression2Context)_localctx, predIndex);
		case 23:
			return expression3_sempred((Expression3Context)_localctx, predIndex);
		case 24:
			return expression4_sempred((Expression4Context)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression2_sempred(Expression2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expression3_sempred(Expression3Context _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expression4_sempred(Expression4Context _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@\u012d\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\3\2\6\2:\n\2\r\2\16\2;\3\2\3\2\3\3\3\3"+
		"\3\3\3\3\5\3D\n\3\3\3\3\3\6\3H\n\3\r\3\16\3I\3\3\3\3\3\4\3\4\5\4P\n\4"+
		"\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6[\n\6\3\6\3\6\3\6\3\6\3\6\5\6"+
		"b\n\6\5\6d\n\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\7\to\n\t\f\t\16\tr"+
		"\13\t\5\tt\n\t\3\t\3\t\3\t\3\n\3\n\3\n\7\n|\n\n\f\n\16\n\177\13\n\3\n"+
		"\3\n\3\n\3\13\3\13\3\13\3\13\3\13\7\13\u0089\n\13\f\13\16\13\u008c\13"+
		"\13\5\13\u008e\n\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\7\r\u009a"+
		"\n\r\f\r\16\r\u009d\13\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5"+
		"\16\u00a8\n\16\3\17\3\17\3\17\3\17\7\17\u00ae\n\17\f\17\16\17\u00b1\13"+
		"\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u00b9\n\17\f\17\16\17\u00bc\13"+
		"\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3"+
		"\21\3\21\3\21\3\21\3\21\7\21\u00d0\n\21\f\21\16\21\u00d3\13\21\3\21\3"+
		"\21\5\21\u00d7\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22"+
		"\u00e2\n\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25"+
		"\3\25\3\26\3\26\3\26\3\26\3\26\5\26\u00f6\n\26\3\27\3\27\3\27\3\27\3\27"+
		"\5\27\u00fd\n\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u0105\n\30\f\30\16"+
		"\30\u0108\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0110\n\31\f\31\16"+
		"\31\u0113\13\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u011b\n\32\f\32\16"+
		"\32\u011e\13\32\3\33\3\33\3\33\5\33\u0123\n\33\3\34\3\34\3\34\3\34\3\34"+
		"\3\34\5\34\u012b\n\34\3\34\2\5.\60\62\35\2\4\6\b\n\f\16\20\22\24\26\30"+
		"\32\34\36 \"$&(*,.\60\62\64\66\2\n\3\2\f\17\4\2\32\32<<\3\2$%\3\2&+\3"+
		"\2\"#\3\2\34\35\3\2\36 \3\2,/\2\u0131\29\3\2\2\2\4?\3\2\2\2\6O\3\2\2\2"+
		"\bQ\3\2\2\2\nc\3\2\2\2\fe\3\2\2\2\16g\3\2\2\2\20i\3\2\2\2\22x\3\2\2\2"+
		"\24\u0083\3\2\2\2\26\u0092\3\2\2\2\30\u0097\3\2\2\2\32\u00a7\3\2\2\2\34"+
		"\u00a9\3\2\2\2\36\u00bf\3\2\2\2 \u00c4\3\2\2\2\"\u00d8\3\2\2\2$\u00e6"+
		"\3\2\2\2&\u00ea\3\2\2\2(\u00ed\3\2\2\2*\u00f5\3\2\2\2,\u00fc\3\2\2\2."+
		"\u00fe\3\2\2\2\60\u0109\3\2\2\2\62\u0114\3\2\2\2\64\u0122\3\2\2\2\66\u012a"+
		"\3\2\2\28:\5\4\3\298\3\2\2\2:;\3\2\2\2;9\3\2\2\2;<\3\2\2\2<=\3\2\2\2="+
		">\7\2\2\3>\3\3\2\2\2?@\7\25\2\2@C\7<\2\2AB\7\67\2\2BD\7<\2\2CA\3\2\2\2"+
		"CD\3\2\2\2DE\3\2\2\2EG\7\63\2\2FH\5\6\4\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2"+
		"\2IJ\3\2\2\2JK\3\2\2\2KL\7\64\2\2L\5\3\2\2\2MP\5\b\5\2NP\5\20\t\2OM\3"+
		"\2\2\2ON\3\2\2\2P\7\3\2\2\2QR\7\22\2\2RS\5\n\6\2ST\7;\2\2T\t\3\2\2\2U"+
		"V\5\16\b\2VW\7\67\2\2WZ\5\f\7\2XY\7\33\2\2Y[\5*\26\2ZX\3\2\2\2Z[\3\2\2"+
		"\2[d\3\2\2\2\\]\5\16\b\2]^\7:\2\2^a\5\n\6\2_`\7:\2\2`b\5*\26\2a_\3\2\2"+
		"\2ab\3\2\2\2bd\3\2\2\2cU\3\2\2\2c\\\3\2\2\2d\13\3\2\2\2ef\t\2\2\2f\r\3"+
		"\2\2\2gh\t\3\2\2h\17\3\2\2\2ij\5\16\b\2js\7\61\2\2kp\5\22\n\2lm\7;\2\2"+
		"mo\5\22\n\2nl\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2qt\3\2\2\2rp\3\2\2"+
		"\2sk\3\2\2\2st\3\2\2\2tu\3\2\2\2uv\7\62\2\2vw\5\30\r\2w\21\3\2\2\2x}\7"+
		"<\2\2yz\7:\2\2z|\7<\2\2{y\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0080"+
		"\3\2\2\2\177}\3\2\2\2\u0080\u0081\7\67\2\2\u0081\u0082\5\f\7\2\u0082\23"+
		"\3\2\2\2\u0083\u0084\7\30\2\2\u0084\u008d\7\61\2\2\u0085\u008a\5\22\n"+
		"\2\u0086\u0087\7;\2\2\u0087\u0089\5\22\n\2\u0088\u0086\3\2\2\2\u0089\u008c"+
		"\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008e\3\2\2\2\u008c"+
		"\u008a\3\2\2\2\u008d\u0085\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\3\2"+
		"\2\2\u008f\u0090\7\62\2\2\u0090\u0091\5\30\r\2\u0091\25\3\2\2\2\u0092"+
		"\u0093\7\31\2\2\u0093\u0094\7\61\2\2\u0094\u0095\7\62\2\2\u0095\u0096"+
		"\5\30\r\2\u0096\27\3\2\2\2\u0097\u009b\7\63\2\2\u0098\u009a\5\32\16\2"+
		"\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c"+
		"\3\2\2\2\u009c\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f\7\64\2\2"+
		"\u009f\31\3\2\2\2\u00a0\u00a8\5\34\17\2\u00a1\u00a8\5\36\20\2\u00a2\u00a8"+
		"\5 \21\2\u00a3\u00a8\5\"\22\2\u00a4\u00a8\5$\23\2\u00a5\u00a8\5&\24\2"+
		"\u00a6\u00a8\5(\25\2\u00a7\u00a0\3\2\2\2\u00a7\u00a1\3\2\2\2\u00a7\u00a2"+
		"\3\2\2\2\u00a7\u00a3\3\2\2\2\u00a7\u00a4\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7"+
		"\u00a6\3\2\2\2\u00a8\33\3\2\2\2\u00a9\u00aa\7\22\2\2\u00aa\u00af\7<\2"+
		"\2\u00ab\u00ac\7:\2\2\u00ac\u00ae\7<\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00b1"+
		"\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1"+
		"\u00af\3\2\2\2\u00b2\u00b3\7\67\2\2\u00b3\u00b4\5\f\7\2\u00b4\u00b5\7"+
		"\33\2\2\u00b5\u00ba\5*\26\2\u00b6\u00b7\7:\2\2\u00b7\u00b9\5*\26\2\u00b8"+
		"\u00b6\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2"+
		"\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00be\7;\2\2\u00be"+
		"\35\3\2\2\2\u00bf\u00c0\5*\26\2\u00c0\u00c1\7\33\2\2\u00c1\u00c2\5*\26"+
		"\2\u00c2\u00c3\7;\2\2\u00c3\37\3\2\2\2\u00c4\u00c5\7\5\2\2\u00c5\u00c6"+
		"\7\61\2\2\u00c6\u00c7\5*\26\2\u00c7\u00c8\7\62\2\2\u00c8\u00d1\5\30\r"+
		"\2\u00c9\u00ca\7\6\2\2\u00ca\u00cb\7\61\2\2\u00cb\u00cc\5*\26\2\u00cc"+
		"\u00cd\7\62\2\2\u00cd\u00ce\5\30\r\2\u00ce\u00d0\3\2\2\2\u00cf\u00c9\3"+
		"\2\2\2\u00d0\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2"+
		"\u00d6\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d5\7\7\2\2\u00d5\u00d7\5\30"+
		"\r\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7!\3\2\2\2\u00d8\u00d9"+
		"\7\b\2\2\u00d9\u00da\7\61\2\2\u00da\u00db\7<\2\2\u00db\u00dc\7\n\2\2\u00dc"+
		"\u00dd\7,\2\2\u00dd\u00de\78\2\2\u00de\u00e1\7,\2\2\u00df\u00e0\7\13\2"+
		"\2\u00e0\u00e2\7,\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3"+
		"\3\2\2\2\u00e3\u00e4\7\62\2\2\u00e4\u00e5\5\30\r\2\u00e5#\3\2\2\2\u00e6"+
		"\u00e7\7\21\2\2\u00e7\u00e8\5*\26\2\u00e8\u00e9\7;\2\2\u00e9%\3\2\2\2"+
		"\u00ea\u00eb\7\3\2\2\u00eb\u00ec\7;\2\2\u00ec\'\3\2\2\2\u00ed\u00ee\7"+
		"\4\2\2\u00ee\u00ef\7;\2\2\u00ef)\3\2\2\2\u00f0\u00f1\5,\27\2\u00f1\u00f2"+
		"\t\4\2\2\u00f2\u00f3\5,\27\2\u00f3\u00f6\3\2\2\2\u00f4\u00f6\5,\27\2\u00f5"+
		"\u00f0\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6+\3\2\2\2\u00f7\u00f8\5.\30\2"+
		"\u00f8\u00f9\t\5\2\2\u00f9\u00fa\5.\30\2\u00fa\u00fd\3\2\2\2\u00fb\u00fd"+
		"\5.\30\2\u00fc\u00f7\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd-\3\2\2\2\u00fe"+
		"\u00ff\b\30\1\2\u00ff\u0100\5\60\31\2\u0100\u0106\3\2\2\2\u0101\u0102"+
		"\f\4\2\2\u0102\u0103\t\6\2\2\u0103\u0105\5\60\31\2\u0104\u0101\3\2\2\2"+
		"\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107/\3"+
		"\2\2\2\u0108\u0106\3\2\2\2\u0109\u010a\b\31\1\2\u010a\u010b\5\62\32\2"+
		"\u010b\u0111\3\2\2\2\u010c\u010d\f\4\2\2\u010d\u010e\t\7\2\2\u010e\u0110"+
		"\5\62\32\2\u010f\u010c\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f\3\2\2\2"+
		"\u0111\u0112\3\2\2\2\u0112\61\3\2\2\2\u0113\u0111\3\2\2\2\u0114\u0115"+
		"\b\32\1\2\u0115\u0116\5\64\33\2\u0116\u011c\3\2\2\2\u0117\u0118\f\4\2"+
		"\2\u0118\u0119\t\b\2\2\u0119\u011b\5\64\33\2\u011a\u0117\3\2\2\2\u011b"+
		"\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\63\3\2\2"+
		"\2\u011e\u011c\3\2\2\2\u011f\u0120\7!\2\2\u0120\u0123\5\64\33\2\u0121"+
		"\u0123\5\66\34\2\u0122\u011f\3\2\2\2\u0122\u0121\3\2\2\2\u0123\65\3\2"+
		"\2\2\u0124\u012b\t\t\2\2\u0125\u012b\7<\2\2\u0126\u0127\7\61\2\2\u0127"+
		"\u0128\5*\26\2\u0128\u0129\7\62\2\2\u0129\u012b\3\2\2\2\u012a\u0124\3"+
		"\2\2\2\u012a\u0125\3\2\2\2\u012a\u0126\3\2\2\2\u012b\67\3\2\2\2\34;CI"+
		"OZacps}\u008a\u008d\u009b\u00a7\u00af\u00ba\u00d1\u00d6\u00e1\u00f5\u00fc"+
		"\u0106\u0111\u011c\u0122\u012a";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}