from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        return reduce(lambda x,y: self.visit(y,x), ctx.decl, [])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        else:
            return o + [ctx.name]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        else:
            return o + [ctx.name]

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        else:
            paramList = reduce(lambda x,y: self.visit(y,x), ctx.param, [])
            reduce(lambda x,y: self.visit(y,x), ctx.body, paramList)
            return o + [ctx.name]

    def visitIntType(self,ctx:IntType,o:object):
        return ctx

    def visitFloatType(self,ctx:FloatType,o:object):
        return ctx

    def visitIntLit(self,ctx:IntLit,o:object):
        return ctx