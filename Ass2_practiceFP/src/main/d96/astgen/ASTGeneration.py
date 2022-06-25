## This version : visitBlock will now return a [Block()] so the {{}} is true
## Will also have to modify all the self.visit(ctx.block_stmt()) by flattening 
## the list to get the object (add [0] behind the visit)
## We apply this addition to every non-terminals that uses block_stmt.
## We also assign the Nullliteral() to param that is ClassType .
## For Foreach statment, if theres no statement for the step then it is assigned to IntLit(1)
## Modify the method Decl to detect main() in the Class Program in a "not accessing directly the member" way

from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from functools import reduce

class ASTGeneration(D96Visitor):
    # program: class_declaration+  EOF;
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        lst = []
        # for x in ctx.class_declaration():
        #     lst += self.visit(x)
        lst = [self.visit(x) for x in ctx.class_declaration() ]
        lst = reduce(lambda x,y : x + y , lst , [])
        return Program(lst)
        # return Program(reduce(lambda prev, curr : prev + self.visit(curr)  , ctx.class_declaration() , []))

    #
    # class_declaration : CLASS ID ( COLON ID )? LP member*  RP;
    def visitClass_declaration(self, ctx : D96Parser.Class_declarationContext ):
        members = []
        if ctx.member() : 
            # for x in ctx.member() : 
            #     members += self.visit(x)
            members = [self.visit(member) for member in ctx.member()]
            members = reduce(lambda x,y : x + y , members, [] )
        if ctx.ID(1) and ctx.COLON(): # with inheritance
            return [ClassDecl(Id(ctx.ID(0).getText()),members,Id(ctx.ID(1).getText()) )] 
        
        # if ctx.ID(0).getText() == 'Program' : # program class
        #     for member in members : 
        #         if type(member) == MethodDecl and member.name.name == 'main' and member.param == [] : 
        #             member.kind = Static() 
        return [ClassDecl(Id(ctx.ID(0).getText()),members)] 

    #member : attribute_declaration | method_declaration | constructor | destructor ;
    def visitMember(self, ctx: D96Parser.MemberContext):
        return self.visitChildren(ctx)
    
    # attribute_declaration : attribute_type attribute_decl_list SEMI_COLON;
    # [(Int,a) , (Int ,b)]
    def visitAttribute_declaration(self, ctx: D96Parser.Attribute_declarationContext):
        att_type = self.visit(ctx.attribute_type())
        res = []
        att_decl_list = self.visit(ctx.attribute_decl_list()) # [(ClassType(),a) (int , $b)]
        if(len(att_decl_list[0]) == 2) : # No expression for vars
            if(att_type == 'Var') : # return Vardecl
                null_list = [NullLiteral() if type(item[0]) == ClassType else None for item in att_decl_list]
                id_list = [Id(item[1]) for item in att_decl_list ]
                data_type_list = [item[0] for item in att_decl_list ]
                type_list = [Static() if item[1][0] == '$' else Instance() for item in att_decl_list]
                lst = zip(type_list ,data_type_list , id_list, null_list)
                res = [AttributeDecl(type, VarDecl(id,data_type , null)) for type, data_type, id , null in lst ]  
                    
                # for data_type,id in att_decl_list : 
                #     nullable = None
                #     if (type(data_type) == ClassType) : 
                #         nullable = NullLiteral()
                #     if id[0] == '$' : 
                #         res += [AttributeDecl(Static(), VarDecl(Id(id),data_type , nullable))]
                #     else : 
                #         res += [AttributeDecl(Instance(), VarDecl(Id(id),data_type , nullable))]
            else : # Val : Immutable
                res = [AttributeDecl(Static(), ConstDecl(Id(id),data_type,None)) if id[0] == '$' else AttributeDecl(Instance(), ConstDecl(Id(id),data_type,None)) for data_type, id in att_decl_list]
            #     for data_type, id in att_decl_list : 
            #         # nullable = None
            #         # if (type(data_type) == ClassType) : 
            #         #     nullable = NullLiteral()
            #         if id[0] == '$' :
            #             res += [ AttributeDecl(Static(), ConstDecl(Id(id),data_type,None))]
            #         else : 
            #             res += [AttributeDecl(Instance(), ConstDecl(Id(id),data_type,None))]
            return res
        else : # initial values for vars
            my_data_type, my_id ,my_expr = zip(*[(data_type , id , expr) for data_type , id , expr in att_decl_list]) 
            
            #xs, ys = zip(*[(km, price) for km, price in data])
            # for data_type , id , expr in att_decl_list : 
            #     my_data_type.append(data_type)
            #     my_id.append(id)
            #     my_expr.append(expr)
            att_decl_list = zip(my_data_type , my_id , reversed(my_expr))

            if(att_type == 'Var') : # return Vardecl
                for data_type,id,expr in att_decl_list : 
                    if id[0] == '$' : 
                        res += [AttributeDecl(Static(), VarDecl(Id(id),data_type,expr ))]
                    else : 
                        res += [AttributeDecl(Instance(), VarDecl(Id(id),data_type,expr))]
            else : # Val : Immutable
                for data_type, id , expr in att_decl_list : 
                    if id[0] == '$' :
                        res += [ AttributeDecl(Static(), ConstDecl(Id(id),data_type , expr ))]
                    else : 
                        res += [AttributeDecl(Instance(), ConstDecl(Id(id),data_type , expr))]
            return res

    def visitAttribute_type(self, ctx: D96Parser.Attribute_typeContext):
        if ctx.IMMUTABLE() : 
            return 'Val'
        return 'Var'
    # attribute_decl_list : testing | testing2 ;
    def visitAttribute_decl_list(self, ctx: D96Parser.Attribute_decl_listContext):
        return self.visitChildren(ctx)

    #testing : att_name ( COLON compound_type (ASSIGN expression)) | (att_name COMMA testing (COMMA expression));
    def visitTesting(self, ctx: D96Parser.TestingContext):
        if ctx.compound_type() : 
            data_type = self.visit(ctx.compound_type())
            att_name = self.visit(ctx.att_name())
            expr = self.visit(ctx.expression())
            return [(data_type, att_name, expr)]
        else : 
            att_list = [self.visit(ctx.att_name())]
            expr_list = [self.visit(ctx.expression())]
            clone = self.visit(ctx.testing())
            for data_type,att_name , expr in clone : 
                att_list.append(att_name)
                expr_list.append(expr)
                x = data_type
            data_type_list = [x] * len(att_list)
            return list(zip(data_type_list,att_list,expr_list))
        # Var a , b,c : Int = 1,2,3 -> [(Int,a , 3) , (Int,b,2)  , (Int,c , 1)]


    # testing2 :  att_name (COMMA att_name )* COLON compound_type ; // Int a,b,c : = Int;
    def visitTesting2(self, ctx: D96Parser.Testing2Context):
        data_type = self.visit(ctx.compound_type())
        att_list = [] 
        for i in ctx.att_name() : 
            att_list.append(self.visit(i)) # att_list is now a list of var with text only
        # print(list(map(lambda att : (data_type, att), att_list )))
        return list(map(lambda att : (data_type, att), att_list )) # [(int,a)]

    # att_name LB parameter_decl_list? RB block_statement;
    def visitMethod_declaration(self, ctx: D96Parser.Method_declarationContext):
        id = self.visit(ctx.att_name()) ## This is the TEXT of ID => String type
        isMain = True if id == "main" else False
        kind = Static() if id[0] == '$' else Instance()
        id = Id(id)   
        param = self.visit(ctx.parameter_decl_list()) if ctx.parameter_decl_list() else []
        block = self.visit(ctx.block_statement())[0]
        if( isMain and param == []) : 
            temp = ctx
            while(not isinstance(temp,D96Parser.Class_declarationContext)):
                temp  = temp.parentCtx
            # temp is now a class decl
            if temp.ID(0).getText() == "Program" : 
                kind = Static()
        return [MethodDecl(kind,id,param,block)]

    #att_name : (ID|DOLLAR_ID);
    def visitAtt_name(self, ctx: D96Parser.Att_nameContext):
        if ctx.ID() : 
            return ctx.ID().getText()
        return ctx.DOLLAR_ID().getText()

    # constructor : CONSTRUCTOR LB parameter_decl_list? RB block_statement; 
    def visitConstructor(self, ctx: D96Parser.ConstructorContext):
        kind = Instance()
        id = Id('Constructor')
        param = self.visit(ctx.parameter_decl_list()) if ctx.parameter_decl_list() else []
        block = self.visit(ctx.block_statement())[0]
        return [MethodDecl(kind,id,param,block)]

    def visitDestructor(self, ctx: D96Parser.DestructorContext):
        kind = Instance()
        id = Id('Destructor')
        param = []
        block = self.visit(ctx.block_statement())[0]
        return [MethodDecl(kind,id,param,block)]


    # parameter_decl_list : (parameter_decl (SEMI_COLON parameter_decl)*)
    def visitParameter_decl_list(self, ctx: D96Parser.Parameter_decl_listContext):
        para_decl_list = [self.visit(para_decl) for para_decl in ctx.parameter_decl() ]
        para_decl_list = reduce(lambda x,y : x + y , para_decl_list, [])
        # for i in ctx.parameter_decl() : 
        #     para_decl_list += self.visit(i)
        res = [VarDecl(id, data_type , NullLiteral()) if type(data_type) == ClassDecl else VarDecl(id, data_type) for id,data_type in para_decl_list  ]
        # for id,data_type in para_decl_list : 
        #     if type(data_type) == ClassDecl : 
        #         res.append(VarDecl(id, data_type , NullLiteral()))
        #     else :
        #         res.append(VarDecl(id, data_type)) 

        return res

    # parameter_decl : ids_list COLON compound_type
    def visitParameter_decl(self, ctx: D96Parser.Parameter_declContext):
        ids_list = self.visit(ctx.ids_list())
        data_type = self.visit(ctx.compound_type())
        return [(id, data_type) for id in ids_list]


    # ids_list : ID ( COMMA ID)*;
    def visitIds_list(self, ctx: D96Parser.Ids_listContext):
        return [Id(id.getText()) for id in ctx.ID()]


    # block_statement : LP statement* RP;
    def visitBlock_statement(self, ctx: D96Parser.Block_statementContext):
        res = []
        if ctx.statement() : 
            for statement in ctx.statement() : 
                res+=self.visit(statement)
        return [Block(res)]


# statement : var_declare_statement 
# | assign_statement 
# | if_statement 
# | for_statement 
# | return_statement 
# | break_statement 
# | continue_statement 
# | block_statement
# | call_stmt; 
    def visitStatement(self, ctx: D96Parser.StatementContext):
        return self.visitChildren(ctx)

    # assign_statement : expression7 ASSIGN expression SEMI_COLON;
    def visitAssign_statement(self, ctx: D96Parser.Assign_statementContext):
        lhs = self.visit(ctx.expression7()); 
        exp = self.visit(ctx.expression())
        return [Assign(lhs,exp)]

    # call_stmt : instance_call_stmt | static_call_stmt;
    def visitCall_stmt(self, ctx: D96Parser.Call_stmtContext):
        return self.visitChildren(ctx)
    
    # instance_call_stmt : (expression8 DOT ID LB expressions_list? RB SEMI_COLON);
    def visitInstance_call_stmt(self, ctx: D96Parser.Instance_call_stmtContext):
        obj = self.visit(ctx.expression7())
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.expressions_list()) if ctx.expressions_list() else []
        return [CallStmt(obj,method, param)]

    #static_call_stmt : expression8 DOUBLE_COLON DOLLAR_ID LB expressions_list RB SEMI_COLON;
    def visitStatic_call_stmt(self, ctx: D96Parser.Static_call_stmtContext):
        obj = self.visit(ctx.expression7())
        method = Id(ctx.DOLLAR_ID().getText())
        param = self.visit(ctx.expressions_list()) if ctx.expressions_list() else []
        return [CallStmt(obj,method, param)]


    # for_statement : FOREACH LB ID IN expression DOUBLEDOT expression (BY expression)?  RB block_statement;
    def visitFor_statement(self, ctx: D96Parser.For_statementContext):
       id = Id(ctx.ID().getText())
       expr1 = self.visit(ctx.expression(0))
       expr2 = self.visit(ctx.expression(1))
       loop = self.visit(ctx.block_statement())[0]
       expr3 = self.visit(ctx.expression(2)) if ctx.expression(2) else IntLiteral(1)
       return [For(id, expr1, expr2, loop, expr3)]


    # if_statement : IF LB  expression RB block_statement (ELSEIF LB  expression RB block_statement)* (ELSE block_statement)? ;
    def visitIf_statement(self, ctx: D96Parser.If_statementContext):
        if len(ctx.block_statement()) == 1 : # If only
            expr = self.visit(ctx.expression(0))
            thenStmt = self.visit(ctx.block_statement(0))[0]
            elseStmt = None 
            return [If(expr,thenStmt,elseStmt)]

        elif len(ctx.block_statement()) == 2 and ctx.ELSE() : # if and else only
            expr = self.visit(ctx.expression(0))
            thenStmt = self.visit(ctx.block_statement(0))[0]
            elseStmt = self.visit(ctx.block_statement(1))[0]
            return [If(expr,thenStmt,elseStmt)]

        elif not ctx.ELSE() : # If and a list of else if stmts
            # go from last to first
            count = len(ctx.block_statement())
            count = list(reversed(list(range(count)))) # count = 5 -> 4,3,2,1,0
            elseStmt = None
            lst = list(zip(ctx.expression() , ctx.block_statement()))
            result = reduce(lambda acc,ele : If(self.visit(ele[0]), self.visit(ele[1])[0] ,acc) ,  reversed(lst), None )
            return [result]
            # result = reduce(lambda x,y : )
            # for i in count:
            #     expr = self.visit(ctx.expression(i))
            #     thenStmt = self.visit(ctx.block_statement(i))[0]
            #     elseStmt = If(expr,thenStmt,elseStmt)
            # return [elseStmt]; 
        
        else : # If , elseif anf else statment combined. 
            # count = len(ctx.block_statement())
            # count = list(reversed(list(range(count))))
            # expr = self.visit(ctx.expression(0))
            # thenStmt = self.visit(ctx.block_statement(0))[0]
            # expr_clone = None
            # thenStmt_clone = None
            # elseStmt_clone = None
            # for i in count : 
            #     if i == 1 : 
            #         break
            #     if i == len(count) - 1 : 
            #         elseStmt_clone = self.visit(ctx.block_statement(i))[0]
            #     expr_clone = self.visit(ctx.expression(i-1))
            #     thenStmt_clone = self.visit(ctx.block_statement(i-1))[0]
            #     elseStmt_clone = If(expr_clone,thenStmt_clone, elseStmt_clone)
            # return [If(expr,thenStmt,elseStmt_clone)]
            count = len(ctx.block_statement())
            else_block = self.visit(ctx.block_statement(count-1))[0]
            lst = reversed(list(zip(ctx.expression(), ctx.block_statement()[:-1])))
            res = reduce(lambda acc, ele : If(self.visit(ele[0]), self.visit(ele[1])[0] , acc ),lst , else_block )
            return [res]
            

        

    
    # return_statement : RETURN (expression | DOLLAR_ID)? SEMI_COLON;
    def visitReturn_statement(self, ctx: D96Parser.Return_statementContext):
        if ctx.expression() : 
            return [Return(self.visit(ctx.expression()))]
        return [Return(None)]

    def visitBreak_statement(self, ctx: D96Parser.Break_statementContext):
        return [Break()]

    def visitContinue_statement(self, ctx: D96Parser.Continue_statementContext):
        return [Continue()]

    # var_declare_statement : attribute_type var_decl_list SEMI_COLON ;
    def visitVar_declare_statement(self, ctx: D96Parser.Var_declare_statementContext):
        var_type = self.visit(ctx.attribute_type())
        res = []
        var_decl_list = self.visit(ctx.var_decl_list()) # [(ClassType(),a) (int , $b)]
        if(len(var_decl_list[0]) == 2) : # No initial values for vars
            if(var_type == 'Var') : # return Vardecl
                res = [ VarDecl(Id(id),data_type , NullLiteral()) if type(data_type) == ClassType else VarDecl(Id(id),data_type , None)  for data_type, id in var_decl_list]
                # for data_type,id in var_decl_list : 
                #     nullable = None
                #     if (type(data_type) == ClassType) : 
                #         nullable = NullLiteral()
                #     res += [VarDecl(Id(id),data_type , nullable)]
                #print(res)
                return res
                        
            else : # Val immutable
                res = [ ConstDecl(Id(id),data_type , None) for data_type, id in var_decl_list]
                # for data_type, id in var_decl_list : 
                #     res += [ConstDecl(Id(id),data_type , None)]
                        
            return res
        else : # initial values for vars
            # xs, ys = zip(*[(km, price) for km, price in data]) 
            my_data_type = []
            my_id = []
            my_expr = []
            my_data_type, my_id , my_expr = zip(*[(data_type,id,expr) for data_type,id,expr in var_decl_list])
            # for data_type,id,expr in var_decl_list : 
            #     my_data_type.append(data_type)
            #     my_id.append(id)
            #     my_expr.append(expr)
            var_decl_list = zip(my_data_type , my_id , reversed(my_expr))

            if(var_type == 'Var') : # return Vardecl
                res = [VarDecl(Id(id),data_type,expr) for data_type,id,expr in var_decl_list]
                # res = reduce(lambda x,y : x + y , res)
                # for data_type,id,expr in var_decl_list : 
                #     res += [VarDecl(Id(id),data_type,expr)]
            else : # Val immutable
                res = [ConstDecl(Id(id),data_type,expr) for data_type,id,expr in var_decl_list]
                # for data_type, id , expr in var_decl_list : 
                #     res += [ConstDecl(Id(id),data_type , expr)]
            return res

    # var_decl_list : (var_decl_stm_only | var_decl_stm_assign) ;
    def visitVar_decl_list(self, ctx: D96Parser.Var_decl_listContext):
        return self.visitChildren(ctx)

    # var_decl_stm_only : ID (COMMA ID )* COLON compound_type; 
    def visitVar_decl_stm_only(self, ctx: D96Parser.Var_decl_stm_onlyContext):
        data_type = self.visit(ctx.compound_type())
        var_list = []
        flag = len(ctx.ID())
        for i in range(flag) : 
            var_list.append(ctx.ID(i).getText())
        return list(map(lambda var : (data_type, var) , var_list))

    # var_decl_stm_assign : ID (COLON compound_type (ASSIGN expression)) | (ID COMMA var_decl_stm_assign (COMMA expression));
    def visitVar_decl_stm_assign(self, ctx: D96Parser.Var_decl_stm_assignContext):
        if ctx.compound_type() : 
            data_type = self.visit(ctx.compound_type())
            var_name = ctx.ID().getText()
            expr = self.visit(ctx.expression())
            return [(data_type,var_name , expr)]
        else : 
            var_list = [ctx.ID().getText()]
            expr_list = [self.visit(ctx.expression())]
            clone = self.visit(ctx.var_decl_stm_assign())
            # xs, ys = zip(*[(km, price) for km, price in data]) 
            var_list = [item[1] for item in clone ]
            var_list.insert(0,ctx.ID().getText())
            expr_list = [item[2] for item in clone ]
            expr_list.insert(0,self.visit(ctx.expression()))
            data_type_list = [clone[0][0]] * len(var_list)

            # for data_type,att_name , expr in clone : 
            #     var_list.append(att_name)
            #     expr_list.append(expr)
            #     x = data_type
            # data_type_list = [x] * len(var_list)
            # var_list.insert(0,ctx.ID().getText())
            # expr_list.insert(0,self.visit(ctx.expression()))

            return list(zip(data_type_list,var_list,expr_list))
    
    
    



    # primitive_type | array_type | ID ;
    def visitCompound_type(self, ctx: D96Parser.Compound_typeContext):
        if ctx.ID() : 
            id_value = ctx.ID().getText()
            return ClassType(Id(id_value))
        # elif ctx.primitive_type() : 
        #     return self.visitPrimitive_type(ctx)
        return self.visitChildren(ctx)

    # array_type: (ARRAY LS type_in_array  COMMA (INTLIT_ARR)  RS) ;
    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        array_type = self.visit(ctx.type_in_array())
        array_size = ctx.INTLIT_ARR().getText()
        if len(array_size) == 1 : 
            array_size = int(array_size)
        elif (array_size[1] == 'X' or array_size[1] == 'x') and len(array_size) > 1 : # hexa 
           array_size = int(array_size , 16)
        elif array_size[1] == 'B' or array_size[1] == 'b' : # Binary 
            array_size = int(array_size , 2)
        elif array_size[0] == '0' and len(array_size) > 1: #octal 
            array_size = int(array_size , 8)
        return ArrayType(array_size , array_type)
    
    # type_in_array : array_type | primitive_type ;
    def visitType_in_array(self, ctx: D96Parser.Type_in_arrayContext):
        return self.visitChildren(ctx)

    def visitPrimitive_type(self, ctx: D96Parser.Primitive_typeContext):
        if ctx.INT_TYPE():
            return  IntType()
        elif ctx.FLOAT_TYPE():
            return FloatType()
        elif ctx.BOOLEAN_TYPE(): 
            return BoolType()
        elif ctx.STRING_TYPE():
            return StringType()

    # def visitIndex_operator(self, ctx: D96Parser.Index_operatorContext):
    #     return self.visit(ctx.expression())

    # expression : expression1 (CONCATE | STRCOMPARE) expression1 | expression1;
    def visitExpression(self, ctx: D96Parser.ExpressionContext):
        if ctx.getChildCount() == 1 : 
            return self.visit(ctx.expression1(0))
        if ctx.CONCATE() : 
            op = ctx.CONCATE().getText()
        elif ctx.STRCOMPARE() : 
            op = ctx.STRCOMPARE().getText()  
        left = self.visit(ctx.expression1(0))
        right = self.visit(ctx.expression1(1))
        return BinaryOp(op,left,right)

    # expression1 : expression2 ( EQUAL | NOTEQUAL | LARGER | SMALLER | LE | SE) expression2 | expression2 ;
    def visitExpression1(self, ctx: D96Parser.Expression1Context):
        if ctx.getChildCount() == 1 : 
            return self.visit(ctx.expression2(0))
        if ctx.EQUAL() : 
            op = ctx.EQUAL().getText()
        elif ctx.NOTEQUAL() : 
            op = ctx.NOTEQUAL().getText()
        elif ctx.LARGER() : 
            op = ctx.LARGER().getText()
        elif ctx.SMALLER() : 
            op = ctx.SMALLER().getText()
        elif ctx.LE() : 
            op = ctx.LE().getText()
        elif ctx.SE() : 
            op = ctx.SE().getText()
        left = self.visit(ctx.expression2(0))
        right = self.visit(ctx.expression2(1))
        return BinaryOp(op,left,right)


    #expression2 : expression2 (OR | AND) expression3 | expression3;
    def visitExpression2(self, ctx: D96Parser.Expression2Context):
        if ctx.getChildCount() == 1 : 
            return self.visit(ctx.expression3())
        if ctx.OR() : 
            op = ctx.OR().getText() 
            left = self.visit(ctx.expression2())
            right = self.visit(ctx.expression3())
            return BinaryOp(op,left,right)
        if ctx.AND(): 
            op = ctx.AND().getText() 
            left = self.visit(ctx.expression2())
            right = self.visit(ctx.expression3())
            return BinaryOp(op,left,right)

    # expression3 : expression3 (ADD | SUB) expression4 | expression4;
    def visitExpression3(self, ctx: D96Parser.Expression3Context):
        if ctx.getChildCount() == 1 : 
            return self.visit(ctx.expression4())
        if ctx.ADD() : 
            op = ctx.ADD().getText()
            left = self.visit(ctx.expression3())
            right = self.visit(ctx.expression4())
            return BinaryOp(op,left,right)
        if ctx.SUB():
            op = ctx.SUB().getText()
            left = self.visit(ctx.expression3())
            right = self.visit(ctx.expression4())
            return BinaryOp(op,left,right)

    # expression4 : expression4 (MUL | DIV | MOD) expression5 | expression5;
    def visitExpression4(self, ctx: D96Parser.Expression4Context):
        if ctx.getChildCount() == 1 : 
            return self.visit(ctx.expression5())
        if ctx.MUL() : 
            op = ctx.MUL().getText() 
            left = self.visit(ctx.expression4())
            right = self.visit(ctx.expression5())
            return BinaryOp(op,left,right)
        if ctx.DIV() : 
            op = ctx.DIV().getText() 
            left = self.visit(ctx.expression4())
            right = self.visit(ctx.expression5())
            return BinaryOp(op,left,right)
        if ctx.MOD() : 
            op = ctx.MOD().getText() 
            left = self.visit(ctx.expression4())
            right = self.visit(ctx.expression5())
            return BinaryOp(op,left,right)

    # expression5 : NOT expression5 | expression6;
    def visitExpression5(self, ctx: D96Parser.Expression5Context):
        if ctx.getChildCount() == 1 : 
            return self.visit(ctx.expression6())
        op = ctx.NOT().getText() 
        body = self.visit(ctx.expression5())
        return UnaryOp(op,body)


    # expression6 : SUB expression6 | expression7;
    def visitExpression6(self, ctx: D96Parser.Expression6Context):
        if ctx.getChildCount() == 1 : 
            return self.visit(ctx.expression7())
        op = ctx.SUB().getText() 
        body = self.visit(ctx.expression6())
        return UnaryOp(op,body)

    # expression7 : expression7 (LS expression RS)+ | expression8;
    def visitExpression7(self, ctx: D96Parser.Expression7Context):
        if ctx.getChildCount() == 1 : 
            return self.visit(ctx.expression8())
        # idx = []
        idx = map(lambda x : self.visit(x) , ctx.expression())
        # for i in ctx.expression(): 
        #     idx.append(self.visit(i))
        arr = self.visit(ctx.expression7())
        return ArrayCell(arr,idx)

    #expression8 : expression8 DOT ID (LB expressions_list? RB)?  | expression9;   
    def visitExpression8(self, ctx: D96Parser.Expression8Context):
        if ctx.getChildCount() == 1 : 
            return self.visit(ctx.expression9())
        if ctx.expressions_list(): # call expr with parameters
            obj = self.visit(ctx.expression8())
            method = Id(ctx.ID().getText())
            params = self.visit(ctx.expressions_list())
            return CallExpr(obj,method,params)
        elif ctx.LB() and ctx.RB() : # call expr with no paras
            obj = self.visit(ctx.expression8())
            method = Id(ctx.ID().getText())
            params = []
            return CallExpr(obj,method,params)
        else : 
            obj = self.visit(ctx.expression8())
            field_name = Id(ctx.ID().getText())
            return FieldAccess(obj, field_name)



    # expression9 : ID DOUBLE_COLON DOLLAR_ID (LB expressions_list? RB)? | expression10; // :: 
    def visitExpression9(self, ctx: D96Parser.Expression9Context):
        if ctx.getChildCount() == 1 : 
            return self.visit(ctx.expression10())
        if ctx.expressions_list() : # a::$f(a,b,c) -> CallExpr
            obj = Id(ctx.ID().getText())  # fix this later
            method = Id(ctx.DOLLAR_ID().getText())
            params = self.visit(ctx.expressions_list())
            return CallExpr(obj,method,params)
        elif ctx.LB() and ctx.RB() : # call expr with no paras
            obj = Id(ctx.ID().getText())  # fix this later
            method = Id(ctx.DOLLAR_ID().getText())
            params = []
            return CallExpr(obj,method,params)
        else : # a::$f -> FieldAccess
            obj = Id(ctx.ID().getText())
            field_name = Id(ctx.DOLLAR_ID().getText())
            return FieldAccess(obj,field_name)

    # expression10 : NEW expression10 LB expressions_list? RB | operands;
    def visitExpression10(self, ctx: D96Parser.Expression10Context):
        if ctx.getChildCount() == 1 : 
            return self.visit(ctx.operands())
        class_params = []
        if ctx.expressions_list() : 
            class_params = self.visit(ctx.expressions_list())
        class_id = self.visit(ctx.expression10())
        return NewExpr(class_id,class_params)

# operands : literals| ID | (LB expression RB)  | indexed_array | multi_array | SELF | NULL;
    def visitOperands(self, ctx: D96Parser.OperandsContext):
        if ctx.ID() : 
            return Id(ctx.ID().getText())
        if ctx.SELF():
            return SelfLiteral()
        if ctx.NULL() : 
            return NullLiteral()
        if ctx.LB() and ctx.RB() and ctx.expression() : 
            return self.visit(ctx.expression())
        return self.visitChildren(ctx)
    
    # literals : ( INTLIT_ARR | STRING_LITERAL | INT_LITERAL | FLOAT_LITERAL | BOOL_LITERAL ) ;
    def visitLiterals(self, ctx: D96Parser.LiteralsContext):
        if ctx.BOOL_LITERAL():
            return BooleanLiteral(ctx.BOOL_LITERAL().getText() == 'True')
        if ctx.STRING_LITERAL(): 
            return StringLiteral(ctx.STRING_LITERAL().getText())
        if ctx.INT_LITERAL(): 
            val = ctx.INT_LITERAL().getText() 
            if len(val) == 1 : 
                return IntLiteral(int(val))
            if (val[1] == 'X' or val[1] == 'x') and len(val) > 1 : # hexa 
                return IntLiteral(int(val, 16))
            if val[1] == 'B' or val[1] == 'b' : # Binary 
                return IntLiteral(int(val, 2))   
            if val[0] == '0' and len(val) > 1: #octal 
                return IntLiteral(int(val, 8))
            return IntLiteral(int(val))

        if ctx.FLOAT_LITERAL() : 
            val = ctx.FLOAT_LITERAL().getText()
            if val[0] == '.' and val[1] == 'e' : # .e10
                return FloatLiteral(float( '0'+ val ))  
            return FloatLiteral(float(val))

        if ctx.INTLIT_ARR(): 
            val = ctx.INTLIT_ARR().getText() 
            if len(val) == 1 : 
                return IntLiteral(int(val))
            if (val[1] == 'X' or val[1] == 'x')  : # hexa 
                return IntLiteral(int(val, 16))
            if val[1] == 'B' or val[1] == 'b' : # Binary 
                return IntLiteral(int(val, 2))   
            if val[0] == '0' and len(val) > 1: #octal 
                return IntLiteral(int(val, 8))
            return IntLiteral(int(val))

    # multi_array : (indexed_array (COMMA indexed_array)* ) | (ARRAY LB multi_array (COMMA multi_array)* RB )  ;


    # indexed_array : ARRAY LB expressions_list? RB;
    def visitIndexed_array(self, ctx: D96Parser.Indexed_arrayContext):
        expression_list = self.visit(ctx.expressions_list()) if ctx.expressions_list() else []
        return ArrayLiteral(expression_list)
        

    # function_call : (ID (LB expressions_list? RB)? );
    # def visitFunction_call(self, ctx: D96Parser.Function_callContext):
    #     id = Id(ctx.ID().getText())
    #     params = self.visit(ctx.expressions_list())
    #     return id , params

    # expressions_list : (expression ( COMMA expression)*); 
    def visitExpressions_list(self, ctx: D96Parser.Expressions_listContext):
        res = map(lambda x :self.visit(x) ,ctx.expression())
        # for exp in ctx.expression() : 
        #     res.append(self.visit(exp))
        return res # [Exp,Exp]
    # #class a : b { var a ;}
    # #classDecls: classDecl classDecls | classDecl
    # def visitClassdecls(self, ctx: D96Parser.ClassdeclsContext):
    #     if ctx.getChildCount() > 1:
    #         left = self.visit(ctx.classdecl())
    #         right = self.visit(ctx.classdecls())
    #         return left + right
        
    #     return self.visit(ctx.classdecl())
        

    # def visitClassdecl(self, ctx: D96Parser.ClassdeclContext):
    #     return [ClassDecl(Id(ctx.ID().getText()),[])]
       
    # def visitIdClass(self, ctx: D96Parser.IdlistContext):
    #     return list(map(lambda x: Id(x.getText()),ctx.ID()))




