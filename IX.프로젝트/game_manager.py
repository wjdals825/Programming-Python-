from tictactoe import TIcTacToe

class GameManager:
    def __init__(selfself):
        self.ttt = TicTacToe()

    def play(self):
        #게임판 보여주자
        print(self.ttt)
        #row, col 입력받자
        self.ttt.set(1, 1)
        print(self.ttt)
        pass

if __name__ == '__main__':
    gm = GameManager()
    gm.play()

