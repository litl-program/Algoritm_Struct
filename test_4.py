A = [3,1,2]
# [1, 5, 7]
# A [3:]= [2,4,2,6,6,7,8,6,7]
# [2,4] <-[1, 5, 7]
# A[2:] = [2,6,6,7,8,6,7]

def getMaxPos(Array):
	results = [];
	start = 0;
	end = 0
	start_max = 0
	end_max = 0
	for i in range(1, len(Array)):
		if(Array[i-1] <= Array[i]):
			end = end + 1
		else:
			results.append(Array[start:end+1])
			if (end - start) > (end_max - start_max):
				start_max = start
				end_max = end
			start = i
			end = i
	results.append(Array[start:end+1])
	return (results,start_max,end_max);


def getMaxPosRecurs(Array,value =[0,0,0,0,1],Result=[]):
	start = value[0];
	end = value[1];
	start_max = value[2]
	end_max = value[3]
	i = value[4]
	try:
		if(Array[i-1] <= Array[i]):
			getMaxPosRecurs(Array,[start,end+1,start_max,end_max,i+1])
		else:
			Result.append(Array[start:end+1])
			if (end - start) > (end_max - start_max):
				start_max = start
				end_max = end
			start = i
			end = i
			getMaxPosRecurs(Array,[start,end,start_max,end_max,i+1])
	except:
		Result.append(Array[start:end+1])
		print(Great(Result));
		



def Great(result):
	arraylist = [len(result[i]) for	i in range(len(result))];
	maxiter = max(arraylist);
	index = arraylist.index(maxiter);
	return result[index];


getMaxPosRecurs(A)



# print(result);print(Result)



