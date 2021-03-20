class Tournament:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
t = Tournament()
class Game:
    def __init__(self):
        self.initialize_game()
        

    def initialize_game(self):
        self.current_state = [['| . |', '| . |', '| . |'],
                              ['| . |', '| . |', '| . |'],
                              ['| . |', '| . |', '| . |']]
        self.player_turn = '| X |'

    def draw_board(self):
        for x in range(0, 3):
            for y in range(0, 3):
                print('{}'.format(self.current_state[x][y]), end=" ")
            print()
        print()
    
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '| . |':
            return False
        else:
            return True

    def is_end(self):
        for i in range(0, 3):
            if (self.current_state[0][i] != '| . |' and
            self.current_state[0][i] == self.current_state[1][i] and
            self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]
        
        for i in range(0, 3):
            if self.current_state[i] == ['| X |', '| X |', '| X |']:
                return '| X |'
            elif self.current_state[i] == ['| O |', '| O |', '| O |']:
                return '| O |'

        if (self.current_state[0][0] != '| . |' and 
        self.current_state[0][0] == self.current_state[1][1] and
        self.current_state[1][1] == self.current_state[2][2]):
            return self.current_state[0][0]
        
        if (self.current_state[0][2] != '| . |' and 
        self.current_state[0][2] == self.current_state[1][1] and 
        self.current_state[1][1] == self.current_state[2][0]):
            return self.current_state[0][2]
        
        for x in range(0, 3):
            for y in range(0, 3):
                if self.current_state[x][y] == '| . |':
                    return None
        return '| . |'
    

    def max_alpha_beta(self, alpha, beta):
        maxvalue = -2
        px = None
        py = None
        result = self.is_end()
        if result == '| X |':
            return (-1, 0, 0)
        elif result == '| O |':
            return (1, 0, 0)
        elif result == '| . |':
            return (0, 0, 0)
        
        for x in range(0, 3):
            for y in range(0, 3):
                if self.current_state[x][y] == '| . |':
                    self.current_state[x][y] = '| O |'
                    (m, min_x, min_y) = self.min_alpha_beta(alpha, beta)
                    if m > maxvalue:
                        maxvalue = m
                        px = x
                        py = y
                    self.current_state[x][y] = '| . |'
                    if maxvalue >= beta:
                        return (maxvalue, px, py)
                    if maxvalue > alpha:
                        alpha = maxvalue
        return (maxvalue, px, py)
    

    def min_alpha_beta(self, alpha, beta):
        minvalue = 2
        qx = None
        qy = None
        result = self.is_end()
        if result == '| X |':
            return (-1, 0, 0)
        if result == '| O |':
            return (1, 0, 0)
        if result == '| . |':
            return (0, 0, 0)
        
        for x in range(0, 3):
            for y in range(0, 3):
                if self.current_state[x][y] == '| . |':
                    self.current_state[x][y] = '| X |'
                    (m, max_x, max_y) = self.max_alpha_beta(alpha, beta)
                    if m < minvalue:
                        minvalue = m
                        qx = x
                        qy = y
                    self.current_state[x][y] = '| . |'
                    if minvalue <= alpha: 
                        return (minvalue, qx, qy)
                    if minvalue < beta: 
                        beta = minvalue
        return (minvalue, qx, qy)
    def replay(self):
        print('Wins: {} Losses: {} Ties: {}'.format(t.wins, t.losses, t.ties))
        self.choice = input('Do you want to play again?\nY/N:')
        if self.choice == 'Y':
            g = Game()
            g.play_alpha_beta()
        elif self.choice == 'N':
            print('Your final total score was\n Wins: {} Losses: {} Ties: {}'.format(t.wins, t.losses, t.ties))
            exit()
        else:
            print('Choose a valid option')
            self.replay()

    def play_alpha_beta(self):
        while True:
            self.draw_board()
            self.result = self.is_end()
            if self.result != None:
                if self.result == '| X |':
                    print('The winner is X!')
                    t.wins += 1
                    self.replay()

                elif self.result == '| O |':
                    print('The winner is O!')
                    t.losses += 1
                    self.replay()
                    
                elif self.result == '| . |':
                    print('Its a tie')
                    t.ties += 1
                    self.replay()
                self.initialize_game()
                return t.wins, t.ties

            if self.player_turn == '| X |':
                while True:
                    (m, qx, qy) = self.min_alpha_beta(-2, 2)
                    print('Recommened move: X = {}, Y = {}'.format(qx, qy))
                    px = int(input('Insert the X coordinate: '))
                    py = int(input('Insert the Y coordinate: '))
                    qx = px
                    qy = py
                    if self.is_valid(px, py):
                        self.current_state[px][py] = '| X |'
                        self.player_turn = '| O |'
                        break
                    else:
                        print('The move is not valid, try again')
            else:
                (m, px, py) = self.max_alpha_beta(-2, 2)
                self.current_state[px][py] = '| O |'
                self.player_turn = '| X |'

def main():
    g = Game()
    g.play_alpha_beta()
if __name__ == '__main__':
    main()








