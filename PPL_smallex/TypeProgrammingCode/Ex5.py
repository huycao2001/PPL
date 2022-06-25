class StaticCheck(Visitor):
    @staticmethod
    def getIndex(myList, name):
        for idx in range(len(myList))[::-1]:
            if myList[idx] == name:
                return idx
    def visitProgram(self,ctx:Program,o):
        symbolStack = []
        funcStack = []
        currDict = {}
        for eachDecl in ctx.decl:
            if currDict.get(eachDecl.name) == None:
                currDict[eachDecl.name] = ''
                if isinstance(eachDecl, FuncDecl):
                    self.visitFuncDecl(eachDecl, (symbolStack, funcStack))
                else:
                    symbolStack.append((eachDecl.name, 'undefined'))
            else:
                raise Redeclared(eachDecl)
        [self.visit(x, (symbolStack, funcStack, None)) for x in ctx.stmts]          

    def visitVarDecl(self,ctx:VarDecl,o): pass

    def visitFuncDecl(self,ctx:FuncDecl,o): 
        symbolStack = o[0]
        currSize = len(symbolStack)
        funcStack = o[1]
        currDict = {}
        funcSignature = [ctx.name]
        for x in ctx.param:
            if currDict.get(x.name) == None:
                currDict[x.name] = ''
                funcSignature.append((x.name, 'undefined'))
            else:
                raise Redeclared(x)
        funcStack.append(funcSignature)
        currSizeFunc = len(funcStack)
        for eachDecl in ctx.local:
            if currDict.get(eachDecl.name) == None:
                currDict[eachDecl.name] = ''
                if isinstance(eachDecl, FuncDecl):
                    self.visitFuncDecl(eachDecl, (symbolStack, funcStack))
                else:
                    symbolStack.append((eachDecl.name, 'undefined'))
            else:
                raise Redeclared(eachDecl)
        [self.visit(x, (symbolStack, funcStack, ctx.name)) for x in ctx.stmts]
        while(len(symbolStack) != currSize):
            symbolStack.pop()
        while(len(funcStack) != currSizeFunc):
            funcStack.pop()


    def visitCallStmt(self,ctx:CallStmt,o):
        symbolStack = o[0]
        funcStack = o[1]
        funcName = o[2]
        allFuncNames = [x[0] for x in funcStack]
        idx = -1
        if ctx.name not in allFuncNames:
            raise UndeclaredIdentifier(ctx.name)
        else:
            idx = allFuncNames.index(ctx.name)
        funcArgs = funcStack[idx][1:]
        if len(funcArgs) != len(ctx.args):
            raise TypeMismatchInStatement(ctx)
        passedParam = []
        for x in ctx.args:
            if isinstance(x, Id):
                passedParam.append(self.visit(x,(symbolStack, funcStack, ctx.name)))
            else:
                passedParam.append(self.visit(x, (symbolStack, funcStack)))
        for index in range(len(passedParam)):
            if passedParam[index] == 'undefined' and funcArgs[index][1] == 'undefined':
                raise TypeCannotBeInferred(ctx)
            elif passedParam[index] == 'undefined':
                argsName = [x[0] for x in funcArgs]
                if ctx.args[index].name in argsName:
                    updateFuncIdx = allFuncNames.index(funcName)
                    updateFuncArgs = funcStack[updateFuncIdx][1:]
                    updateFuncArgsName = [x[0] for x in updateFuncArgs]
                    updatedIndex = updateFuncArgsName.index(ctx.args[index].name)
                    funcStack[updateFuncIdx][1 + updatedIndex] = funcArgs[index][1]
                else:
                    varList = [x[0] for x in symbolStack]
                    updateVarIdx = StaticCheck.getIndex(varList, ctx.args[index].name)
                    symbolStack[updateVarIdx] = (ctx.args[index].name, funcArgs[index][1])
            elif funcArgs[index][1] == 'undefined':
                funcStack[idx][1+index] = passedParam[index]
            else:
                raise TypeMismatchInStatement(ctx)
                
    def visitAssign(self,ctx:Assign,o):
        symbolStack = o[0]
        funcStack = o[1]
        funcName = o[2]
        lhsType = self.visitId(ctx.lhs, (symbolStack, funcStack, funcName))
        rhsType = self.visit(ctx.rhs, (symbolStack, funcStack, funcName))
        if funcName:
            if lhsType == 'undefined' and rhsType == 'undefined':
                raise TypeCannotBeInferred (ctx)
            elif lhsType == 'undefined':
                allFuncNames = [x for x in funcStack[0]]
                funcIdx = allFuncNames.index(funcName)
                funcAgrsName = [x[0] for x in funcStack[funcIdx][1:]]
                if ctx.lhs.name in funcAgrsName:
                    updatedIndex = funcAgrsName.index(ctx.lhs.name)
                    funcStack[funcIdx][1 + updatedIndex] = rhsType
                else:
                    varList = [x[0] for x in symbolStack]
                    updatedIndex = StaticCheck.getIndex(varList, ctx.lhs.name)
                    symbolStack[updatedIndex] = (symbolStack[updatedIndex][0], rhsType)
            elif rhsType == 'undefined':
                allFuncNames = [x for x in funcStack[0]]
                funcIdx = allFuncNames.index(funcName)
                funcAgrsName = [x[0] for x in funcStack[funcIdx][1:]]
                if ctx.rhs.name in funcAgrsName:
                    updatedIndex = funcAgrsName.index(ctx.rhs.name)
                    funcStack[funcIdx][1 + updatedIndex] = lhsType
                else:
                    varList = [x[0] for x in symbolStack]
                    updatedIndex = StaticCheck.getIndex(varList, ctx.rhs.name)
                    symbolStack[updatedIndex] = (symbolStack[updatedIndex][0], lhsType)
            else:
                raise TypeMismatchInStatement(ctx)
        else:
            if lhsType == 'undefined' and rhsType == 'undefined':
                raise TypeCannotBeInferred (ctx)
            elif lhsType == 'undefined':
                varList = [x[0] for x in symbolStack]
                updatedIndex = StaticCheck.getIndex(varList, ctx.lhs.name)
                symbolStack[updatedIndex] = (symbolStack[updatedIndex][0], rhsType)
            elif rhsType == 'undefined':
                varList = [x[0] for x in symbolStack]
                updatedIndex = StaticCheck.getIndex(varList, ctx.rhs.name)
                symbolStack[updatedIndex] = (symbolStack[updatedIndex][0], lhsType)
            else:
                raise TypeMismatchInStatement(ctx)





    def visitIntLit(self,ctx:IntLit,o):
        return 'int' 

    def visitFloatLit(self,ctx,o): 
        return 'float'

    def visitBoolLit(self,ctx,o): 
        return 'bool'

    def visitId(self,ctx,o):
        symbolStack = o[0]
        funcStack = o[1]
        funcName = o[2]
        allFuncNames = [x[0] for x in funcStack]
        if funcName:
            idx = allFuncNames.index(funcName)
            for eachParam in funcStack[idx][1:]:
                if eachParam[0] == ctx.name:
                    return eachParam[1]
        for eachDecl in symbolStack[::-1]:
            if eachDecl[0] == ctx.name:
                return eachDecl[1]
        raise UndeclaredIdentifier(ctx.name)



