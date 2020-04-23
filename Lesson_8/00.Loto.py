import random


class Position:
    def __init__(self, number, crossed):
        self.number = number
        self.crossed = crossed

    def __str__(self):
        if self.crossed:
            if self.number != 0:
                return '\033[31m\033[4m{}\033[0m\033[30m'.format('\u0336' + '\u0336'.join(str(self.number)))
            else:
                return '\033[31m\033[4m{}\033[0m\033[30m'.format('\u0336' + '\u0336'.join(' '))
        else:
            if self.number != 0:
                return '\033[30m{}\033[30m'.format(str(self.number))
            else:
                return '\033[30m{}\033[30m'.format(' ')

    def __repr__(self):
        if self.crossed:
            if self.number != 0:
                return '\033[31m\033[4m{}\033[0m\033[30m'.format('\u0336' + '\u0336'.join(str(self.number)))
            else:
                return '\033[31m\033[4m{}\033[0m\033[30m'.format('\u0336' + '\u0336'.join(' '))
        else:
            if self.number != 0:
                return '\033[30m{}\033[30m'.format(str(self.number))
            else:
                return '\033[30m{}\033[30m'.format(' ')


class Tiket:
    def __init__(self):
        allNums = [num for num in range(1, 91)]
        self.lines = []
        for _ in range(0, 2):
            l = []
            for _ in range(0, 3):
                line = []
                fieldCount = 0
                for pos in range(0, 3):
                    col = 5 - fieldCount if pos == 2 else random.randint(1, 2)
                    fieldCount += col
                    field = [Position(0, False) for _ in range(0, 3 - col)]
                    for _ in range(0, col):
                        posintion = random.randint(0, len(allNums) - 1)
                        num = allNums[posintion]
                        del allNums[posintion]
                        field.insert(random.randint(0, len(field)), Position(num, False))
                    line += field
                l.append(line)
            self.lines.append(l)

    def CheckedFirstRound(self):
        for field in self.lines:
            a = 0
            for l in field:
               a += len([e for e in l if e.crossed])
            if a >= 15:
                return True
        return False

    def CheckSecondRound(self):
        for field in self.lines:
            for l in field:
                if len([e for e in l if e.crossed]) >= 5:
                    return True
        return False

    def CheckThiredRound(self):
        a = 0
        for field in self.lines:
            for l in field:
               a += len([e for e in l if e.crossed])
        return True if a >= 30 else False

    def CrossedNum(self, num):
        for field in self.lines:
            for l in field:
                for e in l:
                    if e.number == num:
                        e.crossed = True
                        return True
        return False

    def __str__(self):
        answer = ''
        answer += ''.join(['_' for _ in range(0, 35)]) + '\n'
        for l in self.lines:
            for line in l:
                answer += '\t'.join([str(pos) for pos in line]) + '\n'
            answer += ''.join(['_' for _ in range(0, 35)]) + '\n'
        return answer

    def __repr__(self):
        answer = ''
        answer += ''.join(['_' for _ in range(0, 35)]) + '\n'
        for l in self.lines:
            for line in l:
                answer += '\t'.join([str(pos) for pos in line]) + '\n'
            answer += ''.join(['_' for _ in range(0, 35)]) + '\n'
        return answer


class Player:
    def __init__(self, name):
        self.name = name
        self.tiket = Tiket()


class Game_loto:

        def __init__(self, numAIplayer):
            self.allNums = [num for num in range(1, 91)]
            self.listPlayers = []
            self.listPlayers.append(Player('player'))

            [self.listPlayers.append(Player('AIplayer{}'.format(n))) for n in range(0, numAIplayer)]
            self.viktory = {
                'first': '',
                'second': '',
                'thired': ''
            }

        def start_game(self):
            print('Начинаеться игра Русское лото')
            step = 0
            while(True):
                step += 1
                print(f'Ход - {step}')
                num = random.randint(0, len(self.allNums) - 1)
                barrel = self.allNums[num]
                del self.allNums[num]
                print(f'Выпал бочонок номер {barrel}')
                isEnd = False
                for player in self.listPlayers:
                    print(player.name)
                    print(player.tiket)
                    if player.name == 'player':
                        answer = input(f'Есть ли в вашем билете число {barrel}? (y - да)\n')
                        if answer == 'y':
                            answer = True
                        else:
                            answer = False
                        inTiket = player.tiket.CrossedNum(barrel)
                        if answer != inTiket:
                            print('Вы проиграли! Вы не нашли число в своем билете')
                            isEnd = True
                            break
                    else:
                        player.tiket.CrossedNum(barrel)
                        if random.randint(1, 1000) == 777:
                            print(f'Игрок {player.name} проиграли! Он не нашел число в своем билете')
                            isEnd = True
                            break

                    if player.tiket.CheckedFirstRound() and self.viktory['first'] == '' and step == 15:
                        print(f'Игрок {player.name} выйграл Джекпот!')
                        input('')
                        isEnd = True
                        break
                    if player.tiket.CheckedFirstRound() and self.viktory['first'] == '':
                        print(f'Игрок {player.name} выйграл в первом туре!')
                        input('')
                        self.viktory['first'] = player.name
                    if player.tiket.CheckSecondRound() and self.viktory['second'] == '':
                        print(f'Игрок {player.name} выйграл во втором туре!')
                        input('')
                        self.viktory['second'] = player.name
                    if player.tiket.CheckThiredRound() and self.viktory['thired'] == '':
                        print(f'Игрок {player.name} выйграл во втором туре!')
                        input('')
                        self.viktory['thired'] = player.name
                        break

                if isEnd:
                    print('Игра завершилась')
                    break

                if self.viktory['first'] != '' and self.viktory['second'] != '' and self.viktory['thired'] != '':
                    print('Игра завершилась')
                    print('Выйграли игроки в слудющих турах:')
                    print('В первом туре игрок {}'.format(self.viktory['first']))
                    print('Во втором туре игрок {}'.format(self.viktory['second']))
                    print('В третьем туре игрок {}'.format(self.viktory['thired']))
                    break


game = Game_loto(1)
game.start_game()
