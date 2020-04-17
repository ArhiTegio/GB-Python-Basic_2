from time import sleep


class Stationery:
    hint = ''
    title = ''

    def draw(self):
        print('Инструмент - {}'.format(str(self)[str(self).find('.') + 1:str(self).find(' ')]))
        print(self.hint)
        print('Запуск отрисовки...')
        for i in range(0, 5):
            print('Прогресс - {}%'.format(i * 25))
            sleep(0.5)
        print('Выполнена отрисовка инструмента - {}'.format(str(self)[str(self).find('.') + 1:str(self).find(' ')]))


class Pen(Stationery):
    def __init__(self):
        self.hint = 'Pen (ручка) — стандартный и типовой инструмент для создания векторных кривых ' \
                    '(быстрый вызов Ctrl+P)'

    def draw(self):
        super().draw()


class Pencil(Stationery):
    def __init__(self):
        self.hint = 'Pencil (Карандаш) - предназначен для рисования произвольных линий с четкими границами. ' \
           'Для этого инструмента можно также задавать длину штриха, степень непрозрачности Opacity ' \
           '(Непрозрачность), режим наложия пикселов Mode (Режим).'

    def draw(self):
        super().draw()


class Handle (Stationery):
    def __init__(self):
        self.hint = 'Handle (маркер) - предназначен для рисования произвольных линий с не четкими границами.'

    def draw(self):
        super().draw()


if __name__ == "__main__":
    pen = Pen()
    pen.draw()

    pencil = Pencil()
    pencil.draw()

    handle = Handle()
    handle.draw()
