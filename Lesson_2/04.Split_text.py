print('Работа со строками')

def print_string(text):
    l_string = text.split(' ')
    print(''.join([str(num + 1) + '. ' + str(l_string[num])[0:10] + '\n' for num in range(len(l_string))]))


n = input('Введите строку: ')
if n != '':
    print_string(n)
