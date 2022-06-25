class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):
        idList = [(x.name, x.typ) for x in ctx.decl]
        self.visit(ctx.exp, idList)
        

    def visitVarDecl(self,ctx:VarDecl,o): pass

    def visitIntType(self,ctx:IntType,o):
        return 'int'

    def visitFloatType(self,ctx:FloatType,o):
        return 'float'

    def visitBoolType(self,ctx:BoolType,o):
        return 'bool'

    def visitBinOp(self,ctx:BinOp,o):
        typeE1 = self.visit(ctx.e1, o)
        typeE2 = self.visit(ctx.e2, o)
        if ctx.op in ['-','+', '*']:
            if typeE1 == 'bool' or typeE2 == 'bool':
                raise TypeMismatchInExpression(ctx)
            elif typeE1 == 'float' or typeE2 == 'float':
                return 'float'
            else:
                return 'int'
        elif ctx.op  == '/':
            if typeE1 == 'bool' or typeE2 == 'bool':
                raise TypeMismatchInExpression(ctx)
            else:
                return 'float'
        elif ctx.op in ['&&', '||']:
            if typeE1 != 'bool' or typeE2 != 'bool':
                raise TypeMismatchInExpression(ctx)
            else:
                return 'bool'
        else:
            if typeE1 != typeE2:
                raise TypeMismatchInExpression(ctx)
            else:
                return 'bool'
        
        
        

    def visitUnOp(self,ctx:UnOp,o):
        typeE = self.visit(ctx.e, o)
        if typeE == 'bool' and ctx.op == '!':
            return 'bool'
        elif ctx.op == '-' and typeE == 'int':
            return 'int'
        elif ctx.op == '-' and typeE == 'float':
            return 'float'
        else:
            raise TypeMismatchInExpression(ctx)


    def visitIntLit(self,ctx:IntLit,o):
        return 'int'

    def visitFloatLit(self,ctx,o):
        return 'float'

    def visitBoolLit(self,ctx,o):
        return 'bool'

    def visitId(self,ctx,o):
        for x in o:
            if ctx.name == x[0]:
                return self.visit(x[1], o)
        raise UndeclaredIdentifier(ctx.name)