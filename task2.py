# Чи належить число ряду фібоначі

N = int(input());


def GetFibonachi(N):
	i = 1;
	first = 0;
	midle = 1;
	second = 0;
	while second <= N:
		second = first + midle;
		first = midle;
		midle = second;
		i+=1;
		if(second == N):
			print(f"\nЦе {i} розряд")
			return;
	
	print(f"Це число не належить ряду найближче до нього це {second}")

GetFibonachi(N);

