# Знаходження найдовшої неспадної 
# послідовності чисел

def getMaxPos(Array):
	result = [];
	i = 0;
	start = 0;
	for i in range(len(Array)):
		if(Array[i-1]<=Array[i]):
			continue;
		else:
			result.append(Array[start:i])
			start = i;
	arraylist = [len(result[i]) for	i in range(len(result))];
	maxiter = max(arraylist);
	index = arraylist.index(maxiter);
	return result[index];

result = getMaxPos([1,32,4,32,12,3,23,233,4,3,4,3,2,3,4,5,6,7,23,1,31,32,3])

print(result);



