"""Module contains classes for playing tic-tac-toe console game"""

import logging.config
import yaml
import random

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)
win_logger = logging.getLogger(__name__)
f_handler = logging.FileHandler("logs/winners.log")
f_handler.setLevel(logging.WARNING)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)
win_logger.addHandler(f_handler)


class Menu:
    """Choose what player want to do"""
    def __init__(self):
        """Suggest options"""
        self.choice = input("Hello. Choose option to continue.\n"
                            "play - start tic-tac-toe game"
                            ", winners - see wins log, clear - clear wins log, quit - quit game\n")
        Menu.do_choice(self)

    def do_choice(self):
        """Run user`s choice"""
        if self.choice.lower() == "play":
            play(tic_tac, player_1, player_2)
            Menu()
        elif self.choice.lower() == "winners":
            with open("logs/winners.log") as log:
                data = log.read()
                print(data)
            Menu()
        elif self.choice.lower() == "clear":
            with open('logs/winners.log', 'w') as log:
                log.truncate(0)
            Menu()
        elif self.choice.lower() == "quit":
            logger.info("Thank you for playing, see you soon!")
            exit()
        else:
            logger.error("Please, input only words suggested")
            Menu()


class Player:
    """Parent class for player"""
    def __init__(self, choice, name):
        self.choice = choice
        self.name = name

    def next_move(self, game):
        pass


class ComputerPlayer(Player):
    """Computer player (random)"""
    def __init__(self, choice, name):
        super().__init__(choice, name)
        logger.info(f"Computer player {name} chooses {choice}")

    def next_move(self, game):
        """Random computer playing"""
        square = random.choice(game.available_moves())
        logger.info(f"Computer Player {self.name} is choosing to put {self.choice} to {square} square")
        return square


class HumanPlayer(Player):
    """Player who makes their own choice"""
    def __init__(self, choice, name):
        super().__init__(choice, name)
        logger.info(f"Human player {name} chooses {choice}")

    def next_move(self, game):
        """Person playing"""
        valid_square = False
        value = None
        while not valid_square:
            square = input(f"Player {self.name} with {self.choice} makes choice.\
             Input from 0 to 8 to make a move:\n")
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                logger.error("You can not choose this square, try again.")
        return value


class TicTacToe:
    """Class that implements game's logic"""
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None
        logger.info(f"The game board was created, current winner is {self.current_winner}")

    def print_board(self):
        """Show printed board"""
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
        logger.info("The board was printed.")

    @staticmethod
    def print_board_nums():
        """Fill in board gaps to understand what moves can be"""
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")
        logger.info("The squares in the board got numbers.")

    def available_moves(self):
        """Return choices that can be played"""
        moves = []
        for (i, space) in enumerate(self.board):
            if space == " ":
                moves.append(i)
        logger.info(f"Available moves are {moves}")
        return moves

    def empty_squares(self):
        """Return gaps in board"""
        return " " in self.board

    def num_empty_squares(self):
        """Count number of gaps"""
        return self.board.count(" ")

    def make_move(self, square, choice):
        """Make moves during play"""
        if self.board[square] == " ":
            self.board[square] = choice
            if self.winner(square, choice):
                self.current_winner = choice
            return True
        return False

    def winner(self, square, choice):
        """Indicates the winner of the game"""
        row_index = square // 3
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([gap == choice for gap in row]):
            return True
        col_index = square % 3
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([gap == choice for gap in column]):
            return True
        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            if all([space == choice for space in diagonal_1]):
                return True
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all([space == choice for space in diagonal_2]):
                return True
        return False


def play(game, player_x, player_o, print_game=True):
    """Logic of game"""
    if print_game:
        game.print_board_nums()
    choice = "X"
    while game.empty_squares():
        if choice == "O":
            square = player_o.next_move(game)
            current_player = player_o
        else:
            square = player_x.next_move(game)
            current_player = player_x
        if game.make_move(square, choice):
            if print_game:
                logger.info(f"{current_player.name} makes a move with {choice} to {square}")
                game.print_board()
                print("")
            if game.current_winner:
                if print_game:
                    logger.warning(f"{current_player.name} with {choice} wins!")
                    win_logger.warning(f"{current_player.name} with {choice} wins!")
                return choice
            choice = "O" if choice == "X" else "X"


if __name__ == "__main__":
    player_1 = HumanPlayer("X", "Vladislav")
    player_2 = ComputerPlayer("O", "Windows")
    tic_tac = TicTacToe()
    menu = Menu()
    menu.do_choice()
