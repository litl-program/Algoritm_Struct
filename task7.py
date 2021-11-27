from math import sqrt
from itertools import count, islice

a = int(input("m = "));
b = int(input("n = "));

print(a,"/",b)

def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True


def izi_veapen(caunt):
	work = caunt;
	i = 2;
	loot = 0;
	result = [];
	while True:
		if(isPrime(i)):
			if(int(work/i) == round((work/i),1)):
				loot +=1;
				work = work/i;
				continue;
			else:
				result.append([i,loot]);
				loot = 0;
		i+=1;
		if(work == 1 and i>10):
			break;
	return result;



def getLenPeriod(arrays):
	caunt = 0;
	if(arrays[0][1]>arrays[2][1]):
		caunt = arrays[0][1]
	else:
		caunt = arrays[2][1]
	return caunt;

def caunt_bigin(arrays):
	caunt = arrays[-1][0]
	i = 1;
	while True:
		if((10**i/caunt)%1 == 0):
			return i;
		else:
			i+=1;






def check(a,b):
	arrays = izi_veapen(b);
	slace = getLenPeriod(arrays);
	caunt = round(a/b, (slace + caunt_bigin(arrays)));
	arrays = str(caunt).split(".")
	print(f"{arrays[0]}.{arrays[1][:slace]} ({arrays[1][slace:]})")


check(a,b)










