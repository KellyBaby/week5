import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', '.', 'O'],
            ['.', 'X', '.'],
            ['.', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_make_empty_board(self):
        board = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        self.assertEqual(logic.make_empty_board(),board)

    def test_other_player(self):
        player=1
        self.assertEqual(logic.other_player(player),2)

    def test_transferInput(self):
        input="2,3"
        self.assertEqual(logic.transferInput(input),(1,2))
    def test_checkInput(self):
        transferred_input="1,4"
        self.assertEqual(logic.checkInput(transferred_input),(-1,-1))
    def test_moveChess(self):
        input_board = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        output_board=[
            ['.', '.', '.'],
            ['.', '.', 'X'],
            ['.', '.', '.'],
        ]
        self.assertEqual(logic.moveChess(1,1,2,input_board),output_board)

    def test_getprintBoard(self):
        input_board = [
            ['.', 'X', '.'],
            ['.', 'O', '.'],
            ['.', '.', '.'],
        ]
        output_board = ".X.\n.O.\n...\n"
        self.assertEqual(logic.getprintBoard(input_board),output_board)

    def test_getInput(self):
        input="2,3"
        self.assertEqual(logic.getInput(input),(1,2))
    # TODO: Test all functions from logic.py!


if __name__ == '__main__':
    unittest.main()
