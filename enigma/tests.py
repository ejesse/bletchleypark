from django.test import TestCase
from enigma.rotors import Rotor, ENIGMA_I_ROTOR_I, ENIGMA_I_ROTOR_II, ENIGMA_I_ROTOR_III, REFLECTOR_B
from enigma.enigmas import Enigma


class TestRotor(TestCase):

    def test_basic_right_to_left(self):
        rotor = Rotor(key='EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        self.assertEqual(rotor.right_to_left('A'), 'K')

    def test_basic_keft_to_right(self):
        rotor = Rotor(key='EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        self.assertEqual(rotor.left_to_right('E'), 'A')

    def test_setting_turnover(self):
        rotor = Rotor(key='EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        rotor.turnover_position = 'd'
        self.assertEqual(rotor.turnover_position, 3)
        rotor.turnover_position = 10
        self.assertEqual(rotor.turnover_position, 10)

    def _test_offset(self):
        rotor = Rotor(key='EKMFLGDQVZNTOWYHXUSPAIBRCJ')
        rotor.offset = 1
        self.assertEqual(rotor.right_to_left('A'), 'K')
        self.assertEqual(rotor.left_to_right('K'), 'A')

    def test_stepping(self):
        rotor = Rotor(key='BDFHJLCPRTXVZNYEIWGAKMUSQO')
        rotor.step()
        self.assertEqual(rotor.key[0], 'D')
        self.assertEqual(rotor.key[25], 'B')
        self.assertEqual(rotor._left_circuit[0], 'B')
        self.assertEqual(rotor._left_circuit[25], 'A')


class TestEnigma(TestCase):

    def test_basic_single_letter(self):
        enigma = Enigma()
        enigma.rotors = [ENIGMA_I_ROTOR_III, ENIGMA_I_ROTOR_II, ENIGMA_I_ROTOR_I]
        enigma.reflector = REFLECTOR_B
        self.assertEqual(enigma.encrypt_letter('A'), 'B')