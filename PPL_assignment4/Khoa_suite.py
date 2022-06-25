import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test_classdecl_0(self):
        input = r"""
        Class Program {
        }
        Class Program {
        }
        """
        expect = r"""Redeclared Class: Program"""
        self.assertTrue(TestChecker.test(input, expect, 19100))

    def test_classdecl_1(self):
        input = r"""
        Class Child : Parent {
        }
        """
        expect = r"""Undeclared Class: Parent"""
        self.assertTrue(TestChecker.test(input, expect, 19101))

    def test_classdecl_2(self):
        input = r"""
        Class Child {
        }
        Class Child : Parent {
        }
        """
        expect = r"""Redeclared Class: Child"""
        self.assertTrue(TestChecker.test(input, expect, 19102))

    def test_classdecl_3(self):
        input = r"""
        Class Child : Parent {
        }
        Class Parent {
        }
        """
        expect = r"""Undeclared Class: Parent"""
        self.assertTrue(TestChecker.test(input, expect, 19103))

    def test_attrdecl_5(self):
        input = r"""
        Class Program {
          Var a: Int;
          Var $a: Int;
          Var a: String;
          main() {
          }
        }
        """
        expect = r"""Redeclared Attribute: a"""
        self.assertTrue(TestChecker.test(input, expect, 19104))

    def test_attrdecl_0(self):
        input = r"""
        Class Program {
          Val i: Int = 2;
          Var i: Float;
        }
        """
        expect = r"""Redeclared Attribute: i"""
        self.assertTrue(TestChecker.test(input, expect, 19105))

    def test_attrdecl_1(self):
        input = r"""
        Class Program {
          Val i: Int = 2;
          main(){
          }
        }
        Class Subprogram : Program {
          Var s, s: String = "OMEGALUL", "KEKW";
        }
        """
        expect = r"""Redeclared Attribute: s"""
        self.assertTrue(TestChecker.test(input, expect, 19106))

    def test_attrdecl_2(self):
        input = r"""
        Class Program {
          Val i: Int = 2;
        }
        Class Subprogram : Program {
          Var s: String = "OMEGALUL";
        }
        Class Subsubprogram : Subprogram {
          Var $f: String = "OMEGALUL";
          Var $f: Float;
        }
        """
        expect = r"""Redeclared Attribute: $f"""
        self.assertTrue(TestChecker.test(input, expect, 19107))

    def test_attrdecl_3(self):
        input = r"""
        Class Program {
          Val g: Int = 2;
        }
        Class Subprogram : Program {
          Var a: String = "OMEGALUL";
        }
        Class Subsubprogram : Subprogram {
          Var y: String = "OMEGALUL";
        }
        Class Subsubsubprogram : Subsubprogram {
          g(){}
          Val g: Boolean = False;
        }
        """
        expect = r"""No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 19108))

    def test_attrdecl_4(self):
        input = r"""
        Class Program {
          Val g: Int = 2;
        }
        Class Subprogram : Program {
          Var a: String = "OMEGALUL";
        }
        Class Subsubprogram : Subprogram {
          Var y: String = "OMEGALUL";
          Var $y: Int;
          foo(){}
          $y(){}
        }
        """
        expect = r"""No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 19109))

    def test_methoddecl_0(self):
        input = r"""
        Class Program {
          Val g: Int = 2;
          $foo() {
          }
          Var $foo: Boolean;
        }
        """
        expect = r"""No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 19110))

    def test_methoddecl_1(self):
        input = r"""
        Class Program {
          Val g: Int = 2;
          foo() {
          }
        }
        Class Subprogram : Program {
          food(){
          }
          food(a: Int){
          }
        }
        """
        expect = r"""Redeclared Method: food"""
        self.assertTrue(TestChecker.test(input, expect, 19111))

    def test_methoddecl_2(self):
        input = r"""
        Class Program {
          Val g: Int = 2;
          foo(a, b: Int) {
          }
          foo(a, b: Int){
          }
        }
        """
        expect = r"""Redeclared Method: foo"""
        self.assertTrue(TestChecker.test(input, expect, 19112))

    def test_methoddecl_3(self):
        input = r"""
        Class Program {
          Val g: Int = 2;
          Val foo: String = "Lmao";
          foo(a, b: Int){
          }
        }
        """
        expect = r"""No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 19113))

    def test_methoddecl_4(self):
        input = r"""
        Class Program {
          Val g: Int = 2;
          foo() {
          }
        }
        Class Subprogram : Program {
          foo(a: Int){
          }
          Var foo: Int;
        }
        """
        expect = r"""No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 19114))

    def test_methoddecl_5(self):
        input = r"""
        Class Program {
          main(){
          }
          foo(a: Int){
          }
        }
        Class Subprogram : Program {
          food(a: Int; a: String){
          }
        }
        """
        expect = r"""Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 19115))

    def test_methoddecl_6(self):
        input = r"""
        Class Program {
          main() {
          }
          foo(a: Int) {
          }
        }
        Class Subprogram {
          foo(a: Int){
          }
          food(a, a: Boolean) {
          }
        }
        """
        expect = r"""Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 19116))

    def test_cardecl_0(self):
        input = r"""
        Class Program {
          main() {
            Var a, a: Int;
          }
        }
        
        """
        expect = r"""Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 19117))

    def test_cardecl_1(self):
        input = r"""
        Class Program {
          main() {
            Var a, b: Int;
            Val a: String = "Hourai - South Wind, Clear Sky";
          }
        }
        
        """
        expect = r"""Redeclared Constant: a"""
        self.assertTrue(TestChecker.test(input, expect, 19118))

    def test_cardecl_2(self):
        input = r"""
        Class Program {
          Var a: String = "Koikaze";
          main() {
            Val a: String = "Sutaaraito taifuun";
          }
          foo(a: String) {
            Var a: Int;
          }
        }
        """
        expect = r"""Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 19119))

    def test_cardecl_3(self):
        input = r"""
        Class Program {
          Var d: String = "Koikaze";
          main() {
            Val a: String = "Sutaaraito taifuun";
            Var c, a: String = "Kougeki", "Shuuto za Muun";
          }
        }
        """
        expect = r"""Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 19120))

    def test_ifstmt_0(self):
        input = r"""
        Class Program {
          main() {
            If(5) {
              Val a: Int = 5;
            }
          }
        }
        """
        expect = r"""Type Mismatch In Statement: If(IntLit(5),Block([ConstDecl(Id(a),IntType,IntLit(5))]))"""
        self.assertTrue(TestChecker.test(input, expect, 19121))

    def test_ifstmt_1(self):
        input = r"""
        Class Program {
          main() {
            Var a: Int = 4;
            If(True) {
              Val a: Int = 5;
              Var a: Float = 1.0;
            }
          }
        }
        """
        expect = r"""Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 19122))

    def test_ifstmt_2(self):
        input = r"""
        Class Program {
          Var a: Boolean = True;
          main() {
            Var a: Boolean = True;
          }
          foo(a: Int) {
            If(False) {
              Val a: Boolean = True;
              Var a: Boolean = False;
            }
          }
        }
        """
        expect = r"""Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 19123))

    def test_ifstmt_3(self):
        input = r"""
        Class Program {
          Var a: Boolean = True;
          main() {
            Var a: Boolean = True;
          }
          foo(a: Int) {
            If(False) {
              Var a: Int;
              If(False) {
                Var a: Float = 0.0e-0;
                Val a: String = "No";
              }
            }
          }
        }
        """
        expect = r"""Redeclared Constant: a"""
        self.assertTrue(TestChecker.test(input, expect, 19124))

    def test_breakstmt_0(self):
        input = r"""
        Class Program {
          main() {
            Break;
          }
        }
        """
        expect = r"""Break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 19125))

    def test_continuestmt_0(self):
        input = r"""
        Class Program {
          main() {
            If(True){
              Continue;
            }
          }
        }
        """
        expect = r"""Continue Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 19126))

    def test_ifstmt_4(self):
        input = r"""
        Class Program {
          foo(a: Int) {
            If(False) {
              Var a: Int;
            }
            Else {
              Var a: Int;
              Var b, b: String;
            }
          }
        }
        """
        expect = r"""Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input, expect, 19127))

    def test_forstmt_0(self):
        input = r"""
        Class Program {
          main() {
            Var a: Int;
            Foreach (i In 1 .. 5) {
              Val i: Int = 6;
            }
          }
        }
        """
        expect = r"""Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input, expect, 19128))

    def test_forstmt_1(self):
        input = r"""
        Class Program {
          main() {
            Foreach (i In 1 .. 5) {
              Break;
              If (True) {
                Break;
              }
              Val a: Int;
            }
          }
        }
        """
        expect = r"""Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input, expect, 19129))

    def test_forstmt_2(self):
        input = r"""
        Class Program {
          main() {
            Foreach (i In 1 .. 5) {
              Break;
              Foreach (i In 1 .. 100 By 20) {
                Continue;
                If (False) {
                  Val i: Float = 213_321.3e-4;
                }
                Var i: Int;
              }
            }
          }
        }
        """
        expect = r"""Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input, expect, 19130))

    def test_array_0(self):
        input = r"""
        Class Program {
          main() {
            Var arr: Array[Int, 5];
            Var arr: Array[Float, 4];
          }
        }
        """
        expect = r"""Redeclared Variable: arr"""
        self.assertTrue(TestChecker.test(input, expect, 19131))

    def test_array_1(self):
        input = r"""
        Class Program {
          main() {
            Var arr: Array[Int, 5] = Array(1, 2, 3, 4, True);
          }
        }
        """
        expect = r"""Illegal Array Literal: [IntLit(1),IntLit(2),IntLit(3),IntLit(4),BooleanLit(True)]"""
        self.assertTrue(TestChecker.test(input, expect, 19132))

    def test_ifstmt_5(self):
        input = r"""
        Class Program {
          foo(a: Int) {
            If(5) {}
          }
        }
        """
        expect = r"""Type Mismatch In Statement: If(IntLit(5),Block([]))"""
        self.assertTrue(TestChecker.test(input, expect, 19133))

    def test_obj_0(self):
        input = r"""
        Class Program {
          main() {
          }
          Var obj: Animal;
        }
        """
        expect = r"""Undeclared Class: Animal"""
        self.assertTrue(TestChecker.test(input, expect, 19134))

    def test_obj_1(self): #sus
        input = r"""
        Class Shape {
        }
        Class Program {
          main() {
          }
          Val obj: Shape = Null;
          Val obj2: Shape;
        }
        """
        expect = r"""Illegal Constant Expression: None"""
        self.assertTrue(TestChecker.test(input, expect, 19135))

    def test_callstmt_0(self):
        input = r"""
        Class Shape {
          foo() {
          }
        }
        Class Program {
          main() {
            Var a: Shape;
            a.foo();
            a.food();
          }
        }
        """
        expect = r"""Undeclared Method: food"""
        self.assertTrue(TestChecker.test(input, expect, 19136))

    def test_callstmt_1(self):
        input = r"""
        Class Shape {
          $soo() {
          }
        }
        Class Program {
          main() {
            Var a: Shape;
            Shape::$soo();
            Shape::$shoo();
          }
        }
        """
        expect = r"""Undeclared Method: $shoo"""
        self.assertTrue(TestChecker.test(input, expect, 19137))

    def test_callstmt_2(self):
        input = r"""
        Class Shape {
          $soo() {
          }
        }
        Class Program {
          main() {
            Var a: Shape;
            a::$soo();
          }
        }
        """
        expect = r"""Illegal Member Access: Call(Id(a),Id($soo),[])"""
        self.assertTrue(TestChecker.test(input, expect, 19138))

    def test_callstmt_3(self):
        input = r"""
        Class Shape {
          foo() {
          }
        }
        Class Program {
          main() {
            Var a: Shape;
            Shape.foo();
          }
        }
        """
        expect = r"""Illegal Member Access: Call(Id(Shape),Id(foo),[])"""
        self.assertTrue(TestChecker.test(input, expect, 19139))

    def test_constructor_0(self):
        input = r"""
        Class Shape {
          foo() {
          }
        }
        Class Program {
          main() {
            Var a: Shape = New Shape();
            Val b: Shape = New Shape(1);
          }
        }
        """
        expect = r"""Type Mismatch In Expression: NewExpr(Id(Shape),[IntLit(1)])"""
        self.assertTrue(TestChecker.test(input, expect, 19140))

    # def test_constructor_1(self):
    #     input = r"""
    #     Class Parent {
    #     }
    #     Class Child : Parent {
    #     }
    #     Class Shape {
    #       foo() {
    #       }
    #       Constructor (a: Float; b: Parent) {
    #       }
    #     }
    #     Class Program {
    #       main() {
    #         Var a: Shape = New Shape(4, New Child());
    #         Val b: Shape = New Shape();
    #       }
    #     }
    #     """
    #     expect = r"""Type Mismatch In Expression: NewExpr(Id(Shape),[])"""
    #     # Type Mismatch In Expression: NewExpr(Id(Shape),[IntLit(4),NewExpr(Id(Child),[])])
    #     self.assertTrue(TestChecker.test(input, expect, 19141))

    def test_constructor_2(self):
        input = r"""
        Class Shape {
          Constructor () {
          }
          Destructor () {
          }
          Constructor (a, b: Float) {
          }
        }
        Class Program {
          main() {
          }
        }
        """
        expect = r"""Redeclared Method: Constructor"""
        self.assertTrue(TestChecker.test(input, expect, 19142))

    def test_array_2(self):
        input = r"""
        Class Program {
          main() {
            Val arr: Array[Int, 5] = Array(1,2,3,4,5);
            Val a: Int = arr[0]; ## ok here because arr is const ##
            Val b: Int = arr[False];
          }
        }
        """
        expect = r"""Type Mismatch In Expression: ArrayCell(Id(arr),[BooleanLit(False)])"""
        # Illegal Constant Expression: ArrayCell(Id(arr),[IntLit(0)])
        self.assertTrue(TestChecker.test(input, expect, 19143))

    def test_array_3(self):
        input = r"""
        Class Program {
          main() {
            Var arr: Array[Int, 5];
            Val a: Int = arr[0]; ## not ok here because arr is var ##
          }
        }
        """
        expect = r"""Illegal Constant Expression: ArrayCell(Id(arr),[IntLit(0)])"""
        self.assertTrue(TestChecker.test(input, expect, 19144))

    def test_array_4(self):
        input = r"""
        Class Program {
          main() {
            Var arr: Array[Int, 5];
            Val v: String = "Reifu [Musou Fuuin]";
            Val a: Int = v[0];
          }
        }
        """
        expect = r"""Type Mismatch In Expression: ArrayCell(Id(v),[IntLit(0)])"""
        self.assertTrue(TestChecker.test(input, expect, 19145))

    def test_self_0(self):
        input = r"""
        Class Program {
          foo() {
          }
          main() {
            Self.foo();
            Self.food();
          }
        }
        """
        expect = r"""Undeclared Method: food"""
        self.assertTrue(TestChecker.test(input, expect, 19146))

    def test_self_1(self):
        input = r"""
        Class Program {
          foo(a: Float) {
          }
          food(a: String) {
          }
          Val a: Int = 2;
          main() {
            Self.foo(Self.a);
            Self.food(Self.a);
          }
        }
        """
        expect = r"""Type Mismatch In Statement: Call(Self(),Id(food),[FieldAccess(Self(),Id(a))])"""
        self.assertTrue(TestChecker.test(input, expect, 19147))

    def test_constdecl_0(self):
        input = r"""
        Class Bullet {
          Constructor(a: Int) {
          }
        }
        Class Program {
          main() {
            Var aV: Bullet = New Bullet(1);
            Val aC: Bullet = New Bullet(2);
            Val b1: Bullet = aC;
            Val b2: Bullet = aV;
          }
        }
        """
        expect = r"""Illegal Constant Expression: Id(aV)"""
        self.assertTrue(TestChecker.test(input, expect, 19148))

    def test_constdecl_1(self):
        input = r"""
        Class Program {
          main() {
            Val a: Int = 1_1.e-3;
          }
        }
        """
        expect = r"""Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(0.011))"""
        self.assertTrue(TestChecker.test(input, expect, 19149))

    
    def test_self_2(self):
        input = r"""
        Class Program {
          foo(a: Float) {
          }
          $soo(){}
          Val a: Int = 2;
          Var $a: Int;
          main() {
            Program::$soo();
            Self.foo(Self.a);
            Program.foo(21);
          }
        }
        """
        expect = r"""Illegal Member Access: Call(Id(Program),Id(foo),[IntLit(21)])"""
        self.assertTrue(TestChecker.test(input, expect, 19150))

    def test_assign_0(self):
        input = r"""
        Class Program {
          main() {
            Var b: Float;
            b = 2;
            b = 41.2;
            b = True;
          }
        }
        """
        expect = r"""Type Mismatch In Statement: AssignStmt(Id(b),BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 19151))

    def test_assign_1(self):
        input = r"""
        Class Program {
          main() {
            Var b: String;
            b = "Mahou '"Fainaru Supaaku'"";
            b = Array("It\'s", "over", "9000");
          }
        }
        """
        expect = r"""Type Mismatch In Statement: AssignStmt(Id(b),[StringLit(It\'s),StringLit(over),StringLit(9000)])"""
        self.assertTrue(TestChecker.test(input, expect, 19152))

    def test_assign_2(self):
        input = r"""
        Class Program {
          main() {
            Var arr: Array[Int, 2] = Array(1,2);
            Var b: Float;
            b = arr[1];
            arr[1] = b;
          }
        }
        """
        expect = r"""Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr),[IntLit(1)]),Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 19153))

    def test_assign_3(self):
        input = r"""
        Class Program {
          main() {
            Var arr: Array[Float, 3];
            arr = Array(1, 2, 3);
            arr = Array(4, 5.6, 0.00001e-3);
            arr = Array(1,1,1,1);
          }
        }
        """
        expect = r"""Illegal Array Literal: [IntLit(4),FloatLit(5.6),FloatLit(1e-08)]"""
        self.assertTrue(TestChecker.test(input, expect, 19154))

    # def test_assign_4(self):
    #     input = r"""
    #     Class P{}
    #     Class C : P{}
    #     Class Program {
    #       main() {
    #         Var arr: Array[Int, 3];
    #         arr = Array(New C(), New C(), New C());
    #         arr[2] = New C();
    #         arr[0] = True;
    #       }
    #     }
    #     """
    #     expect = r"""Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr),[IntLit(0)]),BooleanLit(True))"""
    #     self.assertTrue(TestChecker.test(input, expect, 19155))

    def test_assign_5(self):
        input = r"""
        Class Program {
          main() {
            Val const: Int = 2;
            const = 3;
          }
        }
        """
        expect = r"""Cannot Assign To Constant: AssignStmt(Id(const),IntLit(3))"""
        self.assertTrue(TestChecker.test(input, expect, 19156))

    def test_assign_6(self):
        input = r"""
        Class Program {
          main() {
            Val arr: Array[Int, 2] = Array(6,9);
            arr[1] = 3;
          }
        }
        """
        expect = r"""Cannot Assign To Constant: AssignStmt(ArrayCell(Id(arr),[IntLit(1)]),IntLit(3))"""
        self.assertTrue(TestChecker.test(input, expect, 19157))

    def test_assign_7(self):
        input = r"""
        Class Program {
          main() {
            Val arr: Array[Int, 2] = Array(6,9);
            arr = Array(1,2);
          }
        }
        """
        expect = r"""Cannot Assign To Constant: AssignStmt(Id(arr),[IntLit(1),IntLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 19158))

    def test_assign_8(self):
        input = r"""
        Class Data {
          Var iV: Int;
          Var $sV: Int;
          Val $sC: Int = 4;
          Val iC: Int = Data::$sC;
        }
        Class Program {
          Var d1: Data;
          Val d2: Data = New Data();
          main() {
            Self.d1 = New Data();
            Self.d2 = New Data();
          }
        }
        """
        expect = r"""Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(d2)),NewExpr(Id(Data),[]))"""
        self.assertTrue(TestChecker.test(input, expect, 19159))

    def test_assign_9(self):
        input = r"""
        Class Data {
          Var iV: Int;
          Var $sV: Int;
          Val $sC: Int = 4;
          Val iC: Int = Data::$sC;
        }
        Class Program {
          Var d1: Data;
          Val d2: Data = New Data();
          main() {
            Data::$sV = 4;
            Data::$sC = Data::$sV;
          }
        }
        """
        expect = r"""Cannot Assign To Constant: AssignStmt(FieldAccess(Id(Data),Id($sC)),FieldAccess(Id(Data),Id($sV)))"""
        self.assertTrue(TestChecker.test(input, expect, 19160))

    def test_assign_10(self):
        input = r"""
        Class SubData{
          Var iV: Int;
          Var $sV: Int;
          Val $sC: Int = 4;
          Val iC: Int = SubData::$sC;
          Val d0: SubData = New SubData();
          foo() {
            Self.iV = Self.d0.iC;
            Self.d0.iC = Self.iV;
          }
        }
        Class Program {
          main(){}
        }
        """
        expect = r"""Cannot Assign To Constant: AssignStmt(FieldAccess(FieldAccess(Self(),Id(d0)),Id(iC)),FieldAccess(Self(),Id(iV)))"""
        self.assertTrue(TestChecker.test(input, expect, 19161))

    def test_constructor_3(self):
        input = r"""
        Class Program {
          main() {
          }
          Constructor() {
            Return;
          }
        }
        Class B {
          Constructor() {
            Return Self;
          }
        }
        """
        expect = r"""Type Mismatch In Statement: Return(Self())"""
        self.assertTrue(TestChecker.test(input, expect, 19162))

    def test_destructor_0(self):
        input = r"""
        Class Program {
          main() {
          }
          Constructor() {
            Return;
          }
        }
        Class B {
          Constructor() {
            Return Self;
          }
        }
        """
        expect = r"""Type Mismatch In Statement: Return(Self())"""
        self.assertTrue(TestChecker.test(input, expect, 19163))

    def test_binary_0(self):
        input = r"""
        Class Program {
          main() {
          }
          Var a: Int = 2 + 2;
          Var b: Float = 3 + 4;
          Var c: String = "ZA" +. "WARUDO";
          Var d: Boolean = (2 >= 2) && True;
          Var e: Int = 2.2 + 3;
        }
        """
        expect = r"""Type Mismatch In Statement: VarDecl(Id(e),IntType,BinaryOp(+,FloatLit(2.2),IntLit(3)))"""
        self.assertTrue(TestChecker.test(input, expect, 19164))

    def test_binaryIF_0(self):
        input = r"""
        Class Program {
          main() {
          }
          Var a: Int = 2 + 2;
          Var b: Float = 69 + 420;
          Var c: Float = 21 + 1.4;
          Var d: Float = 5.4 + (19 + 78);
          Var e: Boolean = 2 >= 2;
          Var f: Boolean = 2.1 <= 2.2;
          Var g: Boolean = 2 > 2.6;
          Var h: Boolean = (24.5 < 2) && False;
          Var eatThis: Boolean = 24.5 < 4 && False;
        }
        """
        expect = r"""Type Mismatch In Expression: BinaryOp(&&,IntLit(4),BooleanLit(False))"""
        self.assertTrue(TestChecker.test(input, expect, 19165))

    def test_binaryIB_0(self):
        input = r"""
        Class Program {
          main() {
          }
          Var e: Boolean = 2 == 2;
          Var f: Boolean = 2 != 3;
          Var g: Boolean = True != False;
          Var h: Boolean = !True && ("TOKI WO" ==. "TOMARE");
          Var eatThis: Boolean = 2.3 == 2.3;
        }
        """
        expect = r"""Type Mismatch In Expression: BinaryOp(==,FloatLit(2.3),FloatLit(2.3))"""
        self.assertTrue(TestChecker.test(input, expect, 19166))

    def test_binaryI_0(self):
        input = r"""
        Class Program {
          main() {
          }
          Var e: Int = 4 % 5;
          Var f: Int = (12 + 4) % (2 * 4);
          Var g: Float = ((2 - 5) / 6) % (-2 * (15 - 6 * 4));
          Var h: Float = -4 % -4------4 + 5 * 20;
          Var eatThis: Int = 4.3 % 2;
        }
        """
        expect = r"""Type Mismatch In Expression: BinaryOp(%,FloatLit(4.3),IntLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 19167))

    def test_binaryI_1(self):
        input = r"""
        Class Program {
          main() {
          }
          Var e: Float = "WTF" % (True && !False);
        }
        """
        expect = r"""Type Mismatch In Expression: BinaryOp(%,StringLit(WTF),BinaryOp(&&,BooleanLit(True),UnaryOp(!,BooleanLit(False))))"""
        self.assertTrue(TestChecker.test(input, expect, 19168))

    def test_binaryIF_1(self):
        input = r"""
        Class Program {
          main() {
          }
          Var eatThis: Int = 4.2 - (4 % 5);
        }
        """
        expect = r"""Type Mismatch In Statement: VarDecl(Id(eatThis),IntType,BinaryOp(-,FloatLit(4.2),BinaryOp(%,IntLit(4),IntLit(5))))"""
        self.assertTrue(TestChecker.test(input, expect, 19169))

    def test_binaryIF_2(self):
        input = r"""
        Class Program {
          main() {
          }
          Var eatThis: Int = 3 > 2;
        }
        """
        expect = r"""Type Mismatch In Statement: VarDecl(Id(eatThis),IntType,BinaryOp(>,IntLit(3),IntLit(2)))"""
        self.assertTrue(TestChecker.test(input, expect, 19170))

    def test_constdecl_2(self):
        input = r"""
        Class Program {
          main() {
          }
          Var $a: Float = 420;
          Val b: Int = 2;
          Val c: Float = 3;
          Val d: Float = Self.b + Self.c;
          Val e: Boolean = Self.b > 1;
          Val f: Float = Self.c - Self.d * 2;
          Val eatThis: Int = 69 * Program::$a;
        }
        """
        expect = r"""Illegal Constant Expression: BinaryOp(*,IntLit(69),FieldAccess(Id(Program),Id($a)))"""
        # Type Mismatch In Constant Declaration: ConstDecl(Id(eatThis),IntType,BinaryOp(*,IntLit(69),FieldAccess(Id(Program),Id($a))))
        self.assertTrue(TestChecker.test(input, expect, 19171))

    def test_constdecl_3(self):
        input = r"""
        Class Program {
          main() {
          }
          Var $a: Int = 420;
          Val b: Int = 2;
          Val c: Float = 3;
          Val d: Float = Self.b + Self.c - 2 * (Self.b % Program::$a);
        }
        """
        expect = r"""Illegal Constant Expression: BinaryOp(-,BinaryOp(+,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(c))),BinaryOp(*,IntLit(2),BinaryOp(%,FieldAccess(Self(),Id(b)),FieldAccess(Id(Program),Id($a)))))"""
        self.assertTrue(TestChecker.test(input, expect, 19172))

    def test_binaryS_0(self):
        input = r"""
        Class Program {
          main() {
          }
          Var $a: String = "Hey guys, did you know that in terms of male human and female Pokemon breeding, Vaporeon is the most compatible Pokemon for humans?";
          Val b: String = "According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyways. Because bees don\'t care what humans think is impossible.";
          Var c: String = Program::$a +. (Self.b +. "All warfare is based.");
          Var eatThis: Boolean = Program::$a ==. ("Not all is bad" ==. "Not everything is good");
        }
        """
        expect = r"""Type Mismatch In Expression: BinaryOp(==.,FieldAccess(Id(Program),Id($a)),BinaryOp(==.,StringLit(Not all is bad),StringLit(Not everything is good)))"""
        self.assertTrue(TestChecker.test(input, expect, 19173))

    def test_binaryB_0(self):
        input = r"""
        Class Program {
          main() {
          }
          Var $a: Boolean = True || True;
          Val b: Boolean = 2 > 2;
          Val c: Boolean = Self.b == Self.b;
          Var eatThis: Boolean = 1 + 2.4;
        }
        """
        expect = r"""Type Mismatch In Statement: VarDecl(Id(eatThis),BoolType,BinaryOp(+,IntLit(1),FloatLit(2.4)))"""
        self.assertTrue(TestChecker.test(input, expect, 19174))

    def test_binaryB_1(self):
        input = r"""
        Class Program {
          main() {
          }
          Var $a: Boolean = True && True;
          Val b: Boolean = 2 >= 2;
          Val c: Boolean = (Self.b == Self.b) != (2 != 12);
          Val eatThis: Boolean = "Wut" +. "The Hell";
        }
        """
        expect = r"""Type Mismatch In Constant Declaration: ConstDecl(Id(eatThis),BoolType,BinaryOp(+.,StringLit(Wut),StringLit(The Hell)))"""
        self.assertTrue(TestChecker.test(input, expect, 19175))

    def test_unaryIF_0(self):
        input = r"""
        Class Program {
          main() {
          }
          Var $a: Float = -1;
          foo() {
            Program::$a = -1.2;
          }
          Var b: Int = -12.4;
        }
        """
        expect = r"""Type Mismatch In Statement: VarDecl(Id(b),IntType,UnaryOp(-,FloatLit(12.4)))"""
        self.assertTrue(TestChecker.test(input, expect, 19176))

    def test_unaryB_0(self):
        input = r"""
        Class Program {
          main() {
          }
          Var $a: Boolean = !False && !True;
          Var b: Boolean = !("String" ==. "CharArray") != !("Reimu" ==. "Marisa");
          Var c: Boolean = -1;
        }
        """
        expect = r"""Type Mismatch In Statement: VarDecl(Id(c),BoolType,UnaryOp(-,IntLit(1)))"""
        self.assertTrue(TestChecker.test(input, expect, 19177))

    def test_extra_0(self):
        input = r"""
        Class Program {
          main() {
          }
        }
        Class A : B {
          foo() {
            a = 1;
          }
        }
        """
        expect = r"""Undeclared Class: B"""
        self.assertTrue(TestChecker.test(input, expect, 19180))

    def test_extra_1(self):
        input = r"""
        Class Program {
          main() {
            If (True) {
              Var a: Int;
              Foreach (a In 1 .. 100 By 2) {
                If (True) {
                  Var a: Int;
                }
                If (False) {
                  Var a: Int;
                }
              }
              Foreach (a In 1 .. 2) {
              }
              If (False) {
                Val a: Int = 2;
              }
            }
            B::$somethingIdk();
          }
        }
        """
        expect = r"""Undeclared Class: B"""
        self.assertTrue(TestChecker.test(input, expect, 19181))

    # def test_extra_2(self):
    #     input = r"""
    #     Class Program {
    #       main() {
    #         Foreach (i In 1 .. 100) {
    #           Break;
    #         }
    #         Foreach (i In 1 .. 100) {
    #           Break;
    #           If (False) {
    #             Break;
    #           }
    #           Foreach (i In 1 .. 100) {
    #             Break;
    #             If (True) {
    #               Break;
    #             }
    #             Break;
    #           }
    #         }
    #         Val arr: Array[Array[Int, 2], 2] = Array(Array(1,2), "Huh");
    #       }
    #     }
    #     """
    #     expect = r"""Illegal Array Literal: [[IntLit(1),IntLit(2)],StringLit(Huh)]"""
    #     self.assertTrue(TestChecker.test(input, expect, 19182))

    def test_extra_3(self):
        input = r"""
        Class Program {
          main() {
          }
        }
        Class P {
          Var a: Int;
          Var $a: Int;
        }
        Class C : P{
          Var b: Int;
          Var $b: Int;
          foo() {
            Var c: Int = Self.b;
            Var c2: Int = P::$a;
            Var c3: Int = P::$b;
          }
        }
        """
        expect = r"""Undeclared Attribute: $b"""
        self.assertTrue(TestChecker.test(input, expect, 19183))

    def test_extra_4(self):
        input = r"""
        Class Program {
          main() {
          }
        }
        Class P {
          Var a: Int;
          Var $a: Int;
          $food(i: Int; s:String) {
          }
        }
        Class C : P {
          foo(i: String){
          }
          fuuuu(b: Boolean) {
          }
          Var a: String;
          Var $a: String;
          sub() {
            Self.foo(Self.a);
            P::$food(P::$a, C::$a);
            Self.fuuuu(Self.a);
          }
        }
        """
        expect = r"""Type Mismatch In Statement: Call(Self(),Id(fuuuu),[FieldAccess(Self(),Id(a))])"""
        self.assertTrue(TestChecker.test(input, expect, 19184))

    def test_extra_5(self):
        input = r"""
        Class Program {
          main() {
          }
          Var a: Int = 2;
          Val b: Int = Self.a;
        }
        """
        expect = r"""Illegal Constant Expression: FieldAccess(Self(),Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 19185))

    def test_extra_6(self): # !!! important
        input = r"""
        Class P {
          Constructor() {
          }
          Var a: Int;
        }
        Class C : P {
          a() {
          }
        }
        Class Program {
          main() {
            Break;
          }
        }
        """
        expect = r"""Break Not In Loop""" #no error here, prolly
        self.assertTrue(TestChecker.test(input, expect, 19186))

    # def test_extra_7(self):
    #     input = r"""
    #     Class Program{
    #       Val $someStatic: Int = 10;
    #       main() {
    #         Var Program: Float = 1.0;
    #         Var x: Int = Program::$someStatic;
    #         x = x.something();
    #       }
    #     }
    #     """
    #     expect = r"""Type Mismatch In Expression: CallExpr(Id(x),Id(something),[])"""
    #     # Illegal Member Access: CallExpr(Id(x),Id(something),[])
    #     self.assertTrue(TestChecker.test(input, expect, 19187))

    def test_extra_8(self):
        input = r"""
        Class Program{
          main() {
            Var x: Int = Program;
          }
        }
        """
        expect = r"""Undeclared Identifier: Program"""
        self.assertTrue(TestChecker.test(input, expect, 19188))

    def test_extra_9(self):
        input = r"""
        Class Program{
          main() {
            Var x: Int = a.foo;
          }
        }
        """
        expect = r"""Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 19189))

    # def test_extra_10(self):
    #     input = r"""
    #     Class Program{
    #       main() {
    #         Val v: Array[Array[Int, 2], 2] = Array(Array(2,3), Array(4,5));
    #         Val v2: Int = v[1][0];
    #         Var a: Array[Array[Int, 2], 2];
    #         a[1] = a[0];
    #         Var x: Int;
    #         x = a[1][0];
    #         x = a[1];
    #       }
    #     }
    #     """
    #     expect = r"""Type Mismatch In Statement: AssignStmt(Id(x),ArrayCell(Id(a),[IntLit(1)]))"""
    #     # Illegal Constant Expression: ArrayCell(Id(v),[IntLit(1),IntLit(0)])
    #     self.assertTrue(TestChecker.test(input, expect, 19190))

    def test_extra_11(self):
        input = r"""
        Class Program{
          main() {
            Var a: Array[Array[Int, 10], 1];
            Var b: Array[Float, 10];
            Var c: Float;
            b = a[0];
            c = a[0][9];
            c = a[1];
          }
        }
        """
        expect = r"""Type Mismatch In Statement: AssignStmt(Id(c),ArrayCell(Id(a),[IntLit(1)]))"""
        self.assertTrue(TestChecker.test(input, expect, 19191))

    def test_lunatic_0(self):
        input = r"""
        Class Program{
          main() {
            Var x: Int = a;
          }
        }
        """
        expect = r"""Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 19700))

    def test_lunatic_1(self):
        input = r"""
        Class a{}
        Class Program{
          main() {
            Var x: Int = a;
          }
        }
        """
        expect = r"""Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 19701))

    def test_lunatic_2(self):
        input = r"""
        Class Program{
          main() {
            Var x: Int = A.b;
          }
        }
        """
        expect = r"""Undeclared Identifier: A"""
        self.assertTrue(TestChecker.test(input, expect, 19702))

    def test_lunatic_3(self):
        input = r"""
        Class Program{
          main() {
            Var x: Int = A::$a;
          }
        }
        """
        expect = r"""Undeclared Class: A"""
        self.assertTrue(TestChecker.test(input, expect, 19703))

    # def test_lunatic_4(self):
    #     input = r"""
    #     Class A {
    #       Var b: Int;
    #       Var $b: Int;
    #     }
    #     Class Program{
    #       main() {
    #         Var A: String;
    #         Var x: Int = A.b;
    #       }
    #     }
    #     """
    #     expect = r"""Type Mismatch In Expression: FieldAccess(Id(A),Id(b))"""
    #     self.assertTrue(TestChecker.test(input, expect, 19704))

    # def test_lunatic_5(self):
    #     input = r"""
    #     Class Program{
    #       main() {
    #         Var A: Float;
    #         Var x: Int = A::$b;
    #       }
    #     }
    #     """
    #     expect = r"""Type Mismatch In Expression: FieldAccess(Id(A),Id($b))"""
    #     self.assertTrue(TestChecker.test(input, expect, 19705))

    def test_lunatic_6(self):
        input = r"""
        Class A {
          Var b: Int;
          Var $b: Int;
        }
        Class Program {
          main() {
            Var x: Int = A.b;
          }
        }
        """
        expect = r"""Illegal Member Access: FieldAccess(Id(A),Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 19706))

    def test_lunatic_7(self):
        input = r"""
        Class A {
          Var b: Int;
          Var $b: Int;
        }
        Class Program {
          main() {
            Var b: A;
            Var x: Int = b::$b;
          }
        }
        """
        expect = r"""Illegal Member Access: FieldAccess(Id(b),Id($b))"""
        self.assertTrue(TestChecker.test(input, expect, 19707))

    def test_lunatic_8(self):
        input = r"""
        Class Program {
          foo(){
            Return 2;
          }
          Var goo: Int = 2;
          main() {
            Var b: Int = Program::$goo();
          }
        }
        """
        expect = r"""Undeclared Method: $goo"""
        self.assertTrue(TestChecker.test(input, expect, 19708))

    def test_lunatic_9(self): #sus
        input = r"""
        Class A {
          Var $a: Int = 1;
          Var a: Int = 2;
          Constructor(a: Int) {
          }
        }
        Class Program {
          Var a: Int = 3;
          main() {
            Var A: A = New A(Self.a);
            Self.a = A.a;
            Self.a = A::$A;
          }
        }
        """
        expect = r"""Undeclared Attribute: $A"""
        self.assertTrue(TestChecker.test(input, expect, 19709))

    def test_lunatic_10(self): #sus
        input = r"""
        Class Program {
          main() {
            Var a: Boolean = 3 == 3;
            Var b: Int = 2;
            Var c: Boolean = !False;
            If (a) {
            }
            Elseif (b) {
            }
            Elseif (c) {
            }
          }
        }
        """
        expect = r"""Type Mismatch In Statement: If(Id(b),Block([]),If(Id(c),Block([])))""" #yeah im not throwing from if(a), fuck you
        self.assertTrue(TestChecker.test(input, expect, 19710))

    def test_lunatic_11(self):
        input = r"""
        Class A {
          Val i: Int = 2;
        }
        Class B : A {
          Var i: Int;
        }
        Class Program {
          main() {
            A = 2;
          }
        }
        """
        expect = r"""Undeclared Identifier: A"""
        self.assertTrue(TestChecker.test(input, expect, 19711))

    def test_lunatic_12(self):
        input = r"""
        Class E{}
        Class Program {
          main() {
            Var x: Int = E.v;
          }
        }
        """
        expect = r"""Illegal Member Access: FieldAccess(Id(E),Id(v))"""
        self.assertTrue(TestChecker.test(input, expect, 19712))

    def test_lunatic_13(self):
        input = r"""
        Class Program {
          main() {
            Var x: Int = E.v;
          }
        }
        """
        expect = r"""Undeclared Identifier: E"""
        self.assertTrue(TestChecker.test(input, expect, 19713))

    # def test_lunatic_14(self):
    #     input = r"""
    #     Class Program{
	#         main(){
	# 	        Var E: Int;
	# 	        Var v2: Int = E::$v;
	#         }
    #     }
    #     """
    #     expect = r"""Type Mismatch In Expression: FieldAccess(Id(E),Id($v))"""
    #     self.assertTrue(TestChecker.test(input, expect, 19714))

    def test_lunatic_15(self):
        input = r"""
        Class Program{
        	main(){
		        Var v2: Int = E::$v;
	        }
        }
        """
        expect = r"""Undeclared Class: E"""
        self.assertTrue(TestChecker.test(input, expect, 19715))

    def test_lunatic_16(self):
        input = r"""
        Class Program{
          Var a: Int = 4;
          a() {
            Return 4;
          }
        	main(){
            Break;
	        }
        }
        """
        expect = r"""Break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 19716))

    def test_lunatic_17(self):
        input = r"""
        Class Parent{
          Var a, $a: Int;
          b(){
          }
          $b(){
          }
        }
        Class Child : Parent{
          Var a, $a: Int;
          b(){
          }
          $b(){
          }
        }
        Class Program{
          Var a: Int = 4;
          a() {
            Return 4;
          }
        	main(){
            Break;
	        }
        }
        """
        expect = r"""Break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 19717))

    # def test_lunatic_18(self):
    #     input = r"""
    #     Class Parent{}
    #     Class Child:Parent{}
    #     Class Program{
    #       main(){
    #         Var a: Child = New Child();
    #         Var b: Parent = New Child();
    #         Var c: Parent = a;
    #         c = a;
    #         c = New Child();
    #         Var d: Child;
    #         Val e: Child = Null;
    #         Val f: Parent;
    #       }
    #     }
    #     """
    #     expect = r"""Illegal Constant Expression: None"""
    #     # Type Mismatch In Statement: VarDecl(Id(b),ClassType(Id(Parent)),NewExpr(Id(Child),[]))
    #     self.assertTrue(TestChecker.test(input, expect, 19718))

    def test_lunatic_19(self):
        input = r"""
        Class Parent{
          Val $c: Int = 1;
          Var $v: Int = 1;
        }
        Class Child:Parent{}
        Class Program{
          main(){
            Val a: Int = Parent::$c;
            Val b: Int = Parent::$v;
          }
        }
        """
        expect = r"""Illegal Constant Expression: FieldAccess(Id(Parent),Id($v))"""
        self.assertTrue(TestChecker.test(input, expect, 19719))

    def test_lunatic_20(self):
        input = r"""
        Class Program{
          main(){
            Val a: Array[Array[Int, 2], 2] = Array(Array(True, ("You" ==. "TheGuySheToldYouNotToWorryAbout")), Array(23.3 > 32, !False));
          }
        }
        """
        expect = r"""Type Mismatch In Constant Declaration: ConstDecl(Id(a),ArrayType(2,ArrayType(2,IntType)),[[BooleanLit(True),BinaryOp(==.,StringLit(You),StringLit(TheGuySheToldYouNotToWorryAbout))],[BinaryOp(>,FloatLit(23.3),IntLit(32)),UnaryOp(!,BooleanLit(False))]])"""
        self.assertTrue(TestChecker.test(input, expect, 19720))

    # def test_loggers_0(self):
    #     input = r"""
    #     Class Program {
    #       main() {
    #       }
    #       foo(a, b: Int){
    #       }
    #     }
    #     """
    #     expect = r"""Undeclared Class: B"""
    #     self.assertTrue(TestChecker.test(input, expect, 99000))

    # def test_loggers_1(self):
    #     input = r"""
    #     Class Animal {}
    #     Class Program {
    #       main() {
    #       }
    #       foo(a, b: Int; c: Animal){
    #       }
    #     }
    #     """
    #     expect = r"""Whatever"""
    #     self.assertTrue(TestChecker.test(input, expect, 99001))

    # def test_loggers_2(self):
    #     input = r"""
    #     Class Program {
    #       main() {
    #       }
    #       foo(){
    #         Var a: String = "Hail 2 U";
    #         Return 2;
    #         Return;
    #         Return 3.2;
    #         Return a;
    #         Return Self;
    #         Return Array(Array(3.5,4e2), Array(6.2, 0e4));
    #       }
    #     }
    #     """
    #     expect = r"""Whatever"""
    #     self.assertTrue(TestChecker.test(input, expect, 99002))