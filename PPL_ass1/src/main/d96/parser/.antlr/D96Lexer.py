# Generated from c:\Users\Dell\Desktop\PPL_ass1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u02c9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\5\21\u00fb\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\6\31\u012d\n\31\r\31\16\31\u012e\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3,\3,\5,\u0163\n,\3-\3-\3-\3-\7-\u0169\n-\f-\16")
        buf.write("-\u016c\13-\3-\3-\6-\u0170\n-\r-\16-\u0171\7-\u0174\n")
        buf.write("-\f-\16-\u0177\13-\3.\3.\7.\u017b\n.\f.\16.\u017e\13.")
        buf.write("\3.\3.\6.\u0182\n.\r.\16.\u0183\7.\u0186\n.\f.\16.\u0189")
        buf.write("\13.\3/\3/\3/\7/\u018e\n/\f/\16/\u0191\13/\3/\3/\6/\u0195")
        buf.write("\n/\r/\16/\u0196\7/\u0199\n/\f/\16/\u019c\13/\3\60\3\60")
        buf.write("\3\60\3\60\7\60\u01a2\n\60\f\60\16\60\u01a5\13\60\3\60")
        buf.write("\3\60\6\60\u01a9\n\60\r\60\16\60\u01aa\7\60\u01ad\n\60")
        buf.write("\f\60\16\60\u01b0\13\60\3\61\3\61\3\61\3\61\7\61\u01b6")
        buf.write("\n\61\f\61\16\61\u01b9\13\61\3\61\3\61\6\61\u01bd\n\61")
        buf.write("\r\61\16\61\u01be\7\61\u01c1\n\61\f\61\16\61\u01c4\13")
        buf.write("\61\3\61\5\61\u01c7\n\61\3\62\3\62\3\62\7\62\u01cc\n\62")
        buf.write("\f\62\16\62\u01cf\13\62\3\62\3\62\7\62\u01d3\n\62\f\62")
        buf.write("\16\62\u01d6\13\62\3\62\5\62\u01d9\n\62\3\63\3\63\3\63")
        buf.write("\3\63\7\63\u01df\n\63\f\63\16\63\u01e2\13\63\3\63\3\63")
        buf.write("\6\63\u01e6\n\63\r\63\16\63\u01e7\7\63\u01ea\n\63\f\63")
        buf.write("\16\63\u01ed\13\63\3\63\5\63\u01f0\n\63\3\64\3\64\3\64")
        buf.write("\7\64\u01f5\n\64\f\64\16\64\u01f8\13\64\3\64\3\64\6\64")
        buf.write("\u01fc\n\64\r\64\16\64\u01fd\7\64\u0200\n\64\f\64\16\64")
        buf.write("\u0203\13\64\5\64\u0205\n\64\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u0213\n\65\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u021e")
        buf.write("\n\66\3\67\3\67\3\67\5\67\u0223\n\67\3\67\3\67\3\67\5")
        buf.write("\67\u0228\n\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u0230")
        buf.write("\n\67\3\67\3\67\3\67\5\67\u0235\n\67\38\38\38\78\u023a")
        buf.write("\n8\f8\168\u023d\138\38\38\68\u0241\n8\r8\168\u0242\7")
        buf.write("8\u0245\n8\f8\168\u0248\138\58\u024a\n8\39\39\79\u024e")
        buf.write("\n9\f9\169\u0251\139\3:\3:\5:\u0255\n:\3:\6:\u0258\n:")
        buf.write("\r:\16:\u0259\3;\3;\3;\7;\u025f\n;\f;\16;\u0262\13;\3")
        buf.write(";\3;\3;\3<\3<\3<\3<\7<\u026b\n<\f<\16<\u026e\13<\3<\3")
        buf.write("<\3<\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3")
        buf.write("C\3D\3D\3E\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\7I\u0291\nI\f")
        buf.write("I\16I\u0294\13I\3J\6J\u0297\nJ\rJ\16J\u0298\3J\3J\3K\3")
        buf.write("K\3L\3L\3L\3L\3L\3L\3L\3L\5L\u02a7\nL\3M\3M\3M\3M\5M\u02ad")
        buf.write("\nM\3N\3N\3N\7N\u02b2\nN\fN\16N\u02b5\13N\3N\5N\u02b8")
        buf.write("\nN\3N\3N\3O\3O\3O\7O\u02bf\nO\fO\16O\u02c2\13O\3O\3O")
        buf.write("\3O\3P\3P\3P\3\u026c\2Q\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\2c\2e")
        buf.write("\2g\2i\62k\63m\64o\2q\2s\2u\65w\66y\67{8}9\177:\u0081")
        buf.write(";\u0083<\u0085=\u0087>\u0089?\u008b@\u008dA\u008fB\u0091")
        buf.write("C\u0093D\u0095\2\u0097\2\u0099\2\u009bE\u009dF\u009fG")
        buf.write("\3\2\25\6\2\62;C\\aac|\4\2DDdd\3\2\62\63\3\2\63;\3\2\62")
        buf.write(";\3\2\639\3\2\629\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2GGgg")
        buf.write("\4\2--//\5\2C\\aac|\5\2\13\f\17\17\"\"\5\2\f\f$$^^\7\2")
        buf.write("ddhhppttvv\t\2))^^ddhhppttvv\3\2$$\3\3\f\f\2\u02fc\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\3\u00a1")
        buf.write("\3\2\2\2\5\u00a7\3\2\2\2\7\u00b0\3\2\2\2\t\u00b3\3\2\2")
        buf.write("\2\13\u00ba\3\2\2\2\r\u00bf\3\2\2\2\17\u00c7\3\2\2\2\21")
        buf.write("\u00cd\3\2\2\2\23\u00d0\3\2\2\2\25\u00d3\3\2\2\2\27\u00d7")
        buf.write("\3\2\2\2\31\u00dd\3\2\2\2\33\u00e5\3\2\2\2\35\u00ec\3")
        buf.write("\2\2\2\37\u00f1\3\2\2\2!\u00fa\3\2\2\2#\u00fc\3\2\2\2")
        buf.write("%\u0101\3\2\2\2\'\u0105\3\2\2\2)\u010b\3\2\2\2+\u010f")
        buf.write("\3\2\2\2-\u0113\3\2\2\2/\u011f\3\2\2\2\61\u012a\3\2\2")
        buf.write("\2\63\u0130\3\2\2\2\65\u0132\3\2\2\2\67\u0134\3\2\2\2")
        buf.write("9\u0136\3\2\2\2;\u0138\3\2\2\2=\u013a\3\2\2\2?\u013c\3")
        buf.write("\2\2\2A\u013e\3\2\2\2C\u0141\3\2\2\2E\u0144\3\2\2\2G\u0148")
        buf.write("\3\2\2\2I\u014b\3\2\2\2K\u014e\3\2\2\2M\u0151\3\2\2\2")
        buf.write("O\u0153\3\2\2\2Q\u0155\3\2\2\2S\u0158\3\2\2\2U\u015b\3")
        buf.write("\2\2\2W\u0162\3\2\2\2Y\u0164\3\2\2\2[\u0178\3\2\2\2]\u018a")
        buf.write("\3\2\2\2_\u019d\3\2\2\2a\u01b1\3\2\2\2c\u01c8\3\2\2\2")
        buf.write("e\u01da\3\2\2\2g\u0204\3\2\2\2i\u0212\3\2\2\2k\u021d\3")
        buf.write("\2\2\2m\u0234\3\2\2\2o\u0249\3\2\2\2q\u024b\3\2\2\2s\u0252")
        buf.write("\3\2\2\2u\u025b\3\2\2\2w\u0266\3\2\2\2y\u0274\3\2\2\2")
        buf.write("{\u0276\3\2\2\2}\u0278\3\2\2\2\177\u027a\3\2\2\2\u0081")
        buf.write("\u027c\3\2\2\2\u0083\u027e\3\2\2\2\u0085\u0280\3\2\2\2")
        buf.write("\u0087\u0283\3\2\2\2\u0089\u0285\3\2\2\2\u008b\u0288\3")
        buf.write("\2\2\2\u008d\u028a\3\2\2\2\u008f\u028c\3\2\2\2\u0091\u028e")
        buf.write("\3\2\2\2\u0093\u0296\3\2\2\2\u0095\u029c\3\2\2\2\u0097")
        buf.write("\u02a6\3\2\2\2\u0099\u02ac\3\2\2\2\u009b\u02ae\3\2\2\2")
        buf.write("\u009d\u02bb\3\2\2\2\u009f\u02c6\3\2\2\2\u00a1\u00a2\7")
        buf.write("D\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5")
        buf.write("\7c\2\2\u00a5\u00a6\7m\2\2\u00a6\4\3\2\2\2\u00a7\u00a8")
        buf.write("\7E\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab")
        buf.write("\7v\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae")
        buf.write("\7w\2\2\u00ae\u00af\7g\2\2\u00af\6\3\2\2\2\u00b0\u00b1")
        buf.write("\7K\2\2\u00b1\u00b2\7h\2\2\u00b2\b\3\2\2\2\u00b3\u00b4")
        buf.write("\7G\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6\7u\2\2\u00b6\u00b7")
        buf.write("\7g\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9\7h\2\2\u00b9\n")
        buf.write("\3\2\2\2\u00ba\u00bb\7G\2\2\u00bb\u00bc\7n\2\2\u00bc\u00bd")
        buf.write("\7u\2\2\u00bd\u00be\7g\2\2\u00be\f\3\2\2\2\u00bf\u00c0")
        buf.write("\7H\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3")
        buf.write("\7g\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5\7e\2\2\u00c5\u00c6")
        buf.write("\7j\2\2\u00c6\16\3\2\2\2\u00c7\u00c8\7C\2\2\u00c8\u00c9")
        buf.write("\7t\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc")
        buf.write("\7{\2\2\u00cc\20\3\2\2\2\u00cd\u00ce\7K\2\2\u00ce\u00cf")
        buf.write("\7p\2\2\u00cf\22\3\2\2\2\u00d0\u00d1\7D\2\2\u00d1\u00d2")
        buf.write("\7{\2\2\u00d2\24\3\2\2\2\u00d3\u00d4\7K\2\2\u00d4\u00d5")
        buf.write("\7p\2\2\u00d5\u00d6\7v\2\2\u00d6\26\3\2\2\2\u00d7\u00d8")
        buf.write("\7H\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7c\2\2\u00db\u00dc\7v\2\2\u00dc\30\3\2\2\2\u00dd\u00de")
        buf.write("\7D\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1")
        buf.write("\7n\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4")
        buf.write("\7p\2\2\u00e4\32\3\2\2\2\u00e5\u00e6\7U\2\2\u00e6\u00e7")
        buf.write("\7v\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea")
        buf.write("\7p\2\2\u00ea\u00eb\7i\2\2\u00eb\34\3\2\2\2\u00ec\u00ed")
        buf.write("\7P\2\2\u00ed\u00ee\7w\2\2\u00ee\u00ef\7n\2\2\u00ef\u00f0")
        buf.write("\7n\2\2\u00f0\36\3\2\2\2\u00f1\u00f2\7T\2\2\u00f2\u00f3")
        buf.write("\7g\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6")
        buf.write("\7t\2\2\u00f6\u00f7\7p\2\2\u00f7 \3\2\2\2\u00f8\u00fb")
        buf.write("\5)\25\2\u00f9\u00fb\5+\26\2\u00fa\u00f8\3\2\2\2\u00fa")
        buf.write("\u00f9\3\2\2\2\u00fb\"\3\2\2\2\u00fc\u00fd\7U\2\2\u00fd")
        buf.write("\u00fe\7g\2\2\u00fe\u00ff\7n\2\2\u00ff\u0100\7h\2\2\u0100")
        buf.write("$\3\2\2\2\u0101\u0102\7P\2\2\u0102\u0103\7g\2\2\u0103")
        buf.write("\u0104\7y\2\2\u0104&\3\2\2\2\u0105\u0106\7E\2\2\u0106")
        buf.write("\u0107\7n\2\2\u0107\u0108\7c\2\2\u0108\u0109\7u\2\2\u0109")
        buf.write("\u010a\7u\2\2\u010a(\3\2\2\2\u010b\u010c\7X\2\2\u010c")
        buf.write("\u010d\7c\2\2\u010d\u010e\7n\2\2\u010e*\3\2\2\2\u010f")
        buf.write("\u0110\7X\2\2\u0110\u0111\7c\2\2\u0111\u0112\7t\2\2\u0112")
        buf.write(",\3\2\2\2\u0113\u0114\7E\2\2\u0114\u0115\7q\2\2\u0115")
        buf.write("\u0116\7p\2\2\u0116\u0117\7u\2\2\u0117\u0118\7v\2\2\u0118")
        buf.write("\u0119\7t\2\2\u0119\u011a\7w\2\2\u011a\u011b\7e\2\2\u011b")
        buf.write("\u011c\7v\2\2\u011c\u011d\7q\2\2\u011d\u011e\7t\2\2\u011e")
        buf.write(".\3\2\2\2\u011f\u0120\7F\2\2\u0120\u0121\7g\2\2\u0121")
        buf.write("\u0122\7u\2\2\u0122\u0123\7v\2\2\u0123\u0124\7t\2\2\u0124")
        buf.write("\u0125\7w\2\2\u0125\u0126\7e\2\2\u0126\u0127\7v\2\2\u0127")
        buf.write("\u0128\7q\2\2\u0128\u0129\7t\2\2\u0129\60\3\2\2\2\u012a")
        buf.write("\u012c\7&\2\2\u012b\u012d\t\2\2\2\u012c\u012b\3\2\2\2")
        buf.write("\u012d\u012e\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3")
        buf.write("\2\2\2\u012f\62\3\2\2\2\u0130\u0131\7?\2\2\u0131\64\3")
        buf.write("\2\2\2\u0132\u0133\7-\2\2\u0133\66\3\2\2\2\u0134\u0135")
        buf.write("\7/\2\2\u01358\3\2\2\2\u0136\u0137\7,\2\2\u0137:\3\2\2")
        buf.write("\2\u0138\u0139\7\61\2\2\u0139<\3\2\2\2\u013a\u013b\7\'")
        buf.write("\2\2\u013b>\3\2\2\2\u013c\u013d\7#\2\2\u013d@\3\2\2\2")
        buf.write("\u013e\u013f\7(\2\2\u013f\u0140\7(\2\2\u0140B\3\2\2\2")
        buf.write("\u0141\u0142\7~\2\2\u0142\u0143\7~\2\2\u0143D\3\2\2\2")
        buf.write("\u0144\u0145\7?\2\2\u0145\u0146\7?\2\2\u0146\u0147\7\60")
        buf.write("\2\2\u0147F\3\2\2\2\u0148\u0149\7-\2\2\u0149\u014a\7\60")
        buf.write("\2\2\u014aH\3\2\2\2\u014b\u014c\7?\2\2\u014c\u014d\7?")
        buf.write("\2\2\u014dJ\3\2\2\2\u014e\u014f\7#\2\2\u014f\u0150\7?")
        buf.write("\2\2\u0150L\3\2\2\2\u0151\u0152\7@\2\2\u0152N\3\2\2\2")
        buf.write("\u0153\u0154\7>\2\2\u0154P\3\2\2\2\u0155\u0156\7@\2\2")
        buf.write("\u0156\u0157\7?\2\2\u0157R\3\2\2\2\u0158\u0159\7>\2\2")
        buf.write("\u0159\u015a\7?\2\2\u015aT\3\2\2\2\u015b\u015c\5W,\2\u015c")
        buf.write("\u015d\b+\2\2\u015dV\3\2\2\2\u015e\u0163\5Y-\2\u015f\u0163")
        buf.write("\5[.\2\u0160\u0163\5]/\2\u0161\u0163\5_\60\2\u0162\u015e")
        buf.write("\3\2\2\2\u0162\u015f\3\2\2\2\u0162\u0160\3\2\2\2\u0162")
        buf.write("\u0161\3\2\2\2\u0163X\3\2\2\2\u0164\u0165\7\62\2\2\u0165")
        buf.write("\u0166\t\3\2\2\u0166\u016a\7\63\2\2\u0167\u0169\t\4\2")
        buf.write("\2\u0168\u0167\3\2\2\2\u0169\u016c\3\2\2\2\u016a\u0168")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u0175\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016d\u016f\7a\2\2\u016e\u0170\t\4\2\2")
        buf.write("\u016f\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u016f\3")
        buf.write("\2\2\2\u0171\u0172\3\2\2\2\u0172\u0174\3\2\2\2\u0173\u016d")
        buf.write("\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175")
        buf.write("\u0176\3\2\2\2\u0176Z\3\2\2\2\u0177\u0175\3\2\2\2\u0178")
        buf.write("\u017c\t\5\2\2\u0179\u017b\t\6\2\2\u017a\u0179\3\2\2\2")
        buf.write("\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3")
        buf.write("\2\2\2\u017d\u0187\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0181")
        buf.write("\7a\2\2\u0180\u0182\t\6\2\2\u0181\u0180\3\2\2\2\u0182")
        buf.write("\u0183\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\u0186\3\2\2\2\u0185\u017f\3\2\2\2\u0186\u0189\3")
        buf.write("\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\\")
        buf.write("\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018b\7\62\2\2\u018b")
        buf.write("\u018f\t\7\2\2\u018c\u018e\t\b\2\2\u018d\u018c\3\2\2\2")
        buf.write("\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3")
        buf.write("\2\2\2\u0190\u019a\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0194")
        buf.write("\7a\2\2\u0193\u0195\t\b\2\2\u0194\u0193\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197\u0199\3\2\2\2\u0198\u0192\3\2\2\2\u0199\u019c\3")
        buf.write("\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b^")
        buf.write("\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019e\7\62\2\2\u019e")
        buf.write("\u019f\t\t\2\2\u019f\u01a3\t\n\2\2\u01a0\u01a2\t\13\2")
        buf.write("\2\u01a1\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01ae\3\2\2\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a6\u01a8\7a\2\2\u01a7\u01a9\t\13\2\2")
        buf.write("\u01a8\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01a8\3")
        buf.write("\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ad\3\2\2\2\u01ac\u01a6")
        buf.write("\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af`\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1")
        buf.write("\u01b2\7\62\2\2\u01b2\u01c6\t\3\2\2\u01b3\u01b7\7\63\2")
        buf.write("\2\u01b4\u01b6\t\4\2\2\u01b5\u01b4\3\2\2\2\u01b6\u01b9")
        buf.write("\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write("\u01c2\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u01bc\7a\2\2")
        buf.write("\u01bb\u01bd\t\4\2\2\u01bc\u01bb\3\2\2\2\u01bd\u01be\3")
        buf.write("\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c1")
        buf.write("\3\2\2\2\u01c0\u01ba\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2")
        buf.write("\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c7\3\2\2\2")
        buf.write("\u01c4\u01c2\3\2\2\2\u01c5\u01c7\7\62\2\2\u01c6\u01b3")
        buf.write("\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7b\3\2\2\2\u01c8\u01d8")
        buf.write("\7\62\2\2\u01c9\u01cd\t\7\2\2\u01ca\u01cc\t\b\2\2\u01cb")
        buf.write("\u01ca\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2")
        buf.write("\u01cd\u01ce\3\2\2\2\u01ce\u01d3\3\2\2\2\u01cf\u01cd\3")
        buf.write("\2\2\2\u01d0\u01d1\7a\2\2\u01d1\u01d3\t\b\2\2\u01d2\u01c9")
        buf.write("\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d9\3\2\2\2")
        buf.write("\u01d6\u01d4\3\2\2\2\u01d7\u01d9\7\62\2\2\u01d8\u01d4")
        buf.write("\3\2\2\2\u01d8\u01d7\3\2\2\2\u01d9d\3\2\2\2\u01da\u01db")
        buf.write("\7\62\2\2\u01db\u01ef\t\t\2\2\u01dc\u01e0\t\n\2\2\u01dd")
        buf.write("\u01df\t\13\2\2\u01de\u01dd\3\2\2\2\u01df\u01e2\3\2\2")
        buf.write("\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01eb")
        buf.write("\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e5\7a\2\2\u01e4")
        buf.write("\u01e6\t\13\2\2\u01e5\u01e4\3\2\2\2\u01e6\u01e7\3\2\2")
        buf.write("\2\u01e7\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01ea")
        buf.write("\3\2\2\2\u01e9\u01e3\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb")
        buf.write("\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01f0\3\2\2\2")
        buf.write("\u01ed\u01eb\3\2\2\2\u01ee\u01f0\7\62\2\2\u01ef\u01dc")
        buf.write("\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0f\3\2\2\2\u01f1\u0205")
        buf.write("\7\62\2\2\u01f2\u01f6\t\5\2\2\u01f3\u01f5\t\6\2\2\u01f4")
        buf.write("\u01f3\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6\u01f4\3\2\2\2")
        buf.write("\u01f6\u01f7\3\2\2\2\u01f7\u0201\3\2\2\2\u01f8\u01f6\3")
        buf.write("\2\2\2\u01f9\u01fb\7a\2\2\u01fa\u01fc\t\6\2\2\u01fb\u01fa")
        buf.write("\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd")
        buf.write("\u01fe\3\2\2\2\u01fe\u0200\3\2\2\2\u01ff\u01f9\3\2\2\2")
        buf.write("\u0200\u0203\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3")
        buf.write("\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2\u0204\u01f1")
        buf.write("\3\2\2\2\u0204\u01f2\3\2\2\2\u0205h\3\2\2\2\u0206\u0207")
        buf.write("\5g\64\2\u0207\u0208\b\65\3\2\u0208\u0213\3\2\2\2\u0209")
        buf.write("\u020a\5e\63\2\u020a\u020b\b\65\4\2\u020b\u0213\3\2\2")
        buf.write("\2\u020c\u020d\5c\62\2\u020d\u020e\b\65\5\2\u020e\u0213")
        buf.write("\3\2\2\2\u020f\u0210\5a\61\2\u0210\u0211\b\65\6\2\u0211")
        buf.write("\u0213\3\2\2\2\u0212\u0206\3\2\2\2\u0212\u0209\3\2\2\2")
        buf.write("\u0212\u020c\3\2\2\2\u0212\u020f\3\2\2\2\u0213j\3\2\2")
        buf.write("\2\u0214\u0215\7V\2\2\u0215\u0216\7t\2\2\u0216\u0217\7")
        buf.write("w\2\2\u0217\u021e\7g\2\2\u0218\u0219\7H\2\2\u0219\u021a")
        buf.write("\7c\2\2\u021a\u021b\7n\2\2\u021b\u021c\7u\2\2\u021c\u021e")
        buf.write("\7g\2\2\u021d\u0214\3\2\2\2\u021d\u0218\3\2\2\2\u021e")
        buf.write("l\3\2\2\2\u021f\u0220\5o8\2\u0220\u0222\5q9\2\u0221\u0223")
        buf.write("\5s:\2\u0222\u0221\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0224")
        buf.write("\3\2\2\2\u0224\u0225\b\67\7\2\u0225\u0235\3\2\2\2\u0226")
        buf.write("\u0228\5o8\2\u0227\u0226\3\2\2\2\u0227\u0228\3\2\2\2\u0228")
        buf.write("\u0229\3\2\2\2\u0229\u022a\5q9\2\u022a\u022b\5s:\2\u022b")
        buf.write("\u022c\b\67\b\2\u022c\u0235\3\2\2\2\u022d\u022f\5o8\2")
        buf.write("\u022e\u0230\5q9\2\u022f\u022e\3\2\2\2\u022f\u0230\3\2")
        buf.write("\2\2\u0230\u0231\3\2\2\2\u0231\u0232\5s:\2\u0232\u0233")
        buf.write("\b\67\t\2\u0233\u0235\3\2\2\2\u0234\u021f\3\2\2\2\u0234")
        buf.write("\u0227\3\2\2\2\u0234\u022d\3\2\2\2\u0235n\3\2\2\2\u0236")
        buf.write("\u024a\t\6\2\2\u0237\u023b\t\5\2\2\u0238\u023a\t\6\2\2")
        buf.write("\u0239\u0238\3\2\2\2\u023a\u023d\3\2\2\2\u023b\u0239\3")
        buf.write("\2\2\2\u023b\u023c\3\2\2\2\u023c\u0246\3\2\2\2\u023d\u023b")
        buf.write("\3\2\2\2\u023e\u0240\7a\2\2\u023f\u0241\t\6\2\2\u0240")
        buf.write("\u023f\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0240\3\2\2\2")
        buf.write("\u0242\u0243\3\2\2\2\u0243\u0245\3\2\2\2\u0244\u023e\3")
        buf.write("\2\2\2\u0245\u0248\3\2\2\2\u0246\u0244\3\2\2\2\u0246\u0247")
        buf.write("\3\2\2\2\u0247\u024a\3\2\2\2\u0248\u0246\3\2\2\2\u0249")
        buf.write("\u0236\3\2\2\2\u0249\u0237\3\2\2\2\u024ap\3\2\2\2\u024b")
        buf.write("\u024f\7\60\2\2\u024c\u024e\t\6\2\2\u024d\u024c\3\2\2")
        buf.write("\2\u024e\u0251\3\2\2\2\u024f\u024d\3\2\2\2\u024f\u0250")
        buf.write("\3\2\2\2\u0250r\3\2\2\2\u0251\u024f\3\2\2\2\u0252\u0254")
        buf.write("\t\f\2\2\u0253\u0255\t\r\2\2\u0254\u0253\3\2\2\2\u0254")
        buf.write("\u0255\3\2\2\2\u0255\u0257\3\2\2\2\u0256\u0258\t\6\2\2")
        buf.write("\u0257\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u0257\3")
        buf.write("\2\2\2\u0259\u025a\3\2\2\2\u025at\3\2\2\2\u025b\u0260")
        buf.write("\7$\2\2\u025c\u025f\5\u0095K\2\u025d\u025f\5\u0097L\2")
        buf.write("\u025e\u025c\3\2\2\2\u025e\u025d\3\2\2\2\u025f\u0262\3")
        buf.write("\2\2\2\u0260\u025e\3\2\2\2\u0260\u0261\3\2\2\2\u0261\u0263")
        buf.write("\3\2\2\2\u0262\u0260\3\2\2\2\u0263\u0264\7$\2\2\u0264")
        buf.write("\u0265\b;\n\2\u0265v\3\2\2\2\u0266\u0267\7%\2\2\u0267")
        buf.write("\u0268\7%\2\2\u0268\u026c\3\2\2\2\u0269\u026b\13\2\2\2")
        buf.write("\u026a\u0269\3\2\2\2\u026b\u026e\3\2\2\2\u026c\u026d\3")
        buf.write("\2\2\2\u026c\u026a\3\2\2\2\u026d\u026f\3\2\2\2\u026e\u026c")
        buf.write("\3\2\2\2\u026f\u0270\7%\2\2\u0270\u0271\7%\2\2\u0271\u0272")
        buf.write("\3\2\2\2\u0272\u0273\b<\13\2\u0273x\3\2\2\2\u0274\u0275")
        buf.write("\7*\2\2\u0275z\3\2\2\2\u0276\u0277\7+\2\2\u0277|\3\2\2")
        buf.write("\2\u0278\u0279\7}\2\2\u0279~\3\2\2\2\u027a\u027b\7\177")
        buf.write("\2\2\u027b\u0080\3\2\2\2\u027c\u027d\7]\2\2\u027d\u0082")
        buf.write("\3\2\2\2\u027e\u027f\7_\2\2\u027f\u0084\3\2\2\2\u0280")
        buf.write("\u0281\7<\2\2\u0281\u0282\7<\2\2\u0282\u0086\3\2\2\2\u0283")
        buf.write("\u0284\7<\2\2\u0284\u0088\3\2\2\2\u0285\u0286\7\60\2\2")
        buf.write("\u0286\u0287\7\60\2\2\u0287\u008a\3\2\2\2\u0288\u0289")
        buf.write("\7\60\2\2\u0289\u008c\3\2\2\2\u028a\u028b\7.\2\2\u028b")
        buf.write("\u008e\3\2\2\2\u028c\u028d\7=\2\2\u028d\u0090\3\2\2\2")
        buf.write("\u028e\u0292\t\16\2\2\u028f\u0291\t\2\2\2\u0290\u028f")
        buf.write("\3\2\2\2\u0291\u0294\3\2\2\2\u0292\u0290\3\2\2\2\u0292")
        buf.write("\u0293\3\2\2\2\u0293\u0092\3\2\2\2\u0294\u0292\3\2\2\2")
        buf.write("\u0295\u0297\t\17\2\2\u0296\u0295\3\2\2\2\u0297\u0298")
        buf.write("\3\2\2\2\u0298\u0296\3\2\2\2\u0298\u0299\3\2\2\2\u0299")
        buf.write("\u029a\3\2\2\2\u029a\u029b\bJ\13\2\u029b\u0094\3\2\2\2")
        buf.write("\u029c\u029d\n\20\2\2\u029d\u0096\3\2\2\2\u029e\u029f")
        buf.write("\7^\2\2\u029f\u02a7\t\21\2\2\u02a0\u02a1\7^\2\2\u02a1")
        buf.write("\u02a7\7)\2\2\u02a2\u02a3\7^\2\2\u02a3\u02a7\7^\2\2\u02a4")
        buf.write("\u02a5\7)\2\2\u02a5\u02a7\7$\2\2\u02a6\u029e\3\2\2\2\u02a6")
        buf.write("\u02a0\3\2\2\2\u02a6\u02a2\3\2\2\2\u02a6\u02a4\3\2\2\2")
        buf.write("\u02a7\u0098\3\2\2\2\u02a8\u02a9\7^\2\2\u02a9\u02ad\n")
        buf.write("\22\2\2\u02aa\u02ab\7)\2\2\u02ab\u02ad\n\23\2\2\u02ac")
        buf.write("\u02a8\3\2\2\2\u02ac\u02aa\3\2\2\2\u02ad\u009a\3\2\2\2")
        buf.write("\u02ae\u02b3\7$\2\2\u02af\u02b2\5\u0095K\2\u02b0\u02b2")
        buf.write("\5\u0097L\2\u02b1\u02af\3\2\2\2\u02b1\u02b0\3\2\2\2\u02b2")
        buf.write("\u02b5\3\2\2\2\u02b3\u02b1\3\2\2\2\u02b3\u02b4\3\2\2\2")
        buf.write("\u02b4\u02b7\3\2\2\2\u02b5\u02b3\3\2\2\2\u02b6\u02b8\t")
        buf.write("\24\2\2\u02b7\u02b6\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b9")
        buf.write("\u02ba\bN\f\2\u02ba\u009c\3\2\2\2\u02bb\u02c0\7$\2\2\u02bc")
        buf.write("\u02bf\5\u0095K\2\u02bd\u02bf\5\u0097L\2\u02be\u02bc\3")
        buf.write("\2\2\2\u02be\u02bd\3\2\2\2\u02bf\u02c2\3\2\2\2\u02c0\u02be")
        buf.write("\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c1\u02c3\3\2\2\2\u02c2")
        buf.write("\u02c0\3\2\2\2\u02c3\u02c4\5\u0099M\2\u02c4\u02c5\bO\r")
        buf.write("\2\u02c5\u009e\3\2\2\2\u02c6\u02c7\13\2\2\2\u02c7\u02c8")
        buf.write("\bP\16\2\u02c8\u00a0\3\2\2\2;\2\u00fa\u012e\u0162\u016a")
        buf.write("\u0171\u0175\u017c\u0183\u0187\u018f\u0196\u019a\u01a3")
        buf.write("\u01aa\u01ae\u01b7\u01be\u01c2\u01c6\u01cd\u01d2\u01d4")
        buf.write("\u01d8\u01e0\u01e7\u01eb\u01ef\u01f6\u01fd\u0201\u0204")
        buf.write("\u0212\u021d\u0222\u0227\u022f\u0234\u023b\u0242\u0246")
        buf.write("\u0249\u024f\u0254\u0259\u025e\u0260\u026c\u0292\u0298")
        buf.write("\u02a6\u02ac\u02b1\u02b3\u02b7\u02be\u02c0\17\3+\2\3\65")
        buf.write("\3\3\65\4\3\65\5\3\65\6\3\67\7\3\67\b\3\67\t\3;\n\b\2")
        buf.write("\2\3N\13\3O\f\3P\r")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    IF = 3
    ELSEIF = 4
    ELSE = 5
    FOREACH = 6
    ARRAY = 7
    IN = 8
    BY = 9
    INT_TYPE = 10
    FLOAT_TYPE = 11
    BOOLEAN_TYPE = 12
    STRING_TYPE = 13
    NULL = 14
    RETURN = 15
    ATTRIBUTE_TYPE = 16
    SELF = 17
    NEW = 18
    CLASS = 19
    IMMUTABLE = 20
    MUTABLE = 21
    CONSTRUCTOR = 22
    DESTRUCTOR = 23
    DOLLAR_ID = 24
    ASSIGN = 25
    ADD = 26
    SUB = 27
    MUL = 28
    DIV = 29
    MOD = 30
    NOT = 31
    AND = 32
    OR = 33
    STRCOMPARE = 34
    CONCATE = 35
    EQUAL = 36
    NOTEQUAL = 37
    LARGER = 38
    SMALLER = 39
    LE = 40
    SE = 41
    INTLIT_ARR = 42
    INT_LIT_ARR = 43
    BIN_ = 44
    DEC_ = 45
    OCTAL_ = 46
    HEXA_ = 47
    INT_LITERAL = 48
    BOOL_LITERAL = 49
    FLOAT_LITERAL = 50
    STRING_LITERAL = 51
    BLOCK_COMMENT = 52
    LB = 53
    RB = 54
    LP = 55
    RP = 56
    LS = 57
    RS = 58
    DOUBLE_COLON = 59
    COLON = 60
    DOUBLEDOT = 61
    DOT = 62
    COMMA = 63
    SEMI_COLON = 64
    ID = 65
    WS = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68
    ERROR_CHAR = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'Array'", "'In'", "'By'", "'Int'", "'Float'", "'Boolean'", 
            "'String'", "'Null'", "'Return'", "'Self'", "'New'", "'Class'", 
            "'Val'", "'Var'", "'Constructor'", "'Destructor'", "'='", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'==.'", 
            "'+.'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "'::'", "':'", "'..'", "'.'", 
            "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "ARRAY", 
            "IN", "BY", "INT_TYPE", "FLOAT_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", 
            "NULL", "RETURN", "ATTRIBUTE_TYPE", "SELF", "NEW", "CLASS", 
            "IMMUTABLE", "MUTABLE", "CONSTRUCTOR", "DESTRUCTOR", "DOLLAR_ID", 
            "ASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
            "STRCOMPARE", "CONCATE", "EQUAL", "NOTEQUAL", "LARGER", "SMALLER", 
            "LE", "SE", "INTLIT_ARR", "INT_LIT_ARR", "BIN_", "DEC_", "OCTAL_", 
            "HEXA_", "INT_LITERAL", "BOOL_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
            "BLOCK_COMMENT", "LB", "RB", "LP", "RP", "LS", "RS", "DOUBLE_COLON", 
            "COLON", "DOUBLEDOT", "DOT", "COMMA", "SEMI_COLON", "ID", "WS", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "ARRAY", "IN", "BY", "INT_TYPE", "FLOAT_TYPE", "BOOLEAN_TYPE", 
                  "STRING_TYPE", "NULL", "RETURN", "ATTRIBUTE_TYPE", "SELF", 
                  "NEW", "CLASS", "IMMUTABLE", "MUTABLE", "CONSTRUCTOR", 
                  "DESTRUCTOR", "DOLLAR_ID", "ASSIGN", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "NOT", "AND", "OR", "STRCOMPARE", "CONCATE", 
                  "EQUAL", "NOTEQUAL", "LARGER", "SMALLER", "LE", "SE", 
                  "INTLIT_ARR", "INT_LIT_ARR", "BIN_", "DEC_", "OCTAL_", 
                  "HEXA_", "BINARY", "OCTAL", "HEXA", "NATURAL", "INT_LITERAL", 
                  "BOOL_LITERAL", "FLOAT_LITERAL", "INT_PART", "DECIMAL", 
                  "EXPONENT", "STRING_LITERAL", "BLOCK_COMMENT", "LB", "RB", 
                  "LP", "RP", "LS", "RS", "DOUBLE_COLON", "COLON", "DOUBLEDOT", 
                  "DOT", "COMMA", "SEMI_COLON", "ID", "WS", "STR_CHAR", 
                  "ESC_SEQ", "ESC_ILLEGAL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[41] = self.INTLIT_ARR_action 
            actions[51] = self.INT_LITERAL_action 
            actions[53] = self.FLOAT_LITERAL_action 
            actions[57] = self.STRING_LITERAL_action 
            actions[76] = self.UNCLOSE_STRING_action 
            actions[77] = self.ILLEGAL_ESCAPE_action 
            actions[78] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_ARR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def INT_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

        if actionIndex == 2:
            self.text = self.text.replace("_","")
     

        if actionIndex == 3:
            self.text = self.text.replace("_","")
     

        if actionIndex == 4:
            self.text = self.text.replace("_","")
     

    def FLOAT_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.text = self.text.replace("_","")
     

        if actionIndex == 6:
            self.text = self.text.replace("_","")
     

        if actionIndex == 7:
            self.text = self.text.replace("_","")
     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:

            clone = ['"', '\n']
            if self.text[-1] in clone:
            	raise UncloseString(self.text[1:-1])
            else:
            	raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 10:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 11:
            raise ErrorToken(self.text)
     


