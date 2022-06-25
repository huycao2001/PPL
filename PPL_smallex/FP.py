# # Write a function lstSquare(n:Int) that returns a list of the squares of the numbers from
# # 1 to n?
# # 
# # lst = [1,2,3,4 , [12,34]]
# # listlst = list(filter(lambda x : type(x) == list , lst))
# # print(listlst)

# import functools
# def compose (fun1,fun2,*functions):
#     def clone(f,g): 
#         return lambda x : g(f(x))
#     #print(functools.reduce(clone, reversed(functions), lambda x : x)(3))
#     fun3 = functools.reduce(clone, reversed(functions), lambda x : x)
#     lst = [fun1,fun2 , fun3]
#     return functools.reduce(clone,reversed(lst), lambda x : x)

# def square(n) :
#     return n*n


# def inc(n) : 
#     return n + 1

# f = compose(square,inc)

# def clone(f,g): 
#     return lambda x : g(f(x)) # return a function


# a = clone(square,inc)
# print(type(a))

# print(f(3))
# s = [1,2,3,4,5]
# count = len(s)
# count = list(reversed(list(range(count))))
# for i in count : 
#     if i == len(count) - 1 : 
#         print("hello")
#     else : 
#         print("hi")
# print(count)
def fun(x) : 
	return l + [1]

l = []
for i in range(3) : 
	print(l, " ")
	l = fun(l)
print(l)

