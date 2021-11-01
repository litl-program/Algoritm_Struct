# Феномен Вілла Роджерса
import random as r;


def GetArray(lenght):
	Array = []
	i = 0;
	while i < lenght:
		Array.append(r.randint(0,100))
		i+=1
	return Array;

m = int(input("m = "));
n = int(input("n = "));

# A = GetArray(m);
# B = GetArray(n);

A =  [5, 6, 7, 8, 9];

B =  [1, 2, 3, 4];
print(A,"\n",B,"\n\n");



def	Rodgers(A,B):
	serArB = sum(B)/len(B);
	serArA = sum(A)/len(A);
	result = []
	for i in range(len(A)):
		if(A[i]<serArA and A[i]>serArB):
			result.append(A[i]);
	return result;

print("Числа що задовільняють умові! ", Rodgers(A,B),"\n\n");


def Rodgers2(A,B):
	A.sort(); B.sort();
	result = [];
	i = 0;
	while(i < len(A)):
		serArA = sum(A)/len(A);
		serArB = sum(B)/len(B);
		if(A[i]<serArA and A[i]>serArB):
			result.append(A[i])
			B.append(A[i])
			A.pop(i);
		i+=1
	return result;

print("Вибірка чисел що задовільняють умові 2.",Rodgers2(A,B)
,"\n\n");



def Rodgers3(A,B):
	A.sort(); B.sort();
	print("Work is last:\n")
	serArB = sum(B)/len(B);
	serArA = sum(A)/len(A);
	for	i in range(len(A)):
		for j in range(len(B)):
			A[i],B[j] = B[j],A[i];
			newSerArB = sum(B)/len(B);
			newSerArA = sum(A)/len(A);
			if(newSerArB > serArB and newSerArA > serArA):
				print(f"A = {B[j]} and B = {A[i]} задовільняють умову")
			A[i],B[j] = B[j],A[i];


Rodgers3(A,B);
