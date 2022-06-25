from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce 
 
class ASTGeneration(MPVisitor):
    def toBool(self,x):
        return x == "True"
 
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())
 
    # exp: (term ASSIGN)* term;
    def visitExp(self,ctx:MPParser.ExpContext):
        last_term = ctx.term(len(ctx.term()) - 1)
        lst = list(zip( ctx.ASSIGN(),ctx.term()))
        return reduce(lambda acc , ele : Binary(ele[0].getText() , self.visit(ele[1]), acc ), reversed(lst) , self.visit(last_term) )
        # terms = [self.visit(x) for x in ctx.term()]
        # assigns = [x.getText() for x in ctx.ASSIGN()]
        # right = terms[-1]
        # for i in range(len(assigns)):
        #     op = assigns[len(assigns) - i - 1]
        #     left = terms[len(assigns) - i - 1]
        #     right = Binary(op, left, right)
        # return right


    # term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MPParser.TermContext):
        if ctx.getChildCount() == 3:
            op = ctx.COMPARE().getText()
            left = self.visit(ctx.factor(0))
            right = self.visit(ctx.factor(1))
            return Binary(op, left, right)
 
        else:
            return self.visit(ctx.factor(0))
 

    # factor: operand (ANDOR operand)* 
    def visitFactor(self,ctx:MPParser.FactorContext):
        # acc first will be equal operand(0)
        # ele is a pair (operator , operand)
        # a and b or c -> [(and,b) , (or, c)]
        lst = list(zip(ctx.ANDOR(),ctx.operand()[1:]))
        return reduce(
        lambda acc , ele : Binary(ele[0].getText() , acc , 
        self.visit(ele[1]) ),
        lst,
        self.visit(ctx.operand(0))
        )
        

    # operand: ID | INTLIT | BOOLIT | LB exp RB;
    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():
            if ctx.BOOLIT().getText() == 'True' : 
                return BooleanLiteral(True)
            else : 
                return BooleanLiteral(False)
        else:
            return self.visit(ctx.exp())