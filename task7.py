from math import sqrt
from itertools import count, islice

a = 71;
b = 340;

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
		if(work == 1):
			break;
	return result;

print(izi_veapen(132));






def period(m,n):
	
	return None;
	








