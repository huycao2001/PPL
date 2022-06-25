class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        idList = [x.name for x in ctx.decl]
        myDict = dict(map(lambda x: (x, ""), idList))
        [self.visit(x, myDict) for x in ctx.stmts]

    def visitVarDecl(self,ctx:VarDecl,o): pass

    def visitAssign(self,ctx:Assign,o):
        lhsType = self.visit(ctx.lhs, o)
        rhsType = self.visit(ctx.rhs, o)
        if rhsType == '' and lhsType == '':
            raise TypeCannotBeInferred(ctx)
        elif lhsType == '': # a = 3 
            if o[ctx.lhs.name] == '':
                o[ctx.lhs.name] = rhsType
                lhsType = rhsType
            else: # lhsType = '' , dict[a] = int
                lhsType = o[ctx.lhs.name]
        elif rhsType == '':
            rhsType = lhsType
            o[ctx.rhs.name] = rhsType
        if lhsType != rhsType:
            raise TypeMismatchInStatement(ctx)

    def visitBinOp(self,ctx:BinOp,o): 
        op = ctx.op
        exp1Type = self.visit(ctx.e1, o)
        exp2Type = self.visit(ctx.e2, o)
        if op in ['+', '*', '/', '-']:
            if exp2Type == '':
                exp2Type = 'int'
                o[ctx.e2.name] = 'int'
            if exp1Type == '':
                exp1Type = 'int'
                o[ctx.e1.name] = 'int'
            if exp2Type == 'int' and exp1Type == 'int':
                return 'int'
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['+.', '*.', '/.', '-.']:
            if exp2Type == '':
                exp2Type = 'float'
                o[ctx.e2.name] = 'float'
            if exp1Type == '':
                exp1Type = 'float'
                o[ctx.e1.name] = 'float'
            if exp2Type == 'float' and exp1Type == 'float':
                return 'float'
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['>', '=']:
            if exp2Type == '':
                exp2Type = 'int'
                o[ctx.e2.name] = 'int'
            if exp1Type == '':
                exp1Type = 'int'
                o[ctx.e1.name] = 'int'
            if exp2Type == 'int' and exp1Type == 'int':
                return 'bool'
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['>.', '=.']:
            if exp2Type == '':
                exp2Type = 'float'
                o[ctx.e2.name] = 'float'
            if exp1Type == '':
                exp1Type = 'float'
                o[ctx.e1.name] = 'float'
            if exp2Type == 'float' and exp1Type == 'float':
                return 'bool'
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['&&', '||', '>b', '=b']:
            if exp2Type == '':
                exp2Type = 'bool'
                o[ctx.e2.name] = 'bool'
            if exp1Type == '':
                exp1Type = 'bool'
                o[ctx.e1.name] = 'bool'
            if exp2Type == 'bool' and exp1Type == 'bool':
                return 'bool'
            else:
                raise TypeMismatchInExpression(ctx)



    def visitUnOp(self,ctx:UnOp,o):
        op = ctx.op
        typeExp = self.visit(ctx.e, o)
        if op in ['-', 'i2f']:
            if typeExp == '':
                typeExp = 'int'
                o[ctx.e.name] = typeExp
            if typeExp != 'int':
                raise TypeMismatchInExpression(ctx)
            elif op == '-':
                return 'int'
            else:
                return 'float'
        elif op in ['-.', 'floor']:
            if typeExp == '':
                typeExp = 'float'
                o[ctx.e.name] = typeExp
            if typeExp != "float":
                raise TypeMismatchInExpression(ctx)
            elif op == '-.':
                return "float"
            else:
                return "int"
        else:
            if typeExp == '':
                typeExp = 'bool'
                o[ctx.e.name] = typeExp
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
        if o.get(ctx.name) == None:
            raise UndeclaredIdentifier(ctx.name)
        else:
            return o.[ctx.name]