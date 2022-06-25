'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName))
                    
        ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init() # list of symbols
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class MType:
#     def __init__(self,partype,rettype):
#         self.partype = partype
#         self.rettype = rettype

#     def __repr__(self):
#         return "MType([" + ', '.join(str(x) for x in self.partype) + "], " + str(self.rettype) + ")"


class ioPrintStream : 
    pass

class StringType(Type):
    
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
        
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        # self.emit.printout(self.emit.emitPROLOG("vvv" , "www"))

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any
        # Stmt cho body, Access cho expression
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env) # env -> list of symbols
        for x in ast.decl:
            e = self.visit(x, e)
        # # generate default constructor
        # self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(list(), list())), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()

        return [None]

    def visitClassDecl(self, ast, c):
        ast.classname.name = "D96Class" if ast.classname.name == "Program" else ast.classname.name 
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        # if ast.parentname == None:
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        # else:
        #     self.emit.printout(self.emit.emitPROLOG(
        #         self.className, ast.parentname.name))
        [self.visit(ele, SubBody(None, [])) for ele in ast.memlist]
        # generate default constructor
        # c is Sub Body
        #self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(), None, Block([], [])), c, Frame("<init>", VoidType()))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: SubBody
        #frame: Frame

        isInit = consdecl.name.name  == "Constructor"
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0
        returnType = VoidType()
        isStatic = type(consdecl.kind) is Static 
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)
        
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, isStatic, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        # if isInit:
        #     self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        # body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        # if isInit:
        #     self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
        #     self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        clone = SubBody(frame, o.copy())
        self.visit(consdecl.body, clone )
        # list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        #if type(returnType) is VoidType:
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitAttributeDecl(self, ast, o):
        print("type of o is : " , o)
        print(o.sym)
        pass

    def visitMethodDecl(self, ast, o):
        frame = Frame(ast.name, VoidType())
        self.genMETHOD(ast, o.sym, frame)
        if type(ast.kind) is Static:
            sKind = "Static"
        else:
            sKind = "Instance"
        return Symbol(ast.name, MType([], VoidType()), CName(self.className), sKind, "Method")


    def visitBlock(self, ast , o) : 
        for i in ast.inst : 
            self.visit(i , o )

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        isIO = type(ast.obj) is Id and ast.obj.name == "io"
        if isIO : 
            p1 = self.emit.emitGETSTATIC("java.lang.System.out" , ioPrintStream(), frame)
            access = Access(o.frame, o.sym , False, True)
            p2, type_ = self.visit(ast.param[0] , access)
            p3 = self.emit.emitINVOKEVIRTUAL("java/io/PrintStream/print" , MType([type_] , VoidType()), frame)
            self.emit.printout(p1 + p2 + p3)
            return 
        if type(ast.obj) is SelfLiteral:
            sym = self.handleAccess(ast, o, self.className)
        else:
            obj = self.visit(ast.obj, o)
            sym = self.handleAccess(ast, o, obj[0])
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.method.name, ctype, frame))

    def visitVarDecl(self, ast, o):
        frame = o.frame
        env = o.sym
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, ast.variable.name, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
        o.sym.append(Symbol(ast.variable.name, ast.varType, Index(idx), None, None))
        if ast.varInit : 
            left_access = Access(o.frame, o.sym, True , False)
            right_access = Access(o.frame, o.sym, False, False)
            rhs = ast.varInit.accept(self, right_access)
            lhs = ast.variable.accept(self, left_access)
            return self.emit.printout(rhs[0] + lhs[0])
        

        return Symbol(ast.variable.name, ast.varType, Index(idx), None, None)

    def visitConstDecl(self, ast, o):
        frame = o.frame
        env = o.sym
        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, ast.constant.name, ast.constType, frame.getStartLabel(), frame.getEndLabel(), frame))
        o.sym.append(Symbol(ast.variable.name, ast.varType, Index(idx), None, None))
        return Symbol(ast.constant.name, ast.constType, ast.value, None, None)


    # def visitFuncDecl(self, ast, o):
    #     #ast: FuncDecl
    #     #o: Any

    #     subctxt = o
    #     frame = Frame(ast.name, ast.returnType)
    #     self.genMETHOD(ast, subctxt.sym, frame)
    #     return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)

    # def visitCallExpr(self, ast, o):
    #     #ast: CallExpr
    #     #o: Any

    #     ctxt = o
    #     frame = ctxt.frame
    #     nenv = ctxt.sym
    #     sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
    #     cname = sym.value.value
    
    #     ctype = sym.mtype

    #     in_ = ("", list())
    #     for x in ast.param:
    #         str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
    #         in_ = (in_[0] + str1, in_[1].append(typ1))
    #     self.emit.printout(in_[0])
    #     self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))

    def visitId(self, ast , o ) : 

        sym = o.sym 
        frame = o.frame
        clone = reversed(sym)
        symbol = None
        for i in clone : 
            if i.name == ast.name :
                symbol = i 
        if o.isLeft : 
            return self.emit.emitWRITEVAR(symbol.name , symbol.mtype , symbol.value.value , frame) , symbol.mtype
        else : 

            return self.emit.emitREADVAR(symbol.name , symbol.mtype , symbol.value.value , frame) , symbol.mtype



# class If(Stmt):
#     expr: Expr
#     thenStmt: Stmt
#     elseStmt: Stmt = None  # None if there is no else branch
    def visitIf(self , ast , o ) : 

        if_exprCode, kk = ast.expr.accept(self, Access(o.frame, o.sym, False , False))

        if ast.elseStmt:
            labelElse = str(o.frame.getNewLabel())
            labelExit = str(o.frame.getNewLabel())
            self.emit.printout(if_exprCode)
            self.emit.printout(self.emit.emitIFFALSE(labelElse, o.frame))
            ast.thenStmt.accept(self, o)
            self.emit.printout(self.emit.emitGOTO(labelExit, o.frame))
            self.emit.printout(self.emit.emitLABEL(labelElse, o.frame))
            ast.elseStmt.accept(self, o)
            self.emit.printout(self.emit.emitLABEL(labelExit, o.frame))
        else:
            labelExit = str(o.frame.getNewLabel())
            self.emit.printout(if_exprCode)
            self.emit.printout(self.emit.emitIFFALSE(labelExit, o.frame))
            ast.thenStmt.accept(self, o)
            self.emit.printout(self.emit.emitLABEL(labelExit, o.frame))



    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(int(ast.value), o.frame), BoolType()

    
    def visitBinaryOp(self, ast, o):
        frame = o.frame
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        op = str(ast.op)
        typeop = IntType() # type of 1 operand. 
        if op in ["+" , '-' , '*' , '/' , '>' , '>=' , '<' , '<=']:
            if type(e1t) is FloatType or type(e2t) is FloatType : 
                typeop = FloatType()
                if type(e1t) is IntType : 
                    e1c += self.emit.emitI2F(frame)
                if type(e2t) is IntType : 
                    e2c += self.emit.emitI2F(frame)
            
            if op in ['+' , '-'] : 
                return e1c + e2c + self.emit.emitADDOP(ast.op, typeop, frame), typeop
            if op in ['*' , '/'] : 
                return e1c + e2c + self.emit.emitMULOP(ast.op, typeop, frame), typeop

            if op in ['>' , '>=' , '<' , '<='] : 
                return e1c + e2c + self.emit.emitREOP(ast.op, typeop, frame), BoolType()
        
        elif op == '%' : 
            return e1c + e2c + self.emit.emitMOD(frame), typeop
        
        elif op in ['==' , '!='] :
            return e1c + e2c + self.emit.emitREOP(ast.op, typeop, frame), BoolType()

        elif op in ['||' , '&&'] : 
            code = ""
            if op == '||' : 
                true_label = str(frame.getNewLabel())
                end_label = str(frame.getNewLabel())
                code += e1c 
                code += self.emit.emitIFTRUE(true_label, frame)
                code += e2c 
                code += self.emit.emitIFTRUE(true_label, frame)
                code += self.emit.emitPUSHICONST("false", frame)
                code += self.emit.emitGOTO(end_label, frame)
                code += self.emit.emitLABEL(true_label, frame)
                code += self.emit.emitPUSHICONST("true", frame)
                code += self.emit.emitLABEL(end_label, frame)
            else : 
                true_label = str(frame.getNewLabel())
                end_label = str(frame.getNewLabel())
                code += e1c 
                code += self.emit.emitIFFALSE(true_label, frame)
                code += e2c 
                code += self.emit.emitIFFALSE(true_label, frame)
                code += self.emit.emitPUSHICONST("true", frame)
                code += self.emit.emitGOTO(end_label, frame)
                code += self.emit.emitLABEL(true_label, frame)
                code += self.emit.emitPUSHICONST("false", frame)
                code += self.emit.emitLABEL(end_label, frame)        
            return code, BoolType()
        elif op in ['+.' , '==.'] : 
            if op == "+.":
                mtype = MType([StringType()], StringType())
                opCode = self.emit.emitINVOKEVIRTUAL('java/lang/String/concat', mtype, o.frame)
                return e1c + e2c + opCode , StringType()

            elif op == "==." : 
                return e1c + e2c + BoolType()
        print("????????")





    def visitUnaryOp(self, ast, o):
        body = self.visit(ast.body, o)
        frame = o.frame
        if str(ast.op) == '-':
            return body[0] + self.emit.emitNEGOP(body[1], frame), body[1]
        if str(ast.op) == '!':
            return body[0] + self.emit.emitNOT(body[1], frame), body[1]
