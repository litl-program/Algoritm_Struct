# Знаходження найдовшої неспадної 
# послідовності чисел

A = [1,5,7,2,4,2,6,6,7,8,6,7]



def getMaxPos(Array):
	if(len(Array)==1):
		return Array;
	result = [];
	start = 0;
	i = 1;
	while(i<len(Array)):
		if(Array[i-1] <= Array[i]):	
			i+=1
			continue;
		else:
			result.append(Array[start:i])
			start = i;
			i+=1;
	if(len(result) == 0):
		return Array;
	print(result);
	arraylist = [len(result[i]) for	i in range(len(result))];
	maxiter = max(arraylist);
	index = arraylist.index(maxiter);
	return result[index];

result = getMaxPos(A)

print(result);


