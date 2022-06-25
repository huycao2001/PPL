# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declaration.
    def visitClass_declaration(self, ctx:D96Parser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_declaration.
    def visitAttribute_declaration(self, ctx:D96Parser.Attribute_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#testing.
    def visitTesting(self, ctx:D96Parser.TestingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#testing2.
    def visitTesting2(self, ctx:D96Parser.Testing2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#att_name.
    def visitAtt_name(self, ctx:D96Parser.Att_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_declaration.
    def visitMethod_declaration(self, ctx:D96Parser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter_decl.
    def visitParameter_decl(self, ctx:D96Parser.Parameter_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_statement.
    def visitBlock_statement(self, ctx:D96Parser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_declare_statement.
    def visitVar_declare_statement(self, ctx:D96Parser.Var_declare_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_decl_stm_only.
    def visitVar_decl_stm_only(self, ctx:D96Parser.Var_decl_stm_onlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_decl_stm_assign.
    def visitVar_decl_stm_assign(self, ctx:D96Parser.Var_decl_stm_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_statement.
    def visitAssign_statement(self, ctx:D96Parser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_statement_main.
    def visitAssign_statement_main(self, ctx:D96Parser.Assign_statement_mainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_statement.
    def visitIf_statement(self, ctx:D96Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_statement.
    def visitFor_statement(self, ctx:D96Parser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar.
    def visitScalar(self, ctx:D96Parser.ScalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar_test.
    def visitScalar_test(self, ctx:D96Parser.Scalar_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invocation.
    def visitMethod_invocation(self, ctx:D96Parser.Method_invocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_statement.
    def visitReturn_statement(self, ctx:D96Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_statement.
    def visitBreak_statement(self, ctx:D96Parser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_statement.
    def visitContinue_statement(self, ctx:D96Parser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression.
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression1.
    def visitExpression1(self, ctx:D96Parser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression2.
    def visitExpression2(self, ctx:D96Parser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression3.
    def visitExpression3(self, ctx:D96Parser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression4.
    def visitExpression4(self, ctx:D96Parser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression5.
    def visitExpression5(self, ctx:D96Parser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression6.
    def visitExpression6(self, ctx:D96Parser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression7.
    def visitExpression7(self, ctx:D96Parser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression8.
    def visitExpression8(self, ctx:D96Parser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression9.
    def visitExpression9(self, ctx:D96Parser.Expression9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression10.
    def visitExpression10(self, ctx:D96Parser.Expression10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operator.
    def visitIndex_operator(self, ctx:D96Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#dollar_function.
    def visitDollar_function(self, ctx:D96Parser.Dollar_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#new_object.
    def visitNew_object(self, ctx:D96Parser.New_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#function_call.
    def visitFunction_call(self, ctx:D96Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexed_array.
    def visitIndexed_array(self, ctx:D96Parser.Indexed_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_array.
    def visitMulti_array(self, ctx:D96Parser.Multi_arrayContext):
        return self.visitChildren(ctx)



del D96Parser