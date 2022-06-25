class Visitable:
    def __init__(self):
        pass
    def accept(myVisitor):
        pass
class Visitor:
    def __init__(self):
        pass
    def visit(item):
        pass
class Eval (Visitor):
    def visit(self,item):
        if hasattr(item, 'operator'):
            if item.operator == '+':
                return item.operand1.accept(Eval()) + item.operand2.accept(Eval())
            elif item.operator == '-':
                return item.operand1.accept(Eval()) - item.operand2.accept(Eval())
            elif item.operator == '*':
                return item.operand1.accept(Eval()) * item.operand2.accept(Eval())
            elif item.operator == '/':
                return item.operand1.accept(Eval()) / item.operand2.accept(Eval())
        elif hasattr(item, 'value_bin'):
            return item.value_bin
        else:
            return item.value
class PrintPrefix (Visitor):
    def visit(self, item):
        if hasattr(item, 'operator'):
            return item.operator + ' ' + str(item.operand1.accept(PrintPrefix())) + ' ' + str(item.operand2.accept(PrintPrefix()))
        elif hasattr(item, 'value_bin'):
            if item.value_bin > 0:
                return '+. ' + str(item.value_bin)
            elif item.value_bin < 0:
                return '-. ' + str(-item.value_bin)
            else:
                return '0'
        else:
            return str(item.value)
class PrintPostfix (Visitor):
    def visit(self, item):
        if hasattr(item, 'operator'):
            return str(item.operand1.accept(PrintPostfix())) + ' ' + str(item.operand2.accept(PrintPostfix())) + ' ' + item.operator
        elif hasattr(item, 'value_bin'):
            if item.value_bin > 0:
                return  str(item.value_bin) + ' +.'
            elif item.value_bin < 0:
                return  str(-item.value_bin) + ' -.'
            else:
                return '0'
        else:
            return str(item.value)
class Exp (Visitable):
    def accept(self, myvisitor):
        return myvisitor.visit(self)
        
class BinExp (Visitable):
    def __init__(self, operand1, operator, operand2):
        self.operand1 = operand1
        self.operator = operator
        self.operand2 = operand2
    def accept(self, myvisitor):
        return myvisitor.visit(self)

class UnExp (Visitable):
    def __init__(self, operator, value):
        if operator == '-':
            self.value_bin =  0 - value.value
        else:
            self.value_bin =  value.value
    def accept(self, myvisitor):
        return myvisitor.visit(self)

class IntLit (Visitable):
    def __init__(self, value):
        assert type(value) == int
        self.value = value
    def accept(self, myvisitor):
        return myvisitor.visit(self)

class FloatLit (Visitable):
    def __init__(self, value):
        assert type(value) == float
        self.value = value
    def accept(self, myvisitor):
        return myvisitor.visit(self)
        
intlit1 = IntLit(4)
a = UnExp('-', intlit1)
intlit2 = IntLit(3)
intlit3 = IntLit(2)
exp1 = BinExp(intlit2, '*', intlit3)
exp2 = BinExp(a,'+', exp1)
print(exp2.accept(Eval()))
print(exp2.accept(PrintPostfix()))
print(exp2.accept(PrintPrefix()))
print("The second test")
intlit1_ = IntLit(4)
un_exp = UnExp('-', intlit1_)
floatlit1 = FloatLit(3.2)
my_exp1 = BinExp(un_exp, '*', floatlit1)
intlit2_ = IntLit(2)
intlit3_ = IntLit(3)
my_exp2 = BinExp(intlit2_, '/', intlit3_)
final_exp = BinExp(my_exp1, '+', my_exp2)
print(final_exp.accept(Eval()))
print(final_exp.accept(PrintPostfix()))
print(final_exp.accept(PrintPrefix()))

