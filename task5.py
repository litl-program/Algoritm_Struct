#Схема Горнера


def horner(poly, n, x):
	result = poly[0] 
	for i in range(1, n):
		result = result*x + poly[i]
	return result
  

poly = [2, -6, 2, -7]
x = 3
n = len(poly)
 
print("Value of polynomial is " , horner(poly, n, x))
def hornerRecurs(poly, x, i =1,result =0):
	try:
		if(i ==1):
			result = poly[0];
		result = result*x + poly[i];
		return hornerRecurs(poly, x, i+1,result);
	except:
		return result;



print("Value of polynomial is " , hornerRecurs(poly, x));
