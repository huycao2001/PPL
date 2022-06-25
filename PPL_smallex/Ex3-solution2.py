from abc import ABC

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
        if type(operand1) is int:
            self.operand1 = IntLit(operand1)
        elif type(operand1) is float:
            self.operand1 = FloatLit(operand1)
        else:
            self.operand1 = operand1
            
        if type(operand2) is int:
            self.operand2 = IntLit(operand2)
        elif type(operand2) is float:
            self.operand2 = FloatLit(operand2)
        else:
            self.operand2 = operand2
            
        self.operator = operator
    def eval(self):
        if (self.operator == "+"):
            return self.operand1.eval() + self.operand2.eval()
        elif (self.operator == "-"):
            return self.operand1.eval() - self.operand2.eval()
        elif (self.operator == "*"):
            return self.operand1.eval() * self.operand2.eval()
        else:
            return self.operand1.eval() / self.operand2.eval()
            
    def printPrefix(self):
        return f'{self.operator} {self.operand1.printPrefix()} {self.operand2.printPrefix()}'
    
    def printPostfix(self):
        return f'{self.operand1.printPostfix()} {self.operand2.printPostfix()} {self.operator}'
        
    def accept(self, v: Visitor):
        return v.visit(self)
    
class UnExp(Exp):
    def __init__(self, operator, operand):
        if type(operand) is int:
            self.operand = IntLit(operand)
        elif type(operand) is float:
            self.operand = FloatLit(operand)
        else:
            self.operand = operand
            
        self.operator = operator
    def eval(self):
        if (self.operator == "+"):
            return self.operand.eval()
        else:
            return -1*self.operand.eval()
            
    def printPrefix(self):
        return f'{self.operator}. {self.operand.printPrefix()}'
        
    def printPostfix(self):
        return f'{self.operand.printPostfix()} {self.operator}.'
        
    def accept(self, v: Visitor):
        return v.visit(self)
        
    
class IntLit(Exp):
    def __init__(self, i):
        self.i = i
    def eval(self):
        return self.i
    def printPrefix(self):
        return self.eval()
    def printPostfix(self):
        return self.eval()
    def accept(self, v: Visitor):
        return v.visit(self)
    
class FloatLit(Exp):
    def __init__(self, f):
        self.f = f
    def eval(self):
        return self.f
    def printPrefix(self):
        return self.eval()
    def printPostfix(self):
        return self.eval()
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
