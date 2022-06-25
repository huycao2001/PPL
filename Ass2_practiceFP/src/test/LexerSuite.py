import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier1(self):
        self.assertTrue(TestLexer.test("num1 num2 num3 flag count","num1,num2,num3,flag,count,<EOF>",101))

    def test_identifier2(self):
        self.assertTrue(TestLexer.test("_var1 _var2 __var3  flag_1 flag_2 flag_6969","_var1,_var2,__var3,flag_1,flag_2,flag_6969,<EOF>",102))

    def test_identifier3(self):
        self.assertTrue(TestLexer.test("VAR1 vAriABlE vAri_ABlE","VAR1,vAriABlE,vAri_ABlE,<EOF>",103))

    def test_identifier4(self):
        self.assertTrue(TestLexer.test("_____","_____,<EOF>",104))
    
    def test_static_identifier1(self):
        self.assertTrue(TestLexer.test("$numOfShape $GetLength","$numOfShape,$GetLength,<EOF>",105))

    def test_static_identifier2(self):
        self.assertTrue(TestLexer.test("$__numofShape $GETLENGTH123","$__numofShape,$GETLENGTH123,<EOF>",106))
    
    def test_static_identifier3(self):
        self.assertTrue(TestLexer.test("$_______","$_______,<EOF>",107))

    def test_static_identifier4(self):
        self.assertTrue(TestLexer.test("$6969","$6969,<EOF>",108))

    def test_separator(self):
        self.assertTrue(TestLexer.test("() [] . , ; : {}","(,),[,],.,,,;,:,{,},<EOF>",109))

    def test_octal_1(self):
        self.assertTrue(TestLexer.test("01 0123456 0777777","01,0123456,0777777,<EOF>",110))

    def test_octal_2(self):
        self.assertTrue(TestLexer.test("01_1 0123_456 0_777_777","011,0123456,0777777,<EOF>",111))

    def test_octal_3(self):
        self.assertTrue(TestLexer.test("001","00,1,<EOF>",112))

    def test_octal_4(self):
        self.assertTrue(TestLexer.test("0123456789","01234567,89,<EOF>",113))
    
    def test_octal_5(self):
        self.assertTrue(TestLexer.test("000000123456789","00,00,00,123456789,<EOF>",114))

    def test_octal_6(self):
        self.assertTrue(TestLexer.test("0123__456__789","0123,__456__789,<EOF>",115))
    
    def test_binary_1(self):
        self.assertTrue(TestLexer.test("0b110101011101 0b10000000 0b1111111","0b110101011101,0b10000000,0b1111111,<EOF>",116))

    def test_binary_2(self):
        self.assertTrue(TestLexer.test("0b1 0b0","0b1,0b0,<EOF>",117))

    def test_binary_3(self):
        self.assertTrue(TestLexer.test("0b111_000_111 0b1_1_1_1_1","0b111000111,0b11111,<EOF>",118))
    
    def test_binary_4(self):
        self.assertTrue(TestLexer.test("0b_10101010","0,b_10101010,<EOF>",119))

    def test_binary_5(self):
        self.assertTrue(TestLexer.test("0b1000_000_000","0b1000000000,<EOF>",120))    

    def test_binary_6(self):
        self.assertTrue(TestLexer.test("0b11010__","0b11010,__,<EOF>",121))

    def test_hexa_1(self):
        self.assertTrue(TestLexer.test("0x123456789 0x1023456","0x123456789,0x1023456,<EOF>",122))    

    def test_hexa_2(self):
        self.assertTrue(TestLexer.test("0xABCDABCD 0xFFFFF","0xABCDABCD,0xFFFFF,<EOF>",123))
    
    def test_hexa_3(self):
        self.assertTrue(TestLexer.test("0xA12BCD456789EF 0xABCD00000","0xA12BCD456789EF,0xABCD00000,<EOF>",124))      

    def test_hexa_4(self):
        self.assertTrue(TestLexer.test("0xA_12B_CD4_567_89E_F 0xA_BC_D00_000","0xA12BCD456789EF,0xABCD00000,<EOF>",125))      

    def test_hexa_5(self):
        self.assertTrue(TestLexer.test("0xABC2314DEFGHJKL","0xABC2314DEF,GHJKL,<EOF>",126))      

    def test_hexa_6(self):
        self.assertTrue(TestLexer.test("0x123_456__ABCD__EFGH","0x123456,__ABCD__EFGH,<EOF>",127))      

    def test_hexa_7(self):
        self.assertTrue(TestLexer.test("0x____123_456__ABCD__EFGH","0,x____123_456__ABCD__EFGH,<EOF>",128))

    def test_hexa_8(self):
        self.assertTrue(TestLexer.test("0x0000_ABCD","0x0,00,0,_ABCD,<EOF>",129))          

    def test_hexa_9(self):
        self.assertTrue(TestLexer.test("0x123_4ABCD_","0x1234ABCD,_,<EOF>",130))          

    def test_int_1(self):
        self.assertTrue(TestLexer.test("0 1 2 3 4 5 6 7 8 9 10","0,1,2,3,4,5,6,7,8,9,10,<EOF>",131)) 

    def test_int_2(self):
        self.assertTrue(TestLexer.test("123456 78910 10000","123456,78910,10000,<EOF>",132))

    def test_int_3(self):
        self.assertTrue(TestLexer.test("123_456_789 9_8_7_6_5_4_3_2_1","123456789,987654321,<EOF>",133))     

    def test_int_4(self):
        self.assertTrue(TestLexer.test("123_456__789","123456,__789,<EOF>",134))

    def test_bool_1(self):
        self.assertTrue(TestLexer.test("True False","True,False,<EOF>",135))

    def test_float_1(self):
        self.assertTrue(TestLexer.test("0.27  2.73  0.1 ","0.27,2.73,0.1,<EOF>",136))
    
    def test_float_2(self):
        self.assertTrue(TestLexer.test("0.0001","0.0001,<EOF>",137))

    def test_float_3(self):
        self.assertTrue(TestLexer.test("000000.000","00,00,00,.,00,0,<EOF>",138))

    def test_float_4(self):
        self.assertTrue(TestLexer.test("123.000","123.000,<EOF>",139))

    def test_float_5(self):
        self.assertTrue(TestLexer.test("27.73e+5 27.73e-5 27.73e5","27.73e+5,27.73e-5,27.73e5,<EOF>",140))

    def test_float_6(self):
        self.assertTrue(TestLexer.test("1e5 1e+6 0e-8 12e0","1e5,1e+6,0e-8,12e0,<EOF>",141))

    def test_float_7(self):
        self.assertTrue(TestLexer.test(".2e10 .2e+1 .20001e-6",".2e10,.2e+1,.20001e-6,<EOF>",142))

    def test_float_8(self):
        self.assertTrue(TestLexer.test("123_456.e10  1_2_3_4_5.12e-999 1_0.001e-100","123456.e10,12345.12e-999,10.001e-100,<EOF>",143))

    def test_float_9(self):
        self.assertTrue(TestLexer.test("1_2_3.e","123.,e,<EOF>",144))

    def test_float_10(self):
        self.assertTrue(TestLexer.test("0_1_2_3.e","0123,.,e,<EOF>",145))
    
    def test_float_11(self):
        self.assertTrue(TestLexer.test(".E00b001", ".E00,b001,<EOF>", 146))
    
    def test_float_12(self):
        self.assertTrue(TestLexer.test(".e000X01AB", ".e000,X01AB,<EOF>", 147))
    
    def test_string_1(self):
        self.assertTrue(TestLexer.test("\"\"", ",<EOF>", 148))

    def test_string_2(self):
        self.assertTrue(TestLexer.test("\"A simple string\"", "A simple string,<EOF>", 149))

    def test_string_3(self):
        self.assertTrue(TestLexer.test("\"Invalid Int number : 00000100000100000\"", "Invalid Int number : 00000100000100000,<EOF>", 150))

    def test_string_4(self):
        self.assertTrue(TestLexer.test("\"They asked me :\"\"", "They asked me :,Unclosed String: ", 151))

    def test_string_5(self):
        self.assertTrue(TestLexer.test("\"They asked me : '\"Wheres the lamp sauce ?!?!'\" \"", "They asked me : '\"Wheres the lamp sauce ?!?!'\" ,<EOF>", 152))

    def test_string_6(self):
        self.assertTrue(TestLexer.test("\"A string containing escpape char : \\b \\f \\r \\n \\t \\\\ \\'\"", "A string containing escpape char : \\b \\f \\r \\n \\t \\\\ \\',<EOF>", 153))

    def test_string_7(self):
        self.assertTrue(TestLexer.test("\"A string containing escpape char : \\b \\f \\r \\n \\t \\\\ \\'\"", "A string containing escpape char : \\b \\f \\r \\n \\t \\\\ \\',<EOF>", 154))

    def test_string_8(self):
        self.assertTrue(TestLexer.test("\"\\n \\' I will become the pirate king\"", "\\n \\' I will become the pirate king,<EOF>", 155))

    def test_string_9(self):
        self.assertTrue(TestLexer.test("\"'\" You are weak Sasuke because you lack of hatred \\n \\n \\t'\" Itachi said calmly\"", "'\" You are weak Sasuke because you lack of hatred \\n \\n \\t'\" Itachi said calmly,<EOF>", 156))

    def test_string_10(self):
        self.assertTrue(TestLexer.test("\"First string\" \"Second string \\t \\n\" \"Third string \\t\\n\\b \" ", "First string,Second string \\t \\n,Third string \\t\\n\\b ,<EOF>", 157))
    
    def test_string_11(self):
        self.assertTrue(TestLexer.test("\"....???!!!!!+-/*&^%$#@\" ", "....???!!!!!+-/*&^%$#@,<EOF>", 158))

    def test_unclosed_string1(self):
        self.assertTrue(TestLexer.test("\"He is a pirate", "Unclosed String: He is a pirate", 159))

    def test_unclosed_string2(self):
        self.assertTrue(TestLexer.test("\"", "Unclosed String: ", 160))

    def test_unclosed_string3(self):
        self.assertTrue(TestLexer.test("\"\\b", "Unclosed String: \\b", 161))

    def test_unclosed_string4(self):
        self.assertTrue(TestLexer.test("\"This is a \\t string \\n containing escpape characters \" \"He asked \\n me: '\"Where '\"is'\" the lampsauce?'\"\" \"This string is not closed", "This is a \\t string \\n containing escpape characters ,He asked \\n me: '\"Where '\"is'\" the lampsauce?'\",Unclosed String: This string is not closed", 162))
    
    def test_operator_1(self):
        self.assertTrue(TestLexer.test("||||||||", "||,||,||,||,<EOF>", 163))    

    def test_operator_2(self):
        self.assertTrue(TestLexer.test("!=!!!!=", "!=,!,!,!,!=,<EOF>", 164)) 

    def test_operator_3(self):
        self.assertTrue(TestLexer.test("!=!!!!=", "!=,!,!,!,!=,<EOF>", 165)) 

    def test_operator_4(self):
        self.assertTrue(TestLexer.test("+-*/%", "+,-,*,/,%,<EOF>", 166)) 

    def test_operator_5(self):
        self.assertTrue(TestLexer.test("== != > >= < <=", "==,!=,>,>=,<,<=,<EOF>", 167)) 

    def test_operator_6(self):
        self.assertTrue(TestLexer.test("+. ==.", "+.,==.,<EOF>", 168))

    def test_operator_7(self):
        self.assertTrue(TestLexer.test("|||", "||,Error Token |", 169))

    def test_operator_8(self):
        self.assertTrue(TestLexer.test("-696969", "-,696969,<EOF>", 170))   

    def test_operator_9(self):
        self.assertTrue(TestLexer.test("-01230xAFD20b10", "-,01230,xAFD20b10,<EOF>", 171))

    def test_keyword_1(self):
        self.assertTrue(TestLexer.test("Break Continue If Elseif Else", "Break,Continue,If,Elseif,Else,<EOF>", 172))

    def test_keyword_2(self):
        self.assertTrue(TestLexer.test("Foreach True False Array In", "Foreach,True,False,Array,In,<EOF>", 173))

    def test_keyword_3(self):
        self.assertTrue(TestLexer.test("Int Float Boolean String Return", "Int,Float,Boolean,String,Return,<EOF>", 174))

    def test_keyword_4(self):
        self.assertTrue(TestLexer.test("Null Class Val Var Self", "Null,Class,Val,Var,Self,<EOF>", 175))
    
    def test_keyword_5(self):
        self.assertTrue(TestLexer.test("Constructor Destructor New By", "Constructor,Destructor,New,By,<EOF>", 176))

    def test_illegal_esc_1(self):
        self.assertTrue(TestLexer.test("\"Simple illgegal escape : \\e\"", "Illegal Escape In String: Simple illgegal escape : \e", 177))

    def test_illegal_esc_2(self):
        self.assertTrue(TestLexer.test("\"Another illegal escape \\2 \"", "Illegal Escape In String: Another illegal escape \\2", 178))

    def test_illegal_esc_3(self):
        self.assertTrue(TestLexer.test("\"He is a pirate \\ \"", "Illegal Escape In String: He is a pirate \ ", 179))

    def test_illegal_esc_4(self):
        self.assertTrue(TestLexer.test("\"I will never \\t\\t take back my words \\n\\h thats my ninjaway \"", "Illegal Escape In String: I will never \\t\\t take back my words \\n\\h", 180))

    def test_illegal_esc_5(self):
        self.assertTrue(TestLexer.test("\"Dumbledore : '\" Lily? After all this time? \\n \\n \\t \\j '\" \"", "Illegal Escape In String: Dumbledore : '\" Lily? After all this time? \\n \\n \\t \\j", 181))

    def test_illegal_esc_6(self):
        self.assertTrue(TestLexer.test("\"Prof Snape : '\" \\t \\b Always '\" \\r \\=", "Illegal Escape In String: Prof Snape : '\" \\t \\b Always '\" \\r \\=", 182))

    def test_comment_1(self):
        self.assertTrue(TestLexer.test("## This will be not printed ##", "<EOF>", 183))

    def test_comment_2(self):
        self.assertTrue(TestLexer.test("## \" Unclosed string but this will not be printed ##", "<EOF>", 184))

    def test_comment_3(self):
        self.assertTrue(TestLexer.test("## \" Unclosed string but this will not be printed ##", "<EOF>", 185))

    def test_comment_4(self):
        self.assertTrue(TestLexer.test("## \" Illegal escape : \\2 but will not be printed \" ##", "<EOF>", 186))

    def test_comment_5(self):
        self.assertTrue(TestLexer.test("####", "<EOF>", 187))

    def test_complex_program_1(self):
        input = """
        Val My1stCons, My2ndCons: Int = 1 + 5, 2;
        Var $x, $y : Int = 0, 0;
        """
        expect = "Val,My1stCons,,,My2ndCons,:,Int,=,1,+,5,,,2,;,Var,$x,,,$y,:,Int,=,0,,,0,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 188))

    def test_complex_program_2(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            $getNumOfShape() {
                Return $numOfShape;
            }
        }
        """
        expect = "Class,Shape,{,Val,$numOfShape,:,Int,=,0,;,Val,immutableAttribute,:,Int,=,0,;,Var,length,,,width,:,Int,;,$getNumOfShape,(,),{,Return,$numOfShape,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 189))

    
    def test_complex_program_3(self):
        input = """
        Class Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        """
        expect = "Class,Rectangle,:,Shape,{,getArea,(,),{,Return,Self,.,length,*,Self,.,width,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 190))


    def test_complex_program_4(self):
        input = """
        Class Shape {
            Var a : Array[Int,4] = Array(1,2,3,4);
            Var b : Array[String,3] = Array ("cao", "ba" , "huy");
            $getNumOfShape() {
                Return $numOfShape;
            }
        }

        """
        expect = "Class,Shape,{,Var,a,:,Array,[,Int,,,4,],=,Array,(,1,,,2,,,3,,,4,),;,Var,b,:,Array,[,String,,,3,],=,Array,(,cao,,,ba,,,huy,),;,$getNumOfShape,(,),{,Return,$numOfShape,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test_complex_program_5(self):
        input = """
        Class Program {
            main() {
                Var a, count : Int = 100, 0;
                Foreach(i In 1 .. 100 By 2){
                    If(a % i == 0){
                        Continue;
                    }
                    Else{
                        count = count + 1;
                    }
                }
            }
        }
        """
        expect = "Class,Program,{,main,(,),{,Var,a,,,count,:,Int,=,100,,,0,;,Foreach,(,i,In,1,..,100,By,2,),{,If,(,a,%,i,==,0,),{,Continue,;,},Else,{,count,=,count,+,1,;,},},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 192))


    def test_complex_program_6(self):
        input = """
        Class Shape {
            Var $num1, $num2 : String = "Harry", "Potter";
            Constructor(){}
            Constructor(a: String ; b : String){
                $num1 = a; 
                $num2 = b;
            }

            Destructor(){}
            
        }
        """
        expect = "Class,Shape,{,Var,$num1,,,$num2,:,String,=,Harry,,,Potter,;,Constructor,(,),{,},Constructor,(,a,:,String,;,b,:,String,),{,$num1,=,a,;,$num2,=,b,;,},Destructor,(,),{,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 193))

    def test_complex_program_7(self):
        input = """
        Class Shape{
            Var name : String;
        }

        Class Circle : Shape{
            Var radius : Float; 
            Constructor(a : Float){
                Self.radius = float; ## This will not be printed ##
            }

            getArea(){
                Return Self.radius * Self.Radius * 3.14; 
            }
            ## Define function ##
            getPerimeter(){
                Return Self.radius * 2 * 3.14;
            }
        }
        """
        expect = "Class,Shape,{,Var,name,:,String,;,},Class,Circle,:,Shape,{,Var,radius,:,Float,;,Constructor,(,a,:,Float,),{,Self,.,radius,=,float,;,},getArea,(,),{,Return,Self,.,radius,*,Self,.,Radius,*,3.14,;,},getPerimeter,(,),{,Return,Self,.,radius,*,2,*,3.14,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 194))

    def test_complex_program_8(self):
        input = """
        Class Shape {
            Var a : Float; 
            Constructor(b : Float){
                a = b;
            }

            getFunc(){
                If(a < 0 ){
                    a = a + 1 - 2 * 3 / 4; 
                }
                Elseif(a > 0 ){
                    a = a * a * a; 
                }
                Else{
                    a = -a; 
                }
            }
            
        }
        """
        expect = "Class,Shape,{,Var,a,:,Float,;,Constructor,(,b,:,Float,),{,a,=,b,;,},getFunc,(,),{,If,(,a,<,0,),{,a,=,a,+,1,-,2,*,3,/,4,;,},Elseif,(,a,>,0,),{,a,=,a,*,a,*,a,;,},Else,{,a,=,-,a,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 195))

    def test_error_character_1 (self):
        self.assertTrue(TestLexer.test("huy.cao2001@hcmut.edu,vn", "huy,.,cao2001,Error Token @", 196))

    def test_random_1(self):
        input = """ 
        Class Program{
            main(){
                Var andy : String = "/n/n/n/n/n"; 
            }
        }
        """ 
        expect = "Class,Program,{,main,(,),{,Var,andy,:,String,=,/n/n/n/n/n,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input,expect,197)) 

    def test_random_2(self):
        input = """ 1...............0e """ 
        expect = "1.,..,..,..,..,..,..,..,0,e,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,198)) 

    def test_random_3(self):
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
        expect = "Class,Entity,{,Val,$a,:,Int,=,0b1011010,;,Var,b,:,Int,=,00,;,$getA,(,),{,Return,New,X,(,),.,Y,(,),;,},},Class,Program,{,main,(,),{,Var,sum1,:,Int,=,Example,::,$getA,(,),+,Example,.,b,;,Var,sum2,:,Int,=,Example,.,b,+,Example,::,$getA,(,),;,Out,.,printInt,(,res1,+,res2,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input,expect,199)) 
    
    def test_random_4(self):
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
        expect = "Class,Program,{,addNewNode,(,newNode,,,head,:,Int,),{,newNode,.,next_node,=,head,;,head,=,new_node,;,},deleteNode,(,position,,,head,:,Int,),{,If,(,head,==,0,),{,head,=,head,.,next_node,;,},Else,{,Var,curr,:,Int,=,head,.,next,.,next,;,Var,prev,:,Int,=,curr,;,Foreach,(,i,In,2,..,position,),{,prev,=,curr,;,curr,=,curr,.,next_node,;,},prev,.,next,=,curr,;,head,=,prev,;,},},},<EOF>"
        self.assertTrue(TestLexer.test(input,expect,200)) 
