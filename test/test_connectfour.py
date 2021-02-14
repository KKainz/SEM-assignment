import unittest
import math
from connectfour.connectfour import ConnectFour, MoveResult


class ConnectFourTestCase(unittest.TestCase):

    def setUp(self):
        self.cf_vs_bot = ConnectFour(True, "A", )
        self.cf_vs_bot_two_names = ConnectFour(True, "AA", "B")
        self.cf_2players_same_name = ConnectFour(False, "B", "B")
        self.cf_2players_different_names_1 = ConnectFour(False, "B", "C")
        self.cf_2players_different_names_2 = ConnectFour(False, "B", "C")
        self.cf_2players_different_names_3 = ConnectFour(False, "B", "C")
        self.cf_2players_different_names_4 = ConnectFour(False, "B", "C")
        self.cf_2players_different_names_5 = ConnectFour(False, "B", "C")

        self.moveresult1 = MoveResult("Go on", False, False)
        self.moveresult2 = MoveResult("Again", True, False)
        self.moveresult3 = MoveResult("Won", False, True)

    def test_connectfour_init(self):
        self.assertEqual("A", self.cf_vs_bot.player_name_1)
        self.assertEqual("Bot", self.cf_vs_bot_two_names.player_name_2)

        self.assertEqual("B_1", self.cf_2players_same_name.player_name_1)
        self.assertEqual("B_2", self.cf_2players_same_name.player_name_2)

        self.assertEqual("B", self.cf_2players_different_names_1.player_name_1)
        self.assertEqual("C", self.cf_2players_different_names_1.player_name_2)

    def test_moveresult_init(self):
        self.assertEqual("Go on", self.moveresult1.message)
        self.assertEqual(False, self.moveresult1.failed_move)
        self.assertEqual(False, self.moveresult1.game_won)

        self.assertEqual("Again", self.moveresult2.message)
        self.assertEqual(True, self.moveresult2.failed_move)
        self.assertEqual(False, self.moveresult2.game_won)

        self.assertEqual("Won", self.moveresult3.message)
        self.assertEqual(False, self.moveresult3.failed_move)
        self.assertEqual(True, self.moveresult3.game_won)

    def test_set_stone(self):
        m_result = None
        hashes = '##########################################################################################'
        print(hashes)
        print('Player 1 and 2 only choose same slot everytime (until slot full) > failed move')
        # Player 1 and 2 only choose same slot everytime (until slot full)
        for i in range(7):
            m_result = self.cf_2players_different_names_1.set_stone(1)
            if i == 6:
                self.assertTrue(m_result.failed_move)
                self.assertFalse(m_result.game_won)
            else:
                self.assertFalse(m_result.failed_move)
                self.assertFalse(m_result.game_won)
        print(self.cf_2players_different_names_1.get_board())

        print(hashes)
        print('Checks if vertical win is recognized')
        # Checks if vertical win is recognized
        for i in range(7):
            m_result = self.cf_2players_different_names_2.set_stone(i % 2 + 1)
        self.assertTrue(m_result.game_won)
        print(self.cf_2players_different_names_2.get_board())

        print(hashes)
        print('Checks if horizontal win is recognized')
        # Checks if horizontal win is recognized
        for i in range(7):
            m_result = self.cf_2players_different_names_3.set_stone(math.floor(i / 2) + 1)
        self.assertTrue(m_result.game_won)
        print(self.cf_2players_different_names_3.get_board())

        print(hashes)
        print('Checks if diagonal win (left bottom to top right) is recognized')
        # Checks if diagonal win (left bottom to top right) is recognized
        self.cf_2players_different_names_4.set_stone(1)
        self.cf_2players_different_names_4.set_stone(2)
        self.cf_2players_different_names_4.set_stone(2)
        self.cf_2players_different_names_4.set_stone(3)
        self.cf_2players_different_names_4.set_stone(1)
        self.cf_2players_different_names_4.set_stone(3)
        self.cf_2players_different_names_4.set_stone(3)
        self.cf_2players_different_names_4.set_stone(4)
        self.cf_2players_different_names_4.set_stone(4)
        self.cf_2players_different_names_4.set_stone(4)
        m_result = self.cf_2players_different_names_4.set_stone(4)
        self.assertTrue(m_result.game_won)
        print(self.cf_2players_different_names_4.get_board())

        print(hashes)
        print('Checks if diagonal win (left top to bottom right) is recognized')
        # Checks if diagonal win (left top to bottom right) is recognized
        self.cf_2players_different_names_5.set_stone(4)
        self.cf_2players_different_names_5.set_stone(4)
        self.cf_2players_different_names_5.set_stone(4)
        self.cf_2players_different_names_5.set_stone(4)
        self.cf_2players_different_names_5.set_stone(5)
        self.cf_2players_different_names_5.set_stone(5)
        self.cf_2players_different_names_5.set_stone(1)
        self.cf_2players_different_names_5.set_stone(5)
        self.cf_2players_different_names_5.set_stone(6)
        self.cf_2players_different_names_5.set_stone(6)
        self.cf_2players_different_names_5.set_stone(4)
        m_result = self.cf_2players_different_names_5.set_stone(7)
        print(self.cf_2players_different_names_5.get_board())
        self.assertTrue(m_result.game_won)

if __name__ == '__main__':
    unittest.main()