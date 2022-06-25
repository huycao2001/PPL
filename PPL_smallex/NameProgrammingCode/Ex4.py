from functools import reduce
class StaticCheck(Visitor):
    level = 0
    def visitProgram(self,ctx:Program,o:object):
        return reduce(lambda x,y: self.visit(y,x), ctx.decl, [])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if (ctx.name, self.level) in o:
            raise RedeclaredVariable(ctx.name)
        else:
            return o + [(ctx.name, self.level)]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if (ctx.name, self.level) in o:
            raise RedeclaredConstant(ctx.name)
        else:
            return o + [(ctx.name, self.level)]

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if (ctx.name, self.level) in o:
            raise RedeclaredFunction(ctx.name)
        else:
            o = o + [(ctx.name, self.level)]
            self.level = self.level + 1
            newList = o.copy()
            paramList = reduce(lambda x,y: self.visit(y,x), ctx.param, newList)
            bodyDecl = reduce(lambda x,y: self.visit(y,x), ctx.body[0], paramList)
            reduce(lambda x,y : self.visit(y,x), ctx.body[1], bodyDecl)
            self.level = self.level - 1
            return o

    def visitIntType(self,ctx:IntType,o:object):
        return ctx

    def visitFloatType(self,ctx:FloatType,o:object):
        return ctx

    def visitIntLit(self,ctx:IntLit,o:object):
        return o
    def visitId(self,ctx:Id,o:object):
        availabelName = [x[0] for x in o]
        if ctx.name in availabelName:
            return o
        else:
            raise UndeclaredIdentifier(ctx.name)