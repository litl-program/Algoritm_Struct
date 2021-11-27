#Визначити довжину степеня числа у бінарному коді;

k  =int(input("k = "));
m = int(input("m = "));
if(m<k):
	k  =int(input("k = "));
	m = int(input("m = "));
caunt_repit = 2**m
result = 0;
i = 0;

while result < caunt_repit:
	i+=1
	result = i**k



print("Необхідне число",i);
print(result);
print(bin(result));