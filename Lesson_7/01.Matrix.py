import random
from threading import Thread


class Matrix:
    def __init__(self, N, M):
        self._N = N if N > 0 else self._N
        self._M = M if M > 0 else self._M
        self.matrix = []
        [self.matrix.append([]) for i in range(0, self._N + 1)]
        for n in range(0, self._N + 1):
            t = Thread(target=self.__create_row_async, args=(n, self._M + 1))
            t.start()

    def __create_row_async(self, pos, count):
        self.matrix[pos] = [random.randint(30, 60) for i in range(0, count)]

    def __str__(self):
        answer = ""
        for n in range(0, len(self.matrix) - 1):
                answer += ''.join(c for c in "{}\n".format(self.matrix[n]) if not (c == ',' or c == '[' or c == ']'))
        return answer

    def __add__(self, arg):
        if self._N == arg._N and self._M == arg._M:
            for n in range(0, len(self.matrix)):
                t = Thread(target=self._add_async, args=(n, self.matrix[n], arg.matrix[n]))
                t.start()
        newMatrix = Matrix(self._N, self._M)
        newMatrix.matrix = self.matrix.copy()
        return newMatrix

    def _add_async(self, n, a_matrix, b_matrix):
        self.matrix[n] = [(a_matrix[y] + b_matrix[y]) for y in range(0, len(a_matrix))]


matrix1 = Matrix(5, 5)
print(str(matrix1))

matrix2 = Matrix(5, 5)
print(str(matrix2))

matrix3 = matrix1 + matrix2
print(str(matrix3))

print(str(matrix1 + matrix2 + matrix3))
