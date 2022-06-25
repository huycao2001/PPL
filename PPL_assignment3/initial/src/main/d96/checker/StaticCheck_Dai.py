
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

def getTheRoot(c):
    while (c.parentScope != None):
        c = c.parentScope
    return c

# return node of Class
def getTheClassWithName(c, name):
    while (c.parentScope != None):
        c = c.parentScope
    for i in c.children:
        if i.symbol.name == name:
            return i
    return None

def returnType(c, name):
    while(c.parentScope != None ): 
        for i in c.children:
            if i.symbol.name == name:
                return i.symbol.mtype # Class type (with CLass name)
        c = c.parentScope # Move up to thr previous scope.
    return None # 

def isInFor(c):
    while(c.parentScope.parentScope != None ): 
        #print('aaaaa', c.parentScope.symbol)
        if (type(c.parentScope.symbol.mtype) == ForFlag):
            return True
        c = c.parentScope
    return False

def findAllMem(c, name, attribute = True):
    currentScope = getTheClassWithName(c, name)
    if attribute:
        arrAttribute = [x for x in currentScope.children if type(x.symbol.mtype) != MType]
    else:
        arrAttribute = [x for x in currentScope.children if type(x.symbol.mtype) == MType]
    if currentScope.symbol.inherit == None:
        return arrAttribute
    else:
        return arrAttribute + findAllMem(currentScope, currentScope.symbol.inherit, attribute)

def checkCoerceType(typeDecl, typeAssign, c = None):
    if type(typeDecl) is FloatType:
        if type(typeAssign) in [FloatType, IntType]:
            return True
    elif type(typeDecl) == ClassType and type(typeAssign) == ClassType:
        if typeDecl.classname.name == typeAssign.classname.name:
            return True
               
        classDecl = typeAssign.classname.name
        returnNodeClass = getTheClassWithName(c, classDecl)
        if returnNodeClass.symbol.inherit is None:
            return False
        else:
            return checkCoerceType(typeDecl, ClassType(Id(returnNodeClass.symbol.inherit)))
        
    return type(typeDecl) == type(typeAssign)

def getTheClassAtPosition(c):
    while (type(c.parentScope.symbol.mtype) != CType):
        c = c.parentScope
    return c.parentScope
    
def CheckIllegalConstExpression(target , scope) : # target is the expression we want to check.
    if type(target) == Id : 
        while(scope.parent.symbol.type != CType ) : 
            return
    return

class CType: 
    def __str__(self):
        return "typeOfClass"

class BlockFlag:
    def __str__(self):
        return "BlockFlag"

class IfFlag:
    def __str__(self):
        return "IfFlag"

class ForFlag:
    def __str__(self):
        return "ForFlag"

class ElifFlag:
    def __str__(self):
        return "ElifFlag"


#check continue nam trong for k

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __repr__(self):
        return "MType([" + ', '.join(str(x) for x in self.partype) + "], " + str(self.rettype) + ")"

class node(object):
    def __init__(self, symbol, children = [], parentScope = None):
        self.symbol = symbol
        self.children = children
        self.parentScope = parentScope

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.symbol)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return str(self.symbol)

class Symbol:
    def __init__(self,name,mtype,value = None,kind=None,inherit=None,isConstant=False):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind #static or instance
        self.inherit = inherit # chi dung cho class a:A (type: classType(ID(A)))
        self.isConstant = isConstant

    def __repr__(self):
        return "Symbol(" + str(self.name) + ", " + str(self.mtype) + ', ' + str(self.value) + ', ' + str(self.kind) + ', ' + str(self.inherit) +")"

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    returnTypeStack = []

    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast,[])

    def visitProgram(self,ast, c): 
        c = node('Program', [], None)
        a = [self.visit(x,c) for x in ast.decl]
        print(c)
        return []

    def visitClassDecl(self, ast:ClassDecl, c):
        children = c.children
        className = self.visit(ast.classname, (c, 'CHECK_REDECLARED', Class()))
        inherit = self.visit(ast.parentname, (c, 'CHECK_UNDECLARED_CLASS', Class(), ast.parentname.name)) if ast.parentname is not None else None
        nodeClass = node(Symbol(className, CType(), None, None, inherit), [], c)
        children.append(nodeClass)
        for mem in ast.memlist:
            self.visit(mem, nodeClass)
        return 

    def visitId(self, ast: Id, c):
        currentNode = c[0]
        #c: [currentNode, "Check is arraytype", arr.lhs]
        if c[1] == 'CHECK_IS_ARRAYTYPE':
            typeOfObject = returnType(currentNode, c[2].arr.name)
            if type(typeOfObject) != ArrayType:
                raise TypeMismatchInExpression(c[2])

        if c[1] =='CHECK_CANNOT_ASSIGN_TO_CONSTANT':
            currentNode = currentNode.parentScope
            while (currentNode.parentScope != None):
                for x in currentNode.children:
                    if ast.name == x.symbol.name:
                        if x.symbol.isConstant:
                            raise CannotAssignToConstant(c[2])
                            
                currentNode = currentNode.parentScope            
            return ast.name

        if (c[1] == 'CHECK_UNDECLARED_IDENTIFIER'):
            while (currentNode.parentScope != None):
                identifierList = [x for x in currentNode.children]
                for i in identifierList:
                    if ast.name == i.symbol.name:
                        return i
                currentNode = currentNode.parentScope
            raise Undeclared(c[2], ast.name)

        if c[1] == 'CHECK_UNDECLARED_CLASS': 
            findClass = getTheClassWithName(currentNode, c[3])
            if findClass == None:
                raise Undeclared(c[2], ast.name)
            
        if c[1] == 'CHECK_UNDECLARED_ATTRIBUTE':
            typeOfObject = returnType(currentNode, c[2])
            attributeSymbolInClass = findAllMem(currentNode, typeOfObject.classname.name)
            for i in attributeSymbolInClass:
                if ast.name == i.symbol.name:
                    return i
            return None

        if c[1] == 'CHECK_UNDECLARED_METHOD':
            typeOfObject = returnType(currentNode, c[2])
            methodSymbolInClass = findAllMem(currentNode, typeOfObject.classname.name, False)
            for i in methodSymbolInClass:
                if ast.name == i.symbol.name:
                    #fix return type method
                    return i
            return None
        
        if c[1] == 'CHECK_REDECLARED':
            if ast.name in [x.symbol.name for x in currentNode.children]:
                raise Redeclared(c[2], ast.name)
            else:
                if (type(c[2]) is not Class):
                    #check bien static duoc declare o class khac
                    root = getTheRoot(currentNode)
                    if ast.name in [j.symbol.name for x in root.children for j in x.children if type(j.symbol.kind) is Static]:
                        raise Redeclared(c[2], ast.name)
                
        return ast.name
    
    # sua code cua thang ngu kia ( ||||| )
    # .............................VVVVV

    def visitAttributeDecl(self,ast: AttributeDecl, c):
        children = c.children
        name = self.visit(ast.decl.variable, (c, 'CHECK_REDECLARED', Attribute())) if type(ast.decl) is VarDecl else self.visit(ast.decl.constant, (c, 'CHECK_REDECLARED', Attribute()))
        mtype = ast.decl.varType if type(ast.decl) is VarDecl else ast.decl.constType
        value = ast.decl.varInit if type(ast.decl) is VarDecl else ast.decl.value
        kind = ast.kind
        nodeAttr = node(Symbol(name, mtype, value, kind), [], c)
        children.append(nodeAttr)

        return 

    def visitMethodDecl(self,ast: MethodDecl, c):
        children = c.children
        name = self.visit(ast.name, (c, 'CHECK_REDECLARED', Method()))
        mtype = MType([], VoidType())
        symbolMethod = Symbol(name, mtype, None, ast.kind)
        nodeMethod = node(symbolMethod, [], c)
        children.append(nodeMethod)
        for param in ast.param:
            self.visit(param, (nodeMethod, 'PARAM'))
        self.visit(ast.body, nodeMethod)
        symbolMethod.mtype.partype = [param.varType for param in ast.param]
        symbolMethod.mtype.rettype = self.returnTypeStack.pop() if len(self.returnTypeStack) != 0 else VoidType()        
        return

    def visitVarDecl(self,ast: VarDecl, c_flag):
        c, flag = c_flag
        children = c.children
        name = self.visit(ast.variable, (c, 'CHECK_REDECLARED', Parameter() if flag=='PARAM' else Variable()))
        mtype = ast.varType
        value = ast.varInit
        nodeVarDecl = node(Symbol(name, mtype, value, Instance()), [], c)
        children.append(nodeVarDecl)
        if type(mtype) is ClassType:
            self.visit(ast.varType.classname, (c, 'CHECK_UNDECLARED_CLASS', Class(), mtype.classname.name))
        if not((value is None) or ( isinstance(value, NullLiteral))):
            typeRHS = self.visit(ast.varInit, nodeVarDecl)
            if not checkCoerceType(ast.varType, typeRHS, c):
                raise TypeMismatchInStatement(ast)
        
        return

    def visitConstDecl(self,ast: ConstDecl, c_flag):
        c, flag = c_flag
        children = c.children
        name = self.visit(ast.constant, (c, 'CHECK_REDECLARED', Constant()))
        mtype = ast.constType
        value = ast.value

        nodeConstDecl = node(Symbol(name, mtype, value, Instance(), isConstant=True), [], c)
        children.append(nodeConstDecl)
        if type(mtype) is ClassType:
            self.visit(ast.constType.classname, (c, 'CHECK_UNDECLARED_CLASS', Class(), mtype.classname.name))
        
        if not((value is None) or ( isinstance(value, NullLiteral))):
            typeRHS = self.visit(ast.value, nodeConstDecl)
            if not checkCoerceType(ast.constType, typeRHS, c):
                raise TypeMismatchInConstant(ast)

        
        return

    def visitBlock(self, ast: Block, c):
        children = c.children
        
        for inst in ast.inst:
            if type(inst) in [VarDecl, ConstDecl]:
                self.visit(inst, (c, 'INST'))
            else:
                nodeScope = None
                if type(inst) is Assign:
                    nodeScope = node(Symbol("Assign", (None, None)),[], c)
                elif type(inst) in [CallStmt]:
                    nodeScope = node(Symbol("CallStmt", (None, None)),[], c)
                elif type(inst) in [Block]:
                    nodeScope = node(Symbol("Block", (None, None)),[], c)
                elif type(inst) in [Return]:
                    nodeScope = node(Symbol("Return", (None, None)),[], c)
                elif type(inst) in [Break]:
                    nodeScope = node(Symbol("Break", None),[], c)
                elif type(inst) in [Continue]:
                    nodeScope = node(Symbol("Continue", None),[], c)
                elif type(inst) in [If]:
                    nodeScope = node(Symbol("If", IfFlag()),[], c)
                elif type(inst) in [For]:
                    nodeScope = node(Symbol("For", ForFlag()),[], c)
                children.append(nodeScope)
                self.visit(inst, nodeScope)
        return

    def visitAssign(self, ast: Assign, c):
        children = c.children
        typeLHS = None
        if type(ast.lhs) == Id:
            self.visit(ast.lhs, (c, 'CHECK_CANNOT_ASSIGN_TO_CONSTANT', ast))
            nodeAssignID = self.visit(ast.lhs, (c, 'CHECK_UNDECLARED_IDENTIFIER', Identifier()))
            typeOfID = nodeAssignID.symbol.mtype
            nodeAssign = node(Symbol(ast.lhs.name, typeOfID), [], c)
            children.append(nodeAssign)
            typeLHS = typeOfID

        elif type(ast.lhs) == FieldAccess:
            typeLHS = self.visit(ast.lhs, c)
        
        elif type(ast.lhs) == ArrayCell:
            if type(ast.lhs.arr) == Id:
                nameID = self.visit(ast.lhs.arr, (c, 'CHECK_IS_ARRAYTYPE', ast.lhs))
                typeLHS = returnType(c, nameID).eleType
                
            if not all(isinstance(ele, IntLiteral) for ele in ast.lhs.idx):
                raise TypeMismatchInExpression(ast.lhs)
        
        typeRHS = self.visit(ast.exp, c)
        if not checkCoerceType(typeLHS, typeRHS, c):
            raise TypeMismatchInStatement(ast)

        return

    def visitIf(self,ast:If, c): 
        self.visit(ast.expr, c)
        self.visit(ast.thenStmt, c)
        if ast.elseStmt != []:
            nodeElseIf = node(Symbol("ElseIf", ElifFlag()), [], c.parentScope)
            c.parentScope.children.append(nodeElseIf)
            self.visit(ast.elseStmt, nodeElseIf)
        else: None
        return

    def visitFor(self,ast:For, c): 
        expr1Type = self.visit(ast.expr1, c)
        expr2Type = self.visit(ast.expr2, c)
        if not (checkCoerceType(expr1Type, IntType(), c) and checkCoerceType(expr2Type,IntType(), c)):
            raise TypeMismatchInStatement(ast)
        expr3Type = self.visit(ast.expr3, c) if ast.expr3 is not None else None
        self.visit(ast.loop, c)
    
    def visitCallStmt(self,ast:CallStmt, c): 
        #children = c.children
        if type(ast.obj) == Id:
            nodeMethod = self.visit(ast.method, (c, 'CHECK_UNDECLARED_METHOD', ast.obj.name))
            if nodeMethod == None:
                raise Undeclared(Method(), ast.method.name)

            if type(nodeMethod.symbol.mtype.rettype) is not VoidType:
                raise TypeMismatchInStatement(ast)
            
            typeDeclList = [x for x in nodeMethod.symbol.mtype.partype]
            typeAssignList = [self.visit(x, c) for x in ast.param]
            if len(typeDeclList) != len(typeAssignList):
                raise TypeMismatchInStatement(ast)
            for (typeDecl, typeAssign) in zip(typeDeclList,typeAssignList):
                if not checkCoerceType(typeDecl, typeAssign, c):
                    raise TypeMismatchInStatement(ast)
            return nodeMethod.symbol.mtype.rettype
        return
        
    def visitReturn(self,ast:Return, c): 
        returnType = self.visit(ast.expr, c)
        self.returnTypeStack.append(returnType)
    
    def visitBreak(self,ast:Break, c): 
        if isInFor(c):
            c.children.append(node(Symbol("Break", None), [], c))
        else:
            raise MustInLoop(ast)

    def visitContinue(self,ast:Continue, c): 
        if isInFor(c):
            c.children.append(node(Symbol("Continue", None), [], c))
        else:
            raise MustInLoop(ast)

    def visitBinaryOp(self, ast:BinaryOp, c):
        typeLeft = self.visit(ast.left, c)
        typeRight = self.visit(ast.right, c)
        op = ast.op
        if op in ['+', '-', '*', '/']:
            if not isinstance(typeLeft, (IntType, FloatType)) or not isinstance(typeRight, (IntType, FloatType)):
                raise TypeMismatchInExpression(ast)
            if isinstance(typeLeft, FloatType) or isinstance(typeRight, FloatType):
                return FloatType()
            return IntType()
        elif op in ['%']:
            if not isinstance(typeLeft, IntType) or not isinstance(typeRight, IntType):
                raise TypeMismatchInExpression(ast)
            return IntType()
        elif op in ['&&', '||']:
            if not isinstance(typeLeft, BoolType) or not isinstance(typeRight, BoolType):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif op in ['==.', '+.']:
            if not isinstance(typeLeft, StringType) or not isinstance(typeRight, StringType):
                raise TypeMismatchInExpression(ast)
            if op == '==.':
                return BoolType()
            return StringType()
        elif op in ['==', '!=']:
            if not isinstance(typeLeft, (IntType, BoolType)) or not isinstance(typeRight, (IntType, BoolType)):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif op in ['==', '!=']:
            if not isinstance(typeLeft, (IntType, BoolType)) or not isinstance(typeRight, (IntType, BoolType)):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif op in ['<', '>', '<=', '>=']:
            if not isinstance(typeLeft, (IntType, FloatType)) or not isinstance(typeRight, (IntType, FloatType)):
                raise TypeMismatchInExpression(ast)
            return BoolType()

    def visitUnaryOp(self, ast: UnaryOp, c):
        exp = self.visit(ast.body, c)
        op = ast.op
        if op in ['-']:
            if not isinstance(exp, (IntType, FloatType)):
                raise TypeMismatchInExpression(ast)
            return IntType() if isinstance(exp, IntType) else FloatType()
        if op in ['!']:
            if not isinstance(exp, BoolType):
                raise TypeMismatchInExpression(ast)
            return BoolType()

    
    def visitNewExpr(self,ast:NewExpr, c): 
        return ClassType(Id(ast.classname.name))

    def visitCallExpr(self, ast:CallExpr, c):
        if type(ast.obj) == Id:
            #check co phai object cua 1 class nao do khong
            nodeMethod = self.visit(ast.method, (c, 'CHECK_UNDECLARED_METHOD', ast.obj.name))
            if nodeMethod == None:
                raise TypeMismatchInExpression(ast)
            
            if type(nodeMethod.symbol.mtype.rettype) is VoidType:
                raise TypeMismatchInExpression(ast)
            
            typeDeclList = [x for x in nodeMethod.symbol.mtype.partype]
            typeAssignList = [self.visit(x, c) for x in ast.param]
            if len(typeDeclList) != len(typeAssignList):
                raise TypeMismatchInExpression(ast)
            for (typeDecl, typeAssign) in zip(typeDeclList,typeAssignList):
                if not checkCoerceType(typeDecl, typeAssign, c):
                    raise TypeMismatchInExpression(ast)
            return nodeMethod.symbol.mtype.rettype

    def visitFieldAccess(self,ast:FieldAccess, c): 
        typeRHS = None
        if type(ast.obj) == Id:  
            nodeFieldAccess = self.visit(ast.fieldname, (c, 'CHECK_UNDECLARED_ATTRIBUTE', ast.obj.name))
            if nodeFieldAccess == None:
                raise Undeclared(Attribute(), ast.fieldname.name)
            typeRHS = nodeFieldAccess.symbol.mtype
            
        elif type(ast.obj) == SelfLiteral:
            isUndeclared = True
            returnNodeClass = getTheClassAtPosition(c)
            attributeList = [x for x in returnNodeClass.children if type(x.symbol.mtype) != MType]
            for i in attributeList:
                if ast.fieldname.name == i.symbol.name:
                    typeRHS = i.symbol.mtype
                    isUndeclared = False
            if isUndeclared:
                raise Undeclared(Attribute(), ast.fieldname.name)
        return typeRHS    

    def visitInstance(self,ast, c): 
        pass

    def visitStatic(self,ast, c): 
        pass

    def visitArrayType(self,ast, c): 
        return ArrayType()
    
    def visitClassType(self,ast, c): 
        return ClassType()
    
    def visitVoidType(self,ast, c): 
        return VoidType()

    def visitIntType(self,ast, c): 
        return IntType()
    
    def visitFloatType(self,ast, c): 
        return FloatType()
    
    def visitBoolType(self,ast, c): 
        return BoolType()
    
    def visitStringType(self,ast, c): 
        return StringType()
    

    def visitArrayLiteral(self,ast, c): 
        pass

    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitFloatLiteral(self,ast, c): 
        return FloatType()
    
    def visitStringLiteral(self,ast, c): 
        return StringType()
    
    def visitBooleanLiteral(self,ast, c): 
        return BoolType()
    
    def visitNullLiteral(self,ast, c): 
        pass

    def visitSelfLiteral(self,ast, c): 
        pass

    
