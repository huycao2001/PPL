import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):



    def test_79(self):
        input = """
        Class Program
        {
            main()
            {
                Var myArray : Array[Int, 4] = Array(1,2,3,4);
                Var myFloat : Float = myArray[1];
                Val result : Float = myFloat;
            }
        }"""
        expect = """Illegal Constant Expression: Id(myFloat)"""
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_80(self):
        input = """
        Class Colors
        {
            Val $colors : Array[String, 4] = Array("Red", "Blue", "Green", "Yellow");
        }
        Class Program
        {
            main()
            {
                Var myColor : String = Colors::$colors[1];
                Var myNextColor : String = Colors::$colors[1][2];
            }
        }"""
        expect = """Type Mismatch In Expression: ArrayCell(FieldAccess(Id(Colors),Id($colors)),[IntLit(1),IntLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_81(self):
        input = """
        Class Program
        {
            main()
            {
                Var myArray: Array[Array[Int, 2], 2] = Array(
                    Array(1,2),
                    Array(3,4)
                );
                Var myInt : Int = myArray[1][1];
                Var nextInt : Int = myArray[2];
            }
        }
        """
        expect = """Type Mismatch In Statement: VarDecl(Id(nextInt),IntType,ArrayCell(Id(myArray),[IntLit(2)]))"""
        self.assertTrue(TestChecker.test(input, expect, 480))

    # def test_82(self):
    #     input = """
    #     Class Program
    #     {
    #         main()
    #         {
    #             Var myList : Array [String, 3] = Array ("I", "support", "Ukraine");
    #             myList[3] = "Russia";
    #             Val myArray: Array[Float, 3] = Array(1.0, 3.4, 5.6);
    #             myArray[1] = 5;
    #         }
    #     }"""
    #     expect = """Cannot Assign To Constant: AssignStmt(ArrayCell(Id(myArray),[IntLit(1)]),IntLit(5))"""
    #     self.assertTrue(TestChecker.test(input, expect, 481))

    # def test_83(self):
    #     input = """
    #     Class Program
    #     {
    #         Val $myAnimal : Array[String, 3] = Array("Cow", "Bird", "Alligator");
    #         main()
    #         {
    #             Var favoriteAnimal : String = Program::$myAnimal[1];
    #             Program::$myAnimal[1] = "Parrot";
    #         }
    #     }"""
    #     expect = """Cannot Assign To Constant: AssignStmt(ArrayCell(FieldAccess(Id(Program),Id($myAnimal)),[IntLit(1)]),StringLit(Parrot))"""
    #     self.assertTrue(TestChecker.test(input, expect, 482))

    def test_84(self):
        input = """
        Class Program
        {
            main()
            {
                Var firstArray : Array[Array[Int ,2], 3] = Array(
                    Array(1,2),
                    Array(3,4),
                    Array(5,6)
                );
                Var secondArray : Array[Int , 2] = firstArray[1];
                Var thirdArray : Array[Int, 2] = firstArray;
            }
        }"""
        expect = """Type Mismatch In Statement: VarDecl(Id(thirdArray),ArrayType(2,IntType),Id(firstArray))"""
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_85(self):
        input = """
        Class Program
        {
            main ()
            {
                Var myArray: Array[Array[Array[Int,4],2],2] = Array(
                        Array(
                            Array(1,2,3,4),
                            Array(1,2,3,4)
                        ),
                        Array(
                            Array(1,2,3,4),
                            Array(1,2,3,4)
                        )
                    );
                Var nextArray : Array[Array[Int,4],2] = myArray[1];
                Var value : Int = myArray[1][1][1];
                If (value)
                {
                    Var value : Boolean = True;
                }
            }
        }"""
        expect = """Type Mismatch In Statement: If(Id(value),Block([VarDecl(Id(value),BoolType,BooleanLit(True))]))"""
        self.assertTrue(TestChecker.test(input, expect, 484))
