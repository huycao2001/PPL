class StaticCheck(Visitor):

    def visitBinOp(self,ctx:BinOp,o):
        typeE1 = self.visit(ctx.e1, None)
        typeE2 = self.visit(ctx.e2, None)
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
        typeE = self.visit(ctx.e, None)
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