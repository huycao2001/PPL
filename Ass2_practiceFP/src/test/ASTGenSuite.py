import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_AST1(self):
        input = """
        Class Shape{

        }
        Class People{

        }
        """
        expect = "Program([ClassDecl(Id(Shape),[]),ClassDecl(Id(People),[])])"
        self.assertTrue(TestAST.test(input,expect,301))


    def test_AST2(self):
        input = """
        Class Shape{
            
        }
        Class Dog : Animal{

        }
        """
        expect = "Program([ClassDecl(Id(Shape),[]),ClassDecl(Id(Dog),Id(Animal),[])])"
        self.assertTrue(TestAST.test(input,expect,302))


    def test_AST3(self):
        input = """
        Class Shape{
            Constructor(){
                
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Constructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,303))

    def test_AST4(self):
        input = """
        Class Shape{
            Constructor(){
                
            }

            Destructor(){

            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,304))


    def test_AST5(self):
        input = """
        Class Shape{
            Constructor(a,b : Int){
                
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,305))


    def test_AST6(self):
        input = """
        Class Shape{
            $getShape(a,b : Int){
                
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id($getShape),Static,[param(Id(a),IntType),param(Id(b),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,306))

    def test_AST7(self):
        input = """
        Class A {
            Var a:Int;
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType))])])'
        self.assertTrue(TestAST.test(input, expect, 307))


    def test_AST8(self):
        input = """
        Class A {
            Var a:Array[Int,5];
        }
        """
        expect = "Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType)))])])"
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_AST9(self):
        input = """
        Class A {
            Var a : Int = 123;
        }
        """
        expect = "Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(123)))])])"
                # Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id(a),IntType,IntLit(123)))])])
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_AST10(self):
        input = """
        Class A {
            Var $a : Int = 123;
        }
        """
        expect = "Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($a),IntType,IntLit(123)))])])"
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_AST11(self):
        input = """
        Class Shape {
            Var a,b : Int = 1,2;
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2)))])])"
        # 
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_AST12(self):
        input = """
        Class Shape {
            Var a,b,c : Int = 1,2, 0b1111;
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(15)))])])"
        # Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(15)))])])
        self.assertTrue(TestAST.test(input, expect, 312))


    def test_AST13(self):
        input = """
        Class Shape {
            Var a : Int = 1 + 1 * 100/ 2;
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(100)),IntLit(2)))))])])"
        # 
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_AST14(self):
        input = """Class Program {
            main() {}
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_AST15(self):
        input = """Class Shape {
            main() {}
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_AST16(self):
        input = """Class Program {
            main(a : Int ; b : Float) {}
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_AST17(self):
        input = """Class Program {
            Var a : Shape;
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Shape)),NullLiteral()))])])"
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_AST18(self):
        input = """Class Program {
            Val  a : Array[Int,5] = Array(1,2,3,4,5);
            
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]))])])"
        self.assertTrue(TestAST.test(input, expect, 318))


    def test_AST19(self):
        input = """Class Program {
            Val  a : Array[Array[Int,5],3] = Array(
                Array(1,2,3,4,5) , Array(4,5,6,7,8) , Array(7,8,9,10,11)
            );
            
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(3,ArrayType(5,IntType)),[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)],[IntLit(4),IntLit(5),IntLit(6),IntLit(7),IntLit(8)],[IntLit(7),IntLit(8),IntLit(9),IntLit(10),IntLit(11)]]))])])"
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_AST20(self):
        input = """Class Program {
            Var  a : Array[Array[Array[Array[Int,5],5],5],3];
            
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(3,ArrayType(5,ArrayType(5,ArrayType(5,IntType))))))])])"
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_AST21(self):
        input = """Class Program {
            Var a :Int; 
            getA(){
                Return a;
            }
            
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),MethodDecl(Id(getA),Instance,[],Block([Return(Id(a))]))])])"
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_AST22(self):
        input = """Class Program {
            inc(){
                Var a : Int = 100;
            }
            
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(inc),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(100))]))])])"
        self.assertTrue(TestAST.test(input, expect, 322))


    def test_AST23(self):
        input = """Class Program {
            Var a : Int;
            func(){
                Var b : Int = 100;
                Return a + -b;
            }
            
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),MethodDecl(Id(func),Instance,[],Block([VarDecl(Id(b),IntType,IntLit(100)),Return(BinaryOp(+,Id(a),UnaryOp(-,Id(b))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_AST24(self):
        input = """Class Program {
            Var a : Int;
            Var b : Int; 
            Constructor(a,b : Int){
                Self.a = a; 
                Self.b = b;
            }
            
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(a)),Id(a)),AssignStmt(FieldAccess(Self(),Id(b)),Id(b))]))])])"
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_AST25(self):
        input = """Class Program {
            Var a : Int;
            inc(){
                a = a + 1;
            }

            Constructor(){
                a = 0;
            }
            
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),MethodDecl(Id(inc),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(a),IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_AST26(self):
        input = """Class Program {
            main(){
                Out.print("What do lives mean to you ?");
            }
            
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(print),[StringLit(What do lives mean to you ?)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_AST27(self):
        input = """Class Program {
            main(){
                Out.print(Shape::$getCount());
            }
            
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(print),[CallExpr(Id(Shape),Id($getCount),[])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_AST28(self):
        input = """Class Program {
            main() {
                If (a == b) {
                    Self.print("a equals b");
                } Else {
                    Self.print("No it is not");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(a equals b)])]),Block([Call(Self(),Id(print),[StringLit(No it is not)])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 328))


    def test_AST29(self):
        input = """Class Program {
            main() {
                If(False){}
                Else{}
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BooleanLit(False),Block([]),Block([]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_AST30(self):
        input = """Class Program {
            main() {
                Var a : Array[Array[Array[Array[Int, 0x11], 0x11], 0x11], 0x11];
            }    
        }"""
        expect =  "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(17,ArrayType(17,ArrayType(17,ArrayType(17,IntType)))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_AST31(self):
        input = """Class Program {
            main() {
                If(False){}
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BooleanLit(False),Block([]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_AST32(self):
        input = """
        Class A:B{
            Foo(){
                If(1){}
                If(2){}Else{}
                If(3){}Elseif(4){}Else{a=1;}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(1),Block([])),If(IntLit(2),Block([]),Block([])),If(IntLit(3),Block([]),If(IntLit(4),Block([]),Block([AssignStmt(Id(a),IntLit(1))])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_AST33(self):
        input = """
        Class Program{
            $Foo(){
                If(1){}
                If(2){}Else{}
                If(3){}Elseif(4){}Else{a=1;}
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id($Foo),Static,[],Block([If(IntLit(1),Block([])),If(IntLit(2),Block([]),Block([])),If(IntLit(3),Block([]),If(IntLit(4),Block([]),Block([AssignStmt(Id(a),IntLit(1))])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_AST34(self):
        input = """
        Class Program{
            main(a: Int ; b : Int){
                If(1){}
                If(2){}Else{}
                If(3){}Elseif(4){}Else{a=1;}
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([If(IntLit(1),Block([])),If(IntLit(2),Block([]),Block([])),If(IntLit(3),Block([]),If(IntLit(4),Block([]),Block([AssignStmt(Id(a),IntLit(1))])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_AST35(self):
        input = """Class Program {
            main() {
                Val c, d : Float = .e1000 , 1.e-1;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(c),FloatType,FloatLit(0.0)),ConstDecl(Id(d),FloatType,FloatLit(0.1))]))])])"
        self.assertTrue(TestAST.test(input, expect, 335))


    def test_AST36(self):
        input = """Class Program {
            main() {
                Val a,b,c : Int = 1, 01, 0b1; 
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),IntType,IntLit(1)),ConstDecl(Id(b),IntType,IntLit(1)),ConstDecl(Id(c),IntType,IntLit(1)),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 336))


    def test_AST37(self):
        input = """Class Program {
            main() {
                Val a,b,c : Bool = True && (False || !True) , (True && False || True) || False , !True || !False && !(True && False); 
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),ClassType(Id(Bool)),BinaryOp(&&,BooleanLit(True),BinaryOp(||,BooleanLit(False),UnaryOp(!,BooleanLit(True))))),ConstDecl(Id(b),ClassType(Id(Bool)),BinaryOp(||,BinaryOp(||,BinaryOp(&&,BooleanLit(True),BooleanLit(False)),BooleanLit(True)),BooleanLit(False))),ConstDecl(Id(c),ClassType(Id(Bool)),BinaryOp(&&,BinaryOp(||,UnaryOp(!,BooleanLit(True)),UnaryOp(!,BooleanLit(False))),UnaryOp(!,BinaryOp(&&,BooleanLit(True),BooleanLit(False))))),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_AST38(self):
        line = """
                Class Shape{
                    foo(){
                        Foreach (x In 1 .. 100 By 1){
                            a = a + 1;
                        }
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),IntLit(1),IntLit(100),IntLit(1),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))])])]))])])"
        self.assertTrue(TestAST.test(line, expect, 338))

    def test_AST39(self):
        line = """
                Class Shape{
                    foo(){
                        Foreach (x In 1 .. 100 ){
                            a = a + 1;
                        }
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),IntLit(1),IntLit(100),IntLit(1),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))])])]))])])"
        self.assertTrue(TestAST.test(line, expect, 339))

    def test_AST40(self):
        line = """
                Class Shape{
                    foo(){
                        Foreach (x In 1 .. Self.length(my_array) ){
                            a = a + 1;
                        }
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),IntLit(1),CallExpr(Self(),Id(length),[Id(my_array)]),IntLit(1),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))])])]))])])"
        self.assertTrue(TestAST.test(line, expect, 340))

    def test_AST41(self):
        line = """
                Class Shape{
                    foo(){
                        Foreach (x In 1 .. Self.length(my_array) ){
                            a = a + 1;
                        }
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),IntLit(1),CallExpr(Self(),Id(length),[Id(my_array)]),IntLit(1),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))])])]))])])"
        self.assertTrue(TestAST.test(line, expect, 341))


    def test_AST42(self):
        line = """
                Class Shape{
                    foo(){
                        Foreach (x In Self.length(your_array) .. Self.length(my_array) ){
                            a = a + 1;
                        }
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([For(Id(x),CallExpr(Self(),Id(length),[Id(your_array)]),CallExpr(Self(),Id(length),[Id(my_array)]),IntLit(1),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))])])]))])])"
        self.assertTrue(TestAST.test(line, expect, 342))


    def test_AST43(self):
        input = """Class Entity : Object {
            Var $a, b, c : Float = 10.0, 11., 1e15;
            Val a, c, d : Float = .e5, 0.000, 0.2;
            Var c, d, e : Float = 1e-12, 1E+4, 11.1123e10;
            Val $a, $y, $x : Float = 50.1123E-5, .5e5, .4e+5;
            Var x, y : Float = .1123e-10, 1123E123;
        }"""
        expect = "Program([ClassDecl(Id(Entity),Id(Object),[AttributeDecl(Static,VarDecl(Id($a),FloatType,FloatLit(10.0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(11.0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(1000000000000000.0))),AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(0.0))),AttributeDecl(Instance,ConstDecl(Id(c),FloatType,FloatLit(0.0))),AttributeDecl(Instance,ConstDecl(Id(d),FloatType,FloatLit(0.2))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(1e-12))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(10000.0))),AttributeDecl(Instance,VarDecl(Id(e),FloatType,FloatLit(111123000000.0))),AttributeDecl(Static,ConstDecl(Id($a),FloatType,FloatLit(0.000501123))),AttributeDecl(Static,ConstDecl(Id($y),FloatType,FloatLit(50000.0))),AttributeDecl(Static,ConstDecl(Id($x),FloatType,FloatLit(40000.0))),AttributeDecl(Instance,VarDecl(Id(x),FloatType,FloatLit(1.123e-11))),AttributeDecl(Instance,VarDecl(Id(y),FloatType,FloatLit(1.123e+126)))])])"
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_AST44(self):
        input = """Class Entity : Object {
            Var a : Shape = New Shape(2,3); 
            Var b : Shape = New Shape();
            main(){
                Var a : Shape = New Shape(2,3);
                Var b : Shape = New Shape();
            }
        }"""
        expect = "Program([ClassDecl(Id(Entity),Id(Object),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(2),IntLit(3)]))),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(Shape)),NewExpr(Id(Shape),[]))),MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(2),IntLit(3)])),VarDecl(Id(b),ClassType(Id(Shape)),NewExpr(Id(Shape),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_AST45(self):
        input = """Class Entity : Object {
            Var a : Shape = Null;
            main(){
                
            }
        }"""
        expect = "Program([ClassDecl(Id(Entity),Id(Object),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Shape)),NullLiteral())),MethodDecl(Id(main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_AST346(self):
        input = """Class Program {
            Val a, b, c : Int = 1 + 1 * 100 , 2 * 2 / 4 / 5 % 6 , 3 / 3 + (12 + 23);
            Var a : Array[Int, 5] = Array(1 * 2 / 3, 3 + 3 / 3, 10 - -9, 100 * -3, 100 % 10);
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(1),IntLit(100))))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,BinaryOp(%,BinaryOp(/,BinaryOp(/,BinaryOp(*,IntLit(2),IntLit(2)),IntLit(4)),IntLit(5)),IntLit(6)))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(+,BinaryOp(/,IntLit(3),IntLit(3)),BinaryOp(+,IntLit(12),IntLit(23))))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType),[BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(+,IntLit(3),BinaryOp(/,IntLit(3),IntLit(3))),BinaryOp(-,IntLit(10),UnaryOp(-,IntLit(9))),BinaryOp(*,IntLit(100),UnaryOp(-,IntLit(3))),BinaryOp(%,IntLit(100),IntLit(10))]))])])"
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_AST347(self):
        input = """Class Entity {
            Val $a: Int = 0b1011010;
            Var b: Int = 00;
            $getA(){
                Return New X().Y();
                ## Return $a; ##
            }
        }
        Class Program {
            main() {
                Var sum1: Int = Example::$getA() + Example.b;
                Var sum2: Int = Example.b + Example::$getA();
                Out.printInt(res1 + res2);
            }
        }"""
        expect = "Program([ClassDecl(Id(Entity),[AttributeDecl(Static,ConstDecl(Id($a),IntType,IntLit(90))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(0))),MethodDecl(Id($getA),Static,[],Block([Return(CallExpr(NewExpr(Id(X),[]),Id(Y),[]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(sum1),IntType,BinaryOp(+,CallExpr(Id(Example),Id($getA),[]),FieldAccess(Id(Example),Id(b)))),VarDecl(Id(sum2),IntType,BinaryOp(+,FieldAccess(Id(Example),Id(b)),CallExpr(Id(Example),Id($getA),[]))),Call(Id(Out),Id(printInt),[BinaryOp(+,Id(res1),Id(res2))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 347))




    def test_AST348(self):
        input = """
        Class Program{
           ## main(){
                
            }##
        }""" 
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_AST349(self):
        input = """
        ## Multi If ## 
        Class Program{
            main(){
                Var a : Int = 0x123456;
                If(a > 2){
                    ## do sth##
                }

                If ( a > 3 ){
                    a = a - 1; 
                }

                If ( a > 4 ){

                }
                If(a > 5){
                    a = a /3; 
                }
            }
        }
        """ 
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(1193046)),If(BinaryOp(>,Id(a),IntLit(2)),Block([])),If(BinaryOp(>,Id(a),IntLit(3)),Block([AssignStmt(Id(a),BinaryOp(-,Id(a),IntLit(1)))])),If(BinaryOp(>,Id(a),IntLit(4)),Block([])),If(BinaryOp(>,Id(a),IntLit(5)),Block([AssignStmt(Id(a),BinaryOp(/,Id(a),IntLit(3)))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 349))


    def test_AST50(self):
        input = """
        Class Program{
            main(){
                Var a : Int = 0x123456;
                If(a == -4 + 1 * 9 / 2 * 8 % 4 ){
                    a = -a; 
                }
            }
        }
        """ 
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(1193046)),If(BinaryOp(==,Id(a),BinaryOp(+,UnaryOp(-,IntLit(4)),BinaryOp(%,BinaryOp(*,BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(9)),IntLit(2)),IntLit(8)),IntLit(4)))),Block([AssignStmt(Id(a),UnaryOp(-,Id(a)))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_AST51(self):
        input = """
        Class Program{
            Var a : Int = ( 2 + ((((((a+1) + 2)*3)/(4 + 5) * 6) % 4 /3 * a) + 123 / (456 * 789) ) * 23 / 24 + (a -1));
        }
        """ 
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,BinaryOp(+,IntLit(2),BinaryOp(/,BinaryOp(*,BinaryOp(+,BinaryOp(*,BinaryOp(/,BinaryOp(%,BinaryOp(*,BinaryOp(/,BinaryOp(*,BinaryOp(+,BinaryOp(+,Id(a),IntLit(1)),IntLit(2)),IntLit(3)),BinaryOp(+,IntLit(4),IntLit(5))),IntLit(6)),IntLit(4)),IntLit(3)),Id(a)),BinaryOp(/,IntLit(123),BinaryOp(*,IntLit(456),IntLit(789)))),IntLit(23)),IntLit(24))),BinaryOp(-,Id(a),IntLit(1)))))])])"
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_AST52(self):
        input = """
        Class Program{
            Var a : Array[Array[Array[Array[Array[Array[Array[Int,0b1011],0xABCD],04567],0123],5],4],3];
        }
        """ 
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(3,ArrayType(4,ArrayType(5,ArrayType(83,ArrayType(2423,ArrayType(43981,ArrayType(11,IntType)))))))))])])"
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_AST53(self):
        input = """
        Class Program {
            main(){
                Var a : Shape = New Shape(1,2); 
                Return Shape::$GetCount();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(1),IntLit(2)])),Return(CallExpr(Id(Shape),Id($GetCount),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_AST54(self):
        input = """Class Program {
            Val a, b: Array[Int, 10];
            Var c: Array[String, 1_0_0_0];
            main() {
               a = 1;
               b = Array();
               c = Array("1", "2", "3");
               d = Array(Array(1, 2, 3), Array(4, 5, 6) , Array(1, 2, 3)  ) ;

               e = a + b;
               f = (a +. b) ==. c;
               g = f.callFunc() - g::$something(a, b);
               h = g::$somethingElse;
               i = g.someValue();
               j = "Something special";
               Return;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(10,IntType),None)),AttributeDecl(Instance,ConstDecl(Id(b),ArrayType(10,IntType),None)),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(1000,StringType))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),IntLit(1)),AssignStmt(Id(b),[]),AssignStmt(Id(c),[StringLit(1),StringLit(2),StringLit(3)]),AssignStmt(Id(d),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4),IntLit(5),IntLit(6)],[IntLit(1),IntLit(2),IntLit(3)]]),AssignStmt(Id(e),BinaryOp(+,Id(a),Id(b))),AssignStmt(Id(f),BinaryOp(==.,BinaryOp(+.,Id(a),Id(b)),Id(c))),AssignStmt(Id(g),BinaryOp(-,CallExpr(Id(f),Id(callFunc),[]),CallExpr(Id(g),Id($something),[Id(a),Id(b)]))),AssignStmt(Id(h),FieldAccess(Id(g),Id($somethingElse))),AssignStmt(Id(i),CallExpr(Id(g),Id(someValue),[])),AssignStmt(Id(j),StringLit(Something special)),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 354))


    def test_AST55(self):
        input = """Class Program {
            main() {
                Var c, h: Int = 50, 30;
                Var d: Int = Math.int(System.input("Enter D: "));
                Var Q: Int = Math.int(2 * c * d / h);
                Out.println(Math.round(Math.sqrt(Math.abs(Math.log(Q)))));
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(c),IntType,IntLit(50)),VarDecl(Id(h),IntType,IntLit(30)),VarDecl(Id(d),IntType,CallExpr(Id(Math),Id(int),[CallExpr(Id(System),Id(input),[StringLit(Enter D: )])])),VarDecl(Id(Q),IntType,CallExpr(Id(Math),Id(int),[BinaryOp(/,BinaryOp(*,BinaryOp(*,IntLit(2),Id(c)),Id(d)),Id(h))])),Call(Id(Out),Id(println),[CallExpr(Id(Math),Id(round),[CallExpr(Id(Math),Id(sqrt),[CallExpr(Id(Math),Id(abs),[CallExpr(Id(Math),Id(log),[Id(Q)])])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_AST56(self):
        input = """
        Class Program{
            func(){
               Return Self.a.a.a.a.a.a.a.a.a.a;
            }
        }
        """ 
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(func),Instance,[],Block([Return(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Self(),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)),Id(a)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 356))


    def test_AST57(self):
        input = """
        Class Program{
            func(){
                If(True){
                    If(True){
                        If(True){
                            If(True){
                                If(True){
                                    If(True){

                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

    """ 
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(func),Instance,[],Block([If(BooleanLit(True),Block([If(BooleanLit(True),Block([If(BooleanLit(True),Block([If(BooleanLit(True),Block([If(BooleanLit(True),Block([If(BooleanLit(True),Block([]))]))]))]))]))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 357))


    def test_AST58(self):
        input = """
            Class Shape {
                Var b: Array[Float,0123];
                Var a : Int = array[1][2][3][4][4+1][4-2][4-2][4*3][2/1][2%1];
            }
        """ 
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(b),ArrayType(83,FloatType))),AttributeDecl(Instance,VarDecl(Id(a),IntType,ArrayCell(Id(array),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),BinaryOp(+,IntLit(4),IntLit(1)),BinaryOp(-,IntLit(4),IntLit(2)),BinaryOp(-,IntLit(4),IntLit(2)),BinaryOp(*,IntLit(4),IntLit(3)),BinaryOp(/,IntLit(2),IntLit(1)),BinaryOp(%,IntLit(2),IntLit(1))])))])])"
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_AST59(self):
        input = """
            Class Shape {
                getShape() {
                    Foreach (i In 1 .. 10 By 0.5) {
                        Var v : Int = 6+8-9;
                    }

                    If (s ==. "narutobaco" ){
                        Var d,c: Float = 6.3e45, .e45;
                    }
                    
                }
            }
    """ 
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(getShape),Instance,[],Block([For(Id(i),IntLit(1),IntLit(10),FloatLit(0.5),Block([VarDecl(Id(v),IntType,BinaryOp(-,BinaryOp(+,IntLit(6),IntLit(8)),IntLit(9)))])]),If(BinaryOp(==.,Id(s),StringLit(narutobaco)),Block([VarDecl(Id(d),FloatType,FloatLit(6.3e+45)),VarDecl(Id(c),FloatType,FloatLit(0.0))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_AST60(self):
        input = """
        Class Program{
            myFunc(_1 , _2 : Int; _1___az_11, _122_2333, _aaaz_123__ : String ; _AA_b_z_, CCcA_aa : Float){
                ## Do sth ## 
                ## Do sth else ##
            }
            main(){
                Var a : Int = 0b1011; 
            }
        }
    """ 
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(myFunc),Instance,[param(Id(_1),IntType),param(Id(_2),IntType),param(Id(_1___az_11),StringType),param(Id(_122_2333),StringType),param(Id(_aaaz_123__),StringType),param(Id(_AA_b_z_),FloatType),param(Id(CCcA_aa),FloatType)],Block([])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(11))]))])])"
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_AST61(self):
        input = """ 
        Class Base{
            print(){
                Return "This is base class";
            }
        }

        Class Subclass : Base{
            print(){
                Return "This is sub class";
            }
        }

        Class Subsubclass : Subclass{
            print(){
                Return "This is sub sub class";
            }
        }
        """ 
        expect = "Program([ClassDecl(Id(Base),[MethodDecl(Id(print),Instance,[],Block([Return(StringLit(This is base class))]))]),ClassDecl(Id(Subclass),Id(Base),[MethodDecl(Id(print),Instance,[],Block([Return(StringLit(This is sub class))]))]),ClassDecl(Id(Subsubclass),Id(Subclass),[MethodDecl(Id(print),Instance,[],Block([Return(StringLit(This is sub sub class))]))])])"
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_AST62(self):
        input = """
            Class Program{
                main(){
                    Var a : Array[Int,4] = Array(1,2,3,4);
                    Out.println(a[a[a[a[a[a[a[a[a[a[a[i]]]]]]]]]]]);
                }
            }
        """ 
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(4,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]),Call(Id(Out),Id(println),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[ArrayCell(Id(a),[Id(i)])])])])])])])])])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_AST63(self):
        input = """

        Class Program{
            Greeting(a : String){
                Var newString : String = ("Hello " +. a) +. " Welcome to Gulag :D";
                Out.println(newString);
            }
            main(){
                Var a : String = "Player1";
                Self.Greeting(a);
                Return;
            }
        }
        """ 
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Greeting),Instance,[param(Id(a),StringType)],Block([VarDecl(Id(newString),StringType,BinaryOp(+.,BinaryOp(+.,StringLit(Hello ),Id(a)),StringLit( Welcome to Gulag :D))),Call(Id(Out),Id(println),[Id(newString)])])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),StringType,StringLit(Player1)),Call(Self(),Id(Greeting),[Id(a)]),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_AST64(self):
        input = """
        Class Program{
            Swap(a,b : Int){
                Var c : Int = a; 
                a = b;
                b = c; 
            }
            main(){
                Var a,b : Int = 10,23; 
                Self.Swap(a,b); 
                Out.println(a);
                Out.println(b);
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Swap),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([VarDecl(Id(c),IntType,Id(a)),AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),Id(c))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(10)),VarDecl(Id(b),IntType,IntLit(23)),Call(Self(),Id(Swap),[Id(a),Id(b)]),Call(Id(Out),Id(println),[Id(a)]),Call(Id(Out),Id(println),[Id(b)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_AST65(self):
        input = """
        Class Program
        {
            main(){
                Val myArray: Array[String, 5] = Array("No","clue","what","im","doing");
                Val sum: String = "";
                Foreach (i In 1 .. 5){
                    sum = sum +. myArray[i];
                }
                Out.println(sum);
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(myArray),ArrayType(5,StringType),[StringLit(No),StringLit(clue),StringLit(what),StringLit(im),StringLit(doing)]),ConstDecl(Id(sum),StringType,StringLit()),For(Id(i),IntLit(1),IntLit(5),IntLit(1),Block([AssignStmt(Id(sum),BinaryOp(+.,Id(sum),ArrayCell(Id(myArray),[Id(i)])))])]),Call(Id(Out),Id(println),[Id(sum)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_AST66(self):
        input = """Class Pirate {
            Gold(ratings: Array[Int, 10]) {
                Var n, res: Int = rating.size(), 0;
                Var count: Array[Int, 0123567];
                Foreach(i In 0 .. n) {
                    count[i] = (1+2)*3 + 4 * 5 / 6;
                }
                Foreach(i In 1 .. n){
                    If (ratings[i] > ratings[i-1]) {
                        count[i] = count[i-1] + 1;
                    }
                }
                Foreach(i In n-2 + 3 /2 *4  .. 0 By -1) {
                    If ((ratings[i] > ratings[(i+1)]) && (count[i] <= count[(i+1)])) {
                        count[i] = count[(i+1)] + 1;
                    }
                }
                Foreach(i In 0 .. n) {
                    result = result + count[i];
                }
                Return result*result;
            }
        }"""
        expect = "Program([ClassDecl(Id(Pirate),[MethodDecl(Id(Gold),Instance,[param(Id(ratings),ArrayType(10,IntType))],Block([VarDecl(Id(n),IntType,CallExpr(Id(rating),Id(size),[])),VarDecl(Id(res),IntType,IntLit(0)),VarDecl(Id(count),ArrayType(42871,IntType)),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([AssignStmt(ArrayCell(Id(count),[Id(i)]),BinaryOp(+,BinaryOp(*,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(/,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6))))])]),For(Id(i),IntLit(1),Id(n),IntLit(1),Block([If(BinaryOp(>,ArrayCell(Id(ratings),[Id(i)]),ArrayCell(Id(ratings),[BinaryOp(-,Id(i),IntLit(1))])),Block([AssignStmt(ArrayCell(Id(count),[Id(i)]),BinaryOp(+,ArrayCell(Id(count),[BinaryOp(-,Id(i),IntLit(1))]),IntLit(1)))]))])]),For(Id(i),BinaryOp(+,BinaryOp(-,Id(n),IntLit(2)),BinaryOp(*,BinaryOp(/,IntLit(3),IntLit(2)),IntLit(4))),IntLit(0),UnaryOp(-,IntLit(1)),Block([If(BinaryOp(&&,BinaryOp(>,ArrayCell(Id(ratings),[Id(i)]),ArrayCell(Id(ratings),[BinaryOp(+,Id(i),IntLit(1))])),BinaryOp(<=,ArrayCell(Id(count),[Id(i)]),ArrayCell(Id(count),[BinaryOp(+,Id(i),IntLit(1))]))),Block([AssignStmt(ArrayCell(Id(count),[Id(i)]),BinaryOp(+,ArrayCell(Id(count),[BinaryOp(+,Id(i),IntLit(1))]),IntLit(1)))]))])]),For(Id(i),IntLit(0),Id(n),IntLit(1),Block([AssignStmt(Id(result),BinaryOp(+,Id(result),ArrayCell(Id(count),[Id(i)])))])]),Return(BinaryOp(*,Id(result),Id(result)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_AST67(self):
        input = """Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;

            $getNumOfShape() {
                Return Shape::$numOfShape;
            }
        }
        Class Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(FieldAccess(Id(Shape),Id($numOfShape)))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_AST68(self):
        input = '''
        Class Shape{
            func_tion(){
               A[b[c[d[e[f::$g]]]]][h::$i][j.k()][F::$DDD()]=0;
            }
        }   
        '''
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(func_tion),Instance,[],Block([AssignStmt(ArrayCell(Id(A),[ArrayCell(Id(b),[ArrayCell(Id(c),[ArrayCell(Id(d),[ArrayCell(Id(e),[FieldAccess(Id(f),Id($g))])])])]),FieldAccess(Id(h),Id($i)),CallExpr(Id(j),Id(k),[]),CallExpr(Id(F),Id($DDD),[])]),IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 368))

     
    def test_AST69(self):
        input = """
        Class Program
        {
            main(){
                Var a : Array[Array[Array[Int,5],3],2] = Array(
                    Array(
                        Array(1,2,3,4,5), 
                        Array(1,2,4,5,6),
                        Array(3,6,7,8,9)
                    ),
                    Array(
                        Array(1,2,3,4,5), 
                        Array(1,2,4,5,6),
                        Array(3,6,7,8,9)
                    )
                );
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(2,ArrayType(3,ArrayType(5,IntType))),[[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)],[IntLit(1),IntLit(2),IntLit(4),IntLit(5),IntLit(6)],[IntLit(3),IntLit(6),IntLit(7),IntLit(8),IntLit(9)]],[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)],[IntLit(1),IntLit(2),IntLit(4),IntLit(5),IntLit(6)],[IntLit(3),IntLit(6),IntLit(7),IntLit(8),IntLit(9)]]])]))])])"
        self.assertTrue(TestAST.test(input, expect,369))

    
 
    def test_AST70(self):
        input = """
        Class Rectangle : Shape{
            Var $count : Int = 0;
            Var width : Float;
            Val length : Float;

            Constructor(a,b : Float){
                Self.width = a; 
                Self.length = b;
                Rectangle::$count = Rectangle::$count + 1;
            }

            getArea(){
                Return Self.width * Self.length; 
            }
            
            Destructor(){
                ## Might do something here ##
            }
            
        }

        Class Program{
            main(){
                Var a : Float = 12.5; 
                Var b : Float = 23.101;
                Var rect: Rectangle = New Rectangle(a,b);
                Out.Println(rect.getArea());
                Out.println("The current number of rectange is :");
                Out.println(Rectangle::$count);
            }
            
        }
        """
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[AttributeDecl(Static,VarDecl(Id($count),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),AttributeDecl(Instance,ConstDecl(Id(length),FloatType,None)),MethodDecl(Id(Constructor),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(width)),Id(a)),AssignStmt(FieldAccess(Self(),Id(length)),Id(b)),AssignStmt(FieldAccess(Id(Rectangle),Id($count)),BinaryOp(+,FieldAccess(Id(Rectangle),Id($count)),IntLit(1)))])),MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(width)),FieldAccess(Self(),Id(length))))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),FloatType,FloatLit(12.5)),VarDecl(Id(b),FloatType,FloatLit(23.101)),VarDecl(Id(rect),ClassType(Id(Rectangle)),NewExpr(Id(Rectangle),[Id(a),Id(b)])),Call(Id(Out),Id(Println),[CallExpr(Id(rect),Id(getArea),[])]),Call(Id(Out),Id(println),[StringLit(The current number of rectange is :)]),Call(Id(Out),Id(println),[FieldAccess(Id(Rectangle),Id($count))])]))])])"
        self.assertTrue(TestAST.test(input, expect,370))

    
 
    def test_AST71(self):
        input = """
        Class myProgram {
            Val a, b, c : Int = 10 + 10 , 22*33 , 100/2;
            Val length, width : Float = (25.2 + 3.0 )/4.2 , 22.3 + 33.1 * 4 / 2e10 ; 
            Var $x, $y : Int = 0, 0;
        }
        """
        expect = "Program([ClassDecl(Id(myProgram),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(10),IntLit(10)))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,BinaryOp(*,IntLit(22),IntLit(33)))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(/,IntLit(100),IntLit(2)))),AttributeDecl(Instance,ConstDecl(Id(length),FloatType,BinaryOp(/,BinaryOp(+,FloatLit(25.2),FloatLit(3.0)),FloatLit(4.2)))),AttributeDecl(Instance,ConstDecl(Id(width),FloatType,BinaryOp(+,FloatLit(22.3),BinaryOp(/,BinaryOp(*,FloatLit(33.1),IntLit(4)),FloatLit(20000000000.0))))),AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(0)))])])"
        self.assertTrue(TestAST.test(input, expect,371))

    
 
    def test_AST72(self):
        input = """
        Class Program{
            Swap(a,b : Int){
                Var c : Int = a; 
                a = b;
                b = c; 
            }
            Sort(a : Array[Int,4]){
                Foreach (i In 1 .. 4 By 1){
                    Foreach(j In 1 .. 4 - i By 1){
                        If(a[j] > a[j+1]){
                            Self.Swap(a[j], a[j+1]);
                        }
                    } 
                }
            }

            main(){
                Var a : Array[Int,4] = Array(1,2,3,4); 
                Self.Sort(a);
                Foreach (i In 1 .. 4 By 1){
                    Out.println(a[i]); 
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Swap),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([VarDecl(Id(c),IntType,Id(a)),AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),Id(c))])),MethodDecl(Id(Sort),Instance,[param(Id(a),ArrayType(4,IntType))],Block([For(Id(i),IntLit(1),IntLit(4),IntLit(1),Block([For(Id(j),IntLit(1),BinaryOp(-,IntLit(4),Id(i)),IntLit(1),Block([If(BinaryOp(>,ArrayCell(Id(a),[Id(j)]),ArrayCell(Id(a),[BinaryOp(+,Id(j),IntLit(1))])),Block([Call(Self(),Id(Swap),[ArrayCell(Id(a),[Id(j)]),ArrayCell(Id(a),[BinaryOp(+,Id(j),IntLit(1))])])]))])])])])])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(4,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]),Call(Self(),Id(Sort),[Id(a)]),For(Id(i),IntLit(1),IntLit(4),IntLit(1),Block([Call(Id(Out),Id(println),[ArrayCell(Id(a),[Id(i)])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect,372))

    
 
    def test_AST73(self):
        input = """
        Class Program
        {
            fibonacci(myNum:Int){
                If((myNum == 0) || (myNum == 1)){
                        Return 1;
                }
                Else{
                    Return Self.fibonacci(myNum - 1) + Self.fibonacci(myNum - 1);
                }
            }
            main (){
                Val my_num : Int = 10;
                Var ans : Int = Self.fibonacci(my_num);
                Out.println(ans);
            }
        }""" 
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(fibonacci),Instance,[param(Id(myNum),IntType)],Block([If(BinaryOp(||,BinaryOp(==,Id(myNum),IntLit(0)),BinaryOp(==,Id(myNum),IntLit(1))),Block([Return(IntLit(1))]),Block([Return(BinaryOp(+,CallExpr(Self(),Id(fibonacci),[BinaryOp(-,Id(myNum),IntLit(1))]),CallExpr(Self(),Id(fibonacci),[BinaryOp(-,Id(myNum),IntLit(1))])))]))])),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(my_num),IntType,IntLit(10)),VarDecl(Id(ans),IntType,CallExpr(Self(),Id(fibonacci),[Id(my_num)])),Call(Id(Out),Id(println),[Id(ans)])]))])])"
        self.assertTrue(TestAST.test(input, expect,373))

    
 
    def test_AST74(self):
        input = """
        Class Program {
            main() {
                Var a : Int = 100; 
                If(a > 0){
                    ## do sth ##
                    a = a + 2; 
                    If(a > 3){
                        a = a * 2; 
                        a = a / 2 + 1;
                    }
                    Else{
                        If(True){
                            If(True){
                                ## do sth ##
                            }
                            Else{

                            }
                        }
                        Else{

                        }
                    }
                }
                Else{
                    If(False || False && True){
                        a = a * 2;
                    }
                    Else{
                        If(a > 0){
                            a = a * 3 / 3;
                        }
                        Else{
                            a = a - 1 - 2 -3; 
                        }
                    }

                }
                Out.println(a);
            }
        }

        """ 
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(100)),If(BinaryOp(>,Id(a),IntLit(0)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(2))),If(BinaryOp(>,Id(a),IntLit(3)),Block([AssignStmt(Id(a),BinaryOp(*,Id(a),IntLit(2))),AssignStmt(Id(a),BinaryOp(+,BinaryOp(/,Id(a),IntLit(2)),IntLit(1)))]),Block([If(BooleanLit(True),Block([If(BooleanLit(True),Block([]),Block([]))]),Block([]))]))]),Block([If(BinaryOp(&&,BinaryOp(||,BooleanLit(False),BooleanLit(False)),BooleanLit(True)),Block([AssignStmt(Id(a),BinaryOp(*,Id(a),IntLit(2)))]),Block([If(BinaryOp(>,Id(a),IntLit(0)),Block([AssignStmt(Id(a),BinaryOp(/,BinaryOp(*,Id(a),IntLit(3)),IntLit(3)))]),Block([AssignStmt(Id(a),BinaryOp(-,BinaryOp(-,BinaryOp(-,Id(a),IntLit(1)),IntLit(2)),IntLit(3)))]))]))])),Call(Id(Out),Id(println),[Id(a)])]))])])"
        self.assertTrue(TestAST.test(input, expect,374))

    
 
    def test_AST75(self):
        input = """
        Class Shape{
            Var a : Float;
            Var b : Float;
            Var $count : Int = 0; 
            Constructor(a,b : Float){
                Self.a = a; 
                Self.b = b; 
                Shape::$count = Shape::$count + 1; 
            }
            $getCount(){
                Return Shape::$count;
            }
            getArea(){
                Return Self.a * Self.b;
            }
        }

        Class Program {
            main() {
                Var a : Shape = New Shape(2.0, 3.0);
                Var b : Shape = New Shape(12.45 , 13.e10);
                Var c : Shape = New Shape(.e10 , 12e0);
                Var list : Array[Int, 3] = Array(a,b,c);
                Foreach(i In 1 .. 3){
                    Var clone : Shape = list[i];
                    Out.println(clone.getArea());
                }
            }
        }
        """ 
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),FloatType)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Static,VarDecl(Id($count),IntType,IntLit(0))),MethodDecl(Id(Constructor),Instance,[param(Id(a),FloatType),param(Id(b),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(a)),Id(a)),AssignStmt(FieldAccess(Self(),Id(b)),Id(b)),AssignStmt(FieldAccess(Id(Shape),Id($count)),BinaryOp(+,FieldAccess(Id(Shape),Id($count)),IntLit(1)))])),MethodDecl(Id($getCount),Static,[],Block([Return(FieldAccess(Id(Shape),Id($count)))])),MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(a)),FieldAccess(Self(),Id(b))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ClassType(Id(Shape)),NewExpr(Id(Shape),[FloatLit(2.0),FloatLit(3.0)])),VarDecl(Id(b),ClassType(Id(Shape)),NewExpr(Id(Shape),[FloatLit(12.45),FloatLit(130000000000.0)])),VarDecl(Id(c),ClassType(Id(Shape)),NewExpr(Id(Shape),[FloatLit(0.0),FloatLit(12.0)])),VarDecl(Id(list),ArrayType(3,IntType),[Id(a),Id(b),Id(c)]),For(Id(i),IntLit(1),IntLit(3),IntLit(1),Block([VarDecl(Id(clone),ClassType(Id(Shape)),ArrayCell(Id(list),[Id(i)])),Call(Id(Out),Id(println),[CallExpr(Id(clone),Id(getArea),[])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect,375))

    
 
    def test_AST76(self):
        input = """
        Class Rational{
            Var a : Int;
            Var b : Int;
            Var g : Int;
            Var $count : Int = 0; 
            Constructor(a,b : Int){
                Self.g = Rational::$getGCD(a,b);
                Self.a = Self.a / Self.g;
                Self.b = Self.b / Self.g; 
                Rational::$count = Rational::$count + 1; 
            }
            $getCount(){
                Return Rational::$count;
            }
            $getGCD(a,b : Int){
                If(b == 0){
                    Return a; 
                }
                Else{
                    Return Rational::$getGCD(b,a % b);
                }
            }
        }

        Class Program {
            main() {
               Var num1 : Rational = New Rational(2,3); 
               Var num2 : Rational = New Rational(10,12); 
            }
        }
        """ 
        expect = "Program([ClassDecl(Id(Rational),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(g),IntType)),AttributeDecl(Static,VarDecl(Id($count),IntType,IntLit(0))),MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(g)),CallExpr(Id(Rational),Id($getGCD),[Id(a),Id(b)])),AssignStmt(FieldAccess(Self(),Id(a)),BinaryOp(/,FieldAccess(Self(),Id(a)),FieldAccess(Self(),Id(g)))),AssignStmt(FieldAccess(Self(),Id(b)),BinaryOp(/,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(g)))),AssignStmt(FieldAccess(Id(Rational),Id($count)),BinaryOp(+,FieldAccess(Id(Rational),Id($count)),IntLit(1)))])),MethodDecl(Id($getCount),Static,[],Block([Return(FieldAccess(Id(Rational),Id($count)))])),MethodDecl(Id($getGCD),Static,[param(Id(a),IntType),param(Id(b),IntType)],Block([If(BinaryOp(==,Id(b),IntLit(0)),Block([Return(Id(a))]),Block([Return(CallExpr(Id(Rational),Id($getGCD),[Id(b),BinaryOp(%,Id(a),Id(b))]))]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(num1),ClassType(Id(Rational)),NewExpr(Id(Rational),[IntLit(2),IntLit(3)])),VarDecl(Id(num2),ClassType(Id(Rational)),NewExpr(Id(Rational),[IntLit(10),IntLit(12)]))]))])])"
        self.assertTrue(TestAST.test(input, expect,376))

    
 
    def test_AST77(self):
        input = """
        Class Rational{
            Var a : Int;
            Var b : Int;
            Var g : Int;
            Var $count : Int = 0; 
            Constructor(a,b : Int){
                Self.g = Rational::$getGCD(a,b);
                Self.a = Self.a / Self.g;
                Self.b = Self.b / Self.g; 
                Rational::$count = Rational::$count + 1; 
            }
            $getCount(){
                Return Rational::$count;
            }
            $getGCD(a,b : Int){
                If(b == 0){
                    Return a; 
                }
                Else{
                    Return Rational::$getGCD(b,a % b);
                }
            }

            $multiply(num1,num2 : Rational){
                Return New Rational(num1.a * num2.a , num1.b * num2.b); 
            }
        }

        Class Program {
            main() {
               Var num1 : Rational = New Rational(2,3); 
               Var num2 : Rational = New Rational(10,12);
               Var num3 : Rational = Rational::$multiply(num1,num2); 
            }
        }
        """ 
        expect = "Program([ClassDecl(Id(Rational),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(g),IntType)),AttributeDecl(Static,VarDecl(Id($count),IntType,IntLit(0))),MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(g)),CallExpr(Id(Rational),Id($getGCD),[Id(a),Id(b)])),AssignStmt(FieldAccess(Self(),Id(a)),BinaryOp(/,FieldAccess(Self(),Id(a)),FieldAccess(Self(),Id(g)))),AssignStmt(FieldAccess(Self(),Id(b)),BinaryOp(/,FieldAccess(Self(),Id(b)),FieldAccess(Self(),Id(g)))),AssignStmt(FieldAccess(Id(Rational),Id($count)),BinaryOp(+,FieldAccess(Id(Rational),Id($count)),IntLit(1)))])),MethodDecl(Id($getCount),Static,[],Block([Return(FieldAccess(Id(Rational),Id($count)))])),MethodDecl(Id($getGCD),Static,[param(Id(a),IntType),param(Id(b),IntType)],Block([If(BinaryOp(==,Id(b),IntLit(0)),Block([Return(Id(a))]),Block([Return(CallExpr(Id(Rational),Id($getGCD),[Id(b),BinaryOp(%,Id(a),Id(b))]))]))])),MethodDecl(Id($multiply),Static,[param(Id(num1),ClassType(Id(Rational))),param(Id(num2),ClassType(Id(Rational)))],Block([Return(NewExpr(Id(Rational),[BinaryOp(*,FieldAccess(Id(num1),Id(a)),FieldAccess(Id(num2),Id(a))),BinaryOp(*,FieldAccess(Id(num1),Id(b)),FieldAccess(Id(num2),Id(b)))]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(num1),ClassType(Id(Rational)),NewExpr(Id(Rational),[IntLit(2),IntLit(3)])),VarDecl(Id(num2),ClassType(Id(Rational)),NewExpr(Id(Rational),[IntLit(10),IntLit(12)])),VarDecl(Id(num3),ClassType(Id(Rational)),CallExpr(Id(Rational),Id($multiply),[Id(num1),Id(num2)]))]))])])"
        self.assertTrue(TestAST.test(input, expect,377))

    
 
    def test_AST78(self):
        input = """
        Class Program{
            main(){
               Var a : Int = 100;
               Var b : Boolean = False;
               

               Foreach(i In 1 .. a By 1){
                   If(a % i == 0){
                       b = True; 
                       Break;
                       
                   }
               }
               If(b == True){
                    Out.println("a is not Prime number");
               }
               Else{
                    Out.println("a is Prime number");
               }
            }
        }
        """ 
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(100)),VarDecl(Id(b),BoolType,BooleanLit(False)),For(Id(i),IntLit(1),Id(a),IntLit(1),Block([If(BinaryOp(==,BinaryOp(%,Id(a),Id(i)),IntLit(0)),Block([AssignStmt(Id(b),BooleanLit(True)),Break]))])]),If(BinaryOp(==,Id(b),BooleanLit(True)),Block([Call(Id(Out),Id(println),[StringLit(a is not Prime number)])]),Block([Call(Id(Out),Id(println),[StringLit(a is Prime number)])]))]))])])"
        self.assertTrue(TestAST.test(input, expect,378))

    
 
    def test_AST79(self):
        input = """
            Class Program{
                Func(a : Array[Array[Int,3],3]){
                    Foreach( i In 1 .. 3 By 1){
                        Foreach (j In 1 ..3 By 1){
                            Foreach( z In 1 .. 3 By 1){
                                a[i][j][z] = a[i][j][z] + 1 * 2 /3 * 4 / 5 % 6;
                            }
                        }
                    } 
                }
                main(){
                    Var a : Array[Array[Array[Int,3],3],3] = Array(
                        Array(
                            Array(1,2,3), 
                            Array(4,5,6),
                            Array(7,8,9)
                        ),
                        Array(
                            Array(1,2,3), 
                            Array(4,5,6),
                            Array(7,8,9)
                        ),
                        Array(
                            Array(1,2,3), 
                            Array(4,5,6),
                            Array(7,8,9)
                        )
                    );

                    Foreach( i In 1 .. 3 By 1){
                        Foreach (j In 1 .. 3 By 1){
                            Foreach (z In 1 .. 3 By 1 ){
                                Out.println(a[i][j][z]);
                            }
                        }
                    }
                }
            }
        """ 
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Func),Instance,[param(Id(a),ArrayType(3,ArrayType(3,IntType)))],Block([For(Id(i),IntLit(1),IntLit(3),IntLit(1),Block([For(Id(j),IntLit(1),IntLit(3),IntLit(1),Block([For(Id(z),IntLit(1),IntLit(3),IntLit(1),Block([AssignStmt(ArrayCell(Id(a),[Id(i),Id(j),Id(z)]),BinaryOp(+,ArrayCell(Id(a),[Id(i),Id(j),Id(z)]),BinaryOp(%,BinaryOp(/,BinaryOp(*,BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(6))))])])])])])])])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(3,ArrayType(3,ArrayType(3,IntType))),[[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4),IntLit(5),IntLit(6)],[IntLit(7),IntLit(8),IntLit(9)]],[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4),IntLit(5),IntLit(6)],[IntLit(7),IntLit(8),IntLit(9)]],[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(4),IntLit(5),IntLit(6)],[IntLit(7),IntLit(8),IntLit(9)]]]),For(Id(i),IntLit(1),IntLit(3),IntLit(1),Block([For(Id(j),IntLit(1),IntLit(3),IntLit(1),Block([For(Id(z),IntLit(1),IntLit(3),IntLit(1),Block([Call(Id(Out),Id(println),[ArrayCell(Id(a),[Id(i),Id(j),Id(z)])])])])])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect,379))

    
 
    def test_AST80(self):
        input = """
        Class Program{
            main(){
                Val my_array: Array[Int, 6] = Array(1,2,3,4,5,6);
                Var my_sum_odd : Int = 0;
                Var my_sum_even: Int = 0;
                Foreach (my_index In 1 .. 8){
                    If(my_array[my_index] % 2 == 0){
                        my_sum_even  = my_sum_even + my_array[my_index];
                    }
                    Else{
                        my_sum_odd  = my_sum_odd + my_array[my_index];
                    }
                }
                If (my_sum_even > my_sum_odd){
                    Out.println("even > odd");
                }
                Else{
                    Out.println("odd > even");
                }
            }
        }""" 
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(my_array),ArrayType(6,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5),IntLit(6)]),VarDecl(Id(my_sum_odd),IntType,IntLit(0)),VarDecl(Id(my_sum_even),IntType,IntLit(0)),For(Id(my_index),IntLit(1),IntLit(8),IntLit(1),Block([If(BinaryOp(==,BinaryOp(%,ArrayCell(Id(my_array),[Id(my_index)]),IntLit(2)),IntLit(0)),Block([AssignStmt(Id(my_sum_even),BinaryOp(+,Id(my_sum_even),ArrayCell(Id(my_array),[Id(my_index)])))]),Block([AssignStmt(Id(my_sum_odd),BinaryOp(+,Id(my_sum_odd),ArrayCell(Id(my_array),[Id(my_index)])))]))])]),If(BinaryOp(>,Id(my_sum_even),Id(my_sum_odd)),Block([Call(Id(Out),Id(println),[StringLit(even > odd)])]),Block([Call(Id(Out),Id(println),[StringLit(odd > even)])]))]))])])"
        self.assertTrue(TestAST.test(input, expect,380))

    
 
    def test_AST81(self):
        input = """
        Class Base {
            Var $numOfObjs: Int = 0;
            Constructor() {
                Base::$numOfObjs = BaseClass::$numOfObjs + 1;
            }
            $staticMethod() {
                Out.printLn(Program.gcd(123_456,46*75%3));
            }

            Destructor() {
                Base::$numOfObjs = Base::$numOfObjs - 1;
                Out.printLn("Can\'t do this forever");
            }
        }
        Class DerivedClass : Base{
            DerivedClass(){
                ## Do sth##
            }
        }
    """ 
        expect = "Program([ClassDecl(Id(Base),[AttributeDecl(Static,VarDecl(Id($numOfObjs),IntType,IntLit(0))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Base),Id($numOfObjs)),BinaryOp(+,FieldAccess(Id(BaseClass),Id($numOfObjs)),IntLit(1)))])),MethodDecl(Id($staticMethod),Static,[],Block([Call(Id(Out),Id(printLn),[CallExpr(Id(Program),Id(gcd),[IntLit(123456),BinaryOp(%,BinaryOp(*,IntLit(46),IntLit(75)),IntLit(3))])])])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Base),Id($numOfObjs)),BinaryOp(-,FieldAccess(Id(Base),Id($numOfObjs)),IntLit(1))),Call(Id(Out),Id(printLn),[StringLit(Can't do this forever)])]))]),ClassDecl(Id(DerivedClass),Id(Base),[MethodDecl(Id(DerivedClass),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect,381))

    
 
    def test_AST82(self):
        input = """
        Class Program{
            addNewNode(newNode,head: Int){
                newNode.next_node = head;
                head = new_node;
            }
            deleteNode(position,head: Int){
                If(head == 0){
                    head = head.next_node;
                }
                Else{
                    Var curr: Int = head.next.next;
                    Var prev: Int = curr;
                    Foreach(i In 2 .. position)
                    {
                        prev = curr;
                        curr = curr.next_node;
                    }
                    prev.next = curr;
                    head = prev;
                }

            }
        }
    """ 
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(addNewNode),Instance,[param(Id(newNode),IntType),param(Id(head),IntType)],Block([AssignStmt(FieldAccess(Id(newNode),Id(next_node)),Id(head)),AssignStmt(Id(head),Id(new_node))])),MethodDecl(Id(deleteNode),Instance,[param(Id(position),IntType),param(Id(head),IntType)],Block([If(BinaryOp(==,Id(head),IntLit(0)),Block([AssignStmt(Id(head),FieldAccess(Id(head),Id(next_node)))]),Block([VarDecl(Id(curr),IntType,FieldAccess(FieldAccess(Id(head),Id(next)),Id(next))),VarDecl(Id(prev),IntType,Id(curr)),For(Id(i),IntLit(2),Id(position),IntLit(1),Block([AssignStmt(Id(prev),Id(curr)),AssignStmt(Id(curr),FieldAccess(Id(curr),Id(next_node)))])]),AssignStmt(FieldAccess(Id(prev),Id(next)),Id(curr)),AssignStmt(Id(head),Id(prev))]))]))])])"
        self.assertTrue(TestAST.test(input, expect,382))

    
 
    def test_AST83(self):
        input = """
        Class People{
            Var $count : Int; 
            Var name : String; 
            Var gender : String; 
            Var phone : String; 
            Constructor(name,gender,phone : String){
                Self.name = name; 
                Self.gender = gender; 
                Self.phone = phone; 
            }
            Constructor(){
                Self.name = "Unknown";
                Self.gender = "Unknown";
                Self.phone = "Unknown"; 
            }
            getCount(){
                Return People::$count;
            }

            $getStacticCount(){
                Return People::$count;
            }
            Destructor(){

            }
        }

        Class Employee: People{
            Var salary : Float; 
            Constructor(name,gender,phone : String ; salary : Float){
                Self.name = name; 
                Self.gender = gender; 
                Self.phone = phone; 
                Self.salary = salary;
            }

            GetSalary(){
                Return Self.salary ;
            }
        }

        Class CEO : People{
            Var salary : Float; 
            Var branchID : Int; 
            Constructor(name,gender,phone : String ; salary : Float ; branchID : Int){
                Self.name = name; 
                Self.gender = gender; 
                Self.phone = phone; 
                Self.salary = salary;
                Self.branchID = branchID;
            }

            GetSalary(){
                Return Self.salary + Self.salary * 1.5;
            }

            GetBranch(){
                Return Self.branchID; 
            }
        }

        Class Program{
            main(){
                Var a : Array[Int,5];
                Foreach(i In 1 .. 5 By 1){
                    a[i] = New Employee("Cao ba huy", "Gay" , "012345" , "999");
                }
                Out.println("The number of employees is", People::$getStacticCount());
            }
        }
        """
        expect = "Program([ClassDecl(Id(People),[AttributeDecl(Static,VarDecl(Id($count),IntType)),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(gender),StringType)),AttributeDecl(Instance,VarDecl(Id(phone),StringType)),MethodDecl(Id(Constructor),Instance,[param(Id(name),StringType),param(Id(gender),StringType),param(Id(phone),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(gender)),Id(gender)),AssignStmt(FieldAccess(Self(),Id(phone)),Id(phone))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(name)),StringLit(Unknown)),AssignStmt(FieldAccess(Self(),Id(gender)),StringLit(Unknown)),AssignStmt(FieldAccess(Self(),Id(phone)),StringLit(Unknown))])),MethodDecl(Id(getCount),Instance,[],Block([Return(FieldAccess(Id(People),Id($count)))])),MethodDecl(Id($getStacticCount),Static,[],Block([Return(FieldAccess(Id(People),Id($count)))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Employee),Id(People),[AttributeDecl(Instance,VarDecl(Id(salary),FloatType)),MethodDecl(Id(Constructor),Instance,[param(Id(name),StringType),param(Id(gender),StringType),param(Id(phone),StringType),param(Id(salary),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(gender)),Id(gender)),AssignStmt(FieldAccess(Self(),Id(phone)),Id(phone)),AssignStmt(FieldAccess(Self(),Id(salary)),Id(salary))])),MethodDecl(Id(GetSalary),Instance,[],Block([Return(FieldAccess(Self(),Id(salary)))]))]),ClassDecl(Id(CEO),Id(People),[AttributeDecl(Instance,VarDecl(Id(salary),FloatType)),AttributeDecl(Instance,VarDecl(Id(branchID),IntType)),MethodDecl(Id(Constructor),Instance,[param(Id(name),StringType),param(Id(gender),StringType),param(Id(phone),StringType),param(Id(salary),FloatType),param(Id(branchID),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(gender)),Id(gender)),AssignStmt(FieldAccess(Self(),Id(phone)),Id(phone)),AssignStmt(FieldAccess(Self(),Id(salary)),Id(salary)),AssignStmt(FieldAccess(Self(),Id(branchID)),Id(branchID))])),MethodDecl(Id(GetSalary),Instance,[],Block([Return(BinaryOp(+,FieldAccess(Self(),Id(salary)),BinaryOp(*,FieldAccess(Self(),Id(salary)),FloatLit(1.5))))])),MethodDecl(Id(GetBranch),Instance,[],Block([Return(FieldAccess(Self(),Id(branchID)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(5,IntType)),For(Id(i),IntLit(1),IntLit(5),IntLit(1),Block([AssignStmt(ArrayCell(Id(a),[Id(i)]),NewExpr(Id(Employee),[StringLit(Cao ba huy),StringLit(Gay),StringLit(012345),StringLit(999)]))])]),Call(Id(Out),Id(println),[StringLit(The number of employees is),CallExpr(Id(People),Id($getStacticCount),[])])]))])])"
        self.assertTrue(TestAST.test(input, expect,383))

    
 
    def test_AST84(self):
        input = """
        Class People{
            Var $count : Int; 
            Var name : String; 
            Var gender : String; 
            Var phone : String; 
            Constructor(name,gender,phone : String){
                Self.name = name; 
                Self.gender = gender; 
                Self.phone = phone; 
            }
            Constructor(){
                Self.name = "Unknown";
                Self.gender = "Unknown";
                Self.phone = "Unknown"; 
            }
            getCount(){
                Return People::$count;
            }

            $getStacticCount(){
                Return People::$count;
            }
            Destructor(){

            }
        }

        Class Employee: People{
            Var salary : Float; 
            Constructor(name,gender,phone : String ; salary : Float){
                Self.name = name; 
                Self.gender = gender; 
                Self.phone = phone; 
                Self.salary = salary;
            }

            GetSalary(){
                Return Self.salary ;
            }
        }

        Class CEO : People{
            Var salary : Float; 
            Var branchID : Int; 
            Constructor(name,gender,phone : String ; salary : Float ; branchID : Int){
                Self.name = name; 
                Self.gender = gender; 
                Self.phone = phone; 
                Self.salary = salary;
                Self.branchID = branchID;
            }

            GetSalary(){
                Return Self.salary + Self.salary * 1.5;
            }

            GetBranch(){
                Return Self.branchID; 
            }
        }

        Class Program{
            main(){
                Var a : Array[Int,5];
                Foreach(i In 1 .. 5 By 1){
                    a[i] = New Employee("Cao ba huy", "Gay" , "012345" , "999");
                }
                Out.println("The number of employees is", People::$getStacticCount());
            }
        }
        """
        expect = "Program([ClassDecl(Id(People),[AttributeDecl(Static,VarDecl(Id($count),IntType)),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(gender),StringType)),AttributeDecl(Instance,VarDecl(Id(phone),StringType)),MethodDecl(Id(Constructor),Instance,[param(Id(name),StringType),param(Id(gender),StringType),param(Id(phone),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(gender)),Id(gender)),AssignStmt(FieldAccess(Self(),Id(phone)),Id(phone))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(name)),StringLit(Unknown)),AssignStmt(FieldAccess(Self(),Id(gender)),StringLit(Unknown)),AssignStmt(FieldAccess(Self(),Id(phone)),StringLit(Unknown))])),MethodDecl(Id(getCount),Instance,[],Block([Return(FieldAccess(Id(People),Id($count)))])),MethodDecl(Id($getStacticCount),Static,[],Block([Return(FieldAccess(Id(People),Id($count)))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Employee),Id(People),[AttributeDecl(Instance,VarDecl(Id(salary),FloatType)),MethodDecl(Id(Constructor),Instance,[param(Id(name),StringType),param(Id(gender),StringType),param(Id(phone),StringType),param(Id(salary),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(gender)),Id(gender)),AssignStmt(FieldAccess(Self(),Id(phone)),Id(phone)),AssignStmt(FieldAccess(Self(),Id(salary)),Id(salary))])),MethodDecl(Id(GetSalary),Instance,[],Block([Return(FieldAccess(Self(),Id(salary)))]))]),ClassDecl(Id(CEO),Id(People),[AttributeDecl(Instance,VarDecl(Id(salary),FloatType)),AttributeDecl(Instance,VarDecl(Id(branchID),IntType)),MethodDecl(Id(Constructor),Instance,[param(Id(name),StringType),param(Id(gender),StringType),param(Id(phone),StringType),param(Id(salary),FloatType),param(Id(branchID),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(name)),Id(name)),AssignStmt(FieldAccess(Self(),Id(gender)),Id(gender)),AssignStmt(FieldAccess(Self(),Id(phone)),Id(phone)),AssignStmt(FieldAccess(Self(),Id(salary)),Id(salary)),AssignStmt(FieldAccess(Self(),Id(branchID)),Id(branchID))])),MethodDecl(Id(GetSalary),Instance,[],Block([Return(BinaryOp(+,FieldAccess(Self(),Id(salary)),BinaryOp(*,FieldAccess(Self(),Id(salary)),FloatLit(1.5))))])),MethodDecl(Id(GetBranch),Instance,[],Block([Return(FieldAccess(Self(),Id(branchID)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(5,IntType)),For(Id(i),IntLit(1),IntLit(5),IntLit(1),Block([AssignStmt(ArrayCell(Id(a),[Id(i)]),NewExpr(Id(Employee),[StringLit(Cao ba huy),StringLit(Gay),StringLit(012345),StringLit(999)]))])]),Call(Id(Out),Id(println),[StringLit(The number of employees is),CallExpr(Id(People),Id($getStacticCount),[])])]))])])"
        self.assertTrue(TestAST.test(input, expect,384))

    
 
    def test_AST85(self):
        input = """
        Class Program 
        {
            main()
            {
                Foreach (x In 1 .. 25 By x + 1) 
                {
                    If(("22" +. "22") ==. "2222")
                    {
                        Break;
                    }
                    Continue;
                }
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(x),IntLit(1),IntLit(25),BinaryOp(+,Id(x),IntLit(1)),Block([If(BinaryOp(==.,BinaryOp(+.,StringLit(22),StringLit(22)),StringLit(2222)),Block([Break])),Continue])])]))])])"""
        self.assertTrue(TestAST.test(input, expect,385))

    
 
    def test_AST86(self):
        input = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            Foreach(x In 1 .. 100 By 2){
                                If ( a == -1--1){
                                    Foreach(x In 1 .. 100 By 2){
                                    }
                                }
                            }
                        }
                    }
                }
                """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([For(Id(x),IntLit(1),IntLit(100),IntLit(2),Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([For(Id(x),IntLit(1),IntLit(100),IntLit(2),Block([])])]))])])]))]))])])"
        self.assertTrue(TestAST.test(input, expect,386))

    
 
    def test_AST87(self):
        input = """Class Program {
            Constructor() {
                Naruto::$ab().foo();
                Sasuke::$a.foo();
                Kokushibo::$a().foo();
                AKAZAA::$ab.foo();
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([Call(CallExpr(Id(Naruto),Id($ab),[]),Id(foo),[]),Call(FieldAccess(Id(Sasuke),Id($a)),Id(foo),[]),Call(CallExpr(Id(Kokushibo),Id($a),[]),Id(foo),[]),Call(FieldAccess(Id(AKAZAA),Id($ab)),Id(foo),[])]))])])"
        self.assertTrue(TestAST.test(input, expect,387))

    
 
    def test_AST88(self):
        input = """Class Program {
            main() {}
            main(w, h: Int) {}
        }
        Class ABC {
            main() {}
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(w),IntType),param(Id(h),IntType)],Block([]))]),ClassDecl(Id(ABC),[MethodDecl(Id(main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect,388))

    
 
    def test_AST89(self):
        input = """Class _Program {
            Var $A: Array[Array[String, 3], 3];
            $getMethodA() {
                Return _Program::$A;
            }
            $setMethodA(_a: Array[Array[String, 3], 3]) {
                _Program::$A = _a;
            }
        }
        Class Program {
            main() {
                Var arr: Array[Array[String, 3], 3] = Array(Array("Volvo", "22", "18"), Array("Saab", "5", "2"), Array("Land Rover", "17", "15"));
                _Program::$setMethodA(arr);
                Out.printLn(_Program::$getMethodA());
            }
        }"""
        expect = "Program([ClassDecl(Id(_Program),[AttributeDecl(Static,VarDecl(Id($A),ArrayType(3,ArrayType(3,StringType)))),MethodDecl(Id($getMethodA),Static,[],Block([Return(FieldAccess(Id(_Program),Id($A)))])),MethodDecl(Id($setMethodA),Static,[param(Id(_a),ArrayType(3,ArrayType(3,StringType)))],Block([AssignStmt(FieldAccess(Id(_Program),Id($A)),Id(_a))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(arr),ArrayType(3,ArrayType(3,StringType)),[[StringLit(Volvo),StringLit(22),StringLit(18)],[StringLit(Saab),StringLit(5),StringLit(2)],[StringLit(Land Rover),StringLit(17),StringLit(15)]]),Call(Id(_Program),Id($setMethodA),[Id(arr)]),Call(Id(Out),Id(printLn),[CallExpr(Id(_Program),Id($getMethodA),[])])]))])])"
        self.assertTrue(TestAST.test(input, expect,389))

    
 
    def test_AST90(self):
        input = '''
        Class Program {
            main() {
                (abc[123]).funct();
                a[123] = "1";
                Out.println(f.a[1]);
                ((((efh[32][1]).a[21]).funct()[0]).a[21]).funct();
                Return;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(Id(abc),[IntLit(123)]),Id(funct),[]),AssignStmt(ArrayCell(Id(a),[IntLit(123)]),StringLit(1)),Call(Id(Out),Id(println),[ArrayCell(FieldAccess(Id(f),Id(a)),[IntLit(1)])]),Call(ArrayCell(FieldAccess(ArrayCell(CallExpr(ArrayCell(FieldAccess(ArrayCell(Id(efh),[IntLit(32),IntLit(1)]),Id(a)),[IntLit(21)]),Id(funct),[]),[IntLit(0)]),Id(a)),[IntLit(21)]),Id(funct),[]),Return()]))])])'
        self.assertTrue(TestAST.test(input, expect,390))

    
 
    def test_AST91(self):
        input = """
        Class List {
            Val a : Array[Int,4] = Array(1,2,3,4);
            Var b : Array[Float,4] = Array(1.1 , 2.2e10 , 0.001 , .12e10);
            Val c : Array[Boolean,4] = Array(True, False , True , False );
            Var d : Array [String,4] = Array("huy", "cao" , "ba" , "ppl");
            Val e : Array[Int,4] = Array(1, 0b1010 , 0123, 0xFFFF);
        }
        """
        expect = "Program([ClassDecl(Id(List),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(4,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(4,FloatType),[FloatLit(1.1),FloatLit(22000000000.0),FloatLit(0.001),FloatLit(1200000000.0)])),AttributeDecl(Instance,ConstDecl(Id(c),ArrayType(4,BoolType),[BooleanLit(True),BooleanLit(False),BooleanLit(True),BooleanLit(False)])),AttributeDecl(Instance,VarDecl(Id(d),ArrayType(4,StringType),[StringLit(huy),StringLit(cao),StringLit(ba),StringLit(ppl)])),AttributeDecl(Instance,ConstDecl(Id(e),ArrayType(4,IntType),[IntLit(1),IntLit(10),IntLit(83),IntLit(65535)]))])])"
        self.assertTrue(TestAST.test(input, expect,391))

    
 
    def test_AST92(self):
        input = """
            Class ABCD{
                ___(){
                    Foreach (p In 1+1 .. 200+200 By b.foo(10+2*30,3+"str_"+.1+20)){}
                }
            }
        """
        expect = '''Program([ClassDecl(Id(ABCD),[MethodDecl(Id(___),Instance,[],Block([For(Id(p),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,IntLit(200),IntLit(200)),CallExpr(Id(b),Id(foo),[BinaryOp(+,IntLit(10),BinaryOp(*,IntLit(2),IntLit(30))),BinaryOp(+.,BinaryOp(+,IntLit(3),StringLit(str_)),BinaryOp(+,IntLit(1),IntLit(20)))]),Block([])])]))])])'''
        self.assertTrue(TestAST.test(input, expect,392))

    
 
    def test_AST93(self):
        input = """ 
        Class Program{
            main(){
                Foreach(i In 1 .. 10){
                    Foreach(j In 100 .. 1 By 2){
                        Foreach(z In 100 + 200 .. 500 * 600 + 100 - 200 By -20){
                            Out.print(a[i][j][z]);
                        }
                    }
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(1),IntLit(10),IntLit(1),Block([For(Id(j),IntLit(100),IntLit(1),IntLit(2),Block([For(Id(z),BinaryOp(+,IntLit(100),IntLit(200)),BinaryOp(-,BinaryOp(+,BinaryOp(*,IntLit(500),IntLit(600)),IntLit(100)),IntLit(200)),UnaryOp(-,IntLit(20)),Block([Call(Id(Out),Id(print),[ArrayCell(Id(a),[Id(i),Id(j),Id(z)])])])])])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect,393))

    
 
    def test_AST94(self):
        input = """
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Vehicle),[AttributeDecl(Instance,VarDecl(Id(running),BoolType,BooleanLit(True))),AttributeDecl(Instance,VarDecl(Id(speed),IntType)),AttributeDecl(Instance,VarDecl(Id(model_name),StringType)),AttributeDecl(Static,VarDecl(Id($numOfVehicle),IntType)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(speed)),IntLit(30))])),MethodDecl(Id(Constructor),Instance,[param(Id(speed),IntType),param(Id(model_name),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(speed)),Id(speed)),AssignStmt(FieldAccess(Self(),Id(model_name)),Id(model_name))])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(run),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(True))])),MethodDecl(Id(stop),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(False))]))])])"
        self.assertTrue(TestAST.test(input, expect,394))

    
 
    def test_AST95(self):
        input = """
        Class Program : A { ## Program is a subclass so main will be instance ##
            main(){
                Var b : Shape = Null; 
                Var c : Shape = New Shape(1,2,3);
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),Id(A),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(b),ClassType(Id(Shape)),NullLiteral()),VarDecl(Id(c),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect,395))

    
 
    def test_AST96(self):
        input = """
        Class A{
            Val a : Shape; 
            Var a : Shape; 
            Val a : Shape = Null; 
        }
        """
        expect = "Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(Shape)),None)),AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Shape)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(Shape)),NullLiteral()))])])"
        self.assertTrue(TestAST.test(input, expect,396))


    
 
    def test_AST97(self):
        input = """
        Class A{
            main(){
                Val a : Shape; 
                Var a : Shape; 
                Var a : Shape = New Shape(1,2,3);
                Val a : Shape = Null; 
                Val a : Shape = New Shape(1,2,3); 
            }
        }
        """
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(Shape)),None),VarDecl(Id(a),ClassType(Id(Shape)),NullLiteral()),VarDecl(Id(a),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(1),IntLit(2),IntLit(3)])),ConstDecl(Id(a),ClassType(Id(Shape)),NullLiteral()),ConstDecl(Id(a),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"
        self.assertTrue(TestAST.test(input, expect,397))

    
 
    def test_AST98(self):
        input = """
        Class Laptop : Electrical{
                $Refresh(){
                    Foreach(i In ElectricalDevice::$numOfDevices .. 0 By -1){
                    }
                }
                start(){
                    Laptop::$nothing();
                    Return useBattery;
                }
                stop(){
                    Self.nothing();
                    Return -useBattery;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Laptop),Id(Electrical),[MethodDecl(Id($Refresh),Static,[],Block([For(Id(i),FieldAccess(Id(ElectricalDevice),Id($numOfDevices)),IntLit(0),UnaryOp(-,IntLit(1)),Block([])])])),MethodDecl(Id(start),Instance,[],Block([Call(Id(Laptop),Id($nothing),[]),Return(Id(useBattery))])),MethodDecl(Id(stop),Instance,[],Block([Call(Self(),Id(nothing),[]),Return(UnaryOp(-,Id(useBattery)))]))])])"
        self.assertTrue(TestAST.test(input, expect,398))

    
 
    def test_AST99(self):
        input = """
        Class Program{
            main(){
                {}
                {}
                {}
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Block([]),Block([]),Block([])]))])])"
        self.assertTrue(TestAST.test(input, expect,399))

    
 
    def test_AST100(self):
        line = '''Class jF_:_NS
        {
            Constructor (_N,_:Array [Int ,063];_,V,Nt_1:Array [Array [Array [Array [String ,0x5F],063],063],0b1_1];z_:String ){
                
            }
            Constructor (__:_){
                Val _,_,ZS:String ;
            }
            Var $__,_,$A_V_:Int ;
        }
        
        Class _:_7{
            Constructor (v:a;_6q_l:Array [Boolean ,0x96]){

            } 
        }
        
        Class _B:Hc_{
            
        }'''
        expect = '''Program([ClassDecl(Id(jF_),Id(_NS),[MethodDecl(Id(Constructor),Instance,[param(Id(_N),ArrayType(51,IntType)),param(Id(_),ArrayType(51,IntType)),param(Id(_),ArrayType(3,ArrayType(51,ArrayType(51,ArrayType(95,StringType))))),param(Id(V),ArrayType(3,ArrayType(51,ArrayType(51,ArrayType(95,StringType))))),param(Id(Nt_1),ArrayType(3,ArrayType(51,ArrayType(51,ArrayType(95,StringType))))),param(Id(z_),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(__),ClassType(Id(_)))],Block([ConstDecl(Id(_),StringType,None),ConstDecl(Id(_),StringType,None),ConstDecl(Id(ZS),StringType,None)])),AttributeDecl(Static,VarDecl(Id($__),IntType)),AttributeDecl(Instance,VarDecl(Id(_),IntType)),AttributeDecl(Static,VarDecl(Id($A_V_),IntType))]),ClassDecl(Id(_),Id(_7),[MethodDecl(Id(Constructor),Instance,[param(Id(v),ClassType(Id(a))),param(Id(_6q_l),ArrayType(150,BoolType))],Block([]))]),ClassDecl(Id(_B),Id(Hc_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 400))


    def test_AST401(self):
        input = """
        Class A:B{
            Foo(){
                a.b(1+2,3*4-5.5);
                If(1)
                    {}
                Elseif(2)
                    {}
                Elseif(3)
                    {}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([Call(Id(a),Id(b),[BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(-,BinaryOp(*,IntLit(3),IntLit(4)),FloatLit(5.5))]),If(IntLit(1),Block([]),If(IntLit(2),Block([]),If(IntLit(3),Block([]))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 401))
   


    def test_AST402(self):
        input = """
        Class Motor:Vehicle{
            Foo(){
                motor.foo(1+20,30*4-50.50);
                If(10)
                    {}
                Elseif(20)
                    {}
                Elseif(30)
                    {}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[MethodDecl(Id(Foo),Instance,[],Block([Call(Id(motor),Id(foo),[BinaryOp(+,IntLit(1),IntLit(20)),BinaryOp(-,BinaryOp(*,IntLit(30),IntLit(4)),FloatLit(50.5))]),If(IntLit(10),Block([]),If(IntLit(20),Block([]),If(IntLit(30),Block([]))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 402))


    # def test_AST403(self):
    #     input = """
    #     Class Motor:Vehicle{
    #         Foo(){
    #             motor.foo(1+20,30*4-50.50);
    #             If(10)
    #                 {}
    #             Elseif(20)
    #                 {}
    #             Elseif(30)
    #                 {}
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(Motor),Id(Vehicle),[MethodDecl(Id(Foo),Instance,[],Block([Call(Id(motor),Id(foo),[BinaryOp(+,IntLit(1),IntLit(20)),BinaryOp(-,BinaryOp(*,IntLit(30),IntLit(4)),FloatLit(50.5))]),If(IntLit(10),Block([]),If(IntLit(20),Block([]),If(IntLit(30),Block([]))))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 403))



    # def test_clone(self):
    #     input = """Class Program {
    #         Val a, b, c : Int = 1 + 1 * 100 , 2 * 2 / 4 / 5 % 6 , 3 / 3 + (12 + 23);
    #         Var a : Array[Int, 5] = Array(1 * 2 / 3, 3 + 3 / 3, 10 - -9, 100 * -3, 100 % 10);
    #     }"""
    #     expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(1),IntLit(100))))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,BinaryOp(%,BinaryOp(/,BinaryOp(/,BinaryOp(*,IntLit(2),IntLit(2)),IntLit(4)),IntLit(5)),IntLit(6)))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(+,BinaryOp(/,IntLit(3),IntLit(3)),BinaryOp(+,IntLit(12),IntLit(23))))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType),[BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(+,IntLit(3),BinaryOp(/,IntLit(3),IntLit(3))),BinaryOp(-,IntLit(10),UnaryOp(-,IntLit(9))),BinaryOp(*,IntLit(100),UnaryOp(-,IntLit(3))),BinaryOp(%,IntLit(100),IntLit(10))]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 1000))
        #Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(0b1111))),MethodDecl(Id(main),Instance,[],Block([AssignStmt(FieldAccess(CallExpr(CallExpr(Id(A),Id($a),[]),Id(c),[]),Id(d)),IntLit(12))]))])])


   
   