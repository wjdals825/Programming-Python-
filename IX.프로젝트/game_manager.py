from tictactoe import TicTacToe

class GameManager:
    def __init__(self):
        self.ttt = TicTacToe()

    def play(self):
        #게임판 보여주자
        print(self.ttt)
        while True:
        #row, col 입력받자
            row = int(input("row : "))
            col = int(input("col : "))
            self.ttt.set(row,col)
            self.ttt.set(1, 1)
            print(self.ttt)
            #check_winner 면 끝내자
            if self.ttt.check_winner() == "o":
                print("o win!!!")
                break
            elif self.ttt.check_winner() == "x":
                print("x win!!!")
                break
            elif self.ttt.check_winner() == "d":
                print("무승부")
                break

if __name__ == '__main__':
    gm = GameManager()
    gm.play()

