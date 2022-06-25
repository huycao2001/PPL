
"""
 * @author nhphung
"""
from copyreg import constructor
from inspect import getmembers
from AST import * 
from Visitor import *
# from Utils import Utils
from StaticError import *


def getRoot(c):
    while (c.parent is not None):
        c = c.parent
    return c

def getClassNode(c, name):
    while (c.parent is not None):
        c = c.parent
    for node in c.children:
        if node.symbol.name == name:
            return node
    return None

def isClassName(c, name) : 
    while (c.parent is not None):
        c = c.parent
    for node in c.children:
        if node.symbol.name == name:
            return True
    return False


def returnType(c, name):
            # parentClass = scope.parent
            # while(type(parentClass.symbol.mtype) != CType) :
    if type(c.parent.symbol.mtype) is CType : # already at method. 
        for i in c.children : 
            if i.symbol.name == name :
                return i.symbol.mtype
        return None
    else :
        #parentClass = c

        while(type(c.parent.symbol.mtype) is not CType) :

            for child in c.parent.children : 
                if name == child.symbol.name : 
                    return child.symbol.mtype
            c = c.parent
        return None

def findMembers(c, name, attribute = True):
    # name is Class ID.
    # attribute is set to True when we are looking for att 
    # attribute is set to false when are looking for methods.
    currentScope = getClassNode(c, name) # Find the Class node
    if attribute:
        members = [node for node in currentScope.children if type(node.symbol.mtype) is not MType]
    else:
        members = [node for node in currentScope.children if type(node.symbol.mtype) is MType]
    return members
 
def isSameType(typeDecl, typeAssign ,c= None ):

    if type(typeDecl) is FloatType:
        if type(typeAssign) in [FloatType, IntType]:
            return True
    elif type(typeDecl) is ArrayType and type(typeAssign) is ArrayType:

        if typeDecl.size == typeAssign.size and isSameType(typeDecl.eleType , typeAssign.eleType , c ):
            return True 
        return False
    elif type(typeDecl) is ClassType and type(typeAssign) is ClassType:
        if typeDecl.classname.name == typeAssign.classname.name:
            return True
        return typeDecl.classname.name == typeAssign.classname.name
    if type(typeDecl) is type(typeAssign) :
        return True
        
    return False




def IsValidValueForAttribute(target) : 
    if type(target) is Id : 
        raise Undeclared(Identifier() , target.name)
    if type(target) is FieldAccess : 
        if type(target.obj) is Id and target.fieldname.name[0] != "$" : 
            raise Undeclared(Identifier() , target.obj.name)
        if type(target.obj) is Id and target.fieldname.name[0] == "$" :
            return
        if type(target.obj) is SelfLiteral : 
            return
        IsValidValueForAttribute(target.obj)
    elif type(target) is CallExpr : 
        if type(target.obj) is Id : 
            raise Undeclared(Identifier() , target.obj.name)
        if type(target.obj) is Id and target.fieldname.name[0] == "$" :
            for param in target.param : 
                IsValidValueForAttribute(param)
            return 
        if type(target.obj) is SelfLiteral :
            for param in target.param : 
                IsValidValueForAttribute(param) 
            return
        IsValidValueForAttribute(target.obj)

class CType: 
    def __str__(self):
        return "typeOFClass"

class IfFlag:
    def __str__(self):
        return "IfFlag"
class ElifFlag:
    def __str__(self):
        return "ElifFlag"

class ForType:
    def __str__(self):
        return "ForType"





class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __repr__(self):
        return "MType([" + ', '.join(str(x) for x in self.partype) + "], " + str(self.rettype) + ")"

# pass down the parent node to the children and children will be added there. 

class node(object):
    def __init__(self, symbol, children = [], parent = None):
        self.symbol = symbol
        self.children = children
        self.parent = parent

    def __str__(self, level=0):
        clone = "None" if self.parent is None else self.parent.symbol.name
        ret = "\t" * level + repr(self.symbol) + " , Parent node is " + clone + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return str(self.symbol)

class Symbol:
    def __init__(self,name,mtype,value = None,kind=None , superClass=None , isConst = False):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind 
        self.superClass = superClass 
        self.isConst = isConst 

    def __repr__(self):
        return "Symbol(" + str(self.name) + ", " + str(self.mtype) + ', ' + str(self.value) + ', ' + str(self.kind) + ', ' + str(self.superClass) + ', '+  str(self.isConst) + ")"

class StaticChecker(BaseVisitor):

    global_envi = [

    ]

    MethodTypeStack = []
    
    ArrLitisIllegal = False
    
    def __init__(self,ast):
        self.ast = ast

    def check(self):
        self.MethodTypeStack = []
        self.ArrLitisIllegal = False
        return self.visit(self.ast,[])

    def visitProgram(self,ast, c): 
        c = node(Symbol('ProgramRoot' , None ), [], None)
        a = [self.visit(x,c) for x in ast.decl]
        ProgramClassNode = None
        print(c)
        root = getRoot(c)
        for class_node in root.children : 
            if class_node.symbol.name == "Program" :
                ProgramClassNode = class_node
                break 
        if ProgramClassNode is None : 
            raise NoEntryPoint()
        else : 
            main_node = None
            for method_node in ProgramClassNode.children :
                if method_node.symbol.name == "main" : 
                    main_node = method_node
            if main_node is None : 
                raise NoEntryPoint()
            else :
                if main_node.symbol.mtype.partype != [] or type(main_node.symbol.mtype.rettype) is not VoidType : 
                    raise NoEntryPoint()
                # return []
        
        return []

    def visitClassDecl(self, ast:ClassDecl, c):
        children = c.children
        className = self.visit(ast.classname, (c, 'REDECLARED CHECK', Class()))
        superClass = self.visit(ast.parentname, (c, 'UNDECLARED CLASS CHECK', Class(), ast.parentname.name)) if ast.parentname is not None else None
        nodeClass = node(Symbol(className, CType(), None, None, superClass), [], c) # c is program Node
        children.append(nodeClass)
        for mem in ast.memlist:
            self.visit(mem, nodeClass)
        return 

    def visitId(self, ast: Id, c):
        # c[0] is the upper node we pass in.
        # c[1] is the type of checking, like a service.
        # c[2] is the object that we need to check. 
        # c[3] is name of object to check undeclared

        if type(c) is not tuple : 
            while(type(c.symbol.mtype) is not CType ) : 

                for node in c.children : 
                    if ast.name == node.symbol.name : 
                        return node.symbol.mtype
                c = c.parent

            raise Undeclared(Identifier() , ast.name)
        
        currentNode = c[0]       
        if c[1] == 'IS ARRAY TYPE':
            # c[2] is an array cell 
            typeOfObject = returnType(currentNode, c[2].arr.name)
            if typeOfObject is None : 
                raise Undeclared(Identifier() , c[2].arr.name)
            if type(typeOfObject) is not ArrayType:
                raise TypeMismatchInExpression(c[2])

        ### REMEMBER THIS ### Still out of scope
        if c[1] =='CANNOT ASSIGN TO CONST CHECK':

            currentNode = currentNode.parent

            while (currentNode.parent is not None):
                for x in currentNode.children:
                    if ast.name == x.symbol.name:
                        if x.symbol.isConst:
                            raise CannotAssignToConstant(c[2])
                        

                currentNode = currentNode.parent            
            return ast.name

        if (c[1] == 'UNDECLARED IDENTIFIER CHECK'):            
            while(type(currentNode.symbol.mtype) is not CType) :
                for child in currentNode.children : 
                    if ast.name == child.symbol.name : 
                        return child
                currentNode = currentNode.parent
            raise Undeclared(Identifier(), ast.name)


        if c[1] == 'UNDECLARED CLASS CHECK': 
            root = currentNode
            ClassExist = False
            while(root.parent is not None):
                root = root.parent
            for node in root.children : 
                if c[3] == node.symbol.name :
                    ClassExist = True
                    break
            if ClassExist == False : 
                raise Undeclared(Class(), ast.name)

            
        if c[1] == 'UNDECLARED ATTRIBUTE CHECK':
            # c[2] is the field access
            ClassOfObject = returnType(currentNode, c[2].obj.name) # Type of this object
            if(ClassOfObject is None ) : # We have to check if c[2] is a class name or not ? , if yes -> illegal member access.
                if isClassName( currentNode, c[2].obj.name) == True : 
                    raise IllegalMemberAccess(c[2])
                raise Undeclared(Identifier() , c[2].obj.name)
            if type(ClassOfObject) is not ClassType : 
                raise IllegalMemberAccess(c[2])
            ClassAttributes = findMembers(currentNode, ClassOfObject.classname.name )
            for att_node in ClassAttributes : 
                if ast.name == att_node.symbol.name : 
                    return att_node
            raise Undeclared(Attribute(), ast.name)

        if c[1] == 'UNDECLARED METHOD CHECK':
            # c[3] is the instance => We will have to find which class this object belongs to
            # c[3] is ID.

            objectName = c[2]
            ClassOfObject = returnType(currentNode, c[2].obj.name) # ClassType object with classname as ID() from AST
            if(ClassOfObject is None ) : ####### REMEMBER THIS ##### 
                if isClassName( currentNode, c[2].obj.name) == True :
                    raise IllegalMemberAccess(c[2])
                raise Undeclared(Identifier() , c[2].obj.name)
            # must be a class.
            if type(ClassOfObject) is not ClassType : 
                raise IllegalMemberAccess(c[2])
            ClassMethods = findMembers(currentNode, ClassOfObject.classname.name, False)
 
            for method_node in ClassMethods : 
                if ast.name == method_node.symbol.name : 
                    return method_node
            raise Undeclared(Method(), ast.name) # undeclared method
                

        if c[1] == 'REDECLARED CHECK':
            # the current node should be the upper node of the scope we want to check. 
            # Ex : if c[2] is attribute then currentNode should be a Class Node.
            if type(c[2]) is Method : 
                for child in currentNode.children :
                    if ast.name == child.symbol.name and type(child.symbol.mtype) is MType : 
                        raise Redeclared(c[2], ast.name)
            elif type(c[2]) is Attribute : 
                for child in currentNode.children :
                    if ast.name == child.symbol.name and type(child.symbol.mtype) is not MType : 
                        raise Redeclared(c[2], ast.name) 
            else : 
                for child in currentNode.children : 
                    if ast.name == child.symbol.name :
                        raise Redeclared(c[2], ast.name)    

            # else: # 2 Static vars may not have the same ClassNode but they have global scope. 
            #     if (type(c[2]) is Attribute or type(c[2]) is Method ): 
            #         root = currentNode 
            #         while(root.parent is not None) : root = root.parent
            #         for class_node in root.children : 
            #             for att_method_node in class_node.children : 
            #                 if type(att_method_node.symbol.kind) is Static and ast.name == att_method_node.symbol.name:
            #                     raise Redeclared(c[2], ast.name)      

                
        return ast.name
    

# class AttributeDecl(MemDecl):
#     kind: SIKind  # Instance or Static
#     decl: StoreDecl  # VarDecl for mutable or ConstDecl for immutable
    def visitAttributeDecl(self,ast: AttributeDecl, c):
        children = c.children
        name = None
        if type(ast.decl) is VarDecl : 
            name = self.visit(ast.decl.variable, (c, 'REDECLARED CHECK', Attribute()))
        else :
            name = self.visit(ast.decl.constant, (c, 'REDECLARED CHECK', Attribute()))
        #### REMEMBER THIS ####
        ## Havent checked the type and the class yet.
        mtype = ast.decl.varType if type(ast.decl) is VarDecl else ast.decl.constType
        if type(mtype) is ClassType and type(ast.decl) is VarDecl:
            self.visit(ast.decl.varType.classname, (c, 'UNDECLARED CLASS CHECK', Class(), mtype.classname.name))
        elif type(mtype) is ClassType and type(ast.decl) is ConstDecl:
            self.visit(ast.decl.constType.classname, (c, 'UNDECLARED CLASS CHECK', Class(), mtype.classname.name))

        value = ast.decl.varInit if type(ast.decl) is VarDecl else ast.decl.value

        # we should have a check here, only allow lieral, 
        IsValidValueForAttribute(value)
        if type(ast.decl) is VarDecl : 
            if not((value is None) or ( isinstance(value, NullLiteral))) : 
                VarInit = self.visit(ast.decl.varInit, c)
                if self.ArrLitisIllegal == True and type(VarInit) is ArrayType : 
                    raise IllegalArrayLiteral(value)
                if  isSameType(ast.decl.varType, VarInit , c) == False:
                    raise TypeMismatchInStatement(ast.decl)
        else : # ConstDecl 
            if not((value is None) or ( isinstance(value, NullLiteral))) : 
                ValInit = self.visit(ast.decl.value, c)
                if self.ArrLitisIllegal == True and type(ValInit) is ArrayType : 
                    raise IllegalArrayLiteral(value)
                if self.isValueConst(ast.decl.value ,c) == False :
                    raise IllegalConstantExpression(ast.decl.value)
                if  isSameType(ast.decl.constType, ValInit , c) == False:
                    raise TypeMismatchInConstant(ast.decl)
                
            else : 
                raise IllegalConstantExpression(None)
            
            # if self.isValueConst(ast.decl.value ,c) == False :
            #     raise IllegalConstantExpression(ast.decl.value)
        kind = ast.kind # Static or Instance
        isConst = False if type(ast.decl) is VarDecl else True
        AttNode= node(Symbol(name, mtype, value, kind , None, isConst ), [], c) # c is Class Node.
        children.append(AttNode)

        return 

    def visitMethodDecl(self,ast: MethodDecl, c):
        children = c.children
        name = self.visit(ast.name, (c, 'REDECLARED CHECK', Method()))
        mtype = MType([], VoidType()) #### [Input Type] -> Output Type
        value = None 
        symbolMethod = Symbol(name, mtype, value, ast.kind)
        MethodNode = node(symbolMethod, [], c)
        children.append(MethodNode)
        # param is a Var Decl
        for param in ast.param:
            self.visit(param, (MethodNode, 'PARAM'))
        self.visit(ast.body, MethodNode) # Visit Block
        symbolMethod.mtype.partype = [param.varType for param in ast.param]
        symbolMethod.mtype.rettype = self.MethodTypeStack.pop() if len(self.MethodTypeStack) != 0 else VoidType()    
        return



# class VarDecl(StoreDecl):
#     variable: Id
#     varType: Type
#     varInit: Expr = None  # None if there is no initial

    def visitVarDecl(self,ast: VarDecl, c_flag):

        c, flag = c_flag
        name = self.visit(ast.variable, (c, 'REDECLARED CHECK', Parameter() if flag=='PARAM' else Variable()))
        mtype = ast.varType
        value = ast.varInit
        if type(mtype) is ClassType:
            self.visit(ast.varType.classname, (c, 'UNDECLARED CLASS CHECK', Class(), mtype.classname.name))
        # if type(mtype) == ArrayType : 
        #     print("you areerereerer")
        VarDeclNode = node(Symbol(name, mtype, value, Instance()), [], c)
        c.children.append(VarDeclNode)

        if not((value is None) or ( isinstance(value, NullLiteral))):
            
            VarInit = self.visit(ast.varInit, c)
            if self.ArrLitisIllegal == True and type(VarInit) is ArrayType : 
                raise IllegalArrayLiteral(ast.varInit)
            
            if  isSameType(ast.varType, VarInit , c) == False:
                raise TypeMismatchInStatement(ast)
        
        return


# class ConstDecl(StoreDecl):
#     constant: Id
#     constType: Type
#     value: Expr = None # None if there is no initial

    def visitConstDecl(self,ast: ConstDecl, c_flag):

        c, flag = c_flag
        children = c.children
        name = self.visit(ast.constant, (c, 'REDECLARED CHECK', Constant()))
        mtype = ast.constType
        if type(mtype) is ClassType:
            self.visit(ast.constType.classname, (c, 'UNDECLARED CLASS CHECK', Class(), mtype.classname.name))
        value = ast.value

        #print("type of c is" , type(c)) # this is a node
        if value is None or value is type(value) is NullLiteral : 
            raise IllegalConstantExpression(None)
        else : 

            typeRHS = self.visit(ast.value, c)
            if self.ArrLitisIllegal == True and type(typeRHS) is ArrayType :
                raise IllegalArrayLiteral(ast.value) 
            if  isSameType(ast.constType, typeRHS , c) == False:
                raise TypeMismatchInConstant(ast)

        if self.isValueConst(ast.value ,c) == False :
            raise IllegalConstantExpression(ast.value)

        nodeConstDecl = node(Symbol(name, mtype, value, Instance(), None, isConst = True), [], c)
        children.append(nodeConstDecl )
        # if value != None and type(value) != NullLiteral:
        #     expr = self.visit(ast.value, c)
        #     if not isSameType(ast.constType, expr , c):
        #         raise TypeMismatchInConstant(ast)
        return


    def isValueConst(self, target , scope) : # target is the expression we want to check.
        if type(target) is Id : 
            while(type(scope.symbol.mtype) is not CType ) : 
                for node in scope.children : 
                    if target.name == node.symbol.name : 

                        return node.symbol.isConst
                scope = scope.parent

            return False   
        if type(target ) is UnaryOp : 
            return self.isValueConst(target.body , scope) 
        if type(target) is BinaryOp : 
            return self.isValueConst(target.left , scope) and self.isValueConst(target.right , scope)   
        if type(target) in [IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral, ArrayLiteral, NewExpr, SelfLiteral] : 
                return True   
        if type(target) is FieldAccess : 

            if type(target.obj) is SelfLiteral : 
                
                parentClass = scope
                while(type(parentClass.symbol.mtype) is not CType) :
                    parentClass = parentClass.parent
                Attributes_Nodes = [child for child in parentClass.children if type(child.symbol.mtype) is not MType] # list of Node
                
                for i in Attributes_Nodes : 
                    if i.symbol.name == target.fieldname.name : 
                        return i.symbol.isConst
                raise Undeclared(Attribute() , target.fieldname.name)
                
            elif type(target.obj) is Id and target.fieldname.name[0] != '$' :
                ClassName = returnType(scope , target.obj.name)
                ClassNode = getClassNode(scope , ClassName.classname.name)
                Attributes_Nodes = [child for child in ClassNode.children if type(child.symbol.mtype) is not MType] # list of Node
                for i in Attributes_Nodes : 
                    if i.symbol.name == target.fieldname.name : 
                        return i.symbol.isConst
                raise Undeclared(Attribute() , target.fieldname.name)

            elif type(target.obj) is Id and target.fieldname.name[0] == '$' :
                ClassNode = getClassNode(scope , target.obj.name)
                Attributes_Nodes = [child for child in ClassNode.children if type(child.symbol.mtype) is not MType] # list of Node
                for i in Attributes_Nodes : 
                    if i.symbol.name == target.fieldname.name : 
                        return i.symbol.isConst
                raise Undeclared(Attribute() , target.fieldname.name)

            else : # Recursion 
                if self.isValueConst(target.obj, scope) == True : 
                    subexp = self.visit(target.obj, scope)
                    if type(subexp) is not ClassType : 
                        raise IllegalMemberAccess(target.obj) 
                    Attributes_list = findMembers(scope, subexp.classname.name)
                    for att_node in Attributes_list :
                        if att_node.symbol.name == target.fieldname.name and att_node.symbol.isConst == False : 
                            return False
                    return True
                return False
        elif type(target) is CallExpr:

            return self.isValueConst(target.obj , scope)
        if type(target) is ArrayCell : 
            if self.isValueConst(target.arr , scope) == True :
                return True

        return False
        # return


    # class Block(Stmt):
    #     inst: List[Inst]
    def visitBlock(self, ast: Block, c):
        children = c.children
        
        for inst in ast.inst:
            if type(inst) in [VarDecl, ConstDecl]:
                self.visit(inst, (c, 'INST'))
            else:
                nodeScope = None
                if type(inst) is Assign:
                    nodeScope = node(Symbol("Assign", (None, None)),[], c)
                elif type(inst) is CallStmt:
                    nodeScope = node(Symbol("CallStmt", (None, None)),[], c)
                elif type(inst) is Block:
                    nodeScope = node(Symbol("Block", (None, None)),[], c)
                elif type(inst) is Return:
                    nodeScope = node(Symbol("Return", (None, None)),[], c)
                elif type(inst)  is Break:
                    nodeScope = node(Symbol("Break", None),[], c)
                elif type(inst) is Continue:
                    nodeScope = node(Symbol("Continue", None),[], c)
                elif type(inst) is If:
                    nodeScope = node(Symbol("If", IfFlag()),[], c)
                elif type(inst) is For:
                    nodeScope = node(Symbol("For", ForType()),[], c)
                children.append(nodeScope)
                
                self.visit(inst, nodeScope)
        return



    def visitAssign(self, ast: Assign, c):
        # c is an Assign node
        children = c.children
        typeRHS = self.visit(ast.exp, c)
        typeLHS = None
        if type(ast.lhs) is Id:
            self.visit(ast.lhs, (c, 'CANNOT ASSIGN TO CONST CHECK', ast))
            clone = self.visit(ast.lhs, (c, 'UNDECLARED IDENTIFIER CHECK')) # the node
            nameID = clone.symbol.name
            mtype = clone.symbol.mtype
            typeLHS = mtype
            nodeAssignID = node(Symbol(nameID, mtype), [], c)
            children.append(nodeAssignID)

        elif type(ast.lhs) is FieldAccess:
            typeLHS = self.visit(ast.lhs , c )
            if type(ast.lhs.obj) is Id and ast.lhs.fieldname.name[0] == '$' : # A :: $f
                Attributes_list = findMembers(c,ast.lhs.obj.name , True)
                for att_node in Attributes_list :
                    if att_node.symbol.name ==  ast.lhs.fieldname.name and att_node.symbol.isConst == True : 
                        raise CannotAssignToConstant(ast)

            elif type(ast.lhs.obj) is Id and ast.lhs.fieldname.name[0] != '$' : # a.b -> xet a
                ClassObject = returnType(c , ast.lhs.obj.name )
                Attributes_list = findMembers(c , ClassObject.classname.name , True)
                for att_node in Attributes_list :
                    if att_node.symbol.name ==  ast.lhs.fieldname.name and att_node.symbol.isConst == True : 
                        raise CannotAssignToConstant(ast)
            elif type(ast.lhs.obj) is SelfLiteral :  # Self.a~
                parentClass = c
                while(type(parentClass.symbol.mtype) is not CType) : 
                    parentClass = parentClass.parent
                Attributes_list = findMembers(c , parentClass.symbol.name ,True)
                for att_node in Attributes_list :
                    if att_node.symbol.name ==  ast.lhs.fieldname.name and att_node.symbol.isConst == True : 
                        raise CannotAssignToConstant(ast)
                # nodeAssignID = node(Symbol(ast.lhs, typeLHS , ast.exp), [], c)
                # children.append(nodeAssignID)
            else : # Self.x.y
                objType = self.visit(ast.lhs.obj, c) # Should be a class Type
                Attributes_list = findMembers(c, objType.classname.name)
                for att_node in Attributes_list :
                    if att_node.symbol.name ==  ast.lhs.fieldname.name and att_node.symbol.isConst == True : 
                        raise CannotAssignToConstant(ast)
            
                 
        elif type(ast.lhs) is ArrayCell:
            typeLHS = self.visit(ast.lhs , c)
            if type(ast.lhs.arr) is Id : 
                if self.isValueConst(ast.lhs.arr, c) == True : 
                    raise CannotAssignToConstant(ast)
            # elif type(ast.lhs.arr) == FieldAccess : 
            #     objType = self.visit(ast.lhs.arr) 
        
        
        if type(typeRHS) is ArrayType and self.ArrLitisIllegal == True :
            raise IllegalArrayLiteral(ast.exp)

        if isSameType(typeLHS, typeRHS , c) == False:
            raise TypeMismatchInStatement(ast)


    # class If(Stmt):
    #     expr: Expr
    #     thenStmt: Stmt
    #     elseStmt: Stmt = None  # None if there is no else branch
    def visitIf(self,ast:If, c): 
        print("parent of this if is :", type(c.symbol.mtype))
        ExpType = self.visit(ast.expr, c)
        if type(ExpType) is not BoolType : 
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, c)
        if ast.elseStmt is not None : #### REMEMBER THIS #####
            nodeElseIf = node(Symbol("ElseIf", ElifFlag()), [], c.parent)
            c.parent.children.append(nodeElseIf)
            self.visit(ast.elseStmt, nodeElseIf)
        else:  
            return

    # class For(Stmt):
    #     id: Id
    #     expr1: Expr
    #     expr2: Expr 
    #     loop: Stmt
    #     expr3: Expr = None
    def visitFor(self,ast:For, c): 
        idType = self.visit(ast.id , c)
        if self.isValueConst(ast.id , c) == True :             
            raise CannotAssignToConstant(Assign(ast.id, ast.expr1))
        expr1Type = self.visit(ast.expr1, c)
        expr2Type = self.visit(ast.expr2, c)
        if type(idType) is not IntType or type(expr1Type) is not IntType or type(expr2Type) is not IntType :
            raise TypeMismatchInStatement(ast)
        expr3Type = self.visit(ast.expr3, c) if ast.expr3 is not None else None
        if type(expr3Type) is not IntType :
             raise TypeMismatchInStatement(ast)
        self.visit(ast.loop, c) # Visit the statement
    

    # class CallStmt(Stmt):
    #     obj: Expr
    #     method: Id
    #     param: List[Expr]
    def visitCallStmt(self,ast:CallStmt, c): 

        # c should be a CallStmt node. 
        #children = c.children
        # if type(ast.obj) == Id and ast.fieldname.name[0] != '$':  
        if type(ast.obj) is Id and ast.method.name[0] != '$':
            # ast.obj.name is the name type STRING.
            method_id = ast.method
            nodeMethod = self.visit(method_id, (c, 'UNDECLARED METHOD CHECK', ast))
            self.checkParamsAndArs(ast , nodeMethod, c , False)
        
        elif type(ast.obj) is Id and ast.method.name[0] == '$':
            if isClassName(c, ast.obj.name) == True : 
                Methods_list = findMembers(c, ast.obj.name , False)
                # found = False
                nodeMethod = None
                for method_node in Methods_list : 
                    if method_node.symbol.name == ast.method.name :
                        nodeMethod = method_node 
                        break
                self.checkParamsAndArs(ast, nodeMethod, c, False )
            # obj is not a class name -> definitely an error.
            else : 
                object_type = returnType(c , ast.obj.name)
                if object_type is not None : 
                    raise IllegalMemberAccess(ast)
                raise Undeclared(Class() , ast.obj.name)
        ##### REMEMBER THIS        
        elif type(ast.obj) is SelfLiteral : 
            # Find the class first

            parentClass = c
            while(type(parentClass.symbol.mtype) is not CType) : 
                parentClass = parentClass.parent
            Methods_list = findMembers(c , parentClass.symbol.name, False) 

            nodeMethod = None
            for method_node in Methods_list : 
                if ast.method.name == method_node.symbol.name :
                    nodeMethod = method_node
                    break
            self.checkParamsAndArs(ast , nodeMethod , c , False)
            return
        else : # Recursion case. 
            subexp = self.visit(ast.obj , c) # should be a class type with id 
            Methods_list = findMembers(c, subexp.classname.name, False)
            nodeMethod = None 
            for method_node in Methods_list : 
                if ast.method.name == method_node.symbol.name :
                    nodeMethod = method_node
                    break
            self.checkParamsAndArs(ast, nodeMethod, c, False)
        return 

    def visitReturn(self,ast:Return, c):
        # need to check if this is in a constructor or desturctor or not :b
        scope = c 
        while(type(scope.parent.symbol.mtype) is not CType):
            scope = scope.parent
        inProgram = False    
        # if scope.symbol.name == "Constructor" or scope.symbol.name == "Destructor" : 
        #     if ast.expr is not None : 
        #         raise TypeMismatchInStatement(ast)
        if scope.symbol.name == "Constructor" and ast.expr is not None : 
            raise TypeMismatchInStatement(ast)
        if scope.symbol.name == "Destructor" :
            raise TypeMismatchInStatement(ast)
        clone = scope.parent
        if clone.symbol.name == "Program" :
            inProgram = True
        # ko define -> new A(1,2) -> sai 
        returnType = VoidType() if ast.expr is None or type(ast.expr) is VoidType else self.visit(ast.expr, c)
        if scope.symbol.name == "main" :  
            if scope.symbol.mtype.partype == [] and type(returnType) is not VoidType and inProgram == True : 
                raise TypeMismatchInStatement(ast)
        self.MethodTypeStack.append(returnType)
    

    #  while(c.parent != None ): 
    #     if (type(c.parent.symbol.mtype) == ForType):
    #         return True
    #     c = c.parent   
    def visitBreak(self,ast:Break, c): 
        parent = c.parent
        while(parent.parent is not None) : 
            if type(parent.symbol.mtype) is ForType : 
                return
            parent = parent.parent
        
        raise MustInLoop(ast)

    def visitContinue(self,ast:Continue, c): 
        parent = c.parent
        while(parent.parent is not None) : 
            if type(parent.symbol.mtype) is ForType : 
                return
            parent = parent.parent
        raise MustInLoop(ast)

# class CallExpr(Expr):
#     obj: Expr
#     method: Id
#     param: List[Expr]
    def visitCallExpr(self, ast:CallExpr, c):
        
        if type(ast.obj) is Id and ast.method.name[0] != '$':
            nodeMethod = self.visit(ast.method, (c, 'UNDECLARED METHOD CHECK' , ast))
            self.checkParamsAndArs(ast , nodeMethod , c)
            return nodeMethod.symbol.mtype.rettype

        elif type(ast.obj) is Id and ast.method.name[0] == '$':
            if isClassName(c,ast.obj.name) == True :
                
                Methods_list =findMembers(c , ast.obj.name , False)
                nodeMethod = None
                for method_node in Methods_list:
                    if method_node.symbol.name == ast.method.name : 
                        nodeMethod= method_node
                        break
                self.checkParamsAndArs(ast,nodeMethod , c)
                return nodeMethod.symbol.mtype.rettype
            else : 
                
                object_type = returnType(c , ast.obj.name)
                if object_type is not None : 
                    raise IllegalMemberAccess(ast)
                raise Undeclared(Class() , ast.obj.name)

        elif type(ast.obj) is SelfLiteral : 
            #### REMEMBER THIS.
            found = False
            parentClass = c
            while(type(parentClass.symbol.mtype) is not CType) : 
                parentClass = parentClass.parent
            Methods_list = findMembers(c , parentClass.symbol.name, False) 
            nodeMethod = None
            for method_node in Methods_list : 
                if ast.method.name == method_node.symbol.name :
                    nodeMethod = method_node
                    break
            self.checkParamsAndArs(ast , nodeMethod , c)
            return nodeMethod.symbol.mtype.rettype

        else : ### REMEMBER THIS , recursion
            subexp = self.visit(ast.obj , c) # should be a class type with id 
            if(type(subexp) is not ClassType ) : 
                raise IllegalMemberAccess(ast)
            Methods_list = findMembers(c, subexp.classname.name, False)
            nodeMethod = None 
            
            for method_node in Methods_list :
                if ast.method.name == method_node.symbol.name : 
                    nodeMethod = method_node 
                    break
            
            self.checkParamsAndArs(ast , nodeMethod , c)
            return nodeMethod.symbol.mtype.rettype

    def checkParamsAndArs(self, ast, nodeMethod,c , isCallExpr = True) : 
        if nodeMethod is None :
            raise Undeclared(Method() , ast.method.name )
        if type(nodeMethod.symbol.mtype.rettype) is VoidType and isCallExpr == True:
            raise TypeMismatchInExpression(ast)
        elif type(nodeMethod.symbol.mtype.rettype) is not VoidType and isCallExpr == False : 
            raise TypeMismatchInStatement(ast)
        typeDeclList = [x for x in nodeMethod.symbol.mtype.partype] # List of parameters
        typeAssignList = [self.visit(x, c) for x in ast.param] # Arguments 
        if len(typeDeclList) != len(typeAssignList) :
            if isCallExpr == True :
                raise TypeMismatchInExpression(ast)
            else :
                raise TypeMismatchInStatement(ast)
        for (typeDecl, typeAssign) in zip(typeDeclList,typeAssignList):
            if not isSameType(typeDecl, typeAssign , c):
                if isCallExpr == True :
                    raise TypeMismatchInExpression(ast)
                else : 
                    raise TypeMismatchInStatement(ast)


# class ArrayCell(LHS):
#     arr: Expr
#     idx: List[Expr]
    def visitArrayCell(self, ast, c) : 
        resultType = None
        ArrayObject = self.visit(ast.arr , c) # Should be ArrayType
        if type(ArrayObject) is not ArrayType :
            raise TypeMismatchInExpression(ast)
        resultType = ArrayObject.eleType ## this should be an Array Type object.
        count = len(ast.idx) - 1
        while count > 0 :
            if type(resultType) is ArrayType :
                resultType = resultType.eleType
            else :
                
                raise TypeMismatchInExpression(ast)
            count -= 1
        
        
        type_list = [self.visit(idx,c) for idx in ast.idx]
        for i in type_list : 
            if type(i) is not IntType : 
                raise TypeMismatchInExpression(ast) 
        return resultType
        


    # class BinaryOp(Expr):
    #     op: str
    #     left: Expr
    #     right: Expr
    def visitBinaryOp(self, ast:BinaryOp, c):

        typeLeft = self.visit(ast.left, c) # Type() -> object
        typeRight = self.visit(ast.right, c)
        op = ast.op

        if op in ['+', '-', '*', '/']:  
            if type(typeLeft) not in [IntType , FloatType] or type(typeRight) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            if type(typeLeft) is IntType and type(typeRight) is IntType:
                return IntType()
            return FloatType()

        elif op in ['||' , '&&']:
            if type(typeLeft) is BoolType and type(typeRight) is BoolType :
                return BoolType()
            raise TypeMismatchInExpression(ast)

        elif op in ['==.', '+.']:
            if type(typeLeft) is not StringType or type(typeRight) is not StringType :
                raise TypeMismatchInExpression(ast)
            if op == '+.' :
                return StringType()
            return BoolType() # op == '==.'

        elif op in ['==', '!=']:
            if type(typeLeft) is IntType and type(typeRight) is IntType : 
                return BoolType()
            if type(typeLeft) is BoolType and type(typeRight) is BoolType : 
                return BoolType()          
            raise TypeMismatchInExpression(ast)

        elif op in ['<', '>', '<=', '>=']:
            if type(typeLeft) in [FloatType, IntType] and type(typeRight) in [FloatType, IntType] :
                return BoolType()
            raise TypeMismatchInExpression(ast)

        elif op == '%':
            if type(typeLeft) is IntType and type(typeRight) is IntType :
                return IntType()
            raise TypeMismatchInExpression(ast)

    # class UnaryOp(Expr):
    #     op: str
    #     body: Expr
    def visitUnaryOp(self, ast: UnaryOp, c):
        ExpType = self.visit(ast.body, c)
        op = ast.op
        if op  == '-':
            if type(ExpType) not in [IntType , FloatType] : 
                raise TypeMismatchInExpression(ast)
            return IntType() if type(ExpType) is IntType else FloatType()

        elif op  == '!':
            if type(ExpType) is not BoolType :
                raise TypeMismatchInExpression(ast)
            return BoolType()
    

# class NewExpr(Expr):
#     classname: Id
#     param: List[Expr]
    def visitNewExpr(self,ast:NewExpr, c):

        # first we need to check if there exist a constructor in the class . 
        ClassNode = getClassNode(c , ast.classname.name)
        if ClassNode is None : 
            raise Undeclared(Class() , ast.classname.name)
        Methods_list = findMembers(c , ClassNode.symbol.name , False )
        constructorNode = None
        for node in Methods_list :
            if node.symbol.name == "Constructor" : 
                constructorNode = node
        if constructorNode is not None : ## perform checking. 

            typeDeclList = [x for x in constructorNode.symbol.mtype.partype] # List of parameters
            typeAssignList = [self.visit(param, c) for param in ast.param] if ast.param is not None else [] # Arguments 
            if len(typeDeclList) != len(typeAssignList):
                raise TypeMismatchInExpression(ast)
            for (typeDecl, typeAssign) in zip(typeDeclList,typeAssignList):
                if  isSameType(typeDecl, typeAssign , c) == False:
                    raise TypeMismatchInExpression(ast)
        else : 

            if ast.param != [] :
                raise TypeMismatchInExpression(ast)
        

         
        return ClassType(Id(ast.classname.name))


    # class FieldAccess(LHS):
    #     obj: Expr
    #     fieldname: Id
    def visitFieldAccess(self,ast:FieldAccess, c): 
        resultType = None
        if type(ast.obj) is Id and ast.fieldname.name[0] != '$':  
            
            nodeFieldAccess = self.visit(ast.fieldname, (c, 'UNDECLARED ATTRIBUTE CHECK' , ast))
            if nodeFieldAccess is not None:
                resultType = nodeFieldAccess.symbol.mtype
            else : 
                raise Undeclared(Attribute(), ast.fieldname.name)   
        elif type(ast.obj) is Id and ast.fieldname.name[0] == '$':
            
            # neu la ten class -> check attribute xem co dung ko -> no -> undeclare attribute
            # Neu ko la ten class -> check tiep bien nay khai bao trong scope chua -> neu co -> illegal member access 
            # neu ko co torng scope -> undeclare identifier. 
            if isClassName( c , ast.obj.name) == True : 
                Attributes_list = findMembers(c,ast.obj.name , True)
                found = False 
                for att_node in Attributes_list :
                    if att_node.symbol.name == ast.fieldname.name :
                        found = True
                        resultType = att_node.symbol.mtype
                        break
                if found == False :
                    raise Undeclared(Attribute(),ast.fieldname.name ) 
            else :
                object_type = returnType(c,ast.obj.name)
                if object_type is not None : 
                    raise IllegalMemberAccess(ast)
                raise Undeclared(Class() , ast.obj.name) 
            
        ## REMEMBER THIS    
        elif type(ast.obj) is SelfLiteral:
            found = False
            parentClass = c
            while(type(parentClass.symbol.mtype) is not CType) : 
                parentClass = parentClass.parent
            #Attributes_Nodes = [child for child in parentClass.children if type(child.symbol.mtype) != MType] # list of Node
            Attributes_Nodes = findMembers(c , parentClass.symbol.name ,True)
            for i in Attributes_Nodes:
                if ast.fieldname.name == i.symbol.name:
                    resultType = i.symbol.mtype
                    found = True
            if found == False:
                raise Undeclared(Attribute(), ast.fieldname.name)
        else : # recursion : self.x.y
            subexp = self.visit(ast.obj , c) # should be a class type with id
            if type(subexp) is not ClassType : 
                raise IllegalMemberAccess(ast) 
            Attributes_list = findMembers(c, subexp.classname.name)
            found = False
            for att_node in Attributes_list : 
                if ast.fieldname.name == att_node.symbol.name :
                    resultType = att_node.symbol.mtype 
                    found = True
                    break 
            if found == False : 
                raise Undeclared(Attribute(), ast.fieldname.name)
        return resultType   


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
    
    # class ArrayType(Type):
        # size: int
        # eleType: Type


    # class ArrayLiteral(Literal): # Array(1,2,3,4,5)
    #   value: List[Expr]
    def visitArrayLiteral(self,ast, c):
        if len(ast.value) == 0 : 
            return ArrayType(None,None)
        type_list = [self.visit(x,c) for x in ast.value]
        # list of type -> need to check all of the type is the same first
        testing = [type(x) for x in type_list]
        if testing.count(testing[0]) != len(testing) : 
            self.ArrLitisIllegal = True
            return ArrayType(len(ast.value) , type_list[0])
        clone = []
        if type(type_list[0]) is not ArrayType :
            clone = list(map(lambda x : type(x) , type_list))
            if clone.count(clone[0]) != len(clone) : 
                self.ArrLitisIllegal = True 
        else :
            sampleSize = type_list[0].size
            sampleEletype = type_list[0].eleType
            for arr_type in type_list : 
                if arr_type.size != sampleSize or type(arr_type.eleType) is not type(sampleEletype) : 
                    self.ArrLitisIllegal = True
        return ArrayType(size = len(ast.value) , eleType = type_list[0])

    def checkArrayLiteral(self , ast , c ) :
        type_list = [self.visit(x,c) for x in ast.value] 
        clone = []
        if type(type_list[0]) is not ArrayType :
            clone = list(map(lambda x : type(x) , type_list))
            if clone.count(clone[0]) != len(clone) : 
                return False
        else : 
            size = type_list[0].size
            for i in type_list : 
                if size != i.size : 
                    return False
        return True
        

    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitFloatLiteral(self,ast, c): 
        return FloatType()
    
    def visitStringLiteral(self,ast, c): 
        return StringType()
    
    def visitBooleanLiteral(self,ast, c): 
        return BoolType()
    
    def visitNullLiteral(self,ast, c): 
        return VoidType()

    def visitSelfLiteral(self,ast, c): 
        pass

    
