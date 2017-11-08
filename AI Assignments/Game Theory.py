import sys


class Mybest():
    def __init__(self, i=0, j=0, score=0, type=''):
        self.i = i
        self.j = j
        self.score = score
        self.type = type


class Move():
    def __init__(self, i, j):
        self.m = i
        self.n = j


class Game():
    board_val = []
    board_pos = []
    start = 'X'
    i_width = 0

    def file_read(self, file_name):
        fr = open(file_name, 'r')
        self.i_width = int(fr.readline().strip())
        mode = str(fr.readline().strip())
        player = str(fr.readline().strip())
        depth = int(fr.readline().strip())
        self.start = player
        for i in range(self.i_width):
            each_line = fr.readline().strip().split(' ')
            self.board_val.append(each_line)
        for i in range(self.i_width):
            temp = []
            each_line = str(fr.readline().strip())
            for j in range(len(each_line)):
                temp.append(each_line[j])
            self.board_pos.append(temp)
        fr.close()
        self.gameplay(mode, depth)

    def eval(self, player):
        sumx, sumo = 0, 0
        for i in range(self.i_width):
            for j in range(self.i_width):
                if self.board_pos[i][j] == 'X':
                    sumx += int(self.board_val[i][j])
                elif self.board_pos[i][j] == 'O':
                    sumo += int(self.board_val[i][j])
        if self.start == 'X':
            return (sumx - sumo)
        else:
            return (sumo - sumx)

    def gameplay(self, mode, depth):
        player = self.start
        alpha = -1 * sys.maxsize
        beta = +1 * sys.maxsize
        if mode == 'MINIMAX':
            play = self.minimax(player, depth)
        else:
            play = self.alphabeta(player, depth, alpha, beta)
        self.writefile(play)
        # print(play.i, play.j, play.type)

    def minimax(self, player, depth):
        if depth == 0 or self.boardisfull():
            best = Mybest()
            best.score = self.eval(player)
            return best
        b = Mybest()
        if player == self.start:
            b.score = -1 * sys.maxsize
        else:
            b.score = sys.maxsize
        move = self.legalmove()
        rival = ('X' if player == 'O' else 'O')
        for k in move:
            type, movear = self.makemove(player, k.m, k.n)
            reply = self.minimax(rival, depth - 1)
            # print(movear, reply.score)
            # print(self.board_pos)
            self.undomove(movear, type)
            if ((player == self.start and ((reply.score > b.score) or (reply.score == b.score and
                                                                type == 'Stake' and b.type == 'Raid'))) or
                    (player != self.start and ((reply.score < b.score) or (reply.score == b.score and
                                                                type == 'Stake' and b.type == 'Raid')))):
                b.i = k.m
                b.j = k.n
                b.type = type
                b.score = reply.score
                alpha = reply.score
        return b

    def alphabeta(self, player, depth, alpha, beta):
        if depth == 0 or self.boardisfull():
            best = Mybest()
            best.score = self.eval(player)
            return best
        b = Mybest()
        if player == self.start:
            b.score = alpha
        else:
            b.score = beta
        move = self.legalmove()
        rival = ('X' if player == 'O' else 'O')
        for k in move:
            type, movear = self.makemove(player, k.m, k.n)
            reply = self.alphabeta(rival, depth - 1, alpha, beta)
            # print(movear, reply.score)
            # print(self.board_pos)
            self.undomove(movear, type)
            if (player == self.start and ((reply.score > b.score) or (reply.score == b.score and
                                                                              b.type == 'Raid' and type == 'Stake'))):
                b.i = k.m
                b.j = k.n
                b.type = type
                b.score = reply.score
                alpha = reply.score
            elif (player != self.start and ((reply.score < b.score) or (reply.score == b.score and
                                                                                b.type == 'Raid' and type == 'Stake'))):
                b.i = k.m
                b.i = k.m
                b.j = k.n
                b.type = type
                b.score = reply.score
                beta = reply.score
            if alpha >= beta:
                break
        return b


    def boardisfull(self):
        for i in range(self.i_width):
            for j in range(self.i_width):
                if self.board_pos[i][j] == '.':
                    return False
        return True


    def legalmove(self):
        list = []
        for i in range(len(self.board_pos)):
            for j in range(len(self.board_pos)):
                if self.board_pos[i][j] == '.':
                    move = Move(i, j)
                    list.append(move)
        return list

    def makemove(self, player, row, col):
        movear = []
        if player == 'X':
            self.board_pos[row][col] = 'X'
        else:
            self.board_pos[row][col] = 'O'
        movear.append(row)
        movear.append(col)
        rival = ('O' if player == 'X' else 'X')
        type = "Stake"
        if row < 1 and col < 1:  # checking for left top corner
            if self.board_pos[row][col + 1] == player and self.board_pos[row + 1][col] == rival:
                self.board_pos[row + 1][col] = player
                movear.append(row + 1)
                movear.append(col)
                type = 'Raid'
            elif self.board_pos[row + 1][col] == player and self.board_pos[row][col + 1] == rival:
                self.board_pos[row][col + 1] = player
                movear.append(row)
                movear.append(col + 1)
                type = 'Raid'
            else:
                type = 'Stake'
            return (type, movear)
        if row == self.i_width - 1 and col < 1:  # checking left bottom corner
            if self.board_pos[row][col + 1] == player and self.board_pos[row - 1][col] == rival:
                self.board_pos[row - 1][col] = player
                movear.append(row - 1)
                movear.append(col)
                type = 'Raid'
            elif self.board_pos[row - 1][col] == player and self.board_pos[row][col + 1] == rival:
                self.board_pos[row][col + 1] = player
                movear.append(row)
                movear.append(col + 1)
                type = 'Raid'
            else:
                type = 'Stake'
            return (type, movear)
        if row < 1 and col == self.i_width - 1:  # checking right top corner
            if self.board_pos[row][col - 1] == player and self.board_pos[row + 1][col] == rival:
                self.board_pos[row + 1][col] = player
                movear.append(row + 1)
                movear.append(col)
                type = 'Raid'
            elif self.board_pos[row + 1][col] == player and self.board_pos[row][col - 1] == rival:
                self.board_pos[row][col - 1] = player
                movear.append(row)
                movear.append(col - 1)
                type = 'Raid'
            else:
                type = 'Stake'
            return (type, movear)
        if row == self.i_width - 1 and col == self.i_width - 1:  # checking right bottom corner
            if self.board_pos[row][col - 1] == player and self.board_pos[row - 1][col] == rival:
                self.board_pos[row - 1][col] = player
                movear.append(row - 1)
                movear.append(col)
                type = 'Raid'
            elif self.board_pos[row - 1][col] == player and self.board_pos[row][col - 1] == rival:
                self.board_pos[row][col - 1] = player
                movear.append(row)
                movear.append(col - 1)
                type = 'Raid'
            else:
                type = 'Stake'
            return (type, movear)
        if row == 0:  # checking top row but not corners
            if self.board_pos[row][col - 1] == player:
                if self.board_pos[row + 1][col] == rival:
                    self.board_pos[row + 1][col] = player
                    movear.append(row + 1)
                    movear.append(col)
                    type = 'Raid'
                if self.board_pos[row][col + 1] == rival:
                    self.board_pos[row][col + 1] = player
                    movear.append(row)
                    movear.append(col + 1)
                    type = 'Raid'
            elif self.board_pos[row][col + 1] == player:
                if self.board_pos[row][col - 1] == rival:
                    self.board_pos[row][col - 1] = player
                    movear.append(row)
                    movear.append(col - 1)
                    type = 'Raid'
                if self.board_pos[row + 1][col] == rival:
                    self.board_pos[row + 1][col] = player
                    movear.append(row + 1)
                    movear.append(col)
                    type = 'Raid'
            elif self.board_pos[row + 1][col] == player:
                if self.board_pos[row][col - 1] == rival:
                    self.board_pos[row][col - 1] = player
                    movear.append(row)
                    movear.append(col - 1)
                    type = 'Raid'
                if self.board_pos[row][col + 1] == rival:
                    self.board_pos[row][col + 1] = player
                    movear.append(row)
                    movear.append(col + 1)
                    type = 'Raid'
            else:
                type = 'Stake'
            return (type, movear)
        if row == self.i_width - 1:  # checking for last row but not corners
            if self.board_pos[row][col - 1] == player:
                if self.board_pos[row - 1][col] == rival:
                    self.board_pos[row - 1][col] = player
                    movear.append(row - 1)
                    movear.append(col)
                    type = 'Raid'
                if self.board_pos[row][col + 1] == rival:
                    self.board_pos[row][col + 1] = player
                    movear.append(row)
                    movear.append(col + 1)
                    type = 'Raid'
            elif self.board_pos[row][col + 1] == player:
                if self.board_pos[row][col - 1] == rival:
                    self.board_pos[row][col - 1] = player
                    movear.append(row)
                    movear.append(col - 1)
                    type = 'Raid'
                if self.board_pos[row - 1][col] == rival:
                    self.board_pos[row - 1][col] = player
                    movear.append(row - 1)
                    movear.append(col)
                    type = 'Raid'
            elif self.board_pos[row - 1][col] == player:
                if self.board_pos[row][col - 1] == rival:
                    self.board_pos[row][col - 1] = player
                    movear.append(row)
                    movear.append(col - 1)
                    type = 'Raid'
                if self.board_pos[row][col + 1] == rival:
                    self.board_pos[row][col + 1] = player
                    movear.append(row)
                    movear.append(col + 1)
                    type = 'Raid'
            else:
                type = 'Stake'
            return (type, movear)
        if col == 0:  # checking for first column but not corners
            if self.board_pos[row - 1][col] == player:
                if self.board_pos[row + 1][col] == rival:
                    self.board_pos[row + 1][col] = player
                    movear.append(row + 1)
                    movear.append(col)
                    type = 'Raid'
                if self.board_pos[row][col + 1] == rival:
                    self.board_pos[row][col + 1] = player
                    movear.append(row)
                    movear.append(col + 1)
                    type = 'Raid'
            elif self.board_pos[row][col + 1] == player:
                if self.board_pos[row - 1][col] == rival:
                    self.board_pos[row - 1][col] = player
                    movear.append(row - 1)
                    movear.append(col)
                    type = 'Raid'
                if self.board_pos[row + 1][col] == rival:
                    self.board_pos[row + 1][col] = player
                    movear.append(row + 1)
                    movear.append(col)
                    type = 'Raid'
            elif self.board_pos[row + 1][col] == player:
                if self.board_pos[row][col + 1] == rival:
                    self.board_pos[row][col + 1] = player
                    movear.append(row)
                    movear.append(col + 1)
                    type = 'Raid'
                if self.board_pos[row - 1][col] == rival:
                    self.board_pos[row - 1][col] = player
                    movear.append(row - 1)
                    movear.append(col)
                    type = 'Raid'
            else:
                type = 'Stake'
            return (type, movear)

        if col == self.i_width - 1:  # checking for last column but not corners
            if self.board_pos[row - 1][col] == player:
                if self.board_pos[row + 1][col] == rival:
                    self.board_pos[row + 1][col] = player
                    movear.append(row + 1)
                    movear.append(col)
                    type = 'Raid'
                if self.board_pos[row][col - 1] == rival:
                    self.board_pos[row][col - 1] = player
                    movear.append(row)
                    movear.append(col - 1)
                    type = 'Raid'
            elif self.board_pos[row][col - 1] == player:
                if self.board_pos[row - 1][col] == rival:
                    self.board_pos[row - 1][col] = player
                    movear.append(row - 1)
                    movear.append(col)
                    type = 'Raid'
                if self.board_pos[row + 1][col] == rival:
                    self.board_pos[row + 1][col] = player
                    movear.append(row + 1)
                    movear.append(col)
                    type = 'Raid'
            elif self.board_pos[row + 1][col] == player:
                if self.board_pos[row][col - 1] == rival:
                    self.board_pos[row][col - 1] = player
                    movear.append(row)
                    movear.append(col - 1)
                    type = 'Raid'
                if self.board_pos[row - 1][col] == rival:
                    self.board_pos[row - 1][col] = player
                    movear.append(row - 1)
                    movear.append(col)
                    type = 'Raid'
            else:
                type = 'Stake'
            return (type, movear)
        if (row > 0 and row < self.i_width - 1) and (
                col > 0 and col < self.i_width - 1):  # checking for middle elements
            if self.board_pos[row][col - 1] == player:
                if self.board_pos[row + 1][col] == rival:
                    self.board_pos[row + 1][col] = player
                    movear.append(row + 1)
                    movear.append(col)
                    type = 'Raid'
                if self.board_pos[row - 1][col] == rival:
                    self.board_pos[row - 1][col] = player
                    movear.append(row - 1)
                    movear.append(col)
                    type = 'Raid'
                if self.board_pos[row][col + 1] == rival:
                    self.board_pos[row][col + 1] = player
                    movear.append(row)
                    movear.append(col + 1)
                    type = 'Raid'
            elif self.board_pos[row][col + 1] == player:
                if self.board_pos[row + 1][col] == rival:
                    self.board_pos[row + 1][col] = player
                    movear.append(row + 1)
                    movear.append(col)
                    type = 'Raid'
                if self.board_pos[row - 1][col] == rival:
                    self.board_pos[row - 1][col] = player
                    movear.append(row - 1)
                    movear.append(col)
                    type = 'Raid'
                if self.board_pos[row][col - 1] == rival:
                    self.board_pos[row][col - 1] = player
                    movear.append(row)
                    movear.append(col - 1)
                    type = 'Raid'
            elif self.board_pos[row - 1][col] == player:
                if self.board_pos[row][col - 1] == rival:
                    self.board_pos[row][col - 1] = player
                    movear.append(row)
                    movear.append(col - 1)
                    type = 'Raid'
                if self.board_pos[row][col + 1] == rival:
                    self.board_pos[row][col + 1] = player
                    movear.append(row)
                    movear.append(col + 1)
                    type = 'Raid'
                if self.board_pos[row + 1][col] == rival:
                    self.board_pos[row + 1][col] = player
                    movear.append(row + 1)
                    movear.append(col)
                    type = 'Raid'
            elif self.board_pos[row + 1][col] == player:
                if self.board_pos[row][col - 1] == rival:
                    self.board_pos[row][col - 1] = player
                    movear.append(row)
                    movear.append(col - 1)
                    type = 'Raid'
                if self.board_pos[row][col + 1] == rival:
                    self.board_pos[row][col + 1] = player
                    movear.append(row)
                    movear.append(col + 1)
                    type = 'Raid'
                if self.board_pos[row - 1][col] == rival:
                    self.board_pos[row - 1][col] = player
                    movear.append(row - 1)
                    movear.append(col)
                    type = 'Raid'
            else:
                type = 'Stake'
            return (type, movear)

    def undomove(self, movear, type):
        i = movear[0]
        j = movear[1]
        self.board_pos[i][j] = '.'
        if type == 'Raid':
            for i in range(2, len(movear) - 1, 2):
                if self.board_pos[movear[i]][movear[i + 1]] == 'X':
                    self.board_pos[movear[i]][movear[i + 1]] = 'O'
                else:
                    self.board_pos[movear[i]][movear[i + 1]] = 'X'

    def writefile(self, play):
        lines = []
        self.makemove(self.start, play.i, play.j)
        # print(self.board_pos)
        row = str(chr(65 + play.j))
        pos = row + str(play.i + 1)
        type = play.type
        fw = open('output.txt', 'w')
        fw.writelines(pos + ' ' + type)
        fw.write('\n')
        for j in range(self.i_width):
            for i in range(self.i_width):
                fw.writelines(self.board_pos[j][i])
            fw.write('\n')


g = Game()
g.file_read('input.txt')
