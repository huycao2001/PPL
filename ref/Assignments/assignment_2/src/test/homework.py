item = input()
resultList =[]
clone = ''
for i in item : 
	if i != ',':
		clone += i
	else: 
		resultList.append(clone)
		clone = ''
if clone : 
	resultList.append(clone)
print(resultList)
print(tuple(resultList))
