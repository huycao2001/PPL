from abc import ABC
# from ast import operator

class Exp(ABC): pass

class Visitor(ABC): pass

class Eval(Visitor):
    def visit(self, e: Exp):
        return(e.eval())
    
class PrintPrefix(Visitor):
    def visit(self, e: Exp):
        return(e.printPrefix())
        
class PrintPostfix(Visitor):
    def visit(self, e: Exp):
        return(e.printPostfix())

class BinExp(Exp):
    def __init__(self, operand1, operator, operand2):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator
    def eval(self):
        if (self.operator == "+"):
            return self.operand1.accept(Eval()) + self.operand2.accept(Eval())
        elif (self.operator == "-"):
            return self.operand1.accept(Eval()) - self.operand2.accept(Eval())
        elif (self.operator == "*"):
            return self.operand1.accept(Eval()) * self.operand2.accept(Eval())
        else:
            return self.operand1.accept(Eval()) / self.operand2.accept(Eval())
            
    def printPrefix(self):
        return self.operator + ' '+ str(self.operand1.accept(PrintPrefix())) + ' ' + str(self.operand2.accept(PrintPrefix()))
    
    def printPostfix(self):
        return str(self.operand1.accept(PrintPostfix())) + ' ' + str(self.operand2.accept(PrintPostfix())) + ' '+ self.operator
        
    def accept(self, v: Visitor):
        return v.visit(self)

class UnExp(Exp):
    def __init__(self, operator, operand):
        self.operand = operand
        self.operator = operator
    def eval(self):
        if (self.operator == "+"):
            return self.operand.eval()
        else:
            return -1 * self.operand.eval()
            
    def printPrefix(self):
        if self.operator == '+':
            return '+. ' + str(self.operand.eval())
        else :
            return '-. ' + str(self.operand.eval())
        
    def printPostfix(self):
        if self.operator == '+':
            return str(self.operand.eval()) + ' +.'
        else : 
            return str(self.operand.eval()) + ' -.'
        
    def accept(self, v: Visitor):
        return v.visit(self)


class IntLit(Exp):
    def __init__(self, value):
        self.value = value
    def eval(self):
        return self.value
    def printPrefix(self):
        return str(self.eval())
    def printPostfix(self):
        return str(self.eval())
    def accept(self, v: Visitor):
        return v.visit(self)
    
class FloatLit(Exp):
    def __init__(self, value):
        self.value = value
    def eval(self):
        return self.value
    def printPrefix(self):
        return str(self.eval())
    def printPostfix(self):
        return str(self.eval())
    def accept(self, v: Visitor):
        return v.visit(self)

intlit1 = IntLit(4)
a = UnExp('-', intlit1)
intlit2 = IntLit(3)
intlit3 = IntLit(2)
exp1 = BinExp(intlit2, '*', intlit3)
exp2 = BinExp(a,'+', exp1)
print(exp2.accept(Eval()))
print(exp2.accept(PrintPostfix()))
print(exp2.accept(PrintPrefix()))

