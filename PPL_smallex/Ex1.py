class Exp:
    def __init__(self):
        pass
    def eval():
        pass
class BinExp(Exp):
    def __init__(self, operand1, operator, operand2):
        self.operand1 = operand1
        self.operator = operator
        self.operand2 = operand2
    def eval(self):
        if self.operator == '+':
            return self.operand1.eval() + self.operand2.eval()
        elif self.operator == '-' : 
            return self.operand1.eval() - self.operand2.eval()
        elif self.operator == '*' : 
            return self.operand1.eval() * self.operand2.eval()
        elif self.operator == '/' : 
            return self.operand1.eval() / self.operand2.eval()
    def printPrefix(self):
        return self.operator + ' ' + self.operand1.printPrefix()+ ' ' + self.operand2.printPrefix()
        #return str(self.operator) + ' ' + self.operand1.printPrefix() + ' ' + self.operand2.printPrefix() 
class UnExp(Exp):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def eval(self):
        if self.operator == '-':
            return self.operand.eval() * (-1)
        else: 
            return self.operand.eval()

    def printPrefix(self):
        if self.operator == '-':
            return '-. ' + str(self.operand.eval())
        elif self.operator == '+':
            return '+. ' + str(self.operand.eval())

class IntLit(Exp):
    def __init__(self, value):
        assert type(value) == int
        self.value = value
    def eval(self):
        return self.value
    def printPrefix(self):
        return str(self.value)

class FloatLit(Exp):
    def __init__(self, value):
        assert type(value) == float
        self.value = value
    def eval(self):
        return self.value
    def printPrefix(self):
        return str(self.value)

#print("hello")
y = IntLit(123)
x = UnExp('-',y)
print(x.eval())