# class R : 
# 	def foo(self,i) : 
# 		return i*3

# class S1(R):
# 	def foo(self,i):
# 		return i + 5 

# class S2(R):
# 	def foo(self,i):
# 		return i * 5

# class SS(S2,S1):
# 	pass

# x = SS()
# print(x.foo(9))
# print(SS.mro())


# class Exp:
#     def eval(self):
#         return self.val

# class BinExp(Exp):
#     def __init__(self,x1, op, x2):
#         if op == '+':
#             self.val = x1.val + x2.val
#         if op == '-':
#             self.val = x1.val - x2.val
#         if op == '/':
#             self.val = x1.val / x2.val
#         if op == '*':
#             self.val = x1.val * x2.val
            
# class UnExp(Exp):
#     def __init__(self,op, x2):
#         if op == '+':
#             self.val = x2.val
#         if op == '-':
#             self.val = - x2.val
            
# class IntLit(Exp):
#     def __init__(self,x):
#         self.val = x
        
# class FloatLit(Exp):
#     def __init__(self,x):
        # self.val = x

### each expression will have a value

class Exp:
	def eval(self): 
		return self.value # result of the expression.

class BinExp(Exp):
	def __init__(self,ex1,op,ex2):  ## ex1 and ex2 are expressions
		if op == '+' :
			self.value = ex1.value + ex2.value
		if op == '-' : 
			self.value = ex1.value - ex2.value
		if op == '*' : 
			self.value = ex1.value * ex2.value
		if op == '/' : 
			self.value = ex1.value / ex2.value

class UnExp(Exp):
	def __init__(self,op,ex1):  ## ex1 and ex2 are expressions
		if op == '-':
			self.value = -ex1.value

class IntLit(Exp):
	def __init__(self,value):
		self.value = value

class FloatLit(Exp):
	def __init__(self,value):
		self.value = value

x = IntLit(2)
y = IntLit(3)

z = BinExp(x,'+',y)
w = BinExp(x,'+',y)
ans = BinExp(z,'+',w)



print(ans.eval())


