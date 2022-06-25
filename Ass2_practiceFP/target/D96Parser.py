# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u020b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\3\2\6\2l\n\2\r\2\16\2m\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\5\3v\n\3\3\3\3\3\7\3z\n\3\f\3\16\3}\13\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\5\4\u0085\n\4\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\5\6\u008d\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\5\7\u009b\n\7\3\b\3\b\3\b\7\b\u00a0\n\b\f\b\16")
        buf.write("\b\u00a3\13\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\5\13\u00b3\n\13\3\f\3\f\3\f\5\f\u00b8")
        buf.write("\n\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\5\16\u00c2\n\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\7\20\u00cf\n\20\f\20\16\20\u00d2\13\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\7\22\u00db\n\22\f\22\16\22\u00de")
        buf.write("\13\22\3\23\3\23\7\23\u00e2\n\23\f\23\16\23\u00e5\13\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\5\24\u00f2\n\24\3\25\3\25\3\25\3\25\3\26\3\26\5\26\u00fa")
        buf.write("\n\26\3\27\3\27\3\27\7\27\u00ff\n\27\f\27\16\27\u0102")
        buf.write("\13\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\5\30\u0113\n\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\5\32\u011c\n\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\5\33\u0123\n\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u012d\n\34\3\34\3\34\3\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\7\35")
        buf.write("\u013d\n\35\f\35\16\35\u0140\13\35\3\35\3\35\5\35\u0144")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36")
        buf.write("\u014f\n\36\3\36\3\36\3\36\3\37\3\37\5\37\u0156\n\37\3")
        buf.write("\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\5\"\u0165")
        buf.write("\n\"\3#\3#\3#\3#\3#\5#\u016c\n#\3$\3$\3$\3$\3$\3$\7$\u0174")
        buf.write("\n$\f$\16$\u0177\13$\3%\3%\3%\3%\3%\3%\7%\u017f\n%\f%")
        buf.write("\16%\u0182\13%\3&\3&\3&\3&\3&\3&\7&\u018a\n&\f&\16&\u018d")
        buf.write("\13&\3\'\3\'\3\'\5\'\u0192\n\'\3(\3(\3(\5(\u0197\n(\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\6)\u01a1\n)\r)\16)\u01a2\7)\u01a5")
        buf.write("\n)\f)\16)\u01a8\13)\3*\3*\3*\3*\3*\3*\3*\3*\5*\u01b2")
        buf.write("\n*\3*\5*\u01b5\n*\7*\u01b7\n*\f*\16*\u01ba\13*\3+\3+")
        buf.write("\3+\3+\3+\5+\u01c1\n+\3+\5+\u01c4\n+\3+\5+\u01c7\n+\3")
        buf.write(",\3,\3,\3,\5,\u01cd\n,\3,\3,\3,\5,\u01d2\n,\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u01e1\n.\3/\3/\3\60\3")
        buf.write("\60\3\60\5\60\u01e8\n\60\3\60\5\60\u01eb\n\60\3\61\3\61")
        buf.write("\3\61\5\61\u01f0\n\61\3\61\5\61\u01f3\n\61\3\62\3\62\3")
        buf.write("\62\5\62\u01f8\n\62\3\62\3\62\3\63\3\63\3\63\5\63\u01ff")
        buf.write("\n\63\3\64\3\64\3\64\7\64\u0204\n\64\f\64\16\64\u0207")
        buf.write("\13\64\3\65\3\65\3\65\2\7FHJPR\66\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfh\2\13\3\2\f\17\4\2\31\31BB\3\2#$\3\2%*\3\2")
        buf.write("!\"\3\2\33\34\3\2\35\37\4\2++\61\64\3\2\25\26\2\u0215")
        buf.write("\2k\3\2\2\2\4q\3\2\2\2\6\u0084\3\2\2\2\b\u0086\3\2\2\2")
        buf.write("\n\u008c\3\2\2\2\f\u009a\3\2\2\2\16\u009c\3\2\2\2\20\u00a7")
        buf.write("\3\2\2\2\22\u00a9\3\2\2\2\24\u00b2\3\2\2\2\26\u00b4\3")
        buf.write("\2\2\2\30\u00bc\3\2\2\2\32\u00be\3\2\2\2\34\u00c6\3\2")
        buf.write("\2\2\36\u00cb\3\2\2\2 \u00d3\3\2\2\2\"\u00d7\3\2\2\2$")
        buf.write("\u00df\3\2\2\2&\u00f1\3\2\2\2(\u00f3\3\2\2\2*\u00f9\3")
        buf.write("\2\2\2,\u00fb\3\2\2\2.\u0112\3\2\2\2\60\u0114\3\2\2\2")
        buf.write("\62\u011b\3\2\2\2\64\u011d\3\2\2\2\66\u0127\3\2\2\28\u0131")
        buf.write("\3\2\2\2:\u0145\3\2\2\2<\u0153\3\2\2\2>\u0159\3\2\2\2")
        buf.write("@\u015c\3\2\2\2B\u0164\3\2\2\2D\u016b\3\2\2\2F\u016d\3")
        buf.write("\2\2\2H\u0178\3\2\2\2J\u0183\3\2\2\2L\u0191\3\2\2\2N\u0196")
        buf.write("\3\2\2\2P\u0198\3\2\2\2R\u01a9\3\2\2\2T\u01c6\3\2\2\2")
        buf.write("V\u01d1\3\2\2\2X\u01d3\3\2\2\2Z\u01e0\3\2\2\2\\\u01e2")
        buf.write("\3\2\2\2^\u01e4\3\2\2\2`\u01ec\3\2\2\2b\u01f4\3\2\2\2")
        buf.write("d\u01fe\3\2\2\2f\u0200\3\2\2\2h\u0208\3\2\2\2jl\5\4\3")
        buf.write("\2kj\3\2\2\2lm\3\2\2\2mk\3\2\2\2mn\3\2\2\2no\3\2\2\2o")
        buf.write("p\7\2\2\3p\3\3\2\2\2qr\7\24\2\2ru\7B\2\2st\7=\2\2tv\7")
        buf.write("B\2\2us\3\2\2\2uv\3\2\2\2vw\3\2\2\2w{\78\2\2xz\5\6\4\2")
        buf.write("yx\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|~\3\2\2\2}{\3")
        buf.write("\2\2\2~\177\79\2\2\177\5\3\2\2\2\u0080\u0085\5\b\5\2\u0081")
        buf.write("\u0085\5\26\f\2\u0082\u0085\5\32\16\2\u0083\u0085\5\34")
        buf.write("\17\2\u0084\u0080\3\2\2\2\u0084\u0081\3\2\2\2\u0084\u0082")
        buf.write("\3\2\2\2\u0084\u0083\3\2\2\2\u0085\7\3\2\2\2\u0086\u0087")
        buf.write("\5h\65\2\u0087\u0088\5\n\6\2\u0088\u0089\7A\2\2\u0089")
        buf.write("\t\3\2\2\2\u008a\u008d\5\f\7\2\u008b\u008d\5\16\b\2\u008c")
        buf.write("\u008a\3\2\2\2\u008c\u008b\3\2\2\2\u008d\13\3\2\2\2\u008e")
        buf.write("\u008f\5\30\r\2\u008f\u0090\7=\2\2\u0090\u0091\5d\63\2")
        buf.write("\u0091\u0092\7\32\2\2\u0092\u0093\5B\"\2\u0093\u009b\3")
        buf.write("\2\2\2\u0094\u0095\5\30\r\2\u0095\u0096\7@\2\2\u0096\u0097")
        buf.write("\5\f\7\2\u0097\u0098\7@\2\2\u0098\u0099\5B\"\2\u0099\u009b")
        buf.write("\3\2\2\2\u009a\u008e\3\2\2\2\u009a\u0094\3\2\2\2\u009b")
        buf.write("\r\3\2\2\2\u009c\u00a1\5\30\r\2\u009d\u009e\7@\2\2\u009e")
        buf.write("\u00a0\5\30\r\2\u009f\u009d\3\2\2\2\u00a0\u00a3\3\2\2")
        buf.write("\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a4")
        buf.write("\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\7=\2\2\u00a5")
        buf.write("\u00a6\5d\63\2\u00a6\17\3\2\2\2\u00a7\u00a8\t\2\2\2\u00a8")
        buf.write("\21\3\2\2\2\u00a9\u00aa\7\t\2\2\u00aa\u00ab\7:\2\2\u00ab")
        buf.write("\u00ac\5\24\13\2\u00ac\u00ad\7@\2\2\u00ad\u00ae\7+\2\2")
        buf.write("\u00ae\u00af\7;\2\2\u00af\23\3\2\2\2\u00b0\u00b3\5\22")
        buf.write("\n\2\u00b1\u00b3\5\20\t\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1")
        buf.write("\3\2\2\2\u00b3\25\3\2\2\2\u00b4\u00b5\5\30\r\2\u00b5\u00b7")
        buf.write("\7\66\2\2\u00b6\u00b8\5\36\20\2\u00b7\u00b6\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\7\67\2")
        buf.write("\2\u00ba\u00bb\5$\23\2\u00bb\27\3\2\2\2\u00bc\u00bd\t")
        buf.write("\3\2\2\u00bd\31\3\2\2\2\u00be\u00bf\7\27\2\2\u00bf\u00c1")
        buf.write("\7\66\2\2\u00c0\u00c2\5\36\20\2\u00c1\u00c0\3\2\2\2\u00c1")
        buf.write("\u00c2\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\7\67\2")
        buf.write("\2\u00c4\u00c5\5$\23\2\u00c5\33\3\2\2\2\u00c6\u00c7\7")
        buf.write("\30\2\2\u00c7\u00c8\7\66\2\2\u00c8\u00c9\7\67\2\2\u00c9")
        buf.write("\u00ca\5$\23\2\u00ca\35\3\2\2\2\u00cb\u00d0\5 \21\2\u00cc")
        buf.write("\u00cd\7A\2\2\u00cd\u00cf\5 \21\2\u00ce\u00cc\3\2\2\2")
        buf.write("\u00cf\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3")
        buf.write("\2\2\2\u00d1\37\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d4")
        buf.write("\5\"\22\2\u00d4\u00d5\7=\2\2\u00d5\u00d6\5d\63\2\u00d6")
        buf.write("!\3\2\2\2\u00d7\u00dc\7B\2\2\u00d8\u00d9\7@\2\2\u00d9")
        buf.write("\u00db\7B\2\2\u00da\u00d8\3\2\2\2\u00db\u00de\3\2\2\2")
        buf.write("\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd#\3\2\2")
        buf.write("\2\u00de\u00dc\3\2\2\2\u00df\u00e3\78\2\2\u00e0\u00e2")
        buf.write("\5&\24\2\u00e1\u00e0\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e6\3\2\2\2")
        buf.write("\u00e5\u00e3\3\2\2\2\u00e6\u00e7\79\2\2\u00e7%\3\2\2\2")
        buf.write("\u00e8\u00f2\5(\25\2\u00e9\u00f2\5\60\31\2\u00ea\u00f2")
        buf.write("\58\35\2\u00eb\u00f2\5:\36\2\u00ec\u00f2\5<\37\2\u00ed")
        buf.write("\u00f2\5> \2\u00ee\u00f2\5@!\2\u00ef\u00f2\5$\23\2\u00f0")
        buf.write("\u00f2\5\62\32\2\u00f1\u00e8\3\2\2\2\u00f1\u00e9\3\2\2")
        buf.write("\2\u00f1\u00ea\3\2\2\2\u00f1\u00eb\3\2\2\2\u00f1\u00ec")
        buf.write("\3\2\2\2\u00f1\u00ed\3\2\2\2\u00f1\u00ee\3\2\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2\'\3\2\2\2\u00f3")
        buf.write("\u00f4\5h\65\2\u00f4\u00f5\5*\26\2\u00f5\u00f6\7A\2\2")
        buf.write("\u00f6)\3\2\2\2\u00f7\u00fa\5,\27\2\u00f8\u00fa\5.\30")
        buf.write("\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa+\3\2")
        buf.write("\2\2\u00fb\u0100\7B\2\2\u00fc\u00fd\7@\2\2\u00fd\u00ff")
        buf.write("\7B\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0102\3\2\2\2\u0100")
        buf.write("\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0103\3\2\2\2")
        buf.write("\u0102\u0100\3\2\2\2\u0103\u0104\7=\2\2\u0104\u0105\5")
        buf.write("d\63\2\u0105-\3\2\2\2\u0106\u0107\7B\2\2\u0107\u0108\7")
        buf.write("=\2\2\u0108\u0109\5d\63\2\u0109\u010a\7\32\2\2\u010a\u010b")
        buf.write("\5B\"\2\u010b\u0113\3\2\2\2\u010c\u010d\7B\2\2\u010d\u010e")
        buf.write("\7@\2\2\u010e\u010f\5.\30\2\u010f\u0110\7@\2\2\u0110\u0111")
        buf.write("\5B\"\2\u0111\u0113\3\2\2\2\u0112\u0106\3\2\2\2\u0112")
        buf.write("\u010c\3\2\2\2\u0113/\3\2\2\2\u0114\u0115\5P)\2\u0115")
        buf.write("\u0116\7\32\2\2\u0116\u0117\5B\"\2\u0117\u0118\7A\2\2")
        buf.write("\u0118\61\3\2\2\2\u0119\u011c\5\64\33\2\u011a\u011c\5")
        buf.write("\66\34\2\u011b\u0119\3\2\2\2\u011b\u011a\3\2\2\2\u011c")
        buf.write("\63\3\2\2\2\u011d\u011e\5P)\2\u011e\u011f\7?\2\2\u011f")
        buf.write("\u0120\7B\2\2\u0120\u0122\7\66\2\2\u0121\u0123\5f\64\2")
        buf.write("\u0122\u0121\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\3")
        buf.write("\2\2\2\u0124\u0125\7\67\2\2\u0125\u0126\7A\2\2\u0126\65")
        buf.write("\3\2\2\2\u0127\u0128\5P)\2\u0128\u0129\7<\2\2\u0129\u012a")
        buf.write("\7\31\2\2\u012a\u012c\7\66\2\2\u012b\u012d\5f\64\2\u012c")
        buf.write("\u012b\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012e\3\2\2\2")
        buf.write("\u012e\u012f\7\67\2\2\u012f\u0130\7A\2\2\u0130\67\3\2")
        buf.write("\2\2\u0131\u0132\7\5\2\2\u0132\u0133\7\66\2\2\u0133\u0134")
        buf.write("\5B\"\2\u0134\u0135\7\67\2\2\u0135\u013e\5$\23\2\u0136")
        buf.write("\u0137\7\6\2\2\u0137\u0138\7\66\2\2\u0138\u0139\5B\"\2")
        buf.write("\u0139\u013a\7\67\2\2\u013a\u013b\5$\23\2\u013b\u013d")
        buf.write("\3\2\2\2\u013c\u0136\3\2\2\2\u013d\u0140\3\2\2\2\u013e")
        buf.write("\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0143\3\2\2\2")
        buf.write("\u0140\u013e\3\2\2\2\u0141\u0142\7\7\2\2\u0142\u0144\5")
        buf.write("$\23\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u01449")
        buf.write("\3\2\2\2\u0145\u0146\7\b\2\2\u0146\u0147\7\66\2\2\u0147")
        buf.write("\u0148\7B\2\2\u0148\u0149\7\n\2\2\u0149\u014a\5B\"\2\u014a")
        buf.write("\u014b\7>\2\2\u014b\u014e\5B\"\2\u014c\u014d\7\13\2\2")
        buf.write("\u014d\u014f\5B\"\2\u014e\u014c\3\2\2\2\u014e\u014f\3")
        buf.write("\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\7\67\2\2\u0151")
        buf.write("\u0152\5$\23\2\u0152;\3\2\2\2\u0153\u0155\7\21\2\2\u0154")
        buf.write("\u0156\5B\"\2\u0155\u0154\3\2\2\2\u0155\u0156\3\2\2\2")
        buf.write("\u0156\u0157\3\2\2\2\u0157\u0158\7A\2\2\u0158=\3\2\2\2")
        buf.write("\u0159\u015a\7\3\2\2\u015a\u015b\7A\2\2\u015b?\3\2\2\2")
        buf.write("\u015c\u015d\7\4\2\2\u015d\u015e\7A\2\2\u015eA\3\2\2\2")
        buf.write("\u015f\u0160\5D#\2\u0160\u0161\t\4\2\2\u0161\u0162\5D")
        buf.write("#\2\u0162\u0165\3\2\2\2\u0163\u0165\5D#\2\u0164\u015f")
        buf.write("\3\2\2\2\u0164\u0163\3\2\2\2\u0165C\3\2\2\2\u0166\u0167")
        buf.write("\5F$\2\u0167\u0168\t\5\2\2\u0168\u0169\5F$\2\u0169\u016c")
        buf.write("\3\2\2\2\u016a\u016c\5F$\2\u016b\u0166\3\2\2\2\u016b\u016a")
        buf.write("\3\2\2\2\u016cE\3\2\2\2\u016d\u016e\b$\1\2\u016e\u016f")
        buf.write("\5H%\2\u016f\u0175\3\2\2\2\u0170\u0171\f\4\2\2\u0171\u0172")
        buf.write("\t\6\2\2\u0172\u0174\5H%\2\u0173\u0170\3\2\2\2\u0174\u0177")
        buf.write("\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176")
        buf.write("G\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0179\b%\1\2\u0179")
        buf.write("\u017a\5J&\2\u017a\u0180\3\2\2\2\u017b\u017c\f\4\2\2\u017c")
        buf.write("\u017d\t\7\2\2\u017d\u017f\5J&\2\u017e\u017b\3\2\2\2\u017f")
        buf.write("\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181I\3\2\2\2\u0182\u0180\3\2\2\2\u0183\u0184\b&\1\2")
        buf.write("\u0184\u0185\5L\'\2\u0185\u018b\3\2\2\2\u0186\u0187\f")
        buf.write("\4\2\2\u0187\u0188\t\b\2\2\u0188\u018a\5L\'\2\u0189\u0186")
        buf.write("\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b")
        buf.write("\u018c\3\2\2\2\u018cK\3\2\2\2\u018d\u018b\3\2\2\2\u018e")
        buf.write("\u018f\7 \2\2\u018f\u0192\5L\'\2\u0190\u0192\5N(\2\u0191")
        buf.write("\u018e\3\2\2\2\u0191\u0190\3\2\2\2\u0192M\3\2\2\2\u0193")
        buf.write("\u0194\7\34\2\2\u0194\u0197\5N(\2\u0195\u0197\5P)\2\u0196")
        buf.write("\u0193\3\2\2\2\u0196\u0195\3\2\2\2\u0197O\3\2\2\2\u0198")
        buf.write("\u0199\b)\1\2\u0199\u019a\5R*\2\u019a\u01a6\3\2\2\2\u019b")
        buf.write("\u01a0\f\4\2\2\u019c\u019d\7:\2\2\u019d\u019e\5B\"\2\u019e")
        buf.write("\u019f\7;\2\2\u019f\u01a1\3\2\2\2\u01a0\u019c\3\2\2\2")
        buf.write("\u01a1\u01a2\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3")
        buf.write("\2\2\2\u01a3\u01a5\3\2\2\2\u01a4\u019b\3\2\2\2\u01a5\u01a8")
        buf.write("\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7")
        buf.write("Q\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01aa\b*\1\2\u01aa")
        buf.write("\u01ab\5T+\2\u01ab\u01b8\3\2\2\2\u01ac\u01ad\f\4\2\2\u01ad")
        buf.write("\u01ae\7?\2\2\u01ae\u01b4\7B\2\2\u01af\u01b1\7\66\2\2")
        buf.write("\u01b0\u01b2\5f\64\2\u01b1\u01b0\3\2\2\2\u01b1\u01b2\3")
        buf.write("\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5\7\67\2\2\u01b4")
        buf.write("\u01af\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b7\3\2\2\2")
        buf.write("\u01b6\u01ac\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3")
        buf.write("\2\2\2\u01b8\u01b9\3\2\2\2\u01b9S\3\2\2\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01bb\u01bc\7B\2\2\u01bc\u01bd\7<\2\2\u01bd\u01c3")
        buf.write("\7\31\2\2\u01be\u01c0\7\66\2\2\u01bf\u01c1\5f\64\2\u01c0")
        buf.write("\u01bf\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2\3\2\2\2")
        buf.write("\u01c2\u01c4\7\67\2\2\u01c3\u01be\3\2\2\2\u01c3\u01c4")
        buf.write("\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c7\5V,\2\u01c6\u01bb")
        buf.write("\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7U\3\2\2\2\u01c8\u01c9")
        buf.write("\7\23\2\2\u01c9\u01ca\5V,\2\u01ca\u01cc\7\66\2\2\u01cb")
        buf.write("\u01cd\5f\64\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd\3\2\2\2")
        buf.write("\u01cd\u01ce\3\2\2\2\u01ce\u01cf\7\67\2\2\u01cf\u01d2")
        buf.write("\3\2\2\2\u01d0\u01d2\5Z.\2\u01d1\u01c8\3\2\2\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d2W\3\2\2\2\u01d3\u01d4\7:\2\2\u01d4\u01d5")
        buf.write("\5B\"\2\u01d5\u01d6\7;\2\2\u01d6Y\3\2\2\2\u01d7\u01e1")
        buf.write("\5\\/\2\u01d8\u01e1\7B\2\2\u01d9\u01da\7\66\2\2\u01da")
        buf.write("\u01db\5B\"\2\u01db\u01dc\7\67\2\2\u01dc\u01e1\3\2\2\2")
        buf.write("\u01dd\u01e1\5b\62\2\u01de\u01e1\7\22\2\2\u01df\u01e1")
        buf.write("\7\20\2\2\u01e0\u01d7\3\2\2\2\u01e0\u01d8\3\2\2\2\u01e0")
        buf.write("\u01d9\3\2\2\2\u01e0\u01dd\3\2\2\2\u01e0\u01de\3\2\2\2")
        buf.write("\u01e0\u01df\3\2\2\2\u01e1[\3\2\2\2\u01e2\u01e3\t\t\2")
        buf.write("\2\u01e3]\3\2\2\2\u01e4\u01ea\7\31\2\2\u01e5\u01e7\7\66")
        buf.write("\2\2\u01e6\u01e8\5f\64\2\u01e7\u01e6\3\2\2\2\u01e7\u01e8")
        buf.write("\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01eb\7\67\2\2\u01ea")
        buf.write("\u01e5\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb_\3\2\2\2\u01ec")
        buf.write("\u01f2\7B\2\2\u01ed\u01ef\7\66\2\2\u01ee\u01f0\5f\64\2")
        buf.write("\u01ef\u01ee\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1\3")
        buf.write("\2\2\2\u01f1\u01f3\7\67\2\2\u01f2\u01ed\3\2\2\2\u01f2")
        buf.write("\u01f3\3\2\2\2\u01f3a\3\2\2\2\u01f4\u01f5\7\t\2\2\u01f5")
        buf.write("\u01f7\7\66\2\2\u01f6\u01f8\5f\64\2\u01f7\u01f6\3\2\2")
        buf.write("\2\u01f7\u01f8\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fa")
        buf.write("\7\67\2\2\u01fac\3\2\2\2\u01fb\u01ff\5\20\t\2\u01fc\u01ff")
        buf.write("\5\22\n\2\u01fd\u01ff\7B\2\2\u01fe\u01fb\3\2\2\2\u01fe")
        buf.write("\u01fc\3\2\2\2\u01fe\u01fd\3\2\2\2\u01ffe\3\2\2\2\u0200")
        buf.write("\u0205\5B\"\2\u0201\u0202\7@\2\2\u0202\u0204\5B\"\2\u0203")
        buf.write("\u0201\3\2\2\2\u0204\u0207\3\2\2\2\u0205\u0203\3\2\2\2")
        buf.write("\u0205\u0206\3\2\2\2\u0206g\3\2\2\2\u0207\u0205\3\2\2")
        buf.write("\2\u0208\u0209\t\n\2\2\u0209i\3\2\2\2\63mu{\u0084\u008c")
        buf.write("\u009a\u00a1\u00b2\u00b7\u00c1\u00d0\u00dc\u00e3\u00f1")
        buf.write("\u00f9\u0100\u0112\u011b\u0122\u012c\u013e\u0143\u014e")
        buf.write("\u0155\u0164\u016b\u0175\u0180\u018b\u0191\u0196\u01a2")
        buf.write("\u01a6\u01b1\u01b4\u01b8\u01c0\u01c3\u01c6\u01cc\u01d1")
        buf.write("\u01e0\u01e7\u01ea\u01ef\u01f2\u01f7\u01fe\u0205")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'Array'", "'In'", "'By'", "'Int'", 
                     "'Float'", "'Boolean'", "'String'", "'Null'", "'Return'", 
                     "'Self'", "'New'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
                     "'Destructor'", "<INVALID>", "'='", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'!'", "'&&'", "'||'", "'==.'", "'+.'", 
                     "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "'::'", "':'", "'..'", "'.'", "','", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "ARRAY", "IN", "BY", "INT_TYPE", 
                      "FLOAT_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", "NULL", 
                      "RETURN", "SELF", "NEW", "CLASS", "IMMUTABLE", "MUTABLE", 
                      "CONSTRUCTOR", "DESTRUCTOR", "DOLLAR_ID", "ASSIGN", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                      "STRCOMPARE", "CONCATE", "EQUAL", "NOTEQUAL", "LARGER", 
                      "SMALLER", "LE", "SE", "INTLIT_ARR", "INT_LIT_ARR", 
                      "BIN_", "DEC_", "OCTAL_", "HEXA_", "INT_LITERAL", 
                      "BOOL_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
                      "BLOCK_COMMENT", "LB", "RB", "LP", "RP", "LS", "RS", 
                      "DOUBLE_COLON", "COLON", "DOUBLEDOT", "DOT", "COMMA", 
                      "SEMI_COLON", "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_declaration = 1
    RULE_member = 2
    RULE_attribute_declaration = 3
    RULE_attribute_decl_list = 4
    RULE_testing = 5
    RULE_testing2 = 6
    RULE_primitive_type = 7
    RULE_array_type = 8
    RULE_type_in_array = 9
    RULE_method_declaration = 10
    RULE_att_name = 11
    RULE_constructor = 12
    RULE_destructor = 13
    RULE_parameter_decl_list = 14
    RULE_parameter_decl = 15
    RULE_ids_list = 16
    RULE_block_statement = 17
    RULE_statement = 18
    RULE_var_declare_statement = 19
    RULE_var_decl_list = 20
    RULE_var_decl_stm_only = 21
    RULE_var_decl_stm_assign = 22
    RULE_assign_statement = 23
    RULE_call_stmt = 24
    RULE_instance_call_stmt = 25
    RULE_static_call_stmt = 26
    RULE_if_statement = 27
    RULE_for_statement = 28
    RULE_return_statement = 29
    RULE_break_statement = 30
    RULE_continue_statement = 31
    RULE_expression = 32
    RULE_expression1 = 33
    RULE_expression2 = 34
    RULE_expression3 = 35
    RULE_expression4 = 36
    RULE_expression5 = 37
    RULE_expression6 = 38
    RULE_expression7 = 39
    RULE_expression8 = 40
    RULE_expression9 = 41
    RULE_expression10 = 42
    RULE_index_operator = 43
    RULE_operands = 44
    RULE_literals = 45
    RULE_dollar_function = 46
    RULE_function_call = 47
    RULE_indexed_array = 48
    RULE_compound_type = 49
    RULE_expressions_list = 50
    RULE_attribute_type = 51

    ruleNames =  [ "program", "class_declaration", "member", "attribute_declaration", 
                   "attribute_decl_list", "testing", "testing2", "primitive_type", 
                   "array_type", "type_in_array", "method_declaration", 
                   "att_name", "constructor", "destructor", "parameter_decl_list", 
                   "parameter_decl", "ids_list", "block_statement", "statement", 
                   "var_declare_statement", "var_decl_list", "var_decl_stm_only", 
                   "var_decl_stm_assign", "assign_statement", "call_stmt", 
                   "instance_call_stmt", "static_call_stmt", "if_statement", 
                   "for_statement", "return_statement", "break_statement", 
                   "continue_statement", "expression", "expression1", "expression2", 
                   "expression3", "expression4", "expression5", "expression6", 
                   "expression7", "expression8", "expression9", "expression10", 
                   "index_operator", "operands", "literals", "dollar_function", 
                   "function_call", "indexed_array", "compound_type", "expressions_list", 
                   "attribute_type" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSEIF=4
    ELSE=5
    FOREACH=6
    ARRAY=7
    IN=8
    BY=9
    INT_TYPE=10
    FLOAT_TYPE=11
    BOOLEAN_TYPE=12
    STRING_TYPE=13
    NULL=14
    RETURN=15
    SELF=16
    NEW=17
    CLASS=18
    IMMUTABLE=19
    MUTABLE=20
    CONSTRUCTOR=21
    DESTRUCTOR=22
    DOLLAR_ID=23
    ASSIGN=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    MOD=29
    NOT=30
    AND=31
    OR=32
    STRCOMPARE=33
    CONCATE=34
    EQUAL=35
    NOTEQUAL=36
    LARGER=37
    SMALLER=38
    LE=39
    SE=40
    INTLIT_ARR=41
    INT_LIT_ARR=42
    BIN_=43
    DEC_=44
    OCTAL_=45
    HEXA_=46
    INT_LITERAL=47
    BOOL_LITERAL=48
    FLOAT_LITERAL=49
    STRING_LITERAL=50
    BLOCK_COMMENT=51
    LB=52
    RB=53
    LP=54
    RP=55
    LS=56
    RS=57
    DOUBLE_COLON=58
    COLON=59
    DOUBLEDOT=60
    DOT=61
    COMMA=62
    SEMI_COLON=63
    ID=64
    WS=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67
    ERROR_CHAR=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self.class_declaration()
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 109
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.MemberContext)
            else:
                return self.getTypedRuleContext(D96Parser.MemberContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_class_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(D96Parser.CLASS)
            self.state = 112
            self.match(D96Parser.ID)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 113
                self.match(D96Parser.COLON)
                self.state = 114
                self.match(D96Parser.ID)


            self.state = 117
            self.match(D96Parser.LP)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 19)) & ~0x3f) == 0 and ((1 << (_la - 19)) & ((1 << (D96Parser.IMMUTABLE - 19)) | (1 << (D96Parser.MUTABLE - 19)) | (1 << (D96Parser.CONSTRUCTOR - 19)) | (1 << (D96Parser.DESTRUCTOR - 19)) | (1 << (D96Parser.DOLLAR_ID - 19)) | (1 << (D96Parser.ID - 19)))) != 0):
                self.state = 118
                self.member()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declaration(self):
            return self.getTypedRuleContext(D96Parser.Attribute_declarationContext,0)


        def method_declaration(self):
            return self.getTypedRuleContext(D96Parser.Method_declarationContext,0)


        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_member)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IMMUTABLE, D96Parser.MUTABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.attribute_declaration()
                pass
            elif token in [D96Parser.DOLLAR_ID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.method_declaration()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.destructor()
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


    class Attribute_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_type(self):
            return self.getTypedRuleContext(D96Parser.Attribute_typeContext,0)


        def attribute_decl_list(self):
            return self.getTypedRuleContext(D96Parser.Attribute_decl_listContext,0)


        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_declaration" ):
                return visitor.visitAttribute_declaration(self)
            else:
                return visitor.visitChildren(self)




    def attribute_declaration(self):

        localctx = D96Parser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.attribute_type()
            self.state = 133
            self.attribute_decl_list()
            self.state = 134
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def testing(self):
            return self.getTypedRuleContext(D96Parser.TestingContext,0)


        def testing2(self):
            return self.getTypedRuleContext(D96Parser.Testing2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_decl_list" ):
                return visitor.visitAttribute_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def attribute_decl_list(self):

        localctx = D96Parser.Attribute_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_decl_list)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.testing()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.testing2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def att_name(self):
            return self.getTypedRuleContext(D96Parser.Att_nameContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def compound_type(self):
            return self.getTypedRuleContext(D96Parser.Compound_typeContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def testing(self):
            return self.getTypedRuleContext(D96Parser.TestingContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_testing

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTesting" ):
                return visitor.visitTesting(self)
            else:
                return visitor.visitChildren(self)




    def testing(self):

        localctx = D96Parser.TestingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_testing)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.att_name()

                self.state = 141
                self.match(D96Parser.COLON)
                self.state = 142
                self.compound_type()

                self.state = 143
                self.match(D96Parser.ASSIGN)
                self.state = 144
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.att_name()
                self.state = 147
                self.match(D96Parser.COMMA)
                self.state = 148
                self.testing()

                self.state = 149
                self.match(D96Parser.COMMA)
                self.state = 150
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Testing2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def att_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Att_nameContext)
            else:
                return self.getTypedRuleContext(D96Parser.Att_nameContext,i)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def compound_type(self):
            return self.getTypedRuleContext(D96Parser.Compound_typeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_testing2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTesting2" ):
                return visitor.visitTesting2(self)
            else:
                return visitor.visitChildren(self)




    def testing2(self):

        localctx = D96Parser.Testing2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_testing2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.att_name()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 155
                self.match(D96Parser.COMMA)
                self.state = 156
                self.att_name()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self.match(D96Parser.COLON)
            self.state = 163
            self.compound_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(D96Parser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(D96Parser.FLOAT_TYPE, 0)

        def BOOLEAN_TYPE(self):
            return self.getToken(D96Parser.BOOLEAN_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(D96Parser.STRING_TYPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT_TYPE) | (1 << D96Parser.FLOAT_TYPE) | (1 << D96Parser.BOOLEAN_TYPE) | (1 << D96Parser.STRING_TYPE))) != 0)):
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


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def type_in_array(self):
            return self.getTypedRuleContext(D96Parser.Type_in_arrayContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def INTLIT_ARR(self):
            return self.getToken(D96Parser.INTLIT_ARR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(D96Parser.ARRAY)
            self.state = 168
            self.match(D96Parser.LS)
            self.state = 169
            self.type_in_array()
            self.state = 170
            self.match(D96Parser.COMMA)

            self.state = 171
            self.match(D96Parser.INTLIT_ARR)
            self.state = 172
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_in_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_type_in_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_in_array" ):
                return visitor.visitType_in_array(self)
            else:
                return visitor.visitChildren(self)




    def type_in_array(self):

        localctx = D96Parser.Type_in_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type_in_array)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.array_type()
                pass
            elif token in [D96Parser.INT_TYPE, D96Parser.FLOAT_TYPE, D96Parser.BOOLEAN_TYPE, D96Parser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.primitive_type()
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


    class Method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def att_name(self):
            return self.getTypedRuleContext(D96Parser.Att_nameContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def parameter_decl_list(self):
            return self.getTypedRuleContext(D96Parser.Parameter_decl_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declaration" ):
                return visitor.visitMethod_declaration(self)
            else:
                return visitor.visitChildren(self)




    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.att_name()
            self.state = 179
            self.match(D96Parser.LB)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 180
                self.parameter_decl_list()


            self.state = 183
            self.match(D96Parser.RB)
            self.state = 184
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Att_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_att_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt_name" ):
                return visitor.visitAtt_name(self)
            else:
                return visitor.visitChildren(self)




    def att_name(self):

        localctx = D96Parser.Att_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_att_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            _la = self._input.LA(1)
            if not(_la==D96Parser.DOLLAR_ID or _la==D96Parser.ID):
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


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def parameter_decl_list(self):
            return self.getTypedRuleContext(D96Parser.Parameter_decl_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 189
            self.match(D96Parser.LB)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 190
                self.parameter_decl_list()


            self.state = 193
            self.match(D96Parser.RB)
            self.state = 194
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(D96Parser.DESTRUCTOR)
            self.state = 197
            self.match(D96Parser.LB)
            self.state = 198
            self.match(D96Parser.RB)
            self.state = 199
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Parameter_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Parameter_declContext,i)


        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI_COLON)
            else:
                return self.getToken(D96Parser.SEMI_COLON, i)

        def getRuleIndex(self):
            return D96Parser.RULE_parameter_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_decl_list" ):
                return visitor.visitParameter_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_decl_list(self):

        localctx = D96Parser.Parameter_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parameter_decl_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.parameter_decl()
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI_COLON:
                self.state = 202
                self.match(D96Parser.SEMI_COLON)
                self.state = 203
                self.parameter_decl()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids_list(self):
            return self.getTypedRuleContext(D96Parser.Ids_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def compound_type(self):
            return self.getTypedRuleContext(D96Parser.Compound_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parameter_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_decl" ):
                return visitor.visitParameter_decl(self)
            else:
                return visitor.visitChildren(self)




    def parameter_decl(self):

        localctx = D96Parser.Parameter_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parameter_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.ids_list()
            self.state = 210
            self.match(D96Parser.COLON)
            self.state = 211
            self.compound_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_ids_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds_list" ):
                return visitor.visitIds_list(self)
            else:
                return visitor.visitChildren(self)




    def ids_list(self):

        localctx = D96Parser.Ids_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ids_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(D96Parser.ID)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 214
                self.match(D96Parser.COMMA)
                self.state = 215
                self.match(D96Parser.ID)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StatementContext)
            else:
                return self.getTypedRuleContext(D96Parser.StatementContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = D96Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(D96Parser.LP)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (D96Parser.BREAK - 1)) | (1 << (D96Parser.CONTINUE - 1)) | (1 << (D96Parser.IF - 1)) | (1 << (D96Parser.FOREACH - 1)) | (1 << (D96Parser.ARRAY - 1)) | (1 << (D96Parser.NULL - 1)) | (1 << (D96Parser.RETURN - 1)) | (1 << (D96Parser.SELF - 1)) | (1 << (D96Parser.NEW - 1)) | (1 << (D96Parser.IMMUTABLE - 1)) | (1 << (D96Parser.MUTABLE - 1)) | (1 << (D96Parser.INTLIT_ARR - 1)) | (1 << (D96Parser.INT_LITERAL - 1)) | (1 << (D96Parser.BOOL_LITERAL - 1)) | (1 << (D96Parser.FLOAT_LITERAL - 1)) | (1 << (D96Parser.STRING_LITERAL - 1)) | (1 << (D96Parser.LB - 1)) | (1 << (D96Parser.LP - 1)) | (1 << (D96Parser.ID - 1)))) != 0):
                self.state = 222
                self.statement()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 228
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare_statement(self):
            return self.getTypedRuleContext(D96Parser.Var_declare_statementContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(D96Parser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(D96Parser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(D96Parser.For_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(D96Parser.Return_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(D96Parser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(D96Parser.Continue_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(D96Parser.Call_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statement)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.var_declare_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 233
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 234
                self.return_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 235
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 236
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 237
                self.block_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 238
                self.call_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declare_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_type(self):
            return self.getTypedRuleContext(D96Parser.Attribute_typeContext,0)


        def var_decl_list(self):
            return self.getTypedRuleContext(D96Parser.Var_decl_listContext,0)


        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_declare_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare_statement" ):
                return visitor.visitVar_declare_statement(self)
            else:
                return visitor.visitChildren(self)




    def var_declare_statement(self):

        localctx = D96Parser.Var_declare_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_declare_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.attribute_type()
            self.state = 242
            self.var_decl_list()
            self.state = 243
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_stm_only(self):
            return self.getTypedRuleContext(D96Parser.Var_decl_stm_onlyContext,0)


        def var_decl_stm_assign(self):
            return self.getTypedRuleContext(D96Parser.Var_decl_stm_assignContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_list" ):
                return visitor.visitVar_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_list(self):

        localctx = D96Parser.Var_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_decl_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 245
                self.var_decl_stm_only()
                pass

            elif la_ == 2:
                self.state = 246
                self.var_decl_stm_assign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_stm_onlyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def compound_type(self):
            return self.getTypedRuleContext(D96Parser.Compound_typeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_var_decl_stm_only

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_stm_only" ):
                return visitor.visitVar_decl_stm_only(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_stm_only(self):

        localctx = D96Parser.Var_decl_stm_onlyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_var_decl_stm_only)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(D96Parser.ID)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 250
                self.match(D96Parser.COMMA)
                self.state = 251
                self.match(D96Parser.ID)
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 257
            self.match(D96Parser.COLON)
            self.state = 258
            self.compound_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_stm_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def compound_type(self):
            return self.getTypedRuleContext(D96Parser.Compound_typeContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def var_decl_stm_assign(self):
            return self.getTypedRuleContext(D96Parser.Var_decl_stm_assignContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_decl_stm_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_stm_assign" ):
                return visitor.visitVar_decl_stm_assign(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_stm_assign(self):

        localctx = D96Parser.Var_decl_stm_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_var_decl_stm_assign)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(D96Parser.ID)

                self.state = 261
                self.match(D96Parser.COLON)
                self.state = 262
                self.compound_type()

                self.state = 263
                self.match(D96Parser.ASSIGN)
                self.state = 264
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.match(D96Parser.ID)
                self.state = 267
                self.match(D96Parser.COMMA)
                self.state = 268
                self.var_decl_stm_assign()

                self.state = 269
                self.match(D96Parser.COMMA)
                self.state = 270
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(D96Parser.Expression7Context,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.expression7(0)
            self.state = 275
            self.match(D96Parser.ASSIGN)
            self.state = 276
            self.expression()
            self.state = 277
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_call_stmt(self):
            return self.getTypedRuleContext(D96Parser.Instance_call_stmtContext,0)


        def static_call_stmt(self):
            return self.getTypedRuleContext(D96Parser.Static_call_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = D96Parser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_call_stmt)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.instance_call_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.static_call_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(D96Parser.Expression7Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def expressions_list(self):
            return self.getTypedRuleContext(D96Parser.Expressions_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instance_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_call_stmt" ):
                return visitor.visitInstance_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def instance_call_stmt(self):

        localctx = D96Parser.Instance_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_instance_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.expression7(0)
            self.state = 284
            self.match(D96Parser.DOT)
            self.state = 285
            self.match(D96Parser.ID)
            self.state = 286
            self.match(D96Parser.LB)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (D96Parser.ARRAY - 7)) | (1 << (D96Parser.NULL - 7)) | (1 << (D96Parser.SELF - 7)) | (1 << (D96Parser.NEW - 7)) | (1 << (D96Parser.SUB - 7)) | (1 << (D96Parser.NOT - 7)) | (1 << (D96Parser.INTLIT_ARR - 7)) | (1 << (D96Parser.INT_LITERAL - 7)) | (1 << (D96Parser.BOOL_LITERAL - 7)) | (1 << (D96Parser.FLOAT_LITERAL - 7)) | (1 << (D96Parser.STRING_LITERAL - 7)) | (1 << (D96Parser.LB - 7)) | (1 << (D96Parser.ID - 7)))) != 0):
                self.state = 287
                self.expressions_list()


            self.state = 290
            self.match(D96Parser.RB)
            self.state = 291
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(D96Parser.Expression7Context,0)


        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def expressions_list(self):
            return self.getTypedRuleContext(D96Parser.Expressions_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_call_stmt" ):
                return visitor.visitStatic_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def static_call_stmt(self):

        localctx = D96Parser.Static_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_static_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.expression7(0)
            self.state = 294
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 295
            self.match(D96Parser.DOLLAR_ID)
            self.state = 296
            self.match(D96Parser.LB)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (D96Parser.ARRAY - 7)) | (1 << (D96Parser.NULL - 7)) | (1 << (D96Parser.SELF - 7)) | (1 << (D96Parser.NEW - 7)) | (1 << (D96Parser.SUB - 7)) | (1 << (D96Parser.NOT - 7)) | (1 << (D96Parser.INTLIT_ARR - 7)) | (1 << (D96Parser.INT_LITERAL - 7)) | (1 << (D96Parser.BOOL_LITERAL - 7)) | (1 << (D96Parser.FLOAT_LITERAL - 7)) | (1 << (D96Parser.STRING_LITERAL - 7)) | (1 << (D96Parser.LB - 7)) | (1 << (D96Parser.ID - 7)))) != 0):
                self.state = 297
                self.expressions_list()


            self.state = 300
            self.match(D96Parser.RB)
            self.state = 301
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LB)
            else:
                return self.getToken(D96Parser.LB, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RB)
            else:
                return self.getToken(D96Parser.RB, i)

        def block_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_statementContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_statementContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ELSEIF)
            else:
                return self.getToken(D96Parser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(D96Parser.IF)
            self.state = 304
            self.match(D96Parser.LB)
            self.state = 305
            self.expression()
            self.state = 306
            self.match(D96Parser.RB)
            self.state = 307
            self.block_statement()
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 308
                self.match(D96Parser.ELSEIF)
                self.state = 309
                self.match(D96Parser.LB)
                self.state = 310
                self.expression()
                self.state = 311
                self.match(D96Parser.RB)
                self.state = 312
                self.block_statement()
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 319
                self.match(D96Parser.ELSE)
                self.state = 320
                self.block_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def DOUBLEDOT(self):
            return self.getToken(D96Parser.DOUBLEDOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = D96Parser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(D96Parser.FOREACH)
            self.state = 324
            self.match(D96Parser.LB)
            self.state = 325
            self.match(D96Parser.ID)
            self.state = 326
            self.match(D96Parser.IN)
            self.state = 327
            self.expression()
            self.state = 328
            self.match(D96Parser.DOUBLEDOT)
            self.state = 329
            self.expression()
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 330
                self.match(D96Parser.BY)
                self.state = 331
                self.expression()


            self.state = 334
            self.match(D96Parser.RB)
            self.state = 335
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(D96Parser.RETURN)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (D96Parser.ARRAY - 7)) | (1 << (D96Parser.NULL - 7)) | (1 << (D96Parser.SELF - 7)) | (1 << (D96Parser.NEW - 7)) | (1 << (D96Parser.SUB - 7)) | (1 << (D96Parser.NOT - 7)) | (1 << (D96Parser.INTLIT_ARR - 7)) | (1 << (D96Parser.INT_LITERAL - 7)) | (1 << (D96Parser.BOOL_LITERAL - 7)) | (1 << (D96Parser.FLOAT_LITERAL - 7)) | (1 << (D96Parser.STRING_LITERAL - 7)) | (1 << (D96Parser.LB - 7)) | (1 << (D96Parser.ID - 7)))) != 0):
                self.state = 338
                self.expression()


            self.state = 341
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = D96Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(D96Parser.BREAK)
            self.state = 344
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI_COLON(self):
            return self.getToken(D96Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = D96Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(D96Parser.CONTINUE)
            self.state = 347
            self.match(D96Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expression1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expression1Context,i)


        def CONCATE(self):
            return self.getToken(D96Parser.CONCATE, 0)

        def STRCOMPARE(self):
            return self.getToken(D96Parser.STRCOMPARE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = D96Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.expression1()
                self.state = 350
                _la = self._input.LA(1)
                if not(_la==D96Parser.STRCOMPARE or _la==D96Parser.CONCATE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 351
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expression2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expression2Context,i)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(D96Parser.NOTEQUAL, 0)

        def LARGER(self):
            return self.getToken(D96Parser.LARGER, 0)

        def SMALLER(self):
            return self.getToken(D96Parser.SMALLER, 0)

        def LE(self):
            return self.getToken(D96Parser.LE, 0)

        def SE(self):
            return self.getToken(D96Parser.SE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = D96Parser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.expression2(0)
                self.state = 357
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOTEQUAL) | (1 << D96Parser.LARGER) | (1 << D96Parser.SMALLER) | (1 << D96Parser.LE) | (1 << D96Parser.SE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 358
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(D96Parser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(D96Parser.Expression2Context,0)


        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 371
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 366
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 367
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 368
                    self.expression3(0) 
                self.state = 373
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(D96Parser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(D96Parser.Expression3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 382
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 377
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 378
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 379
                    self.expression4(0) 
                self.state = 384
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(D96Parser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(D96Parser.Expression4Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 393
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 388
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 389
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 390
                    self.expression5() 
                self.state = 395
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(D96Parser.Expression5Context,0)


        def expression6(self):
            return self.getTypedRuleContext(D96Parser.Expression6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = D96Parser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expression5)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(D96Parser.NOT)
                self.state = 397
                self.expression5()
                pass
            elif token in [D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.SUB, D96Parser.INTLIT_ARR, D96Parser.INT_LITERAL, D96Parser.BOOL_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.expression6()
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


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(D96Parser.Expression6Context,0)


        def expression7(self):
            return self.getTypedRuleContext(D96Parser.Expression7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = D96Parser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expression6)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(D96Parser.SUB)
                self.state = 402
                self.expression6()
                pass
            elif token in [D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.INTLIT_ARR, D96Parser.INT_LITERAL, D96Parser.BOOL_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.expression7(0)
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


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression8(self):
            return self.getTypedRuleContext(D96Parser.Expression8Context,0)


        def expression7(self):
            return self.getTypedRuleContext(D96Parser.Expression7Context,0)


        def LS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LS)
            else:
                return self.getToken(D96Parser.LS, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def RS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RS)
            else:
                return self.getToken(D96Parser.RS, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)



    def expression7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expression7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expression7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.expression8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 420
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expression7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression7)
                    self.state = 409
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 414 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 410
                            self.match(D96Parser.LS)
                            self.state = 411
                            self.expression()
                            self.state = 412
                            self.match(D96Parser.RS)

                        else:
                            raise NoViableAltException(self)
                        self.state = 416 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
             
                self.state = 422
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression9(self):
            return self.getTypedRuleContext(D96Parser.Expression9Context,0)


        def expression8(self):
            return self.getTypedRuleContext(D96Parser.Expression8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expressions_list(self):
            return self.getTypedRuleContext(D96Parser.Expressions_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)



    def expression8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expression8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expression8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.expression9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 438
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expression8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression8)
                    self.state = 426
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 427
                    self.match(D96Parser.DOT)
                    self.state = 428
                    self.match(D96Parser.ID)
                    self.state = 434
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        self.state = 429
                        self.match(D96Parser.LB)
                        self.state = 431
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (D96Parser.ARRAY - 7)) | (1 << (D96Parser.NULL - 7)) | (1 << (D96Parser.SELF - 7)) | (1 << (D96Parser.NEW - 7)) | (1 << (D96Parser.SUB - 7)) | (1 << (D96Parser.NOT - 7)) | (1 << (D96Parser.INTLIT_ARR - 7)) | (1 << (D96Parser.INT_LITERAL - 7)) | (1 << (D96Parser.BOOL_LITERAL - 7)) | (1 << (D96Parser.FLOAT_LITERAL - 7)) | (1 << (D96Parser.STRING_LITERAL - 7)) | (1 << (D96Parser.LB - 7)) | (1 << (D96Parser.ID - 7)))) != 0):
                            self.state = 430
                            self.expressions_list()


                        self.state = 433
                        self.match(D96Parser.RB)

             
                self.state = 440
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expressions_list(self):
            return self.getTypedRuleContext(D96Parser.Expressions_listContext,0)


        def expression10(self):
            return self.getTypedRuleContext(D96Parser.Expression10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression9" ):
                return visitor.visitExpression9(self)
            else:
                return visitor.visitChildren(self)




    def expression9(self):

        localctx = D96Parser.Expression9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expression9)
        self._la = 0 # Token type
        try:
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.match(D96Parser.ID)
                self.state = 442
                self.match(D96Parser.DOUBLE_COLON)
                self.state = 443
                self.match(D96Parser.DOLLAR_ID)
                self.state = 449
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 444
                    self.match(D96Parser.LB)
                    self.state = 446
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (D96Parser.ARRAY - 7)) | (1 << (D96Parser.NULL - 7)) | (1 << (D96Parser.SELF - 7)) | (1 << (D96Parser.NEW - 7)) | (1 << (D96Parser.SUB - 7)) | (1 << (D96Parser.NOT - 7)) | (1 << (D96Parser.INTLIT_ARR - 7)) | (1 << (D96Parser.INT_LITERAL - 7)) | (1 << (D96Parser.BOOL_LITERAL - 7)) | (1 << (D96Parser.FLOAT_LITERAL - 7)) | (1 << (D96Parser.STRING_LITERAL - 7)) | (1 << (D96Parser.LB - 7)) | (1 << (D96Parser.ID - 7)))) != 0):
                        self.state = 445
                        self.expressions_list()


                    self.state = 448
                    self.match(D96Parser.RB)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.expression10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def expression10(self):
            return self.getTypedRuleContext(D96Parser.Expression10Context,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expressions_list(self):
            return self.getTypedRuleContext(D96Parser.Expressions_listContext,0)


        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression10" ):
                return visitor.visitExpression10(self)
            else:
                return visitor.visitChildren(self)




    def expression10(self):

        localctx = D96Parser.Expression10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expression10)
        self._la = 0 # Token type
        try:
            self.state = 463
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.match(D96Parser.NEW)
                self.state = 455
                self.expression10()
                self.state = 456
                self.match(D96Parser.LB)
                self.state = 458
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (D96Parser.ARRAY - 7)) | (1 << (D96Parser.NULL - 7)) | (1 << (D96Parser.SELF - 7)) | (1 << (D96Parser.NEW - 7)) | (1 << (D96Parser.SUB - 7)) | (1 << (D96Parser.NOT - 7)) | (1 << (D96Parser.INTLIT_ARR - 7)) | (1 << (D96Parser.INT_LITERAL - 7)) | (1 << (D96Parser.BOOL_LITERAL - 7)) | (1 << (D96Parser.FLOAT_LITERAL - 7)) | (1 << (D96Parser.STRING_LITERAL - 7)) | (1 << (D96Parser.LB - 7)) | (1 << (D96Parser.ID - 7)))) != 0):
                    self.state = 457
                    self.expressions_list()


                self.state = 460
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.INTLIT_ARR, D96Parser.INT_LITERAL, D96Parser.BOOL_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.operands()
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


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = D96Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(D96Parser.LS)
            self.state = 466
            self.expression()
            self.state = 467
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_operands)
        try:
            self.state = 478
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT_ARR, D96Parser.INT_LITERAL, D96Parser.BOOL_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.literals()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 471
                self.match(D96Parser.LB)
                self.state = 472
                self.expression()
                self.state = 473
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 4)
                self.state = 475
                self.indexed_array()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 476
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 477
                self.match(D96Parser.NULL)
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


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT_ARR(self):
            return self.getToken(D96Parser.INTLIT_ARR, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def INT_LITERAL(self):
            return self.getToken(D96Parser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(D96Parser.FLOAT_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(D96Parser.BOOL_LITERAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT_ARR) | (1 << D96Parser.INT_LITERAL) | (1 << D96Parser.BOOL_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL))) != 0)):
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


    class Dollar_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expressions_list(self):
            return self.getTypedRuleContext(D96Parser.Expressions_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_dollar_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDollar_function" ):
                return visitor.visitDollar_function(self)
            else:
                return visitor.visitChildren(self)




    def dollar_function(self):

        localctx = D96Parser.Dollar_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_dollar_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(D96Parser.DOLLAR_ID)
            self.state = 488
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.LB:
                self.state = 483
                self.match(D96Parser.LB)
                self.state = 485
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (D96Parser.ARRAY - 7)) | (1 << (D96Parser.NULL - 7)) | (1 << (D96Parser.SELF - 7)) | (1 << (D96Parser.NEW - 7)) | (1 << (D96Parser.SUB - 7)) | (1 << (D96Parser.NOT - 7)) | (1 << (D96Parser.INTLIT_ARR - 7)) | (1 << (D96Parser.INT_LITERAL - 7)) | (1 << (D96Parser.BOOL_LITERAL - 7)) | (1 << (D96Parser.FLOAT_LITERAL - 7)) | (1 << (D96Parser.STRING_LITERAL - 7)) | (1 << (D96Parser.LB - 7)) | (1 << (D96Parser.ID - 7)))) != 0):
                    self.state = 484
                    self.expressions_list()


                self.state = 487
                self.match(D96Parser.RB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expressions_list(self):
            return self.getTypedRuleContext(D96Parser.Expressions_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = D96Parser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(D96Parser.ID)
            self.state = 496
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.LB:
                self.state = 491
                self.match(D96Parser.LB)
                self.state = 493
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (D96Parser.ARRAY - 7)) | (1 << (D96Parser.NULL - 7)) | (1 << (D96Parser.SELF - 7)) | (1 << (D96Parser.NEW - 7)) | (1 << (D96Parser.SUB - 7)) | (1 << (D96Parser.NOT - 7)) | (1 << (D96Parser.INTLIT_ARR - 7)) | (1 << (D96Parser.INT_LITERAL - 7)) | (1 << (D96Parser.BOOL_LITERAL - 7)) | (1 << (D96Parser.FLOAT_LITERAL - 7)) | (1 << (D96Parser.STRING_LITERAL - 7)) | (1 << (D96Parser.LB - 7)) | (1 << (D96Parser.ID - 7)))) != 0):
                    self.state = 492
                    self.expressions_list()


                self.state = 495
                self.match(D96Parser.RB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexed_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expressions_list(self):
            return self.getTypedRuleContext(D96Parser.Expressions_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_indexed_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexed_array" ):
                return visitor.visitIndexed_array(self)
            else:
                return visitor.visitChildren(self)




    def indexed_array(self):

        localctx = D96Parser.Indexed_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(D96Parser.ARRAY)
            self.state = 499
            self.match(D96Parser.LB)
            self.state = 501
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (D96Parser.ARRAY - 7)) | (1 << (D96Parser.NULL - 7)) | (1 << (D96Parser.SELF - 7)) | (1 << (D96Parser.NEW - 7)) | (1 << (D96Parser.SUB - 7)) | (1 << (D96Parser.NOT - 7)) | (1 << (D96Parser.INTLIT_ARR - 7)) | (1 << (D96Parser.INT_LITERAL - 7)) | (1 << (D96Parser.BOOL_LITERAL - 7)) | (1 << (D96Parser.FLOAT_LITERAL - 7)) | (1 << (D96Parser.STRING_LITERAL - 7)) | (1 << (D96Parser.LB - 7)) | (1 << (D96Parser.ID - 7)))) != 0):
                self.state = 500
                self.expressions_list()


            self.state = 503
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_compound_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_type" ):
                return visitor.visitCompound_type(self)
            else:
                return visitor.visitChildren(self)




    def compound_type(self):

        localctx = D96Parser.Compound_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_compound_type)
        try:
            self.state = 508
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_TYPE, D96Parser.FLOAT_TYPE, D96Parser.BOOLEAN_TYPE, D96Parser.STRING_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 506
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 507
                self.match(D96Parser.ID)
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


    class Expressions_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expressions_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressions_list" ):
                return visitor.visitExpressions_list(self)
            else:
                return visitor.visitChildren(self)




    def expressions_list(self):

        localctx = D96Parser.Expressions_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expressions_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.expression()
            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 511
                self.match(D96Parser.COMMA)
                self.state = 512
                self.expression()
                self.state = 517
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMMUTABLE(self):
            return self.getToken(D96Parser.IMMUTABLE, 0)

        def MUTABLE(self):
            return self.getToken(D96Parser.MUTABLE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_type" ):
                return visitor.visitAttribute_type(self)
            else:
                return visitor.visitChildren(self)




    def attribute_type(self):

        localctx = D96Parser.Attribute_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_attribute_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            _la = self._input.LA(1)
            if not(_la==D96Parser.IMMUTABLE or _la==D96Parser.MUTABLE):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[34] = self.expression2_sempred
        self._predicates[35] = self.expression3_sempred
        self._predicates[36] = self.expression4_sempred
        self._predicates[39] = self.expression7_sempred
        self._predicates[40] = self.expression8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression7_sempred(self, localctx:Expression7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression8_sempred(self, localctx:Expression8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




