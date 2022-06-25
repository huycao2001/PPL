import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_parser_1(self):
        """Simple program"""
        input = """ Class myProgram {
            ## Hello World ##           
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_parser_2(self):
        ## Attribute declarations
        input = """ Class myProgram {
            Var a : Int = 3;
            Var b : Float = 4e3;
            Val c : Boolean = True; 
            Var l : String = "Siuuu";             
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_parser_3(self):
        ## Attribute declarations 
        input = """
        Class myProgram {
            Var a ,b ,c : Int = 1,2,3; 
            Val $num1, $num2, $num3 : Float = 2.5, .e2 , 12_34.56e10;    
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_parser_4(self):
        ## Attribute declarations 
        input = """
        Class myProgram {
            Val a ,b ,c , d ,e : Int;
            Var $f , $g , $h : Float; 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_parser_5(self):
        ## Attribute declarations constraint : number of expression = number of variables 
        input = """
        Class myProgram {
            Val a, d, c : Int = 1,2; 
        }
        """
        expect = "Error on line 3 col 35: ;"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_parser_6(self):
        ## Attribute declarations constraint : number of expression = number of variables 
        input = """
        Class myProgram {
            Val a, d: Int = 1,2,3; 
        }
        """
        expect = "Error on line 3 col 31: ,"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_parser_7(self):
        ## Declare var and assign with expressions
        input = """
        Class myProgram {
            Val a, b, c : Int = 10 + 10 , 22*33 , 100/2;
            Val length, width : Float = (25.2 + 3.0 )/4.2 , 22.3 + 33.1 * 4 / 2e10 ; 
            Var $x, $y : Int = 0, 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_parser_8(self):
        ## No declaration for class -> error
        input = """
        Class myProgram
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_parser_9(self):
        ## Method declaration
        input = """
        Class myProgram{
            Val num1 : Int;

            increment(){
                num1 = num1 + 1;
                Return num1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_parser_10(self):
        ## Method declaration with parameter
        input = """
        Class myProgram{
            Val num1 : Int;

            ComputeSth(a,b : Int; c,d : Float){
                num1 = a + b - c * d;
                Return num1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))


    def test_parser_11(self):
        ## Inheritance
        input = """
        Class Shape{
            getArea(){}
        }
        Class Rectangle : Shape{
            Var width : Float;
            Val length : Float;

            Constructor(a,b : Float){
                Self.width = a; 
                Self.length = b;
            }

            getArea(){
                Return Self.width * Self.length; 
            }
            
            Destructor(){
                ## Might do something here ##
            }
            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_parser_12(self):
        ## Array declaration 
        input = """
        Class List {
            Val a : Array[Int,4] = Array(1,2,3,4);
            Var b : Array[Float,4] = Array(1.1 , 2.2e10 , 0.001 , .12e10);
            Val c : Array[Boolean,4] = Array(True, False , True , False );
            Var d : Array [String,4] = Array("huy", "cao" , "ba" , "ppl");
            Val e : Array[Int,4] = Array(1, 0b1010 , 0123, 0xFFFF);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_parser_13(self):
        ## Array size constraint
        input = """
        Class myProgram{
            Val myarray : Array[Int,0]; 
        }
        """
        expect = "Error on line 3 col 36: 0"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_parser_14(self):
        ## Class type
        input = """
        Class Rectangle : Shape{
            Var width : Float;
            Val length : Float;

            Constructor(a,b : Float){
                Self.width = a; 
                Self.length = b;
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
            }
            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_parser_15(self):
        ## Array size constraint
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_parser_16(self):
        ## Array test
        input = """
        Class Program
        {
            main()
            {
                Val myArray: Array[Int, 5] = Array(1,2,3,4,5);
                Val sum: Int = 0;
                Foreach (i In 1 .. 5){
                    sum = sum + myArray[i];
                    If(i % 2 == 0){
                        Break;
                    }
                    Else{
                        Continue;
                    }
                }
                Out.println(sum);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))

    def test_parser_17(self):
        ## Array test
        input = """
        Class Program
        {
            main(){
                Val myArray: Array[Int, 5] = Array(1,2,3,4,5);
                Val sum: Int = 0;
                Foreach (i In 1 .. 5){
                    sum = sum + myArray[i];
                    If(i % 2 == 0){
                        Break;
                    }
                    Elseif(i % 2 != 0){
                        sum = sum * 2 + 3 / 4;
                    }
                    Else{
                        Continue;
                    }
                }
                Out.println(sum);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))

    def test_parser_18(self):
        ## Array test
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))

    def test_parser_19(self):
        ## Array test
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_parser_20(self):
        ## Multi dim array
        input = """
        Class Program
        {
            main(){
                Var a : Array[Array[Int,5],3] = Array(
                    Array(1,2,3,4,5), 
                    Array(1,2,4,5,6),
                    Array(3,6,7,8,9)
                );
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_parser_21(self):
        ## another Multi dim array
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_parser_22(self):
        ## empty
        input = """
        Class Program
        {
            main(){
                Var a : Array[Int,3] = Array();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_parser_23(self):
        ## assign statment.
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_parser_24(self):
        ## assign statement 2.
        input = """
        Class Program{
            main(){
                Var a : Array[Int,4] = Array(1,2,3,4); 
                Foreach (i In 1 .. 4 By 1){
                    a[i] = a[i] * a[i] + 200 - 100/4; 
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_parser_25(self):
        ## assign statement 2.
        input = """
        Class Program{
            increment(a : Array[Int,4]){
                Foreach (i In 1 .. 4 By 1){
                    a[i] = a[i] * a[i] + 200 - 100/4; 
                }
            }

            main(){
                Var a : Array[Int,4] = Array(1,2,3,4); 
                Self.increment(a);
                Foreach (i In 1 .. 4 By 1){
                    Out.println(a[i]); 
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_parser_26(self):
        ## bubble sort.
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_parser_27(self):
        ## assign statement 2.
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_parser_28(self):
        ## assign statement 2.
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
        }
        Class Program{
            main(){
                Var ans : Shape = New Shape(); 
                Out.println(ans.$count);
            }
        }""" 
        expect = "Error on line 15 col 32: $count"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_parser_29(self):
        ## assign statement 2.
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
        }
        Class Program{
            main(){
                Var ans : Shape = New Shape(); 
                Out.println(ans.$count);
            }
        }""" 
        expect = "Error on line 15 col 32: $count"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_parser_30(self):
        ## assign statement 2.
        input = """
        Class Shape {
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_parser_31(self):
        ## test if else
        input = """
        Class Program {
            main() {
                Var a : Int = 100; 
                If(a == 0){
                    Return a;
                }
                Elseif((a > 0) && (a < 20)){
                    a = a + 1; 
                }
                Elseif((a >= 20) && (a <= 40)){
                    a = a % 2; 
                }
                Elseif( (a > 40) || (a <= 80)){
                    a = a * 20 /4; 
                }
                Else{
                    a = a + 1 - 2 * 3 /4 % 5;
                }
                Out.println(a);
            }
        }

        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_parser_32(self):
        ## test if else
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_parser_33(self):
        ## test if else
        input = """
        Class Program {
            main() {
                Else{

                }
            }
        }

        """ 
        expect = "Error on line 4 col 16: Else"
        self.assertTrue(TestParser.test(input,expect,233))

    def test_parser_34(self):
        ## test if else
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
            $getArea(){
                Return Self.a * Self.b;
            }
        }

        Class Program {
            main() {
                Var a : Shape = New Shape(2.0, 3.0);
                Var b : Shape = New Shape(12.45 , 13.e10);
                Var c : Shape = New Shape(.e10 , 12e0);
                Var list : Array[Int, 3] = Array(a,b,c);
            }
        }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))


    def test_parser_35(self):
        ## test if else
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))


    def test_parser_36(self):
        ## test if else
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))


    def test_parser_37(self):
        ## test if else
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))


    def test_parser_38(self):
        ## test expression and atts in function.
        input = """
        Class Program{
            main(){
                Var a,b : Int = 0; 
            }
        }
        """ 
        expect = "Error on line 4 col 33: ;"
        self.assertTrue(TestParser.test(input,expect,238))


    def test_parser_39(self):
        ## test expression and atts in function.
        input = """
        Class Program{
            main(){
                Var a,b : Int = 10,12; 
                ## Raise error because no static var in functions ##
                Var $c , $d : Int = 123,456; 
            }
        }
        """ 
        expect = "Error on line 6 col 20: $c"
        self.assertTrue(TestParser.test(input,expect,239))



    def test_parser_40(self):
        ## test if else.
        input = """
        Class Program{
            main(){
               If(){ ## no expression for if ## 
                   Out.println("hello");
               }
            }
        }
        """ 
        expect = "Error on line 4 col 18: )"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_parser_41(self):
        ## test if else.
        input = """
        Class Program{
            main(){
               Elseif(True)
                   Out.println("hello");
               }
            }
        }
        """ 
        expect = "Error on line 4 col 15: Elseif"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_parser_42(self):
        ## test if else.
        input = """
        Class Program{
            main(){
               Elseif(True)
                   Out.println("hello");
               }
            }
        }
        """ 
        expect = "Error on line 4 col 15: Elseif"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_parser_43(self):
        ## test if else.
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))


    def test_parser_44(self):
        ## test if else.
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))


    def test_parser_45(self):
        ## eMultiple constructor
        input = """
        Class Shape{
            Var width : Float;
            Var length : Float;
            Constructor(){
                Self.width =  0;
                Self.length = 0;
            }

            Constructor(a,b : Float){
                Self.width = a;
                Self.length = b;
            }

            Destructor(){
                a = 0;
                b = 0;  
            }
        }
        Class Program{
            ## Do sth ##
        }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_parser_46(self):
        ## eMultiple constructor
        input = """
        Class Program
        """ 
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,246))


    def test_parser_47(self):
        ## eMultiple constructor
        input = """
        Class Program{
            Var a : Array[Array[Array[Array[Array[Array[Array[Int,0b1011],0xABCD],04567],0123],5],4],3];
        }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))        



    def test_parser_48(self):
        ## eMultiple expression
        input = """
        Class Program{
            Var a : Int = ( 2 + ((((((a+1) + 2)*3)/(4 + 5) * 6) % 4 /3 * a) + 123 / (456 * 789) ) * 23 / 24 + (a -1));
        }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))   


    def test_parser_49(self):
        ## Boolean operator 
        input = """
        Class Program{
            Var a : Boolean = ((a || a || a && (!a && !a || a )) || (!a || a) && a );
        }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))      


    def test_parser_50(self):
        ## Boolean operator 
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))  


    def test_parser_51(self):
        ## Error when calling function directly 
        input = """

        Class Program{
            Greeting(a : String){
                Var newString : String = ("Hello " +. a) +. " Welcome to Gulag :D";
                Out.println(newString);
            }
            main(){
                Var a : String = "Player1";
                Greeting(a);
                Return;
            }
        }
        """ 
        expect = "Error on line 10 col 24: ("
        self.assertTrue(TestParser.test(input,expect,251))  


    def test_parser_52(self):
        ## Error when calling function directly 
        input = """
            Class Program{
                main(){
                    Self.a = Self.b * Self.c - Self::$e + (Self.x - Self.Y());
                    Self.a = Self::$A();
                    Self::$b = Self.B();
                    Self.a = Self.$A;
                }
            }
        """ 
        expect = "Error on line 4 col 51: ::"
        self.assertTrue(TestParser.test(input,expect,252))  

    def test_parser_53(self):
        ## Error expression in index operator 
        input = """
            Class Program{
                main(){
                    Var a : Array[Int,4] = Array(1,2,3,4);
                    Out.println(a[a[a[a[a[a[a[a[a[a[a[i]]]]]]]]]]]);
                }
            }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))  


    def test_parser_54(self):
        ## Error expression in index operator 
        input = """
            Class Program{
                main(){
                    Var a : Array[Array[Int,3],3] = Array(
                        Array(1,2,3),
                        Array(4,5,6),
                        Array(7,8,9)
                    );

                    Foreach( i In 1 .. 3 By 1){
                        Foreach (j In 1 ..3 By 1){
                            Out.println(a[i][j]);
                        }
                    }
                }
            }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))  


    def test_parser_55(self):
        ## Error expression in index operator 
        input = """
            Class Program{
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255)) 


    def test_parser_56(self):
        ## Error expression in index operator 
        input = """
            Class Program{
                Func(a : Array[Array[Int,3],3]){
                    Foreach( i In 1 .. 3 By 1){
                        Foreach (j In 1 ..3 By 1){
                            a[i][j] = a[i][j] + 1 * 2 /3 * 4 / 5 % 6;
                        }
                    } 
                }
                main(){
                    Var a : Array[Array[Int,3],3] = Array(
                        Array(1,2,3),
                        Array(4,5,6),
                        Array(7,8,9)
                    );
                    Self.Func(a);
                    Foreach( i In 1 .. 3 By 1){
                        Foreach (j In 1 ..3 By 1){
                            Out.println(a[i][j]);
                        }
                    }
                }
            }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))  


    def test_parser_57(self):
        ## Error expression in index operator 
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257)) 


    def test_parser_58(self):
        input = """
        Var i : Int = 4;
        """ 
        expect = "Error on line 2 col 8: Var"
        self.assertTrue(TestParser.test(input,expect,258)) 


    def test_parser_59(self):
        input = """
        Class Program{
            Var True : Boolean = True;
        }
        """ 
        expect = "Error on line 3 col 16: True"
        self.assertTrue(TestParser.test(input,expect,259)) 


    def test_parser_60(self):
        input = """
        Class Program{
            Var True : Boolean = True;
        }
        """ 
        expect = "Error on line 3 col 16: True"
        self.assertTrue(TestParser.test(input,expect,260)) 


    def test_parser_61(self):
        input = """
        Class Program{
            Var clone : String = "##comment in a string##";
        }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261)) 


    def test_parser_62(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262)) 


    def test_parser_63(self):
        input = """
        Class Program{
            main(){
                Var a : Int = 0x123456;
                If(a == +4 + 1 * 9 / 2 * 8 % 4 ){
                    a = -a; 
                }
            }
        }
        """ 
        expect = "Error on line 5 col 24: +"
        self.assertTrue(TestParser.test(input,expect,263)) 

    def test_parser_63(self):
        input = """
        Class Program{
            main(){
                Var a : Int = 0x123456;
                If(a == +4 + 1 * 9 / 2 * 8 % 4 ){
                    a = -a; 
                }
            }
        }
        """ 
        expect = "Error on line 5 col 24: +"
        self.assertTrue(TestParser.test(input,expect,263)) 


    def test_parser_64(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264)) 


    def test_parser_65(self):
        input = """
        ## Multi elsIf ## 
        Class Program{
            main(){
                Elseif(a > 3){
                    a = a + 1; 
                }
                Elseif(a == 3){
                    a = a/ 2; 
                }
            }
        }
        """ 
        expect = "Error on line 5 col 16: Elseif"
        self.assertTrue(TestParser.test(input,expect,265)) 


    def test_parser_66(self):
        input = """ 
        Class Program{
            main(){
                Var andy : String = "/n/n/n/n/n/b/f/r/t"; 
            }
        }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266)) 

    def test_parser_67(self):
        input = """ 
        Class Program{
            other(a : Int){

            }

            main(){
                
            }
        }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267)) 


    def test_parser_68(self):
        input = """ 
        Class Program{
            other(a : Int){

            }

            main(){
                
            }
        }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268)) 

    def test_parser_69(self):
        input = """ 
        Class Program{
            Int(a : Int){

            }

            main(){
                
            }
        }
        """ 
        expect = "Error on line 3 col 12: Int"
        self.assertTrue(TestParser.test(input,expect,269)) 


    def test_parser_70(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270)) 

    def test_parser_71(self):
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

        Class Subsubclass : Subclass, Base{
            print(){
                Return "This is sub sub class";
            }
        }
        """ 
        expect = "Error on line 14 col 36: ,"
        self.assertTrue(TestParser.test(input,expect,271)) 


    def test_parser_72(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,272))


    def test_parser_73(self):
        input = """
        Class Program{
           ## main(){
                
            }##
        }""" 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,273))


    def test_parser_74(self):
        input = """
        ##Class Program{
           main(){
                
            }
        }##""" 
        expect = """Error on line 6 col 11: <EOF>"""
        self.assertTrue(TestParser.test(input,expect,274))

    def test_parser_75(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,275))


    def test_parser_76(self):
        input = """
        Class Program{
            main(){
                Var _ : Int = 0b1011; 
            }
        }
    """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,276))


    def test_parser_77(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,277))

    def test_parser_77(self):
        input = """
        Class Program{
            myFunc(_1 , _2 : Int; _1___az_11, _122_2333, _aaaz_123__ : String ; _AA_b_z_, CCcA_aa : Float){
                ## Do sth ## 
                ## Do sth else ##
            }
            main(){
                Var a : Int = 0b1011; 
                Return (1+1).x;
            }
        }
    """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,277))


    def test_parser_78(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,278))

    def test_parser_79(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,279))


    def test_parser_80(self):
        input = """
            Class Shape {
                Var b: Array[Float,0123];
                Var a : Int = array[1][2][3][4][4+1][4-2][4-2][4*3][2/1][2%1];
            }
    """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,280))


    def test_parser_81(self):
        input = """
        Class Program {
            main() {
                Var a,b,c : Int = 1,2,3;
                Var a, count : Int = 100, 0;
                Foreach(i In 1 .. 100 By 2){
                    If(a % i == 0){
                        Continue;
                    }
                    Else{
                        count = count + 1;
                    }
                }
                Return New X().Y();
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))


    def test_parser_82(self):
        input = """
            Class Shape {
                Var b: Array[Float,0b0];
                Var a : Int = array[1][2][3][4][4+1][4-2][4-2][4*3][2/1][2%1];
            }
    """ 
        expect = """Error on line 3 col 35: 0b0"""
        self.assertTrue(TestParser.test(input,expect,282))

    def test_parser_83(self):
        input = """
            Class Shape {
                Var b: Array[Float,0X0];
                Var a : Int = array[1][2][3][4][4+1][4-2][4-2][4*3][2/1][2%1];
            }
    """ 
        expect = """Error on line 3 col 35: 0X0"""
        self.assertTrue(TestParser.test(input,expect,283))


    def test_parser_84(self):
        input = """
            Class Shape {
                If(e > 1){
                    e = 1 + 1; ## Raise erroe## 
                }
            }
    """ 
        expect = """Error on line 3 col 16: If"""
        self.assertTrue(TestParser.test(input,expect,284))


    def test_parser_85(self):
        input = """
            Class Shape {
                Var a : Int = 1 * * 1;
            }
    """ 
        expect = """Error on line 3 col 34: *"""
        self.assertTrue(TestParser.test(input,expect,285))


    def test_parser_86(self):
        input = """
            Class Shape {
                Var a : Int = 1 * * 1;
            }
    """ 
        expect = """Error on line 3 col 34: *"""
        self.assertTrue(TestParser.test(input,expect,286))


    def test_parser_87(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,287))


    def test_parser_88(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,288))


    def test_parser_89(self):
        input = """
        Class Program{
            func(){
                Foreach (i In 1-1+2+3*5 .. 1 + 1 + 1 + 2 * 3 By -2+1/2*3){
                    Out.println("Always");
                }
                Return;
            }
        }

    """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,289))


    def test_parser_90(self):
        input = """
        Class Program{
            func(){
                Foreach (1 In 1-1+2+3*5 .. 1 + 1 + 1 + 2 * 3 By -2+1/2*3){
                    Out.println("Always");
                }
                Return;
            }
        }

    """ 
        expect = """Error on line 4 col 25: 1"""
        self.assertTrue(TestParser.test(input,expect,290))


    def test_parser_91(self):
        input = """
        Class Program{
            func(){
               Return Self.a.a.a.a.a.a.a.a.a.a;
            }
        }
        """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,291))

    def test_parser_92(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_parser_93(self):
        input = """Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0, 1;
            Var length, width: Int;

            $getNumOfShape() {
                Return Self::$numOfShape;
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
        expect = "Error on line 3 col 43: ,"
        self.assertTrue(TestParser.test(input, expect, 293))


    def test_parser_94(self):
        input = """Class Program {
            main() {
                Var c, h: Int = 50, 30;
                Var d: Int = Math.int(System.input("Enter D: "));
                Var Q: Int = Math.int(2 * c * d / h);
                Out.println(Math.round(Math.sqrt(Math.abs(Math.log(Q)))));
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_parser_95(self):
        input = """Class Program {
            main() {
                Var a,b,c,d,e,f,g,h : Int;
                a = 0x123456ABCDEF;
                
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_parser_96(self):
        input = """Class Program {
            main() {
                Foreach( x In 1 .. 10 By 1){
                    a[x] = a[x] + 1;
                }
                
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_parser_97(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))


    def test_parser_98(self):
        input = """
        Class Program {
            main(){
                Var a : Shape = New Shape(1,2); 
                Return a::$GetCount();
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_parser_99(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_parser_100(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))



    def test_huycao1(self):
        input = """Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;

            $getNumOfShape() {
                Return huycao::$numOfShape;
            }
        }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2010))


    # def test_complex_program1(self):
    #     input = """
    #     Class Shape {
    #         Val $numOfShape: Int = 0;
    #         Val immutableAttribute: Int = 0;
    #         Var length, width: Int;
    #         Var a : Array[Int,3] = Array( 
    #             Array(
    #                 Array(
    #                     Array(1,2,3,4)
    #                 )
    #             ), 
    #             Array(3,4,5,6),
    #             Array(7,8,9,10)
    #         );

    #         $getNumOfShape() {
    #             Return $numOfShape;
    #         }
    #     }

        
    #     Class Program{
    #         main(){
    #             Var a : Int = 12;
    #             If( a + 1 + 2 == 9 ){
                    
    #                 a = b = c = d = Self.Pi ; 
    #                 Foreach(i In 1 .. 100 By 2){
    #                     a =  a[1+2+3];
    #                     a = a::$getShape();
    #                     Continue;
    #                 }
                    
    #             }
    #             Else{
    #                 a = a * 3 / 3 /3 /4 /4 + 5 -9; 
    #             }
    #         }
    #     }
        
    #    """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 202))


    # def test_complex_program_2001(self):
    #     input = """Class Shape {
    #         Val $numOfShape: Int = 0;
    #         Val immutableAttribute , x: Int = 12,0;
    #         Var length, width: Int;
           

    #         $getNumOfShape() {
    #             Return $numOfShape;
    #         }
    #     }
    #     Class Rectangle: Shape {
    #         getArea() {
    #             Return Self.length * Self.width;
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 290))

    # def test_random(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a,b,c : Int = 1,2,3;
    #             Var a, count : Int = 100, 0;
    #             Foreach(i In 1 .. 100 By 2){
    #                 If(a % i == 0){
    #                     Continue;
    #                 }
    #                 Else{
    #                     count = count + 1;
    #                 }
    #             }
    #             Return New X().Y();
                
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 888))

    # def test_static_accesmmmms1(self):
    #     input = """Class Program {
    #         Var $a: Int = 0b1111;
    #         Var b: Float = 5.5;
    #         main() {
    #             Var res: Int = a + b;
    #             Out.printInt(res);
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 999))

