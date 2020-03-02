import copy


class Node:
    def __init__(self, depth, parent, state, turn):

        self.turn = turn
        self.depth = depth
        self.parent = parent
        self.state = state
        self.children = []
        self.score = self.getscore()

        self.createChildren()

    def createChildren(self):
        # player 1 state generation
        if self.turn == 1 and self.depth >= 0:
            if self.state[1][0] != 0 and self.state[0][0] != 0:
                ll = self.state[0][0] + self.state[1][0]
                if ll >= 5:
                    ll = ll - 5
                s1 = copy.deepcopy(self.state)
                s1[1][0] = ll
                self.children.append(Node(self.depth - 1, self, s1, -self.turn))

            if self.state[1][1] != 0 and self.state[0][0] != 0:
                lr = self.state[0][0] + self.state[1][1]
                if lr >= 5:
                    lr = lr - 5
                s2 = copy.deepcopy(self.state)
                s2[1][1] = lr
                self.children.append(Node(self.depth - 1, self, s2, -self.turn))

            if self.state[1][0] != 0 and self.state[0][1] != 0:
                rl = self.state[0][1] + self.state[1][0]
                if rl >= 5:
                    rl = rl - 5
                s3 = copy.deepcopy(self.state)
                s3[1][0] = rl
                self.children.append(Node(self.depth - 1, self, s3, -self.turn))

            if self.state[1][1] != 0 and self.state[0][1] != 0:
                rr = self.state[0][1] + self.state[1][1]
                if rr >= 5:
                    rr = rr - 5
                s4 = copy.deepcopy(self.state)
                s4[1][1] = rr
                self.children.append(Node(self.depth - 1, self, s4, -self.turn))
            total = self.state[0][0] + self.state[0][1]
            if total == 2:
                sp1 = copy.deepcopy(self.state)
                if sp1[0][0] == 1:
                    sp1[0][0] = 0
                    sp1[0][1] = 2
                else:
                    sp1[0][0] = 1
                    sp1[0][1] = 1
                self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
            elif total == 3:
                sp1 = copy.deepcopy(self.state)
                sp2 = copy.deepcopy(self.state)
                if sp1[0][0] == 1 or sp1[0][0] == 2:
                    sp1[0][0] = 0
                    sp1[0][1] = 3
                    self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
                else:
                    sp1[0][0] = 1
                    sp1[0][1] = 2
                    self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
                #      self.sp1.append(evaluate(sp1))
            elif total == 4:
                sp1 = copy.deepcopy(self.state)
                sp2 = copy.deepcopy(self.state)
                sp3 = copy.deepcopy(self.state)
                if sp1[0][0] == 1 or sp1[0][0] == 3:
                    sp1[0][0] = 0
                    sp1[0][1] = 4
                    self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
                    sp2[0][0] = 2
                    sp2[0][1] = 2
                    self.children.append(Node(self.depth - 1, self, sp2, -self.turn))
                elif sp1[0][0] == 0 or sp1[0][0] == 4:
                    sp1[0][0] = 1
                    sp1[0][1] = 3
                    self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
                    sp2[0][0] = 2
                    sp2[0][1] = 2
                    #      self.sp2.append(evaluate(sp2))
                    self.children.append(Node(self.depth - 1, self, sp2, -self.turn))
                else:
                    sp1[0][0] = 1
                    sp1[0][1] = 3
                    #      self.sp1.append(evaluate(sp1))
                    self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
                    sp2[0][0] = 0
                    sp2[0][1] = 4
                    #      self.sp2.append(evaluate(sp2))
                    self.children.append(Node(self.depth - 1, self, sp2, -self.turn))
            elif total == 5:
                sp1 = copy.deepcopy(self.state)
                if sp1[0][0] == 1 or sp1[0][0] == 4:
                    sp1[0][0] == 2
                    sp1[0][1] == 3
                else:
                    sp1[0][0] == 1
                    sp1[0][0] == 4
                self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
            elif total == 6:
                sp1 = copy.deepcopy(self.state)
                if sp1[0][0] == 2 or sp1[0][0] == 4:
                    sp1[0][0] = 3
                    sp1[0][1] = 3
                else:
                    sp1[0][0] = 2
                    sp1[0][1] = 4
                self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
        # Player 2's state generation
        if self.turn < 0 and self.depth >= 0:
            if self.state[1][0] != 0 and self.state[0][0] != 0:
                ll = self.state[1][0] + self.state[0][0]
                if ll >= 5:
                    ll = ll - 5
                s1 = copy.deepcopy(self.state)
                s1[0][0] = ll
                self.children.append(Node(self.depth - 1, self, s1, -self.turn))

            if self.state[1][1] != 0 and self.state[0][0] != 0:
                rl = self.state[1][1] + self.state[0][0]
                if rl >= 5:
                    rl = rl - 5
                s2 = copy.deepcopy(self.state)
                s2[0][0] = rl
                self.children.append(Node(self.depth - 1, self, s2, -self.turn))

            if self.state[1][0] != 0 and self.state[0][1] != 0:
                lr = self.state[1][0] + self.state[0][1]
                if lr >= 5:
                    lr = lr - 5
                s3 = copy.deepcopy(self.state)
                s3[0][1] = lr
                self.children.append(Node(self.depth - 1, self, s3, -self.turn))

            if self.state[1][1] != 0 and self.state[0][1] != 0:
                rr = self.state[1][1] + self.state[0][1]
                if rr >= 5:
                    rr = rr - 5
                s4 = copy.deepcopy(self.state)
                s4[0][1] = rr
                self.children.append(Node(self.depth - 1, self, s4, -self.turn))
            total = self.state[1][0] + self.state[1][1]
            if total == 2:
                sp1 = copy.deepcopy(self.state)
                if sp1[1][0] == 1:
                    sp1[1][0] = 0
                    sp1[1][1] = 2
                else:
                    sp1[1][0] = 1
                    sp1[1][1] = 1
                #   self.sp1.append(evaluate(sp1))
                self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
            elif total == 3:
                sp1 = copy.deepcopy(self.state)
                if sp1[1][0] == 1 or sp1[1][0] == 2:
                    sp1[1][0] = 0
                    sp1[1][1] = 3
                    self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
                #      self.sp1.append(evaluate(sp1))
                #     self.sp2.append(evaluate(sp2))
                else:
                    sp1[1][0] = 1
                    sp1[1][1] = 2
                    self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
                #      self.sp1.append(evaluate(sp1))
            elif total == 4:
                sp1 = copy.deepcopy(self.state)
                sp2 = copy.deepcopy(self.state)
                sp3 = copy.deepcopy(self.state)
                if sp1[1][0] == 1 or sp1[1][0] == 3:
                    sp1[1][0] = 0
                    sp1[1][1] = 4
                    #      self.sp1.append(evaluate(sp1))
                    self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
                    sp2[1][0] = 2
                    sp2[1][1] = 2
                    #      self.sp2.append(evaluate(sp2))
                    #      self.sp3.append(evaluate(sp3))
                    self.children.append(Node(self.depth - 1, self, sp2, -self.turn))
                elif sp1[1][0] == 0 or sp1[1][0] == 4:
                    sp1[1][0] = 1
                    sp1[1][1] = 3
                    #      self.sp1.append(evaluate(sp1))
                    self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
                    sp2[1][0] = 2
                    sp2[1][1] = 2
                    #      self.sp2.append(evaluate(sp2))
                    self.children.append(Node(self.depth - 1, self, sp2, -self.turn))
                else:
                    sp1[1][0] = 1
                    sp1[1][1] = 3
                    #      self.sp1.append(evaluate(sp1))
                    self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
                    sp2[1][0] = 0
                    sp2[1][1] = 4
                    #      self.sp2.append(evaluate(sp2))
                    self.children.append(Node(self.depth - 1, self, sp2, -self.turn))
            elif total == 5:
                sp1 = copy.deepcopy(self.state)
                if sp1[1][0] == 1 or sp1[1][0] == 4:
                    sp1[1][0] == 2
                    sp1[1][1] == 3
                    self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
                else:
                    sp1[1][0] == 1
                    sp1[1][0] == 4
                    self.children.append(Node(self.depth - 1, self, sp1, -self.turn))
            elif total == 6:
                sp1 = copy.deepcopy(self.state)
                if sp1[1][0] == 2 or sp1[1][0] == 4:
                    sp1[1][0] = 3
                    sp1[1][1] = 3
                else:
                    sp1[1][0] = 2
                    sp1[1][1] = 4
                self.children.append(Node(self.depth - 1, self, sp1, -self.turn))

    def getscore(self):
        score = 0
        if self.state[0][0] == 0 and self.state[0][1] == 0:
            score -= 10000
        if self.state[1][0] == 0 and self.state[1][1] == 0:
            score += 10000
        if self.state[0][0] + self.state[1][0] == 5 or self.state[0][0] + self.state[1][1] == 5 or self.state[0][1] + \
                self.state[1][0] == 5 or self.state[0][1] + self.state[1][1] == 5:
            if self.turn == 1:
                score += 200
            else:
                score -= 200
        if self.state[0][0] == self.state[0][1]:
            score += 50
        if self.state[0][0] == 0 or self.state[0][1] == 0:
            score -= 40
        if self.state[0][0] == 2 or self.state[0][1] == 2:
            score += 30
        if self.state[0][0] == 3 or self.state[0][1] == 3:
            score += 20
        if self.state[1][0] == self.state[1][1]:
            score -= 50
        if self.state[1][0] == 0 or self.state[1][1] == 0:
            score += 40
        if self.state[1][0] == 2 or self.state[1][1] == 2:
            score -= 30
        if self.state[1][0] == 3 or self.state[1][1] == 3:
            score -= 20

        return score


def selectMenu():
    print('Welcome to chopsticks. \n 1. Play against your friend \n 2. Play against a bot')

# checks for winning state
def checkWin(state):
    if state[1][1] == 0 and state[1][0] == 0:
        win = 1
        print(currentState[0], '\n', currentState[1], 'Player 1 wins!')
    elif state[0][1] == 0 and state[0][0] == 0:
        win = -1
        print(currentState[0], '\n', currentState[1], 'Player 2 wins!')
    else:
        win = 0
    return win

# minimax function
def minimax(node, depth, Maxplayer):
    if depth == 0 or abs(node.score) > 500:
        return node.score
    elif Maxplayer:
        value = -10000
        for child in node.children:
            value = max(value, minimax(child, depth - 1, False))
        return value
    else:
        value = 10000
        for child in node.children:
            value = min(value, minimax(child, depth - 1, True))
        return value
        # return node.state

# displays best possible move for player
def showbestmove(currentState, player):
    if player == 1:
        nodeturn = 1
    elif player == 2:
        nodeturn = -1
    node = Node(1, None, currentState, nodeturn)
    if player == 1:
        value = minimax(node, 1, True)
        length = len(node.children)
        iterate = 0
        while iterate != length:
            if value == node.children[iterate].score:
                index = iterate
                print('\n')
                print('Best state for player %d be is: ' % player)
                print(node.children[index].state)
                break
            iterate += 1
    else:
        value = minimax(node, 1, False)
        length = len(node.children)
        iterate = 0
        # prints score
        # print('value is %d' % value)
        while iterate != length:
            if value == node.children[iterate].score:
                index = iterate
                print('\n')
                print('Best state for player %d be is: ' % player)
                print(node.children[index].state)
                break
            iterate += 1


def aimove(currentState, player):
    if player == 1:
        nodeturn = 1
    elif player == 2:
        nodeturn = -1
    node = Node(1, None, currentState, nodeturn)
    if player == 2:
        value = minimax(node, 1, False)
        length = len(node.children)
        iterate = 0
        while iterate != length:
            if value == node.children[iterate].score:
                index = iterate
                return node.children[index].state
                break
            iterate += 1
    else:
        value = minimax(node, 1, True)
        length = len(node.children)
        iterate = 0
        while iterate != length:
            if value == node.children[iterate].score:
                index = iterate
                return node.children[index].state
                break
            iterate += 1


def moves(move, state, turn):
    # Turn factor ensures that the person acting is indeed the player's turn.
    # Game starts with turn 1, turn 1 is player1's turn. 1 % 2 == 1, 1-1 = 0, 1st set of values is player1's.
    # 1st player, turn factor is 0
    # 2nd player, turn factor is 1
    turn_factor = ((turn + 1) % 2)
    # cancelled
    # print('turn factor is currently %d' % turn_factor)
    attack_possibility = ['l', 'r']
    target = {
        'l': state[1][0],
        'r': state[1][1]
    }

    actor = {
        'l': state[0][0],
        'r': state[0][1]
    }

    def split():
        if turn_factor == 0:
            total = actor['l'] + actor['r']
        else:
            total = target['l'] + target['r']
        # Error handling to make sure integer is inputted
        while True:
            try:
                left = int(input('Left: '))
                while left > total:
                    print('Please enter a valid number')
                    left = int(input('Left: '))
                while left == actor['l'] or left == actor['r']:
                    print('Please enter a valid number')
                    left = int(input('Left: '))
            except ValueError:
                print('Please enter an integer')
                continue
            else:
                break

        if turn_factor == 0:
            right = total - left
            if left == actor['l'] or left == actor['r']:
                print('Cannot pass turn.')
                split()

            else:
                actor['l'] = left
                actor['r'] = right
        else:
            total = target['l'] + target['r']
            right = total - left
            if left == target['l'] or left == target['r']:
                split()
            else:
                target['l'] = left
                target['r'] = right

    def attack():
        actor_index = input('Enter which of your hand is attacking: ')
        while actor_index not in attack_possibility:
            print('\n')
            print('Please enter l or r for which hand you would like to use to attack. ')
            actor_index = input('Enter which of your hand is attacking: ')

        target_index = input('Which hand would you like to attack? ')
        while target_index not in attack_possibility:
            print('\n')
            print('Please enter l or r for which hand you would like to attack. ')
            target_index = input('Which hand would you like to attack? ')

        if turn_factor == 0:
            if actor[actor_index] == 0:
                print('cannot attack with a value of 0. \n')
                attack()
            elif target[target_index] == 0:
                print('Cannot attack value of 0. \n')
                attack()
            else:
                result = actor[actor_index] + target[target_index]
                result = result % 5
                target[target_index] = result
        else:
            if target[actor_index] == 0:
                print('cannot attack with the value of 0. \n')
                attack()
            elif actor[target_index] == 0:
                print('Cannot attack value of 0. \n')
                attack()
            else:
                result = target[actor_index] + actor[target_index]
                result = result % 5
                actor[target_index] = result

    if move == 'split':
        split()
        state = [[actor['l'], actor['r']], [target['l'], target['r']]]
        return state

    elif move == 'attack':
        attack()
        state = [[actor['l'], actor['r']], [target['l'], target['r']]]
        return state


turn = 1
currentState = [[1, 1], [1, 1]]
playingFriend = False
playingBot = False
choice = 0
choices = [1, 2]
selectMenu()
while choice not in choices:
    choice = int(input('Enter your choice: '))
    if choice == 1:
        playingFriend = True
        print('You are playing against your friend!')
    elif choice == 2:
        playingBot = True
        print('You are playing against a bot!')
print('\n')

while playingFriend:
    if turn % 2 == 0:
        player_playing = 2
    else:
        player_playing = 1
    print('It is currently turn %d' % turn)
    print('It is player %d\'s turn right now' % player_playing)
    potential_moves = ['a', 'attack', 'split', 's']
    print('player 1: ' + str(currentState[0]), '\n', 'player 2: ' + str(currentState[1]))
    showbestmove(currentState, player_playing)

    move = input('Please enter your move: ')
    while move not in potential_moves:
        print('Enter a valid move')
        move = input('Please enter your move: ')
    if move == 'a':
        move = 'attack'
    elif move == 's':
        move = 'split'
    currentState = moves(move, currentState, turn)

    turn += 1
    win = checkWin(currentState)
    if win != 0:
        break

while playingBot:
    if turn % 2 == 0:
        player_playing = 2
    else:
        player_playing = 1
    print('\n')
    print('It is currently turn %d' % turn)
    print('It is player %d\'s turn right now' % player_playing)
    potential_moves = ['a', 'attack', 'split', 's']
    print('player 1: ' + str(currentState[0]), '\n', 'player 2: ' + str(currentState[1]))
    if player_playing == 1:
        move = input('Please enter your move: ')
        while move not in potential_moves:
            print('Enter a valid move')
            move = input('Please enter your move: ')
        if move == 'a':
            move = 'attack'
        elif move == 's':
            move = 'split'
        currentState = moves(move, currentState, turn)
        turn += 1
        win = checkWin(currentState)
        if win != 0:
            break
    elif player_playing == 2:
        currentState = aimove(currentState, player_playing)
        turn += 1
        win = checkWin(currentState)
        if win != 0:
            break
