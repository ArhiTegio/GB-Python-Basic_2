from enum import Enum

print('Обработка проекта исследования представленных товаров')


class Type_processing(Enum):
    ProString = 1
    ProNum = 2


class Goods:
    __list_goods = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
                    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
                    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})]
    __num = 0
    __dict_specifications_good = {'название': Type_processing.ProString, 'цена': Type_processing.ProNum,
                                  'количество': Type_processing.ProNum}
    __dict_pro = {Type_processing.ProNum: frozenset(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']),
                  Type_processing.ProString: frozenset(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                                                        'ё', 'й', 'ф', 'я', 'ц', 'ы', 'ч', 'у', 'в', 'с', 'к', 'а',
                                                        'м', 'е', 'п', 'и', 'н', 'р', 'т', 'г', 'о', 'ь', 'ш', 'л',
                                                        'б', 'щ', 'д', 'ю', 'з', 'ж', 'х', 'э', 'ъ', '`', '~', '-',
                                                        '_', '+', '=', '(', ')', '!', '@', '#', '%', '^', '&', '*',
                                                        '|', '\\', '/', ':', ';', '\'', ',', '.', '?', '№', '[', ']',
                                                        '{', '}'])}

    def __get_param(self, txt, type_p):
        while True:
            answer = input('Введите ' + txt + ': ')
            if all([f in self.__dict_pro[type_p] for f in answer]):
                return answer

    def add(self):
        self.__num += 1
        answers = {}
        all([answers.update({key: self.__get_param(key, value)}) for key, value in self.__dict_specifications_good.items()])
        answers.update({'eд': 'шт.'})
        self.__list_goods.append((self.__num, answers))

    def get_handling_goods(self):
        answer = {}
        for tup in self.__list_goods:
            item1, item2 = tup
            for key, value in item2.items():
                if key in answer.keys():
                    answer[key].append(value)
                else:
                    answer.update({key: []})
                    answer[key].append(value)
        checker = set()

        # для уникальных значений нужно переписать тут
        all([checker.add(e) for e in answer['eд']])
        answer['eд'] = list(checker)
        #####
        return answer


goods = Goods()
while True:
    answer = input('Добавить новый товар?(Введите любую не пустую строку):')
    if answer != '':
        goods.add()
    else:
        break

handling_goods = goods.get_handling_goods()
print(handling_goods)
