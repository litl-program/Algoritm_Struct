A = [1,5,7,2,4,2,6,6,7,8,6]
# [1, 5, 7]
# A [3:]= [2,4,2,6,6,7,8,6,7]
# [2,4] <-[1, 5, 7]
# A[2:] = [2,6,6,7,8,6,7]

def getMaxPos(Array):
	result = [];
	start = 0;
	end = 0
	start_max = 0
	end_max = 0
	for i in range(1, len(Array)):
		if(Array[i-1] <= Array[i]):
			end = end + 1
		else:
			result.append(Array[start:end+1])
			if (end - start) > (end_max - start_max):
				start_max = start
				end_max = end
			start = i
			end = i
	result.append(Array[start:end+1])
	return (result,start_max,end_max);



def getMaxPosRecurs(Array,value =[0,0,0,0,1]):
	start = value[0];
	end = value[1];
	start_max = value[2]
	end_max = value[3]
	i = value[4]
	if(i>=len(Array)):
		return (start_max,end_max)
	try:
		if(Array[i-1] <= Array[i]):
			getMaxPosRecurs(Array,[start,end+1,start_max,end_max,i+1])
		else:
			if (end - start) > (end_max - start_max):
				start_max = start
				end_max = end
			start = i
			end = i
			getMaxPosRecurs(Array,[start,end,start_max,end_max,i+1])
	except:
		print(Array[start_max:end_max])
		return Array[start_max:end_max]
		




result = getMaxPosRecurs(A)



# print(result);
print(result);



