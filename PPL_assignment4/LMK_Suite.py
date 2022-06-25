import unittest
from TestUtils import TestChecker
from TestUtils import TestAST
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_simple_redeclared_class(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {}
        Class DEF {}
        Class ABC {}
        """
        expect = "Redeclared Class: ABC"
        self.assertTrue(TestChecker.test(input, expect, 700))

    def test_simple_redeclared_attr_1(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            Var a: Int;
            Val b: Float = 1.2;
            Var a: Float;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 701))

    def test_simple_redeclared_attr_2(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            Var a: Int;
            Val b: Float = 1.2;
            Val a: Float;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 702))

    def test_simple_redeclared_attr_3(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            Val a: Int = 1;
            Val b: Float = 1.2;
            Val a: Float = 1;
        }
        Class DEF {
            Var b : Float;
            Var a : Int;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 703))

    def test_simple_redeclared_attr_4(self):
        """Inheritance checking"""
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            Val a: Int = 1;
            Val b: Float = 1.2;
        }
        Class DEF {
            Val b: Float = 1.2;
            Val b : Int = 1;
        }
        """
        expect = "Redeclared Attribute: b"
        self.assertTrue(TestChecker.test(input, expect, 704))

    def test_simple_redeclared_method_1(self):
        """Inheritance checking"""
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            main() {}
            foo() {}
            bar() {}
            foo() {}
        }
        """
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input, expect, 705))

    def test_simple_redeclared_method_2(self):
        """Inheritance checking"""
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            main() {}
            foo() {}
            bar() {}
        }
        Class DEF {
            bar() {}
            bar(w: Int; f: Float) {}
        }
        """
        expect = "Redeclared Method: bar"
        self.assertTrue(TestChecker.test(input, expect, 706))

    def test_redeclared_param_1(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            main(w: Int; h, f: Float; a, w: Int) {}
        }"""
        expect = "Redeclared Parameter: w"
        self.assertTrue(TestChecker.test(input, expect, 707))

    def test_redeclared_const(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            main(w: Int; h, f: Float; a: Int) {
                Var b : Float;
                Var c : Int;
                Val b : String = "";
            }
        }"""
        expect = "Redeclared Constant: b"
        self.assertTrue(TestChecker.test(input, expect, 708))

    def test_redeclared_var(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            main(w: Int; h, f: Float; a: Int) {
                Var b : Float;
                Var c : Int;
                Var b : String;
            }
        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 709))

    def test_redeclared_var_param(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            main(w: Int; h, f: Float; a: Int) {
                Var w : Int;
            }
        }"""
        expect = "Redeclared Variable: w"
        self.assertTrue(TestChecker.test(input, expect, 710))

    def test_redeclared_const_param(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            main(w: Int; h, f: Float; a: Int) {
                Val w : Int = 10;
            }
        }"""
        expect = "Redeclared Constant: w"
        self.assertTrue(TestChecker.test(input, expect, 711))

    def test_redeclared_param_2(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            main(w: Int; h, f: Float; a: Int) {
            }
            foo(w: Int; a, b: String; b: String) {}
        }"""
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 712))

    def test_type_mismatch_const_1(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            main() {
                Val b : Int = "Hello World";
            }
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(b),IntType,StringLit(Hello World))"
        self.assertTrue(TestChecker.test(input, expect, 713))

    def test_type_mismatch_const_2(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            Val a : Int = 1.2;
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 714))

    def test_type_mismatch_const_3(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class ABC {
            Val b : Float = 1;
            Val a : Int = 1.2;
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 715))

    def test_type_mismatch_const_4(self):
        input = """
        Class Program{
            main(){
                Return;
            }
        }
        Class B{}
        Class A{}
        Class ABC {
            method(){
                Var a : A;
                Var b : B;
                b = a;
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 716))

    def test_type_mismatch_const_5(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class A{
            Constructor(){}
        }
        Class B{}
        Class ABC {
            Val c : A = New A();
            Val b : B = Self.c;
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(b),ClassType(Id(B)),FieldAccess(Self(),Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 717))

    def test_type_mismatch_const_6(self):
        input = """
        Class Program {
            main(){
                Return;
            }
        }
        Class B{
            Constructor(){}
        }
        Class C{}
        Class D{}
        Class ABC {
            Val b : B = New B();
            Val d : D = Self.b;
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(d),ClassType(Id(D)),FieldAccess(Self(),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 718))

    def test_unary_type_1(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val d : Int = -1;
                Val e : Float = -1.1;
                Val b : Boolean = !True;
                Val a : Int = -1.0;
            }
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,UnaryOp(-,FloatLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 719))

    def test_binary_type_1(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val a : Float = 1.0 + 2.5;
                Val b : Int = 1 + 3;
                Val d : Int = 1 - 2;
                Val e : Float = 1.0 - 2.0;
                Val f : Float = 1 - 3.5;
                Val g : Int = 1 * 2;
                Val h : Float = 1.0 * 2.5;
                Val i : Float = 1 * 2.5;
                Val j : Int = 1 / 2;
                Val k : Float = 1.0 / 2.0;
                Val l : Float = 1.0 / 3;
                Val m : Int = 1 % 10;
                Val c : Int = 1 + 3.0;
            }
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(c),IntType,BinaryOp(+,IntLit(1),FloatLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 720))

    def test_binary_type_2(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val m : Int = 1 % 10.3;
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(%,IntLit(1),FloatLit(10.3))"
        self.assertTrue(TestChecker.test(input, expect, 721))

    def test_binary_type_3(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val a : Int = 1 % 10;
                Val b : Float = 10 % 100;
                Val c : Boolean = True && False;
                Val d : Boolean = ((True || False) && True) || False;
                Val e : Bool = 1 && True;
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(&&,IntLit(1),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 722))

    def test_binary_type_4(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val a : String = "abc" +. "def";
                Val b : Boolean = "abc" ==. "def";
                Val c : Boolean = (("abc" +. "def") ==. "def") && (1 == 1);
                Val d : String = 1.0 +. "2";
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+.,FloatLit(1.0),StringLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 723))

    def test_binary_type_5(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val a : Boolean = 1 != 2;
                Val b : Boolean = 1 == 2;
                Val c : Boolean = 1.0 == 2;
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLit(1.0),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 724))

    def test_binary_type_6(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val b : Boolean = True == True;
                Val c : Boolean = True != False;
                Val a : Boolean = 1.0 ==. "2";
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==.,FloatLit(1.0),StringLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 725))

    def test_binary_type_7(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val a : Boolean = 1.0 + 2.0 == 3.0;
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,BinaryOp(+,FloatLit(1.0),FloatLit(2.0)),FloatLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 726))

    def test_binary_type_8(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val a : Boolean = 10 > 2;
                Val b : Boolean = 1 < 2;
                Val c : Boolean = 2 <= 2;
                Val d : Boolean = 2 >= 2;
                Val e, f, g, h : Boolean = 1.0 > 2.0, 3.0 < 4.0, 5.6 >= 5.5, 4.8 <= 10.0;
                Val i, j, k, l : Boolean = 1 > 2.0, 2.2 < 1000, 5 >= 0.5, 6.2 <= 10e10;
                Val m : Boolean = True > False;
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(>,BooleanLit(True),BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 727))

    def test_binary_type_9(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val a : Boolean = ((-1 >= 2.0) && (("abc" +. "bec") ==. "def")) || ((1 + 2 - 4.0 >= 5) && !False);
                Val b : Float = (((1 % 10 >= 1.0) && !True) == False) ==. "False";
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==.,BinaryOp(==,BinaryOp(&&,BinaryOp(>=,BinaryOp(%,IntLit(1),IntLit(10)),FloatLit(1.0)),UnaryOp(!,BooleanLit(True))),BooleanLit(False)),StringLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 728))

    def test_binun_with_id_1(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val b : Int = 1;
                Val c : Int = 1 + b;
                Val d : String = 1 + b;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(d),StringType,BinaryOp(+,IntLit(1),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 729))

    def test_binun_with_id_2(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val a : Boolean = True;
                Val b : Boolean = !a;
                Val d : Int = 1;
                Val c : Float = 1.0 + d * 2;
                Val f : Boolean = (a || b) && (d >= c);
                Val e : String = a;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(e),StringType,Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 730))

    def test_undeclared_id_1(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            somehin() {
                Val b : Int = a;
            }
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 731))

    def test_undeclared_id_2(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class A{
            Constructor(){}
        }
        Class B{}
        Class ABC {
            somehin() {
                Val a : A = New A();
                Val b : B = a;
            }
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(b),ClassType(Id(B)),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 732))

    def test_undeclared_classtype_1(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class A{
            Var a : C;
        }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 733))

    def test_undeclared_classtype_2(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class A{}
        Class ABC {
            something() {
                Var a : C;
            }
        }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 734))

    def test_if_stmt_1(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val a : Int = 1;
                Var b, d : Int;
                If (True) {
                    Foreach (b In 1 .. 10 By -1) {
                        Val a : Float = 1.0;
                    }
                } Else {
                    Val c : Int = 1;
                    Foreach (d In 10 .. 100) {
                        If (d == 1) {
                            Val d : String = "abc";
                        } Elseif (d >= 2.0) {
                            Val a : Int = 1;
                        } Elseif ("abc" ==. "def") {
                            Val c : Float = 1.0;
                            If (c == 2) {
                                Val e : Int = 1;
                            }
                        }
                    }
                }
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(c),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 735))

    def test_if_stmt_2(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val a : Int = 1;
                If (a + 1) {
                    Foreach (b In 1 .. 10 By -1) {
                        Val a : Float = 1.0;
                    }
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),IntLit(1)),Block([For(Id(b),IntLit(1),IntLit(10),UnaryOp(-,IntLit(1)),Block([ConstDecl(Id(a),FloatType,FloatLit(1.0))])])]))"
        self.assertTrue(TestChecker.test(input, expect, 736))

    def test_foreach_1(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            something() {
                Val a : Int = 1;
                Var b, e : Int;
                If (a == 1) {
                    Foreach (b In 1 .. 10 By -1) {
                        Val a : Float = 1.0;
                        Val c : Float = 1;
                        If (a >= c + 1) {
                            Foreach (e In 1 .. 2 By 1) {
                                Val d : Int = 1;
                                If (e + 1 == 1) {
                                    Continue;
                                }
                            }
                            Continue;
                        } Else {
                            Continue;
                        }
                    }
                    Break;
                }
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 737))

    def test_return_type_1(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            somehing(w, i: Int; h, e: Float) {
                Val a : Int = 1;
                Return a + 1;
            }
            aaa() {
                Val a : Int = "";
            }
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,StringLit())"
        self.assertTrue(TestChecker.test(input, expect, 738))

    def test_array_cell_1(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            somehing(w, i: Int; h, e: Float) {
                Val a : Array[Int, 1] = Array(1);
                Val b : Int = a[0];
                Val c : Array[Array[String, 1], 1] = Array(Array("1"));
                Val d : String = c[0][0];
                Val f : Array[String, 9] = c[0];
            }
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(f),ArrayType(9,StringType),ArrayCell(Id(c),[IntLit(0)]))"
        self.assertTrue(TestChecker.test(input, expect, 739))

    def test_array_cell_2(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            somehing(w, i: Int; h, e: Float) {
                Val a : Array[Int, 1] = Array(1);
                Val b : Int = a[0];
                Val c : Array[Array[String, 1], 1] = Array(Array("1"));
                Val d : String = c[0][0];
                Val f : Array[String, 1] = c[0];
                Val g : Int = b[0];
            }
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),[IntLit(0)])"
        self.assertTrue(TestChecker.test(input, expect, 740))

    def test_array_cell_3(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            somehing(w, i: Int; h, e: Float) {
                Val a : Array[Int, 1] = Array(1);
                Val b : Int = a[1 + 10 - 2];
                Val c : Array[Array[String, 2], 2] = Array(Array("1", "2"), Array("3", "4"));
                Val d : String = c[2 * 3][2 > 0];
            }
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(c),[BinaryOp(*,IntLit(2),IntLit(3)),BinaryOp(>,IntLit(2),IntLit(0))])"
        self.assertTrue(TestChecker.test(input, expect, 741))

    def test_array_cell_4(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            somehing(w, i: Int; h, e: Float) {
                Val a : Array[Int, 1] = Array(1);
                Val b : Boolean = a[1 + 10 - 2] + 1 > 2;
                Val d : String = a[2 * 3];
            }
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(d),StringType,ArrayCell(Id(a),[BinaryOp(*,IntLit(2),IntLit(3))]))"
        self.assertTrue(TestChecker.test(input, expect, 742))

    # def test_field_access_1(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Return;
    #         }
    #     }
    #     Class ABC {
    #         Var a : Int = 1;
    #         Var $b : Int = 1;
    #     }
    #     Class BCD {
    #         Val a : String = "";
    #         Val $b : Float = 0.5;
    #         something(){
    #             Var c : ABC;
    #             Var b : Int = c.a + 1;
    #             Val a : Int = 1;
    #             Var d : Float = ABC::$b + 1.0;
    #             Val e : String = Self.a +. "Hello";
    #             Var f : Int = a + 2 + c.a;
    #             Var g : Boolean = BCD::$b >= 2.0;
    #             Val h : Int = a.a;
    #         }
    #     }"""
    #     expect = "Type Mismatch In Expression: FieldAccess(Id(a),Id(a))"
    #     self.assertTrue(TestChecker.test(input, expect, 743))

    def test_field_access_2(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            Var a : Int = 1;
            Var $b : Int = 1;
        }
        Class BCD {
            Val a : String = "";
            Val $b : Float = 0.5;
            something(){
                Var c : ABC;
                Var b : Int = c.a + 1;
                Val a : Int = 1;
                Var d : Float = ABC::$b + 1.0;
                Val e : String = Self.a +. "Hello";
                Var f : Int = a + 2 + c.a;
                Var g : Boolean = CDE::$b >= 2.0;
            }
        }"""
        expect = "Undeclared Class: CDE"
        self.assertTrue(TestChecker.test(input, expect, 744))

    def test_field_access_3(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            Var a : Int = 1;
            Var $b : Int = 1;
            Constructor() {}
        }
        Class BCD {
            Val a : String = "";
            Val $b : Float = 0.5;
            something(){
                Val c : ABC = New ABC();
                Var b : Int = c.a + 1;
                Val a : Int = 1;
                Var d : Float = ABC::$b + 1.0;
                Val e : String = Self.b +. "Hello";
            }
        }"""
        expect = "Undeclared Attribute: b"
        self.assertTrue(TestChecker.test(input, expect, 745))

    def test_field_access_4(self):
        input = """
        Class Program {
            main() {
                Return;
            }
        }
        Class ABC {
            Val a : Int = 1;
            Var $b : Int = 1;
            Constructor() {}
        }
        Class BCD {
            Val a : String = "";
            Val $b : Float = 0.5;
            something(){
                Val c : ABC = New ABC();
                Val b : Int = c.a + 1;
                Val d : Int = e.a;
            }
        }"""
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 746))

    def test_no_entry_point_1(self):
        input = """
        Class ABC {}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 747))

    def test_field_access_5(self):
        input = """
        Class Program {
            Val a : Int = 1;
            main() {
                Val c : Int = Self.a;
                Val b : Int = a;
                Return;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 748))

    def test_field_access_6(self):
        input = """
        Class Program {
            Val a : Int = 1;
            Val c : Int = Self.a;
            Val b : Int = a;
            main() {
                Return;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 749))

    def test_call_stmt_1(self):
        input = """
        Class Program {
            a() {
                Return;
            }
            c() {
                Val a : Int = 1;
            }
            d() {
                Return 1 + 1 * 2;
            }
            b() {
                Self.a();
                Self.c();
                Self.d();
            }
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: Call(Self(),Id(d),[])"
        self.assertTrue(TestChecker.test(input, expect, 750))

    def test_no_entry_point_2(self):
        input = """
        Class Program {
            mainABC() {
                Return;
            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 751))

    def test_no_entry_point_3(self):
        input = """
        Class Program {
            main(w: Int) {
                Return;
            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 752))

    def test_no_entry_point_4(self):
        input = """
        Class Program {
            main() {
            }
            method() {
                Val a : Int = 1.2;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 753))

    def test_no_entry_point_5(self):
        input = """
        Class ABC{}
        Class DEF{
            main() {
                Return;
            }
        }
        Class Program {
            abc(){}
            abcedf(){}
            mainAAA() {
                Return;
            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 754))

    def test_no_entry_point_6(self):
        input = """
        Class ABC{}
        Class DEF{
            main() {
                Return;
            }
        }
        Class Program {
            Val a: Int = 1;
            a(){}
            b(){}
            c(){}
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 755))

    def test_call_stmt_2(self):
        input = """
        Class ABC{}
        Class Program {
            a(w : Int) {
                Return;
            }
            c(w, h: Int) {
                Val a : Int = 1;
            }
            d(w, h: Int; a : String) {
                Return;
            }
            e(w, h: Int; a : String; b: ABC) {
                Return;
            }
            b() {
                Self.a(1);
                Self.c(1, 2 * 2 + 3);
                Var c : ABC;
                Self.e(1 * 2 + 3 - 4, 26 % 50, "Hello World", c);
                Self.d(1, "He", 2);
            }
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: Call(Self(),Id(d),[IntLit(1),StringLit(He),IntLit(2)])"
        # Type Mismatch In Statement: Call(Self(),Id(c),[IntLit(1),BinaryOp(+,BinaryOp(*,IntLit(2),IntLit(2)),IntLit(3))])
        self.assertTrue(TestChecker.test(input, expect, 756))

    def test_call_stmt_3(self):
        input = """
        Class ABC{}
        Class Program {
            a(w : Float) {
                Return;
            }
            b() {
                Self.a(1);
                Self.c();
            }
            main(){
                Return;
            }
        }
        """
        expect = "Undeclared Method: c"
        self.assertTrue(TestChecker.test(input, expect, 757))

    def test_call_stmt_4(self):
        input = """
        Class ABC{}
        Class Program {
            a(w : Float) {
                Return;
            }
            b() {
                Self.a(1);
                ABC::$c();
            }
            main(){
                Return;
            }
        }
        """
        expect = "Undeclared Method: $c"
        self.assertTrue(TestChecker.test(input, expect, 758))

    def test_call_stmt_5(self):
        input = """
        Class ABC{}
        Class Program {
            a(w : Float) {
                Return;
            }
            b() {
                Self.a(1);
                Var a : ABC;
                a.c();
            }
            main(){
                Return;
            }
        }
        """
        expect = "Undeclared Method: c"
        self.assertTrue(TestChecker.test(input, expect, 759))

    def test_call_stmt_6(self):
        input = """
        Class ABC{}
        Class DEF{}
        Class Program {
            a(w : ABC) {
                Return;
            }
            c(w: DEF; a: ABC; c: String) {}
            b() {
                Var a : DEF;
                Var e : ABC;
                Self.a(e);
                Val d : String = "Hello World";
                Self.c(a, e, d);
                Self.c(Null, e, d);
                Var b : ABC;
                Self.c(b, b, d);
            }
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: Call(Self(),Id(c),[NullLiteral(),Id(e),Id(d)])"
        # Type Mismatch In Statement: Call(Self(),Id(c),[NullLiteral(),Id(e),Id(d)])
        self.assertTrue(TestChecker.test(input, expect, 760))

    def test_call_expr_1(self):
        input = """
        Class Program {
            a() {
                Return 1;
            }
            b() {
                Val b : Int = Self.a() + 1;
                Self.a();
            }
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: Call(Self(),Id(a),[])"
        self.assertTrue(TestChecker.test(input, expect, 761))

    def test_call_expr_2(self):
        input = """
        Class Program {
            a() {
                Return;
            }
            b() {
                Val b : Int = Self.a() + 1;
            }
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Self(),Id(a),[])"
        self.assertTrue(TestChecker.test(input, expect, 762))

    def test_call_expr_3(self):
        input = """
        Class Program {
            c() {
                Val a : Int = 1;
                Return;
            }
            a() {
                Self.c();
                Return 1 + 1;
            }
            b() {
                Val b : Int = Self.a() + 1;
                Self.a();
            }
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: Call(Self(),Id(a),[])"
        self.assertTrue(TestChecker.test(input, expect, 763))

    def test_call_expr_4(self):
        input = """
        Class ABC{
            bbb(j, i: String; k: Boolean) {
                If (k) {
                    Return j;
                } Else {
                    Return i;
                }
            }
        }
        Class Program {
            a(w: Float; h: Int; a : ABC) {
                If ((a.bbb("Hello", "World", True) +. "Cool") ==. "Amazing") {
                    Return h + 1.0;
                } Else {
                    Return w;
                }
            }
            b() {
                Var a : ABC;
                Var b : Float = Self.a(1.0, 1, a) + 1;
                Self.a(1.0, 1, a);
            }
            main(){
                Return;
            }
            c(){}
        }
        """
        expect = "Type Mismatch In Statement: Call(Self(),Id(a),[FloatLit(1.0),IntLit(1),Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 764))

    def test_new_expr_1(self):
        input = """
        Class ABC{
            Constructor() {
                Return;
            }
            bbb(j, i: String; k: Boolean) {
                If (k) {
                    Return j;
                } Else {
                    Return i;
                }
            }
        }
        Class CED {
            Constructor(w, h: Int; a : String) {
                Var b : Boolean = a ==. "Hi";
                Var c : Float = w * h;
                Return;
            }
        }
        Class Program {
            a(w: Float; h: Int; a : ABC) {
                If ((a.bbb("Hello", "World", True) +. "Cool") ==. "Amazing") {
                    Return h + 1.0;
                } Else {
                    Return w;
                }
            }
            b() {
                Var a : ABC = New ABC();
                Var b : Float = Self.a(1.0, 1, a) + 1;
                Var c : CED = New CED(1, 2, "Hi");
                Self.a(1.0, 1, a);
            }
            main(){
                Return;
            }
            c(){}
        }
        """
        expect = "Type Mismatch In Statement: Call(Self(),Id(a),[FloatLit(1.0),IntLit(1),Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 765))

    def test_array_literal_1(self):
        input = """
        Class Program {
            main(){
                Val a : Array[Int, 1] = Array(1);
                Val b : Array[String, 2] = Array("Hello", "World");
                Val c : Array[Array[Int, 2], 2] = Array(Array(1, 2), Array(2, 3));
                Val d : Array[Int, 2] = c[0];
                Val e : Array[Array[Array[Int, 2], 2], 2] = Array(Array(Array(2, 3), Array(4, 5)), Array(Array(6, 7), Array(5 * 8, 7 % 2)));
                Val f : Array[Int, 2] = Array(2, 3.0);
                Return;
            }
        }
        """
        expect = "Illegal Array Literal: [IntLit(2),FloatLit(3.0)]"
        self.assertTrue(TestChecker.test(input, expect, 766))

    def test_array_literal_2(self):
        input = """
        Class Program {
            main(){
                Val f : Array[Array[Int, 2], 2] = Array(Array(2, 3), Array(1));
                Return;
            }
        }
        """
        expect = "Illegal Array Literal: [[IntLit(2),IntLit(3)],[IntLit(1)]]"
        self.assertTrue(TestChecker.test(input, expect, 767))

    def test_array_literal_3(self):
        input = """
        Class Program {
            main(){
                Val f : Array[Array[Int, 2], 2] = Array(Array(2, 3), Array());
                Return;
            }
        }
        """
        expect = "Illegal Array Literal: []"
        self.assertTrue(TestChecker.test(input, expect, 768))

    def test_array_literal_4(self):
        input = """
        Class Program {
            main(){
                Val f : Array[Array[Int, 2], 2] = Array(Array(2, 3));
                Return;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(f),ArrayType(2,ArrayType(2,IntType)),[[IntLit(2),IntLit(3)]])"
        self.assertTrue(TestChecker.test(input, expect, 769))

    def test_array_literal_5(self):
        input = """
        Class Program {
            main(){
                Val f : Array[Array[Int, 2], 2] = Array(Array(1, 2), Array("Hello", "World"));
                Return;
            }
        }
        """
        expect = "Illegal Array Literal: [[IntLit(1),IntLit(2)],[StringLit(Hello),StringLit(World)]]"
        self.assertTrue(TestChecker.test(input, expect, 770))

    def test_array_literal_6(self):
        input = """
        Class Program {
            main(){
                Val a : Array[Float, 2] = Array(1, 2);
                Return;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),ArrayType(2,FloatType),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 771))

    def test_assign_id_const_1(self):
        input = """
        Class Program {
            main(){
                Val a : Int = 1;
                a = 2;
                Return;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 772))

    def test_assign_id_const_2(self):
        input = """
        Class Program {
            Val a : Int = 1;
            main(){
                Self.a = 2;
                Return;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(a)),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 773))

    def test_assign_id_const_3(self):
        input = """
        Class ABC {
            Val a : Int = 1;
            Var b : String = "Hello";
            Constructor(){
                Return;
            }
        }
        Class Program {
            Val a : Int = 1;
            Val b : ABC = New ABC();
            main(){
                Self.b.b = "Hi";
                Self.a = 2;
                Return;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(a)),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 774))

    def test_assign_id_const_4(self):
        input = """
        Class ABC {
            Val a : Int = 1;
            Var b : String = "Hello";
            Constructor(){
                Return;
            }
        }
        Class Program {
            Val a : Int = 1;
            Val b : ABC = New ABC();
            main(){
                Self.b.b = "Hi";
                Self.a = 2;
                Return;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(a)),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 775))

    def test_assign_id_const_5(self):
        input = """
        Class Program {
            main(){
                Val a : Array[Int, 1] = Array(1);
                a[0] = 1;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(a),[IntLit(0)]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 776))

    def test_assign_id_const_6(self):
        input = """
        Class Program {
            Val a : Array[Int, 1] = Array(1);
            main(){
                Self.a[0] = 1;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(0)]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 777))

    def test_assign_id_const_7(self):
        input = """
        Class Program {
            Val a : Array[Int, 1] = Array(1);
            main(){
                Self.a[0] = 1;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(0)]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 778))

    def test_assign_id_const_8(self):
        input = """
        Class ABC {
            Val b : Array[Int, 1] = Array(1);
        }
        Class Program {
            main(){
                Var b : ABC;
                b.b = 1;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(b),Id(b)),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 779))

    def test_assign_id_const_9(self):
        input = """
        Class ABC {
            Val b : Array[Int, 1] = Array(1);
        }
        Class Program {
            main(){
                Var b : ABC;
                b.b[0] = 1;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(FieldAccess(Id(b),Id(b)),[IntLit(0)]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 780))

    def test_assign_id_const_10(self):
        input = """
        Class ABC {
            Val b : Array[Int, 1] = Array(1);
        }
        Class Program {
            main(){
                Var b : ABC;
                b.b[0] = 1;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(FieldAccess(Id(b),Id(b)),[IntLit(0)]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 781))

    def test_assign_id_const_11(self):
        input = """
        Class ABC {
            Var b : Array[Int, 1] = Array(1);
        }
        Class Program {
            main(){
                Var b : ABC;
                Val a : Int = 1;
                b.b[a + 1] = 1;
                a = 2;
                Return;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 782))

    def test_const_assign_immutable_1(self):
        input = """
        Class Program {
            main(){
                Var b : Int;
                Val a : Int = b;
                Return;
            }
        }
        """
        expect = "Illegal Constant Expression: Id(b)"
        self.assertTrue(TestChecker.test(input, expect, 783))

    def test_const_assign_immutable_2(self):
        input = """
        Class Program {
            Var b : Int;
            Val a : Int = Self.b;
            main(){
                Return;
            }
        }
        """
        expect = "Illegal Constant Expression: FieldAccess(Self(),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 784))

    def test_const_assign_immutable_3(self):
        input = """
        Class ABC {
            Val b : Int = 1;
            Constructor(){}
        }
        Class Program {
            main(){
                Var c : ABC = New ABC();
                Val d : ABC = New ABC();
                Val a : Int = d.b;
                Val b : ABC = c;
                Return;
            }
        }
        """
        expect = "Illegal Constant Expression: Id(c)"
        self.assertTrue(TestChecker.test(input, expect, 785))

    def test_const_assign_immutable_4(self):
        input = """
        Class ABC {
            Val $b : Int = 1;
            Var $e : Int = 1;
        }
        Class Program {
            Val $a : Int = 1;
            main(){
                Val c : Array[Int, 1] = Array(1);
                Val a : Int = c[0];
                Val b : Int = Program::$a;
                Val d : Int = ABC::$b;
                Val e : Int = ABC::$e;
                Return;
            }
        }
        """
        expect = "Illegal Constant Expression: FieldAccess(Id(ABC),Id($e))"
        self.assertTrue(TestChecker.test(input, expect, 786))

    def test_assign_const_1(self):
        input = """
        Class Program {
            Val $a : Int = 1;
            main(){
                Program::$a = 2;
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(Program),Id($a)),IntLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 787))

    def test_assign_1(self):
        input = """
        Class Program {
            main(){
                Var a : Int = 1;
                a = "Hello";
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),StringLit(Hello))"
        self.assertTrue(TestChecker.test(input, expect, 788))

    def test_assign_2(self):
        input = """
        Class ABC{}
        Class DEF{}
        Class Program {
            main(){
                Var a : ABC = Null;
                Var d : DEF = Null;
                d = a;
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(d),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 789))

    def test_param_is_var(self):
        input = """
        Class Program {
            main(){
                Return;
            }
            method(w: Int) {
                Val a : Int = w;
            }
        }"""
        expect = "Illegal Constant Expression: Id(w)"
        self.assertTrue(TestChecker.test(input, expect, 790))

    def test_attr_method_same_name_1(self):
        input = """
        Class A{
            Val x : Int = 1;
        }
        Class B {
            Var x : Int = 1;
            x(w: Int) {
                Return Self.x;
            }
        }
        Class Program {
            main(){
                Var b : B;
                Var a : Int = b.x(1);
                Val a : String = "Hi";
                Return;
            }
        }"""
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 791))

    def test_recursive_class_1(self):
        input = """
        Class A{
            Constructor(){}
            Var $a : A = New A();
            Var a : A = A::$a;
        }
        Class Program {
            main(){
                Var b : A = New A();
                Val b : Int = 1;
                Return;
            }
        }"""
        expect = "Redeclared Constant: b"
        self.assertTrue(TestChecker.test(input, expect, 792))

    def test_mismatch_statment_1(self):
        input = """
        Class A{
            Var a : Int = 1.1;
        }
        Class Program {
            main(){
                Return;
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,FloatLit(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 793))

    def test_mismatch_statment_2(self):
        input = """
        Class Program {
            main(){
                Var a : Int = 1.1;
                Return;
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,FloatLit(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 794))

    def test_illegal_member_access_1(self):
        input = """
        Class ABC {
            Var a : Int = 1;
        }
        Class Program {
            main(){
                Return;
            }
            method(){
                Var b : Int = ABC.a;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(ABC),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 795))

    def test_illegal_member_access_2(self):
        input = """
        Class ABC {
            Var a : Int = 1;
            Var $a : Int = 1;
            $b(){}
            b(){}
            c(){Return 1;}
            $c(){Return 1;}
        }
        Class Program {
            main(){
                Return;
            }
            method(){
                Var abc : ABC;
                Var b : Int = abc.a;
            }
            $method() {
                Val a : Int = 1.2;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 796))

    def test_illegal_member_access_3(self):
        input = """
        Class ABC {
            Var a : Int = 1;
            Var $a : Int = 1;
            $b(){}
            b(){}
            c(){Return 1;}
            $c(){Return 1;}
        }
        Class Program {
            main(){
                Return;
            }
            method(){
                Var b : Int = ABC::$a;
            }
            $method() {
                Val a : Int = 1.2;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 797))

    def test_illegal_member_access_4(self):
        input = """
        Class ABC {
            Var a : Int = 1;
            Var $a : Int = 1;
            $b(){}
            b(){}
            c(){Return 1;}
            $c(){Return 1;}
        }
        Class Program {
            main(){
                Return;
            }
            method(){
                Var abc : ABC;
                Var b : Int = abc::$a;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(abc),Id($a))"
        self.assertTrue(TestChecker.test(input, expect, 798))

    def test_illegal_member_access_5(self):
        input = """
        Class ABC {
            Var a : Int = 1;
            Var $a : Int = 1;
            $b(){}
            b(){}
            c(){Return 1;}
            $c(){Return 1;}
        }
        Class Program {
            main(){
                Return;
            }
            method(){
                Var b : Int = ABC.c();
            }
        }
        """
        expect = "Illegal Member Access: CallExpr(Id(ABC),Id(c),[])"
        self.assertTrue(TestChecker.test(input, expect, 799))

    def test_illegal_member_access_6(self):
        input = """
        Class ABC {
            Var a : Int = 1;
            Var $a : Int = 1;
            $b(){}
            b(){}
            c(){Return 1;}
            $c(){Return 1;}
        }
        Class Program {
            main(){
                Return;
            }
            method(){
                Var b : Int = ABC::$c();
            }
            $method() {
                Val a : Int = 1.2;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 800))

    def test_illegal_member_access_7(self):
        input = """
        Class ABC {
            Var a : Int = 1;
            Var $a : Int = 1;
            $b(){}
            b(){}
            c(){Return 1;}
            $c(){Return 1;}
        }
        Class Program {
            main(){
                Return;
            }
            method(){
                Var abc : ABC;
                Var b : Int = abc.c();
            }
            $method() {
                Val a : Int = 1.2;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 801))

    def test_illegal_member_access_8(self):
        input = """
        Class ABC {
            Var a : Int = 1;
            Var $a : Int = 1;
            $b(){}
            b(){}
            c(){Return 1;}
            $c(){Return 1;}
        }
        Class Program {
            main(){
                Return;
            }
            method(){
                Var abc : ABC;
                Var b : Int = abc::$c();
            }
        }
        """
        expect = "Illegal Member Access: CallExpr(Id(abc),Id($c),[])"
        self.assertTrue(TestChecker.test(input, expect, 802))

    def test_illegal_member_access_9(self):
        input = """
        Class ABC {
            Var a : Int = 1;
            Var $a : Int = 1;
            $b(){}
            b(){}
            c(){Return 1;}
            $c(){Return 1;}
        }
        Class Program {
            main(){
                Return;
            }
            method(){
                ABC.b();
            }
        }
        """
        expect = "Illegal Member Access: Call(Id(ABC),Id(b),[])"
        self.assertTrue(TestChecker.test(input, expect, 803))

    def test_illegal_member_access_10(self):
        input = """
        Class ABC {
            Var a : Int = 1;
            Var $a : Int = 1;
            $b(){}
            b(){}
            c(){Return 1;}
            $c(){Return 1;}
        }
        Class Program {
            main(){
                Return;
            }
            method(){
                ABC::$b();
            }
            $method() {
                Val a : Int = 1.2;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 804))

    def test_illegal_member_access_11(self):
        input = """
        Class ABC {
            Var a : Int = 1;
            Var $a : Int = 1;
            $b(){}
            b(){}
            c(){Return 1;}
            $c(){Return 1;}
        }
        Class Program {
            main(){
                Return;
            }
            method(){
                Var abc : ABC;
                abc::$b();
            }
        }
        """
        expect = "Illegal Member Access: Call(Id(abc),Id($b),[])"
        self.assertTrue(TestChecker.test(input, expect, 805))

    def test_illegal_member_access_12(self):
        input = """
        Class ABC {
            Var a : Int = 1;
            Var $a : Int = 1;
            $b(){}
            b(){}
            c(){Return 1;}
            $c(){Return 1;}
        }
        Class Program {
            main(){
                Return;
            }
            method(){
                Var abc : ABC;
                abc.b();
            }
            $method() {
                Val a : Int = 1.2;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 806))

    def test_default_constructor_1(self):
        input = """
        Class ABC {}
        Class Program{
            main() {
                Var a : ABC = New ABC();
                Val a : Int = 1;
                Return;
            }
        }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 807))

    def test_default_constructor_2(self):
        input = """
        Class ABC {
            Constructor(w: Int) {}
        }
        Class Program{
            main() {
                Var a : ABC = New ABC(1);
                Var b : ABC = New ABC();
                Return;
            }
        }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(ABC),[])"
        self.assertTrue(TestChecker.test(input, expect, 808))

    def test_random_thing_1(self):
        input = """
        Class Program{
            main() {
                Var x : Int = 1.2;
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 809))

    def test_random_thing_2(self):
        input = """
        Class C {}
        Class A{
            Var c: C = New C(); 
            Var d: C = New C(1); 
        }
        """
        expect = "Type Mismatch In Expression: NewExpr(Id(C),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 810))

    def test_constructor_1(self):
        input = """
        Class C {
            Constructor(w : Int){}
            Constructor(){}
        }
        Class A{
            Var c: C = New C(); 
            Var d: C = New C(1); 
        }
        """
        expect = "Redeclared Method: Constructor"
        self.assertTrue(TestChecker.test(input, expect, 811))

    def test_destructor_1(self):
        input = """
        Class C {
            Destructor(){}
            Destructor(){
                Val a : Int = 1;
            }
        }
        Class A{
            Var c: C = New C(); 
            Var d: C = New C(1); 
        }
        """
        expect = "Redeclared Method: Destructor"
        self.assertTrue(TestChecker.test(input, expect, 812))

    def test_random_thing_3(self):
        input = """
        Class Program {
            Var a : Int;
            a() {}
            main(){
                Return;
                Val a : Int = Self.a;
            }
        }
        """
        expect = "Illegal Constant Expression: FieldAccess(Self(),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 813))

    # def test_random_thing_4(self):
    #     input = """
    #     Class Program {
    #         main(){
    #             Var a : Int = 1;
    #             Val b : Array[Int, 2] = Array(1, a);
    #             Return;
    #         }
    #     }
    #     """
    #     expect = "Illegal Constant Expression: [IntLit(1),Id(a)]"
    #     self.assertTrue(TestChecker.test(input, expect, 814))

    def test_random_thing_5(self):
        input = """
        Class ABC {
            $a() {}
        }
        Class Program {
            main(){
                Var a, c : Boolean = True, False;
                Var b : Int = 1;
                If (a) {
                    ABC::$a();
                } Elseif (b) {
                    ABC::$a();
                } Elseif (c) {
                    ABC::$a();
                } Else {
                    ABC::$a();
                }
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: If(Id(b),Block([Call(Id(ABC),Id($a),[])]),If(Id(c),Block([Call(Id(ABC),Id($a),[])]),Block([Call(Id(ABC),Id($a),[])])))"
        self.assertTrue(TestChecker.test(input, expect, 815))

    def test_random_thing_6(self):
        input = """
        Class Program {
            main(){
                Var a : Int = 1;
                Var x : Int;
                Foreach (x In 1 .. 10 By 2) {
                    Break;
                    Break;
                    a = "ABC";
                }
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),StringLit(ABC))"
        self.assertTrue(TestChecker.test(input, expect, 816))

    def test_random_thing_7(self):
        input = """
        Class Program {
            Val a : Int = 1;
            mainAAA(){
                Val a : Int = Self.a;
                Val b : Int = a;
                Return;
            }
            main() {
                Return;
            }
            $method() {
                Val a : Int = 1.2;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 817))

    def test_random_thing_8(self):
        input = """
        Class Program{
            main() {
                Val a: Int = a;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 818))

    def test_random_thing_9(self):
        input = """
        Class Program{
            main() {
                Val a: Float = 9e4;
                Var b: Boolean = 1 + (0B101011 - 5) * 0.4 + a;
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b),BoolType,BinaryOp(+,BinaryOp(+,IntLit(1),BinaryOp(*,BinaryOp(-,IntLit(43),IntLit(5)),FloatLit(0.4))),Id(a)))"
        self.assertTrue(TestChecker.test(input, expect, 819))

    def test_random_thing_10(self):
        input = """
        Class ABC {
            Var x : Int = 1;
        }
        Class Program{
            main() {
                Val a : ABC = New ABC();
                a.x = 2;
                Return;
            }
            $method() {
                Val a : Int = 1.2;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 820))

    def test_random_thing_11(self):
        input = """
        Class ABC {
            Var x : Int = 1;
        }
        Class Program{
            main() {
                Var a : Int = ABC.x;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(ABC),Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 821))

    def test_random_thing_12(self):
        input = """
        Class CED {
            Var c : Int;
        }
        Class ABC {
            Var ced : CED;
        }
        Class Program{
            main() {
                Val x : Int = ABC.ced.c;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(ABC),Id(ced))"
        self.assertTrue(TestChecker.test(input, expect, 822))

    def test_random_thing_13(self):
        input = """
        Class CED {
            Val c : Int = 1;
        }
        Class ABC {
            Var ced : CED;
        }
        Class Program{
            main() {
                Val a : ABC = New ABC();
                Val x : Int = a.ced.c;
                Return;
            }
        }
        """
        expect = "Illegal Constant Expression: FieldAccess(FieldAccess(Id(a),Id(ced)),Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 823))

    def test_random_thing_14(self):
        input = """
        Class A{
            Val y: Int = 10;
        }
        Class B{
            Var x: A;
            func(){
                Val z: Int = Self.x.y;
            }
        }
        Class Program{
            main(){}
        }
        """
        expect = "Illegal Constant Expression: FieldAccess(FieldAccess(Self(),Id(x)),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 824))

    def test_random_thing_15(self):
        input = """
        Class A{}
        Class B{}
        Class Program {
            Var x: A = New B();
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x),ClassType(Id(A)),NewExpr(Id(B),[]))"
        self.assertTrue(TestChecker.test(input, expect, 825))

    def test_random_thing_16(self):
        input = """
        Class Program {
            Var $myArray: Array[Array[Array[Int,4],2],2] = Array(
                    Array(
                        Array(1,2,3,4),
                        Array(5,6,7,8)
                    ),
                    Array(
                        Array(-1,-2,-3,-4),
                        Array(-5,-6,-7, False)
                    )
                );
            main(){}
        }
        """
        expect = "Illegal Array Literal: [[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(5),IntLit(6),IntLit(7),IntLit(8)]],[[UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2)),UnaryOp(-,IntLit(3)),UnaryOp(-,IntLit(4))],[UnaryOp(-,IntLit(5)),UnaryOp(-,IntLit(6)),UnaryOp(-,IntLit(7)),BooleanLit(False)]]]"
        # Illegal Array Literal: [[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(5),IntLit(6),IntLit(7),IntLit(8)]],[[UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2)),UnaryOp(-,IntLit(3)),UnaryOp(-,IntLit(4))],[UnaryOp(-,IntLit(5)),UnaryOp(-,IntLit(6)),UnaryOp(-,IntLit(7)),BooleanLit(False)]]]
        self.assertTrue(TestChecker.test(input, expect, 826))

    def test_random_thing_17(self):
        input = """
        Class A {
            Val x : Int = 1;
        }
        Class D : A {
            Val x : Int = 1;
        }
        Class B : C {}
        Class Program {
            main() {
                Return;
            }
        }
        """
        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 827))

    def test_random_thing_18(self):
        input = """
        Class A {
            Val x : Int = 1;
        }
        Class D : A {
            Val x : Int = 1;
        }
        Class E {
            main() {
                Var a : A = New D();
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),ClassType(Id(A)),NewExpr(Id(D),[]))"
        self.assertTrue(TestChecker.test(input, expect, 828))

    def test_random_thing_19(self):
        input = """
        Class P {
            Destructor() {
                Return;
            }
        }
        Class Program {
            main() {
                Var p : P;
                Val a : Int = 1.2;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 829))

    def test_random_thing_20(self):
        input = """
        Class A{
            Val x : Int = 1;
        }
        Class B : A {
            x(w: Int) {
                Return Self.x;
            }
        }
        Class Program {
            main(){
                Var b : B;
                Var a : Int = b.x(1);
                Val a : String = "Hi";
                Return;
            }
        }"""
        expect = "Undeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 830))

    def test_return_constructor_main_1(self):
        input = """
        Class Program {
            main() {
                Return 1;
            }
        }"""
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 831))

    def test_return_constructor_main_2(self):
        input = """
        Class Program {
            Constructor() {
                Return 1;
            }
        }"""
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 832))

    def test_foreach_loop_1(self):
        input = """
        Class Program {
            Var x : Int = 1;
            main() {
                Return;
            }
            method() {
                Foreach (b In 1 .. 10 By 1) {
                    Val a : Int = 1;
                }
            }
        }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 833))

    def test_foreach_loop_2(self):
        input = """
        Class Program {
            Var x : Int = 1;
            main() {
                Return;
            }
            method() {
                Val b : Int = 1;
                Foreach (b In 100 .. 10000 By 1) {
                    Val a : Int = 1;
                }
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(Id(b),IntLit(100))"
        self.assertTrue(TestChecker.test(input, expect, 834))

    def test_foreach_loop_3(self):
        input = """
        Class Program {
            Var x : Int = 1;
            main() {
                Return;
            }
            method() {
                Var b : String = "Hello";
                Foreach (b In 100 .. 10000 By 1) {
                    Val a : Int = 1;
                }
            }
        }"""
        expect = "Type Mismatch In Statement: For(Id(b),IntLit(100),IntLit(10000),IntLit(1),Block([ConstDecl(Id(a),IntType,IntLit(1))])])"
        self.assertTrue(TestChecker.test(input, expect, 835))

    def test_random_thing_21(self):
        input = """
        Class A{
            Val y:Int=10;
        }
        Class B{
            Var x:A = New A();
            func (){
                Self.x.y = 1;
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(FieldAccess(Self(),Id(x)),Id(y)),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 836))

    def test_random_thing_22(self):
        input = """
        Class A{
            $method() {
                Val a : Array[Int, 2] = Array(2, 2);
                a[0] = 1;
            }   
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(a),[IntLit(0)]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 837))

    def test_random_thing_23(self):
        input = """
        Class A : A{}
        """
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 838))

    def test_random_thing_24(self):
        input = """
        Class A {
            Var a : Int = 1.2;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 839))

    def test_random_thing_25(self):
        input = """
        Class A {
            Var a : Int;
            $a() {
                Var a : Int = Self.a;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Self(),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 840))

    ## REM
    # def test_random_thing_26(self):
    #     input = """
    #     Class Program{
    #         Var a: Int = 10; 
    #         foo() { 
    #             Val a : Array[Int, 3] = Array(Self.a, 1, 2);
    #             Val b : Int = a[0];
    #         }
    #         main(){}
    #     }
    #     """
    #     expect = "Illegal Constant Expression: [FieldAccess(Self(),Id(a)),IntLit(1),IntLit(2)]"
    #     self.assertTrue(TestChecker.test(input, expect, 841))

    def test_random_thing_27(self):
        input = """
        Class A {
            a() {Return 1;}
            $a() {
                Var a : Int = Self.a();
            }
        }
        """
        expect = "Illegal Member Access: CallExpr(Self(),Id(a),[])"
        self.assertTrue(TestChecker.test(input, expect, 842))

    def test_random_thing_28(self):
        input = """
        Class A {
            a() {}
            $a() {
                Self.a();
            }
        }
        """
        expect = "Illegal Member Access: Call(Self(),Id(a),[])"
        self.assertTrue(TestChecker.test(input, expect, 843))

    def test_random_thing_29(self):
        input = """
        Class A {
            a() {}
            $b() {}
            b() {
                Self.a();
            }
            $a() {
                Self.a();
            }
        }
        """
        expect = "Illegal Member Access: Call(Self(),Id(a),[])"
        self.assertTrue(TestChecker.test(input, expect, 844))

    ###################################### TO HEREE ############################################

    # def test_confused_array(self):
    #     input = """
    #     Class A {
    #         Var d, e: Int;
    #         Val f: Array[Array[Int,1], 2] = Array( Array(Self.d), Array(Self.e) );
    #     }
    #     Class Program{main(){}}
    #     """
    #     expect = "Illegal Constant Expression: [[FieldAccess(Self(),Id(d))],[FieldAccess(Self(),Id(e))]]"
    #     self.assertTrue(TestChecker.test(input, expect, 845))

    # def test_multiple_return_1(self):
    #     input = """
    #     Class A {
    #         method() {
    #             If (True) {
    #                 Return 1;
    #             } Else {
    #                 Return "String";
    #             }
    #         }
    #     }"""
    #     expect = "Type Mismatch In Statement: Return(StringLit(String))"
    #     self.assertTrue(TestChecker.test(input, expect, 846))

    # def test_multiple_return_1(self):
    #     input = """
    #     Class A {
    #         method() {
    #             Val a : Int = 1;
    #             If (True) {
    #                 Return 1;
    #             } Elseif (False) {
    #                 Return 1 + a;
    #             } Elseif (True) {
    #                 Return 2 * a;
    #             } Else {
    #                 Return "String";
    #             }
    #         }
    #     }"""
    #     expect = "Type Mismatch In Statement: Return(StringLit(String))"
    #     self.assertTrue(TestChecker.test(input, expect, 846))

    # def test_mutable_method_1(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Return;
    #         }
    #         method() {
    #             Var a : Int = 1;
    #             Var b : Int = a;
    #             Val c : Int = 1;
    #             Return a;
    #         }
    #         method2() {
    #             Val b : Int = Self.method();
    #         }
    #     }"""
    #     expect = "Illegal Constant Expression: CallExpr(Self(),Id(method),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 847))

    # def test_mutable_method_2(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Return;
    #         }
    #         method() {
    #             Var a : Int = 1;
    #             Var b : Int = a;
    #             Val c : Int = 1;
    #             If (True) {
    #                 Return c;
    #             } Else {
    #                 Return a;
    #             }
    #         }
    #         method2() {
    #             Val b : Int = Self.method();
    #         }
    #     }"""
    #     expect = "Illegal Constant Expression: CallExpr(Self(),Id(method),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 848))
