A = [2,1]



def getMaxPosRecurs(Array):
	try:
		newArray = [int(Array[0])]
	except IndexError:
		return []
	for i in range(1, len(Array)):
		Array[i] = int(Array[i])
		if(Array[i]>=newArray[-1]):
			newArray.append(Array[i])
		else:
			newArray2 = getMaxPosRecurs(Array[i::].copy())
			if(len(newArray)>len(newArray2)):
				return newArray;
			else:
				return newArray2;
	return newArray;



result = getMaxPosRecurs(A)

print(result);

