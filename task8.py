from fractions import Fraction
import math
def FromFloat(caunt):
	result = [];
	jo = 1;	
	rez = 4;
	result.append(int(caunt//1))
	# caunt = Fraction(f"{round(caunt,rez)}");
	while jo > 0:
		jo = caunt % 1
		# jo = Fraction(f"{round(jo,rez)}")
		rez-= 1;
		caunt = 1/jo;
		# caunt = Fraction(f"{round(1/jo,rez)}");
		if(caunt % 1 == 0.00000):
			result.append(caunt);
			break;
		result.append(caunt//1)
		print(result);
	return result;

print(FromFloat(math.pi))
	


def FromArray(Array):
	return None;













	# while jo > 0:
	# 	jo = caunt % 1.0
	# 	print(jo)
	# 	result.append(caunt//1)
	# 	caunt = 1/jo;
	# 	if(caunt%1 == 0):
	# 		break;


# def FromFloat(caunt):
# 	result = [];
# 	result.append(int(caunt//1))
# 	rez = 3;
# 	caunt = caunt%1 - 0.0000000000000001;
# 	while caunt > 0:
# 		result.append(caunt//1)
# 		caunt = caunt % 1 - 0.0000000000000001
# 		caunt = round((1/caunt),rez);
# 		rez-=1; 
# 		print(caunt)
# 		if(caunt % 1 == 0.00000):
# 			break;
# 	print(caunt)
# 	return result;

# print(FromFloat(2.515))