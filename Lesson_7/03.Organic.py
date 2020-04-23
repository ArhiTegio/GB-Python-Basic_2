class CellOrganic:
    def __init__(self, counts=1):
        if isinstance(counts, int):
            self.count = counts
        else:
            self.count = 1

    def __add__(self, other):
        if isinstance(other, CellOrganic):
            return CellOrganic(self.count + other.count)
        return self

    def __sub__(self, other):
        if isinstance(other, CellOrganic):
            answer = self.count - other.count;
            if answer > 0:
                return CellOrganic(self.count - other.count)
            else:
                print('Число клеток может стать слишком малым. Операция {} отменена.'
                      .format(f'{str(self.count)} - {str(other.count)}'))
                return self
        return self

    def __mul__(self, other):
        if isinstance(other, CellOrganic):
            return CellOrganic(self.count * other.count)
        return self


    def __truediv__(self, other):
        if isinstance(other, CellOrganic):
            if other.count > 0:
                answer = round(self.count / other.count)
                if answer == 0:
                    print('Число клеток может стать слишком малым. Операция {} отменена'
                          .format(f'{str(self.count)} / {str(other.count)}'))
                    return self
                else:
                    return CellOrganic(answer)
            else:
                print('Деление на ноль. Операция {} отменена'.format(f'{str(self.count)} / {str(other.count)}'))
                return self
        return self

    def _view_row_cell(self, i, count_row):
         return '*' if i % count_row != 0 else '*\n'

    def make_order(self, count_row):
        answer = ''.join([self._view_row_cell(i, count_row) for i in range(0, self.count)])
        if answer[len(answer) - 1] == 'n':
            return answer[0: len(answer) - 3]
        return answer

    def __str__(self):
        return f'Всего клеток: {str(self.count)}'


cell1 = CellOrganic(10)
cell2 = CellOrganic(5)
cell3 = CellOrganic(2)

print(cell1 * cell2)
print(cell1 - cell2)
print(cell1 + cell2)
print(cell1 / cell2)
print(cell2 / cell1)
print(cell2 - cell1)

print((cell1 / cell2 * cell3) + cell1 - cell3 - 1)
