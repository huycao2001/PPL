import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int_0(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,500))


    def test_int_1(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,501))


    def test_int_2(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,502))


    def test_int_3(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,503))


    def test_int_4(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,504))


    def test_int_5(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,505))


    def test_int_6(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,506))


    def test_int_7(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,507))


    def test_int_8(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,508))


    def test_int_9(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,509))


    def test_int_10(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,510))


    def test_int_11(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,511))


    def test_int_12(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,512))


    def test_int_13(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,513))


    def test_int_14(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,514))


    def test_int_15(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,515))


    def test_int_16(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,516))


    def test_int_17(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,517))


    def test_int_18(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,518))


    def test_int_19(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,519))


    def test_int_20(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,520))


    def test_int_21(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,521))


    def test_int_22(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,522))


    def test_int_23(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,523))


    def test_int_24(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,524))


    def test_int_25(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,525))


    def test_int_26(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,526))


    def test_int_27(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,527))


    def test_int_28(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,528))


    def test_int_29(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,529))


    def test_int_30(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,530))


    def test_int_31(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,531))


    def test_int_32(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,532))


    def test_int_33(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,533))


    def test_int_34(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,534))


    def test_int_35(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,535))


    def test_int_36(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,536))


    def test_int_37(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,537))


    def test_int_38(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,538))


    def test_int_39(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,539))


    def test_int_40(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,540))


    def test_int_41(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,541))


    def test_int_42(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,542))


    def test_int_43(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,543))


    def test_int_44(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,544))


    def test_int_45(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,545))


    def test_int_46(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,546))


    def test_int_47(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,547))


    def test_int_48(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,548))


    def test_int_49(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,549))


    def test_int_50(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,550))


    def test_int_51(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,551))


    def test_int_52(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,552))


    def test_int_53(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,553))


    def test_int_54(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,554))


    def test_int_55(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,555))


    def test_int_56(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,556))


    def test_int_57(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,557))


    def test_int_58(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,558))


    def test_int_59(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,559))


    def test_int_60(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,560))


    def test_int_61(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,561))


    def test_int_62(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,562))


    def test_int_63(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,563))


    def test_int_64(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,564))


    def test_int_65(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,565))


    def test_int_66(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,566))


    def test_int_67(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,567))


    def test_int_68(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,568))


    def test_int_69(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,569))


    def test_int_70(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,570))


    def test_int_71(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,571))


    def test_int_72(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,572))


    def test_int_73(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,573))


    def test_int_74(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,574))


    def test_int_75(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,575))


    def test_int_76(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,576))


    def test_int_77(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,577))


    def test_int_78(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,578))


    def test_int_79(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,579))


    def test_int_80(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,580))


    def test_int_81(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,581))


    def test_int_82(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,582))


    def test_int_83(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,583))


    def test_int_84(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,584))


    def test_int_85(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,585))


    def test_int_86(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,586))


    def test_int_87(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,587))


    def test_int_88(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,588))


    def test_int_89(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,589))


    def test_int_90(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,590))


    def test_int_91(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,591))


    def test_int_92(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,592))


    def test_int_93(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,593))


    def test_int_94(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,594))


    def test_int_95(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,595))


    def test_int_96(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,596))


    def test_int_97(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,597))


    def test_int_98(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,598))


    def test_int_99(self):

        input = """   
        Class Program{
            main(){
                Var a : Int = 1; 
                If(a == 2 ){
                    io.readInt(4); 

                }
                Else{
                    io.readInt(3);
                }
            }
        } """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,599))
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],VoidType(),Block([],[
    # 			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))
