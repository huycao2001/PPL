import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test_400(self):
    #     input = """
    #                 Class huycao{
    #                     Var a :Int;
    #                     Var a : Float;
    #                 }
    #                 """
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_401(self):
    #     input = """
    #     Class Shape{

    #     }
    #     Class Shape{
    #         Var vv : Int;
    #     }"""
    #     expect = "Redeclared Class: Shape"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_402(self):
    #     input = """Class Shape{
    #                 goo(length:Int; length:String){}
    #                 }"""
    #     expect = "Redeclared Parameter: length"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_403(self):

    #     input = """Class Shape{
    #                     a(){}
    #                     a(){}
    #                 }"""
    #     expect = "Redeclared Method: a"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_404(self):
    #     input = """Class a{
    #                 lelelele(){
    #                     Var a: Int;
    #                     Var a: Int;
    #                 }
    #                 }"""
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_405(self):
    #     input = """Class Shape{
    #                 foo(){
    #                     Var a:Int;
    #                     Val a:Int;
    #                 }
    #                 }"""
    #     expect = "Redeclared Constant: a"
    #     self.assertTrue(TestChecker.test(input,expect,405))

    # def test_406(self):
    #     input = """Class Shape{
    #                     foo(a:Int){
    #                         Val a:Int = 1;
    #                     }
    #                 }"""
    #     expect = "Redeclared Constant: a"
    #     self.assertTrue(TestChecker.test(input,expect,406))

    # def test_407(self):
    #     input = """Class Shape{
    #                 function(huycao:Int){
    #                     Var huycao: Int = 4444555;
    #                 }
    #                 }"""
    #     expect = "Redeclared Variable: huycao"
    #     self.assertTrue(TestChecker.test(input,expect,407))

    # def test_408(self):
    #     input = """Class Shape{
    #                 function(){
    #                     Var a:Int = 1;
    #                     {
    #                         Var a:Int = 1;
    #                         Var b:Int = 1;
    #                         Var b:Int = 1;
    #                     }
    #                 }
    #                 }"""
    #     expect = "Redeclared Variable: b"
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_409(self):
    #     input = """Class Shape{
    #                 foo(){
    #                     Var a:Int = 1;
    #                     {
    #                         {
    #                         Var a:Int = 1;
    #                         Var b:Int = 1;
    #                         Val b:Int = 1;
    #                         }
    #                     }
    #                 }
    #                 }"""
    #     expect = "Redeclared Constant: b"
    #     self.assertTrue(TestChecker.test(input,expect,409))

    # def test_410(self):
    #     input = """Class Shape{
    #                 function(){
    #                     Var gg:Int = 1;
    #                     Var hh:Int = 1;
    #                     bb = 1234;
    #                 }
    #                 }"""
    #     expect = "Undeclared Identifier: bb"
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_411(self):

    #     input = """
    #                 Class Huycao{}
    #                 Class Huycao2{
    #                 function(){
                        
    #                     Var c:Huycao;
    #                     Var a:Datcao;
    #                 }
    #                 }"""
    #     expect = "Undeclared Class: Datcao"
    #     self.assertTrue(TestChecker.test(input,expect,411))

    # def test_412(self):
    #     input = """
    #                 Class B{
    #                     Var b:Int = 1;
    #                 }
    #                 Class A{
    #                 foo(){
    #                     Var b:Int = 1;
    #                     Var obj:B;
    #                     obj.b = 1;
    #                     obj.aa = 1;
    #                 }
    #                 }"""
    #     expect = "Undeclared Attribute: aa"
    #     self.assertTrue(TestChecker.test(input,expect,412))

    # def test_413(self):
    #     input = """
    #                 Class B{
    #                     Var b:Int = 1;
    #                     c(){
    #                         Return 1;
    #                     }
    #                 }
    #                 Class A{
    #                 foo(){
    #                     Var b:Int = 1;
    #                     Var obj:B;
    #                     obj.b = 1;
    #                     obj.aa = 1;
    #                 }
    #                 }"""
    #     expect = "Undeclared Attribute: aa"
    #     self.assertTrue(TestChecker.test(input,expect,413))

    # def test_414(self):
    #     input = """
    #                 Class B{
    #                     Var b:Int = 1;
    #                     Var clone : Float;
    #                 }
    #                 Class A{
    #                 foo(){
    #                     Var b:Int = 1;
    #                     Var obj:B;
    #                     obj.clone();
    #                 }
    #                 }"""
    #     expect = "Undeclared Method: clone"
    #     self.assertTrue(TestChecker.test(input,expect,414))

    # def test_415(self):
    #     input = """
    #                 Class B{
    #                     Var b:Int = 1;
    #                     Var clone : Float;
    #                 }
    #                 Class A{
    #                 foo(){
    #                     Var b:Int = 1;
    #                     Var obj:B;
    #                     obj.clone = 1.2;
    #                 }
    #                 }"""
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,415))

    # def test_416(self):
    #     input = """
    #                 Class B{
    #                     Var b:Int = 1;
    #                     Var clone : Float;
    #                 }
    #                 Class A{
    #                 foo(){
    #                     Var b:Int = 1;
    #                     Var obj:B;
    #                     obj.clone = 1;
    #                 }
    #                 }"""
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,416))

    # def test_417(self):
    #     input = """
    #                 Class B{
    #                     Var b:Int = 1;
    #                     Var clone : Boolean;
    #                 }
    #                 Class A{
    #                 foo(){
    #                     Var b:Int = 1;
    #                     Var obj:B;
    #                     obj.clone = True;
    #                 }
    #                 }"""
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,417))


    # def test_418(self):
    #     input = """
    #                 Class B{
    #                     Var b:Int = 1;
    #                     Var clone : String;
    #                 }
    #                 Class A{
    #                 foo(){
    #                     Var b:Int = 1;
    #                     Var obj:B;
    #                     obj.clone = "True";
    #                 }
    #                 }"""
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,418))

    # def test_419(self):
    #     input = """
    #                 Class B{
    #                     Var b:Int = 1;
    #                     c(){}
    #                 }
    #                 Class A:B{
    #                 }
    #                 Class C : cc{
    #                 }"""
    #     expect = "Undeclared Class: cc"
    #     self.assertTrue(TestChecker.test(input, expect, 419))

    # def test_420(self):
    #     input = """
    #                     Class Shape{
    #                         huy(){
    #                             Val a:Int = 2;
    #                             a = 3;
    #                         }
    #                     }"""
    #     expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(3))"
    #     self.assertTrue(TestChecker.test(input, expect, 420))

    # def test_421(self):
    #     input = """
    #                     Class Shape{
    #                         huy(){
    #                             Val a:Int ;
                                
    #                         }
    #                     }"""
    #     expect = "Illegal Constant Expression: None"
    #     self.assertTrue(TestChecker.test(input, expect, 421))

    # def test_422(self):
    #     input = """
    #                     Class Shape{
                            
    #                             Val a:Int ;
                                
                            
    #                     }"""
    #     expect = "Illegal Constant Expression: None"
    #     self.assertTrue(TestChecker.test(input, expect, 422))

    # def test_423(self):
    #     input = """
    #     Class Shape{
    #         main()
    #         {
    #             Var a: Int;
    #             {
    #                 Var a : Int;
    #                 {
    #                     Var a: Int;
    #                     Var b: Int;
    #                 }
    #                 Var b: Int;
    #             }
    #         }
    #     }"""
    #     expect = """No Entry Point"""
    #     self.assertTrue(TestChecker.test(input, expect, 423))

    # def test_424(self):
    #     input = """
    #     Class Shape{
    #         main()
    #         {
    #             Var a: Int;
    #             {
    #                 Var a : Int;
    #                 {
    #                     Var a: Int;
    #                     Var b: Int;
    #                 }
    #                 Var b: Int;
    #             }
    #         }
    #     }"""
    #     expect = """No Entry Point"""
    #     self.assertTrue(TestChecker.test(input, expect, 424))

    # def test_425(self):
    #     """Simple program: int main() {} """
    #     input = """
    #                     Class Shape{
    #                         function(){
    #                             Var a:Int = 2;
    #                             Var b:Array[Int,5];
    #                             b[1]=1;
    #                             cccccc[1]=1;
    #                         }
    #                     }"""
    #     expect = "Undeclared Identifier: cccccc"
    #     self.assertTrue(TestChecker.test(input, expect, 425))

    # def test_426(self):
    #     """Simple program: int main() {} """
    #     input = """
    #                     Class Shape{
    #                         function(){
    #                             Var a:Int = 2;
    #                             Var b:Array[Int,5];
    #                             b[1]=1;
    #                             b[9.6]=1;
    #                         }
    #                     }"""
    #     expect = "Type Mismatch In Expression: ArrayCell(Id(b),[FloatLit(9.6)])"
    #     self.assertTrue(TestChecker.test(input, expect, 426))

    # def test_427(self):
    #     """Simple program: int main() {} """
    #     input = """
    #                     Class Shape{
    #                         function(){
    #                             Var a:Int = 2;
    #                             Var b:Array[Int,5];
    #                             b[1]=1;
    #                             b[a]=1;
    #                         }
    #                     }"""
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 427))


    # def test_428(self):
    #     input = """
    #                     Class C{
    #                         e(){
    #                             Var a:Int = 1+2;
    #                             Var b:Float = 1+2.2;
    #                             Var c:Float = 1 + 1.2;
    #                         }
    #                     }"""
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 428))

    # def test_429(self):
    #     input = """
    #                     Class C{
    #                         e(){
    #                             Var a:Int = 1+2;
    #                             Var b:Float = 1+2.2;
    #                             Var c:Float = 1 + True;
    #                         }
    #                     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(+,IntLit(1),BooleanLit(True))"
    #     self.assertTrue(TestChecker.test(input, expect, 429))


    # def test_430(self):
    #     input = """
    #                     Class C{
    #                         e(){
    #                             Var a:Int = 1+2;
    #                             Var b:Float = 1+2.2;
    #                             Var c:Float = 1 + "True";
    #                         }
    #                     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(+,IntLit(1),StringLit(True))"
    #     self.assertTrue(TestChecker.test(input, expect, 430))

    # def test_431(self):
    #     input = """
    #                     Class C{
    #                         e(){
    #                             Var a:Int = 1+2;
    #                             Var b:Float = 1+2.2;
    #                             Var c:Int = 1 / 2.2;
    #                         }
    #                     }"""
    #     expect = "Type Mismatch In Statement: VarDecl(Id(c),IntType,BinaryOp(/,IntLit(1),FloatLit(2.2)))"
    #     self.assertTrue(TestChecker.test(input, expect, 431))


    # def test_432(self):
    #     input = """
    #     Class Shape
    #     {
    #         Var $a: Float = -1 + 80.0;
    #         Val $b: Boolean = ! True;
    #         Val $c: Int = 1 + False;
    #     }"""
    #     expect = """Type Mismatch In Expression: BinaryOp(+,IntLit(1),BooleanLit(False))"""
    #     self.assertTrue(TestChecker.test(input, expect, 432))


    # def test_433(self):
    #     input = """
    #             Class A {
    #                   Var $foo: Int = 1;
    #                   $foo() {
    #                   }
    #             }
    #         """
    #     expect = """No Entry Point"""
    #     self.assertTrue(TestChecker.test(input, expect, 433))

    # def test_434(self):
    #     input = """
    #                     Class Shape{
    #                         ffufuf(){
    #                             Val a : Int = "1.2.2.2";
    #                         }
    #                     }"""
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,StringLit(1.2.2.2))"
    #     self.assertTrue(TestChecker.test(input, expect, 434))

    # def test_435(self):
    #     input = """
    #                     Class Shape{
    #                         ffufuf(){
    #                             Val a : Int = "1.2.2.2";
    #                         }
    #                     }"""
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,StringLit(1.2.2.2))"
    #     self.assertTrue(TestChecker.test(input, expect, 435))


    # def test_436(self):
    #     input = """
    #                     Class Shape{
    #                         ffufuf(){
    #                             Var a : Int = 1 + 1 + 1 + 1 + True;
    #                         }
    #                     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(1)),IntLit(1)),IntLit(1)),BooleanLit(True))"
    #     self.assertTrue(TestChecker.test(input, expect, 436))


    # def test_437(self):
    #     input = """
    #                     Class Shape{
    #                         ffufuf(){
    #                             Var a : String = "abc" +. "def" ;
    #                             Val b : Boolean = "aaaa" ==. "sss";
    #                         }
    #                     }"""
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 437))


    # def test_438(self):
    #     """Simple program: int main() {} """
    #     input = """
    #                     Class B{
    #                         Var b:Int = 1;
    #                         c(g:Int; h:Float){
    #                             Return 1;
    #                         }
    #                         d(){}
    #                     }
    #                     Class Shape{
    #                         foo(){
    #                             Var a:B;
    #                             Var d:Int = a.c(1,2);
    #                             Var e:Int = a.c(1, "trtrtrtrtrt");
    #                         }
    #                     }"""
    #     expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(c),[IntLit(1),StringLit(trtrtrtrtrt)])"
    #     self.assertTrue(TestChecker.test(input, expect, 438))


    # def test_439(self):
    #     input = """
    #     Class Program
    #     {
    #         getArea(a, b: Float)
    #         {
    #             Return a*b;
    #         }
    #         main()
    #         {
    #             Var height: Int = 5;
    #             Var width: Int = 6;
    #             Var myArea: Float = Self.getArea(height, width);
    #             Return myArea;
    #         }
    #     }"""
    #     expect = """Type Mismatch In Statement: Return(Id(myArea))"""
    #     self.assertTrue(TestChecker.test(input, expect, 439))


    # def test_440(self):
    #     input = """
    #     Class Person
    #     {
    #         Var name: String;
    #     }
    #     Class Dog
    #     {
    #         goOut(myPerson: Person)
    #         {
    #             Val owner: String = myPerson.getName();
    #         }
    #     }"""
    #     expect = """Undeclared Method: getName"""
    #     self.assertTrue(TestChecker.test(input, expect, 440))

    # def test_441(self):

    #     input = """
    #                     Class B{
    #                         Var b:Int = 1;
    #                         c(g:Int; h:Float){
    #                             Return 1;
    #                         }
    #                         d(){}
    #                     }
    #                     Class Shape{
    #                         foo(){
    #                             Var a:B;
    #                             Var d:Float = a.c(1,2);
    #                             a.d();
    #                             Var e:Float = a.b;
    #                             Var f:String = a.b;
    #                         }
    #                     }"""
    #     expect = "Type Mismatch In Statement: VarDecl(Id(f),StringType,FieldAccess(Id(a),Id(b)))"
    #     self.assertTrue(TestChecker.test(input, expect, 441))


    # def test_442(self):
    #     input = """
    #                     Class Shape{
    #                         foo(){
    #                             Var a:Int = 1;
    #                             Var b:Float = 1;
    #                             Var c:Float = a+b;
    #                             Var huycao:Int = a+b;
    #                         }
    #                     }"""
    #     expect = "Type Mismatch In Statement: VarDecl(Id(huycao),IntType,BinaryOp(+,Id(a),Id(b)))"
    #     self.assertTrue(TestChecker.test(input, expect, 442))


    # def test_443(self):
    #     input = """
    #                     Class Shape{
    #                         Foo(){
    #                             Var a:Int = 1;
    #                             Var flag:Int = 1;
    #                             If (True){
    #                                 Var a:Int = 2;
    #                             }
    #                             Elseif(True){
    #                                 Var a:Int = 2;
    #                             }
    #                             Else{
    #                                 Var a:Int = 2;
    #                             }
    #                             Var flag:Int = 2 ;
    #                         }
    #                     }"""
    #     expect = "Redeclared Variable: flag"
    #     self.assertTrue(TestChecker.test(input, expect, 443))


    # def test_444(self):
    #     input = """
    #                     Class Shape{
    #                         Foo(){
    #                             Var a:Int = 1;
    #                             Var flag:Int = 1;
    #                             If (True){
    #                                 Var a : Float = 12.4;
    #                                 Var a:Int = 2;
    #                             }
    #                             Elseif(True){
    #                                 Var a:Int = 2;
    #                             }
    #                             Else{
    #                                 Var a:Int = 2;
    #                             }
    #                             Var flag:Int = 2 ;
    #                         }
    #                     }"""
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 444))


    # def test_445(self):
    #     input = """
    #                     Class Shape{
    #                         Var a : Int = 1; 
    #                         Foo(){
    #                             a = 12;
    #                         }
    #                     }"""
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input, expect, 445))


    # def test_446(self):
    #     input = """
    #                     Class Shape{
    #                         Var a : Int = 1; 
    #                         Foo(){
    #                             Self.a = 12;
    #                         }
    #                     }"""
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 446))


    # def test_447(self):
    #     input = """
    #                     Class Shape{
    #                         Var a : Int = 1;
    #                         func(){

    #                         } 
    #                         Foo(){
    #                             Self.func();
                                
    #                         }
    #                     }"""
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 447))


    # def test_448(self):
    #     input = """
    #                     Class C{
    #                         e(){
    #                             Var a:Int = 1;
    #                             Var b:Int = 1;
    #                             Var i:Int = 0;
    #                             Foreach(i In 1 .. 10 By 1){
    #                                 Var a:Int = 1;
    #                                 Break;
    #                                 If (True){
    #                                     Var a:Int = 1;
    #                                     Continue;
    #                                 }
    #                             }
    #                             Var b:Int = 2 ;
    #                         }
    #                     }"""
    #     expect = "Redeclared Variable: b"
    #     self.assertTrue(TestChecker.test(input, expect, 448))

    # def test_449(self):
    #     input = """
    #                     Class C{
    #                         e(){
    #                             Var a:Int = 1;
    #                             Var b:Int = 1;
    #                             Var i:Int = 0;
    #                             Foreach(i In 1 .. 10 By 1){
    #                                 Var a:Int = 1;
    #                                 Var a:Int = 2;
    #                                 Break;
    #                                 If (True){
    #                                     Var a:Int = 1;
    #                                     Continue;
    #                                 }
    #                             }
    #                             Var b:Int = 2 ;
    #                         }
    #                     }"""
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 449))


    # def test_450(self):
    #     input = """
    #                     Class C{
    #                         e(){
    #                             Var a:Int = 1;
    #                             Var b:Int = 1;
    #                             Var i:Int = 0;
    #                             Foreach(i In 1 .. 10 By 1){
    #                                 Var a:Int = 1;
    #                                 Break;
    #                                 If (True){
    #                                     Var a:Int = 1;
    #                                     Continue;
    #                                 }
    #                             }
    #                             Break;
    #                         }
    #                     }"""
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 450))


    # def test_451(self):
    #     input = """
    #                     Class Huycao{
    #                         Shape(){
    #                             Var i:Int;
    #                             Foreach(i In 1 .. 10 By 1){
    #                                 Var a:Int = 1;
    #                                 Break;
    #                                 If (True){
    #                                     Var a:Int = 1;
    #                                     Continue;
    #                                 }
    #                             }
    #                             Continue;
    #                         }
    #                     }"""
    #     expect = "Continue Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 451))


    # def test_452(self):
    #     input = """
    #                     Class Huycao{
    #                         Shape(){
    #                             Var i:Int;
    #                             Var Flag :Boolean= True; 
    #                             Var Clone : Boolean = False;
    #                             Foreach(i In 1 .. 10 By 1){
    #                                 Var a:Int = 1;
    #                                 Break;
    #                                 If (True){
    #                                     Var a:Int = 1;
    #                                     If(Flag || Clone){
    #                                         Break;
    #                                     }
    #                                     Continue;
    #                                 }
    #                             }
    #                             Continue;
    #                         }
    #                     }"""
    #     expect = "Continue Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 452))


    # def test_453(self):
    #     input = """
    #     Class Program
    #     {
    #         Var myArray : Array[Int, 5];
    #         main()
    #         {
    #             Val Clone: Array[String, 5] = 5;
    #         }
    #     }"""
    #     expect = """Type Mismatch In Constant Declaration: ConstDecl(Id(Clone),ArrayType(5,StringType),IntLit(5))"""
    #     self.assertTrue(TestChecker.test(input, expect, 453))


    # def test_454(self):
    #     input = """
    #     Class Program
    #     {
    #         main()
    #         {
    #             Var myyArr: Array[Array[Array[Int,4],2],2] = Array(
    #                 Array(
    #                     Array(1,2,3,4),
    #                     Array(5,6,7,8)
    #                 ),
    #                 Array(
    #                     Array(2,2,3,4),
    #                     Array(6,7,8,8)
    #                 )
    #             );
    #             Return;
    #         }
    #     }"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 454))

    # def test_455(self):
    #     input = """
    #     Class Program
    #     {
    #         main()
    #         {
                
    #             Var clone : Array[Int, 5] = Array(1,2,3,4, False);
    #         }
    #     }"""
    #     expect = """Illegal Array Literal: [IntLit(1),IntLit(2),IntLit(3),IntLit(4),BooleanLit(False)]"""
    #     self.assertTrue(TestChecker.test(input, expect, 455))


    # def test_456(self):
    #     input = """
    #     Class Program
    #     {
    #         Var $myArray: Array[Array[Array[Int,5],2],2] = Array(
    #                 Array(
    #                     Array(1,2,3,4),
    #                     Array(1,2,3,4)
    #                 ),
    #                 Array(
    #                     Array(1,2,3,4),
    #                     Array(1,2,3,4)
    #                 )
    #             );
    #     }"""
    #     expect = """Type Mismatch In Statement: VarDecl(Id($myArray),ArrayType(2,ArrayType(2,ArrayType(5,IntType))),[[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]],[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]]])"""
    #     # Type Mismatch In Statement: AttributeDecl(Static,VarDecl(Id($myArray),ArrayType(2,ArrayType(2,ArrayType(5,IntType))),[[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]],[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]]]))
    #     self.assertTrue(TestChecker.test(input, expect, 456))



    # def test_457(self):
    #     input = """
    #     Class Program
    #     {
    #         main()
    #         {
    #             Var myyArr: Array[Array[Array[Int,4],2],2] = Array(
    #                 Array(
    #                     Array(1,2,3,4),
    #                     Array(5,6,7,8)
    #                 ),
    #                 Array(
    #                     Array(2,2,3,4),
    #                     Array(6,7,8,20.01)
    #                 )
    #             );
    #             Return;
    #         }
    #     }"""
    #     expect = "Illegal Array Literal: [[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(5),IntLit(6),IntLit(7),IntLit(8)]],[[IntLit(2),IntLit(2),IntLit(3),IntLit(4)],[IntLit(6),IntLit(7),IntLit(8),FloatLit(20.01)]]]"
    #     self.assertTrue(TestChecker.test(input, expect, 457))


    # def test_458(self):
    #     input = """
    #     Class Program
    #     {
    #         main()
    #         {
    #             Var myyArr: Array[Array[Array[Float,4],2],2] = Array(
    #                 Array(
    #                     Array(1,2,3,4),
    #                     Array(5,6,7,8)
    #                 ),
    #                 Array(
    #                     Array(2,2,3,4),
    #                     Array(6,7,8,20.01)
    #                 )
    #             );
    #             Return;
    #         }
    #     }"""
    #     expect = "Illegal Array Literal: [[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(5),IntLit(6),IntLit(7),IntLit(8)]],[[IntLit(2),IntLit(2),IntLit(3),IntLit(4)],[IntLit(6),IntLit(7),IntLit(8),FloatLit(20.01)]]]"
    #     self.assertTrue(TestChecker.test(input, expect, 458))

    # def test_459(self):
    #     input = """
    #     Class Program
    #     {
    #         Var $myArray: Array[Array[Array[Int,4],2],3] = Array(
    #                 Array(
    #                     Array(3,5,2,1),
    #                     Array(2,4,5,6)
    #                 ),
    #                 Array(
    #                     Array(5,7,6,5),
    #                     Array(1,3,5,7)
    #                 )
    #             );
    #     }"""
    #     expect =  "Type Mismatch In Statement: VarDecl(Id($myArray),ArrayType(3,ArrayType(2,ArrayType(4,IntType))),[[[IntLit(3),IntLit(5),IntLit(2),IntLit(1)],[IntLit(2),IntLit(4),IntLit(5),IntLit(6)]],[[IntLit(5),IntLit(7),IntLit(6),IntLit(5)],[IntLit(1),IntLit(3),IntLit(5),IntLit(7)]]])"
    #     self.assertTrue(TestChecker.test(input, expect, 459))


    # def test_460(self):
    #     input = """
    #     Class Program
    #     {
    #         Var a: Int;
    #         main()
    #         {
    #             Var a: Int = Array(0,1,1,11);
    #         }
    #     }"""
    #     expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,[IntLit(0),IntLit(1),IntLit(1),IntLit(11)])"
    #     self.assertTrue(TestChecker.test(input, expect, 460))


    # def test_461(self):
    #     """Simple program: int main() {} """
    #     input = """
    #                     Class C{
    #                         e(){
    #                             Var flag:Int = 0;
    #                             Val b:Int = 1;
    #                             Val c:Float = b+1;
    #                             Val d:Float = flag + "caobahuy";
    #                         }
    #                     }"""
    #     expect = "Type Mismatch In Expression: BinaryOp(+,Id(flag),StringLit(caobahuy))"
    #     self.assertTrue(TestChecker.test(input, expect, 461))


    # def test_462(self):
    #     input = """
    #                     Class Program{
    #                         main(){
    #                             Val flag:Int = 0;
    #                             Val b:Int = 1;
    #                             Val c:Float = b+1;
    #                             Val d:Float = flag + 1;
    #                         }
    #                     }"""
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 462))

    # def test_463(self):
    #     input = """
                        
    #                      Class Shape {

    #                         Var a : Int = 10;
    #                         foo() {
    #                             Var x : Int = Self.a;
    #                             Var y : Int = a;
    #                         }
    #                     }"""
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input, expect, 463))


    # def test_464(self):
    #     input = """         
    #                     Class Shape{
    #                     flag(){
    #                         obj.foo();
    #                     }
    #                     }"""
    #     expect = "Undeclared Identifier: obj"
    #     self.assertTrue(TestChecker.test(input, expect, 464))

    # def test_465(self):
    #     input = """         
    #                     Class Shape{
    #                     flag(){
    #                         Var obj : Int; 
    #                         obj.foo();
    #                     }
    #                     }"""
    #     expect = "Illegal Member Access: Call(Id(obj),Id(foo),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 465))


    # def test_466(self):
    #     input = """
    #                     Class Shape{
    #                         Var $a:Int = 5;
    #                         Var b:Int = 4;
    #                     }         
    #                     Class B{
    #                     func(){
    #                         Var b:Int = Shape::$a;
    #                         b = count.foo();
    #                     }
    #                     }"""
    #     expect = "Undeclared Identifier: count"
    #     self.assertTrue(TestChecker.test(input, expect, 466))

    # def test_467(self): 
    #     input = """         
    #                     Class Shape{
    #                         Var $a:Int = 5;
    #                         Var b:Int = 4;
    #                     }         
    #                     Class B{
    #                     func(){
    #                         Var b:Int = Shape::$a;
    #                         b = Shape.b;
    #                     }
    #                     }"""
    #     expect = "Illegal Member Access: FieldAccess(Id(Shape),Id(b))"
    #     self.assertTrue(TestChecker.test(input, expect, 467)) 

    # def test_468(self): 
    #     input = """         
    #                     Class A{
    #                         Var $a:Int = 5;
    #                         Var b:Int = 4;
    #                     }         
    #                     Class B{
    #                     func(){
    #                         Var b:A = New A();
    #                         Var c:Int = b.b;
    #                         Var d:Int = b::$a;
    #                     }
    #                     }"""
    #     expect = "Illegal Member Access: FieldAccess(Id(b),Id($a))"  
    #     self.assertTrue(TestChecker.test(input, expect, 468)) 

    # def test_469(self): 
    #     input = """
    #     Class Foo
    #     {
    #         $foo()
    #         {

    #         }
    #     }
    #     Class Program
    #     {
    #         main()
    #         {
    #             Var obj : Foo;
    #             obj::$foo();
    #         }
    #     }
    #     """
    #     expect = """Illegal Member Access: Call(Id(obj),Id($foo),[])"""
    #     self.assertTrue(TestChecker.test(input, expect, 469)) 


    # def test_470(self): 
    #     input = """         
    #                     Class Shape{
    #                         $a(){}
    #                         b(){}
    #                     }         
    #                     Class CCC{
    #                     func(){
    #                         Shape::$a();
    #                         Var b : Shape = New Shape();
    #                         b.b();
    #                         b::$a();
    #                     }
    #                     }"""
    #     expect = "Illegal Member Access: Call(Id(b),Id($a),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 470)) 


    # def test_471(self): 
    #     input = """
    #     Class Shape{
    #         Val isCopied: Boolean = True;
    #         compose(){
    #         }
    #     }
    #     Class Program{
    #     main(){
    #         Shape.compose();
    #     }
    #     }"""
    #     expect = """Illegal Member Access: Call(Id(Shape),Id(compose),[])"""  
    #     self.assertTrue(TestChecker.test(input, expect, 471)) 

    # def test_472(self): 
    #     input = """         
    #                     Class Shape{
    #                         $a(){}
    #                         b(){}
    #                     }         
    #                     Class B{
    #                     func(){
    #                         Shape::$a();
    #                         Var b:Shape = New Shape();
    #                         b.b();
    #                         Shape.b();
    #                     }
    #                     }"""
    #     expect = "Illegal Member Access: Call(Id(Shape),Id(b),[])" 
    #     self.assertTrue(TestChecker.test(input, expect, 472)) 

    # def test_473(self): 
    #     input = """
    #     Class Program{
    #         main(){
    #             Var a: Int = 5 + 4 + 4 + 4;
    #             Var b: Int = a.maxSize;
    #         }
    #     }"""
    #     expect = """Illegal Member Access: FieldAccess(Id(a),Id(maxSize))""" 
    #     self.assertTrue(TestChecker.test(input, expect, 473)) 

    # def test_474(self): 
    #     input = """         
    #                     Class A{
    #                         $a(){}
    #                         b(){}
    #                     }         
    #                     Class B{
    #                     func(){
    #                         A::$a();
    #                         Var b:A = New A();
    #                         b.b();
    #                         A.b();
    #                     }
    #                     }"""
    #     expect = "Illegal Member Access: Call(Id(A),Id(b),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 474)) 

    # def test_475(self): 
    #     input = """         
    #                     Class A{
    #                         $a(){
    #                             Return 1;
    #                         }
    #                         b(){
    #                             Return 1;
    #                         }
    #                     }
    #                     Class Program{

    #                     }
    #                      """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 475)) 

    # def test_476(self): 
    #     input = """         
    #                     Class A{
    #                         $a(){
    #                             Return 1;
    #                         }
    #                         b(){
    #                             Return 1;
    #                         }
    #                     } 
    #                     Class Program{
    #                         mainFake(){
    #                             Return 1;
    #                         }
    #                     }"""
    #     expect = "No Entry Point"   
    #     self.assertTrue(TestChecker.test(input, expect, 476)) 

    # def test_477(self): 
    #     input = """         
    #                     Class Program{
    #                         $main(){
    #                             Return;
    #                         }
    #                     }"""
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 477)) 

    # def test_478(self): 
    #     input = """         
    #                     Class Program{
    #                         main( a : Int){
    #                             Return;
    #                         }
    #                     }"""
    #     expect = "No Entry Point" 
    #     self.assertTrue(TestChecker.test(input, expect, 478)) 

    # def test_479(self): 
    #     input = """         
    #                     Class Program{
    #                         main(){
    #                             Return;
    #                         }
    #                     }"""
    #     expect = "[]"  
    #     self.assertTrue(TestChecker.test(input, expect, 479)) 

    # def test_480(self): 
    #     input = """         
    #                     Class A{
    #                     Var y:Int=10;
    #                     }
    #                     Class B{
    #                     Val x : A = New A();
    #                     func (){
    #                         Val z:Int=Self.x.y;
    #                     }
    #                     } """
    #     expect = "Illegal Constant Expression: FieldAccess(FieldAccess(Self(),Id(x)),Id(y))"    
    #     self.assertTrue(TestChecker.test(input, expect, 480)) 


    # def test_481(self): 
    #     input = """     
    #                     Class Shape{
    #                     Var x:Int = 1;
    #                     Area(){
    #                         Return 1;
    #                     }
    #                     func (){
    #                         Var a:Int = Self.x;
    #                         a = Self.Area();
    #                         Var b:String = Self.Area();
    #                     }
    #                     } """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(b),StringType,CallExpr(Self(),Id(Area),[]))"    
    #     self.assertTrue(TestChecker.test(input, expect, 481)) 


    # def test_482(self): 
    #     input = """     
    #                     Class Shape {
    #                        func() {                        
    #                        } 
    #                        Constructor(a:Int){
    #                        }                       
    #                     }                        
    #                     Class Test{                        
    #                       Var e: Shape = New Shape(1);              
    #                       Var b: Shape = New Shape();                                
    #                     } """
    #     expect = "Type Mismatch In Expression: NewExpr(Id(Shape),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 482)) 


    # def test_483(self): 
    #     input = """     
    #                     Class Shape {
    #                        func() {                        
    #                        } 
    #                        Constructor(a:Int){
    #                        }                       
    #                     }                        
    #                     Class Test{                        
    #                       Var e: Shape = New Shape("ccccc");              
                                                      
    #                     } """
    #     expect = "Type Mismatch In Expression: NewExpr(Id(Shape),[StringLit(ccccc)])" 
    #     self.assertTrue(TestChecker.test(input, expect, 483)) 


    # def test_484(self): 
    #     input = """     
    #                     Class Shape {
    #                        func() {                        
    #                        } 
                                                
    #                     }                        
    #                     Class Test{                        
    #                       Var e: Shape = New Shape("ccccc");              
                                                      
    #                     } """
    #     expect = "Type Mismatch In Expression: NewExpr(Id(Shape),[StringLit(ccccc)])"  
    #     self.assertTrue(TestChecker.test(input, expect, 484)) 


    # def test_485(self): 
    #     input = """
    #     Class Program
    #     {
    #         main()
    #         {
    #             Var sum: Int = 0;
    #             Var myArray: Array[Int, 5] = Array(1,2,3,4,5);
    #             Var i:Int;
    #             Foreach(i In 1 .. 5)
    #             {
    #                 If(sum >= 5)
    #                 {
    #                     Break;
    #                 }
    #                 Else
    #                 {
    #                     Continue;
    #                 }
    #             }
    #             Val result: Int = sum * 2;
    #         }
    #     }"""
    #     expect = """Illegal Constant Expression: BinaryOp(*,Id(sum),IntLit(2))""" 
    #     self.assertTrue(TestChecker.test(input, expect, 485)) 

    # def test_486(self): 
    #     input = """     
    #                     Class Shape {
    #                        Var a:Int = 1;                      
    #                     }                        
    #                     Class B{ 
    #                         Var b:Shape = New Shape(); 
    #                     }
    #                     Class C{
    #                         foo(){
    #                             Var c:B = New B();
    #                             Var e:Int = c.b.a;
    #                             Var f:Int = c.clone.a;
    #                         }
    #                     }"""
    #     expect = "Undeclared Attribute: clone"  
    #     self.assertTrue(TestChecker.test(input, expect, 486)) 

    # def test_487(self): 
    #     input = """     
    #                     Class A {
    #                        Var a:Int = 1;                      
    #                     }                        
    #                     Class B{ 
    #                         Var $b:A = New A(); 
    #                     }
    #                     Class C{
    #                         foo(){
    #                             Var count:B = New B();
    #                             Var entity:Int = B::$b.a;
    #                             Var flag:Int = B::$b.fun;
    #                         }
    #                     }"""
    #     expect = "Undeclared Attribute: fun"  
    #     self.assertTrue(TestChecker.test(input, expect, 487)) 
        
    # def test_488(self): 
    #     input = """     
    #                     Class Shape {
    #                        Funtion(){
    #                             Var a: Array[Array[Int, 2],2] = Array(Array(1,2),Array(4,5));
    #                             Var b: Array[Array[Int, 2],2] = Array(Array(2,3),Array(10));
    #                        }               
    #                     }"""
    #     expect = "Illegal Array Literal: [[IntLit(2),IntLit(3)],[IntLit(10)]]"   
    #     self.assertTrue(TestChecker.test(input, expect, 488)) 


    # def test_489(self): 
    #     input = """     
    #                     Class Shape {
    #                        Function(){
    #                             Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
    #                             Var b: Array[Array[Int, 2],2] = Array(Array("pirate","king"),Array("lffy","zoro"));
    #                        }               
    #                     }"""
    #     expect = "Type Mismatch In Statement: VarDecl(Id(b),ArrayType(2,ArrayType(2,IntType)),[[StringLit(pirate),StringLit(king)],[StringLit(lffy),StringLit(zoro)]])"
    #     self.assertTrue(TestChecker.test(input, expect, 489)) 

    # def test_490(self): 
    #     input = """     
    #                     Class Shape {
    #                        funtion(){
    #                             Var myArr: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
    #                             myArr[1] = Array(1,1);
    #                             myArr[1][1] = 1;
    #                             myArr = 1;
    #                        }               
    #                     }"""
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(myArr),IntLit(1))"   
    #     self.assertTrue(TestChecker.test(input, expect, 490)) 

    # def test_491(self): 
    #     input = """
    #             Class Shape {

    #                 Function() {
    #                     Var a: Array[Int, 3] = Array(12,22,1);
    #                     a[4] = 5; 
    #                     a[1][2] = 4; 
    #                 }
    #             }
    #         """
    #     expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(1),IntLit(2)])"  
    #     self.assertTrue(TestChecker.test(input, expect, 491)) 

    # def test_492(self): 
    #     input = """
    #                     Class Person{
    #                         Var name: String;
    #                         Var phone: Int;
    #                         Constructor(newName: String; newphone : Int){
    #                             Self.name = newName;
    #                             Self.phone = newphone;
    #                         }
    #                     }
    #                     Class Program{
    #                         main(){
    #                             Var huycao: Person = New Person ();
    #                         }
    #                     }
    #         """

    #     expect = "Type Mismatch In Expression: NewExpr(Id(Person),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 492)) 

    # def test_493(self): 
    #     input = """
    #             Class A {
    #                   Var $foo: Int = 1;
    #                   $foo() {
    #                   }
    #             }
    #         """
    #     expect = "No Entry Point"  
    #     self.assertTrue(TestChecker.test(input, expect, 493)) 

    # def test_494(self): 
    #     input = """
    #             Class A {
    #                   Var $foo: Int = 1;
    #                   $foo() {
    #                   }
    #             }

    #             Class B{
    #                 flag(){
    #                     huycao::$foo();
    #                 }
    #             }
    #         """
    #     expect = "Undeclared Class: huycao" 
    #     self.assertTrue(TestChecker.test(input, expect, 494))
     
    # def test_495(self): 
    #     input = """
    #     Class Program
    #     {
    #         main()
    #         {
    #             Var firstArray : Array[Array[Int ,2], 3] = Array(
    #                 Array(1,2),
    #                 Array(3,4),
    #                 Array(5,6)
    #             );
    #             Var secondArray : Array[Int , 2] = firstArray[1];
    #             Var thirdArray : Array[Int, 2] = firstArray;
    #         }
    #     }"""
    #     expect = """Type Mismatch In Statement: VarDecl(Id(thirdArray),ArrayType(2,IntType),Id(firstArray))"""
    #     self.assertTrue(TestChecker.test(input, expect, 495)) 

    # def test_496(self): 
    #     input = """
    #     Class Program
    #     {
    #         main ()
    #         {
    #             Var myArray: Array[Array[Array[Int,4],2],2] = Array(
    #                     Array(
    #                         Array(1,2,3,4),
    #                         Array(1,2,3,4)
    #                     ),
    #                     Array(
    #                         Array(1,2,3,4),
    #                         Array(1,2,3,4)
    #                     )
    #                 );
    #             Var nextArray : Array[Array[Int,4],2] = myArray[1];
    #             Var value : Int = myArray[1][1][1];
    #             If (value)
    #             {
    #                 Var value : Boolean = True;
    #             }
    #         }
    #     }"""
    #     expect = """Type Mismatch In Statement: If(Id(value),Block([VarDecl(Id(value),BoolType,BooleanLit(True))]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 496)) 

    # def test_497(self): 
    #     input = """
    #     Class Program
    #     {
    #         main()
    #         {
    #             Var a: Int = 6;
    #             Foreach (i In 1 .. a By True)
    #             {
    #                 Var a:Boolean = True;
    #             }
    #         }
    #     }"""
    #     expect = "Undeclared Identifier: i"
    #     self.assertTrue(TestChecker.test(input, expect, 497))
     
    # def test_498(self): 
    #     input = """
    #     Class Program
    #     {
    #         main()
    #         {
    #             Var a: Int = 6;
    #             Val i : Int = 0;
    #             Foreach (i In 1 .. a By True)
    #             {
    #                 Var a:Boolean = True;
    #             }
    #         }
    #     }"""
    #     expect = "Cannot Assign To Constant: AssignStmt(Id(i),IntLit(1))"  
    #     self.assertTrue(TestChecker.test(input, expect, 498)) 

    # def test_499(self): 
    #     input = """
    #     Class Program{
    #         main(){
    #             Var ToMe : String = "This is the end , i wish you all the best in your journey, appreciate your effort so much, lets fight together";
    #             Var a: Int = 6;
    #             Var i : Int = 0;
    #             Foreach (i In 1 .. a By 1)
    #             {
    #                 Var a:Boolean = True;
    #             }
    #         }
    #     }"""
    #     expect = "[]"    
    #     self.assertTrue(TestChecker.test(input, expect, 499)) 

    # def test_500(self): 
    #     input = """
    #     Class A {
    #         Var a : Int;
    #         Val arr : Array[Int,2] = Array(
    #             Array(1,2),
    #             Array(True, False),
    #             Array("String" , "eeww")
    #         );
    #     }

    #     Class Program{
    #         main(){}
    #     }
    #     """
    #     # Illegal Array Literal: [[IntLit(1),IntLit(2)],[[IntLit(1),IntLit(2)],[IntLit(1),IntLit(2)]]]
    #     expect = "Illegal Array Literal: [[IntLit(1),IntLit(2)],[BooleanLit(True),BooleanLit(False)],[StringLit(String),StringLit(eeww)]]"
    #     self.assertTrue(TestChecker.test(input, expect, 500)) 


    def test_501(self): 
        input = """


        Class Program{
            func(a,b : Int){
                Var c : Int;
            }
            
        }
        """
        # Illegal Array Literal: [[IntLit(1),IntLit(2)],[[IntLit(1),IntLit(2)],[IntLit(1),IntLit(2)]]]
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 501)) 


