class StaticCheck(Visitor):
    @staticmethod
    def getIndex(name, symbolStack):
        for x in range(len(symbolStack))[::-1]:
            if name == symbolStack[x][0]:
                return x
    def visitProgram(self,ctx:Program,o):
        symbolStack = []
        currDict = {}
        for var in ctx.decl:
            if currDict.get(var.name) == None:
                currDict[var.name] = ''
                symbolStack.append((var.name, 'undefined'))
            else:
                raise Redeclared(var)
        [self.visit(x, symbolStack) for x in ctx.stmts]


    def visitVarDecl(self,ctx:VarDecl,o): pass

    # class Block(Stmt): #decl:List[VarDecl],stmts:List[Stmt]
    def visitBlock(self,ctx:Block,o): 
        currDict = {} # Dictionary defines the type of the vars in their SCOPE only
        symbolStack = o # stack stores all the vars delared and its type.
        for var in ctx.decl:
            #symbolStack.append((var.name, 'undefined'))
            # If the var is not yet declared in this scope 
            # then we mark it to the currDict
            if currDict.get(var.name) == None:
                currDict[var.name] = 'existed'
                symbolStack.append((var.name, 'undefined'))
            else: # This variable is already declared in this scope.
                raise Redeclared(var)
        # Perform checking for all the stmts in this block.         
        [self.visit(x, symbolStack) for x in ctx.stmts]
        ## when getting out of the scope then we have to
        ## pop all the vars declared in the scope. 
        for x in range(len(ctx.decl)):
            o.pop()
        


    def visitAssign(self,ctx:Assign,o):
        lhsType = self.visitId(ctx.lhs, o)
        rhsType = self.visit(ctx.rhs, o)
        if lhsType == 'undefined' and rhsType == 'undefined':
            raise TypeCannotBeInferred(ctx)
        elif lhsType == 'undefined':
            indexType = StaticCheck.getIndex(ctx.lhs.name, o)
            if o[indexType][1] == 'undefined':
                o[indexType] = (o[indexType][0], rhsType)
            lhsType = rhsType
        elif rhsType == 'undefined':
            indexType = StaticCheck.getIndex(ctx.rhs.name, o)
            if o[indexType][1] == 'undefined':
                o[indexType] = (o[indexType][0], lhsType)
            rhsType = lhsType
        if lhsType != rhsType:
            raise TypeMismatchInStatement(ctx)       

    def visitBinOp(self,ctx:BinOp,o):
        op = ctx.op
        exp1Type = self.visit(ctx.e1, o)
        exp2Type = self.visit(ctx.e2, o)
        if op in ['+', '*', '/', '-']:
            if exp2Type == 'undefined':
                exp2Type = 'int'
                idx = StaticCheck.getIndex(ctx.e2.name, o)
                o[idx] = (o[idx][0], 'int')
            if exp1Type == 'undefined':
                exp1Type = 'int'
                idx = StaticCheck.getIndex(ctx.e1.name, o)
                o[idx] = (o[idx][0], 'int')
            if exp2Type == 'int' and exp1Type == 'int':
                return 'int'
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['+.', '*.', '/.', '-.']:
            if exp2Type == 'undefined':
                exp2Type = 'float'
                idx = StaticCheck.getIndex(ctx.e2.name, o)
                o[idx] = (o[idx][0], 'float')
            if exp1Type == 'undefined':
                exp1Type = 'float'
                idx = StaticCheck.getIndex(ctx.e1.name, o)
                o[idx] = (o[idx][0], 'float')
            if exp2Type == 'float' and exp1Type == 'float':
                return 'float'
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['>', '=']:
            if exp2Type == 'undefined':
                exp2Type = 'int'
                idx = StaticCheck.getIndex(ctx.e2.name, o)
                o[idx] = (o[idx][0], 'int')
            if exp1Type == 'undefined':
                exp1Type = 'int'
                idx = StaticCheck.getIndex(ctx.e1.name, o)
                o[idx] = (o[idx][0], 'int')
            if exp2Type == 'int' and exp1Type == 'int':
                return 'bool'
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['>.', '=.']:
            if exp2Type == 'undefined':
                exp2Type = 'float'
                idx = StaticCheck.getIndex(ctx.e2.name, o)
                o[idx] = (o[idx][0], 'float')
            if exp1Type == 'undefined':
                exp1Type = 'float'
                idx = StaticCheck.getIndex(ctx.e1.name, o)
                o[idx] = (o[idx][0], 'float')
            if exp2Type == 'float' and exp1Type == 'float':
                return 'bool'
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['&&', '||', '>b', '=b']:
            if exp2Type == 'undefined':
                exp2Type = 'bool'
                idx = StaticCheck.getIndex(ctx.e2.name, o)
                o[idx] = (o[idx][0], 'bool')
            if exp1Type == 'undefined':
                exp1Type = 'bool'
                idx = StaticCheck.getIndex(ctx.e1.name, o)
                o[idx] = (o[idx][0], 'bool')
            if exp2Type == 'bool' and exp1Type == 'bool':
                return 'bool'
            else:
                raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        op = ctx.op
        typeExp = self.visit(ctx.e, o)
        if op in ['-', 'i2f']:
            if typeExp == 'undefined':
                idx = StaticCheck.getIndex(ctx.e.name, o)
                o[idx] = (o[index][0], 'int')
                typeExp = 'int'
            if typeExp != 'int':
                raise TypeMismatchInExpression(ctx)
            elif op == '-':
                return 'int'
            else:
                return 'float'
        elif op in ['-.', 'floor']:
            if typeExp == 'undefined':
                idx = StaticCheck.getIndex(ctx.e.name, o)
                o[idx] = (o[index][0], 'float')
                typeExp = 'float'
            if typeExp != "float":
                raise TypeMismatchInExpression(ctx)
            elif op == '-.':
                return "float"
            else:
                return "int"
        else:
            if typeExp == 'undefined':
                idx = StaticCheck.getIndex(ctx.e.name, o)
                o[idx] = (o[index][0], 'bool')
                typeExp = 'bool'
            if typeExp != 'bool':
                raise TypeMismatchInExpression(ctx)
            else:
                return "bool"        

    def visitIntLit(self,ctx:IntLit,o): 
        return 'int' 

    def visitFloatLit(self,ctx,o): 
        return 'float'

    def visitBoolLit(self,ctx,o): 
        return 'bool'

    def visitId(self,ctx,o):
        for var_name,var_type in reversed(o):
            if var_name == ctx.name:
                return var_type
        raise UndeclaredIdentifier(ctx.name)

