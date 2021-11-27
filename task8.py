

def FromFloat(get):
	print(get);
	result = [];
	caunt = get;
	jo= 0;
	solo = precision(caunt);
	result.append(int(caunt));
	while(get != round(FromArray(result),solo)):
		jo = round(caunt - int(caunt),solo);
		caunt = 1 / jo;
		result.append(int(caunt));
	return result;

def precision(caunt):
	len_array = str(caunt).split(".");
	dens = int(len(len_array[1]));
	if(dens<=2):
		dens+=2
	else:
		dens+=1;
	return dens;

def FromArray(Array):
	i  = len(Array)-1;
	repit = Array[i];
	if(i == 0):
		return repit;
	while(i>=0):
		repit = Array[i]+(1/repit)
		i -=1;
	return repit;
		

#[2,1,1,16,6]
# print(FromCaunt([2,1,1,16,6]))

caunt = float(input());

print(FromFloat(caunt))

print(FromArray(FromFloat(caunt)))



















