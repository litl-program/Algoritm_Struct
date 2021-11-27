# Task: <Ортогоналізація Грама-Шмідта>
# Group: 'КН-20-Б'


from random import *
import numpy


def createVectorsArray(size):
	numList = []
	for vector in range(size):
		vectorList = []
		for number in range(size):
			vectorList.append(randint(-10, 10))
		numList.append(vectorList)
	return numList

def printMatrix(matrix):
    for row in matrix:
        print(row)



def det_1(matrix):
    def gaussIteration(matrix, row):
        N = len(matrix)
        m1 = matrix[row][row]
        for i in range(row, N):
            matrix[row][i] = matrix[row][i] / m1
        for i in range(row + 1, N):
            m2 = matrix[i][row]
            for k in range(row, N):
                matrix[i][k] -= matrix[row][k]* m2
        return m1
    D = 1.0
    for k in range(len(matrix)):
        D = D * gaussIteration(matrix, k)
    return D

def gaussIteration(matrix, row):
        N = len(matrix)
        sign = 1.0
        index_max_element = row
        max_element_in_row = abs(matrix[row][row])
        for i in range(row, N):
            if abs(matrix[row][i]) > max_element_in_row:
                max_element_in_row = abs(matrix[row][i])
                index_max_element = i
        if max_element_in_row == 0.0:
            return 0.0
        if index_max_element != row:
            sign = sign * (-1.0)
            for i in range(N):
                tmp = matrix[i][row]
                matrix[i][row] = matrix[i][index_max_element]
                matrix[i][index_max_element] = tmp
                matrix[i][row], matrix[i][index_max_element] = matrix[i][index_max_element], matrix[i][row]
        m1 = matrix[row][row]
        for i in range(row, N):
            matrix[row][i] = matrix[row][i] / m1
        for i in range(row + 1, N):
            m2 = matrix[i][row]
            for k in range(row, N):
                matrix[i][k] -= matrix[row][k]* m2
        return sign * m1

def det_2(matrix):
    D = 1.0
    for k in range(len(matrix)):
        D = D * gaussIteration(matrix, k)
    return D



def checkLinearDepByGaussian(a_matrix):
	# Перевіряємо на лінійну незалежність вектори,
	# за допомогою перевірки утворення базису (рангу матриці та детермінанту)
	if len(a_matrix) != len(a_matrix[0]):
		return True
	else:
		result_det = det_1(numericalVectorsList);
		if result_det != 0:
			return False
		else:
			return True


def vectorOrthogonalization(vectorsList):
	k = len(vectorsList[0])
	N = len(vectorsList)
	b = [[0] * k for i in range(N)]
	b[0] = vectorsList[0]
	for i in range(1, N):
		sum = vectorsList[i]
		for j in range(0, i):
			scolar_ab = 0
			scolar_bb = 0
			proj = [i for i in range(k)]
			for n in range(k):
				scolar_ab += b[j][n] * vectorsList[i][n]
				scolar_bb += b[j][n] * b[j][n]
			for n in range(k):
				proj[n] = (scolar_ab / scolar_bb) * b[j][n]
			for n in range(k):
				sum[n] -= proj[n]
		b[i] = sum
	return b


# Входные данные
N = int(input("Enter number: "))
numericalVectorsList = createVectorsArray(N)

#numericalVectorsList = [[1, 1, 1], [1, 2, 0], [0, -1, 2]] # Незалежні

print(f"\n___<Generated vectors>___\n{numericalVectorsList}")

IsVectorsDependence = checkLinearDepByGaussian(numericalVectorsList)
if IsVectorsDependence:
	print("Вектори лінійно залежні. Неможливо реалізувати процес ортогоналізації векторів за алгоритмом Грама-Шмідта.")
else:
	print("Вектори лінійно незалежні. Реалізація алгоритму ...\n")
	print("Result:")
	print(vectorOrthogonalization(numericalVectorsList))


# Тести

# numericalVectorsList = [[3, 4, 5], [-3, 0, 5], [4, 4, 4], [3,4,0]] # Залежні
# numericalVectorsList = [[1, 1, -1, -2], [5, 8, -2, -3], [3, 9, 3, 8]] # Залежні
# numericalVectorsList = [[1, 1, 1], [1, 2, 0], [0, -1, 1]] # Залежні
# numericalVectorsList = [[0, 1, 2], [1, 0, 1], [-1, 2, 4]] # Незалежні

