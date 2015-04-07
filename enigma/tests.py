from django.test import TestCase

from enigma.enigmas import Enigma
from enigma.rotors import Rotor, ENIGMA_I_ROTOR_I, ENIGMA_I_ROTOR_II, ENIGMA_I_ROTOR_III, REFLECTOR_B, \
    get_next_alpha


class TestRotor(TestCase):

    def test_basic_right_to_left(self):
        rotor = Rotor(key='BDFHJLCPRTXVZNYEIWGAKMUSQO')
        self.assertEqual(rotor.right_to_left('A'), 'B')

    def test_basic_left_to_right(self):
        rotor = Rotor(key='AJDKSIRUXBLHWTMCQGZNPYFVOE')
        self.assertEqual(rotor.left_to_right('S'), 'E')

    def _test_offset(self):
        rotor = Rotor(key='BDFHJLCPRTXVZNYEIWGAKMUSQO')
        rotor.offset = 1
        self.assertEqual(rotor.right_to_left('A'), 'K')
        self.assertEqual(rotor.left_to_right('K'), 'A')

    def _test_stepping(self):
        rotor = Rotor(key='BDFHJLCPRTXVZNYEIWGAKMUSQO')
        rotor.step()
        self.assertEqual(rotor.key[0], 'D')
        self.assertEqual(rotor.key[25], 'B')
        self.assertEqual(rotor._left_circuit[0], 'B')
        self.assertEqual(rotor._left_circuit[25], 'A')

    def test_next_alpha(self):
        self.assertEqual(get_next_alpha('A'),'B')
        self.assertEqual(get_next_alpha('Z'),'A')


class TestEnigma(TestCase):

    def test_ignore_non_alphas(self):
        troll_plaintext = 'a *&^%$#@;><?'
        enigma = Enigma(rotors = [Rotor.rotor_for_name(ENIGMA_I_ROTOR_III),
                         Rotor.rotor_for_name(ENIGMA_I_ROTOR_II),
                         Rotor.rotor_for_name(ENIGMA_I_ROTOR_I)])
        enigma.reflector = Rotor.rotor_for_name(REFLECTOR_B)
        ciphered = enigma.encrypt_string(troll_plaintext)
        self.assertEqual(ciphered, 'B')

    def test_basic_single_letter(self):
        enigma = Enigma(rotors = [Rotor.rotor_for_name(ENIGMA_I_ROTOR_III),
                         Rotor.rotor_for_name(ENIGMA_I_ROTOR_II),
                         Rotor.rotor_for_name(ENIGMA_I_ROTOR_I)])
        enigma.reflector = Rotor.rotor_for_name(REFLECTOR_B)
        ciphered = enigma.encrypt_letter('A')
        self.assertEqual(ciphered, 'B')

    def test_basic_string(self):
        enigma = Enigma(rotors = [Rotor.rotor_for_name(ENIGMA_I_ROTOR_III),
                         Rotor.rotor_for_name(ENIGMA_I_ROTOR_II),
                         Rotor.rotor_for_name(ENIGMA_I_ROTOR_I)])
        enigma.reflector = Rotor.rotor_for_name(REFLECTOR_B)
        ciphered = enigma.encrypt_string('AAAAA')
        self.assertEqual(ciphered, 'BDZGO')

    def test_second_turnover(self):
        rotor2 = Rotor.rotor_for_name(ENIGMA_I_ROTOR_II)
        rotor2.turnover_position = 'V'
        enigma = Enigma(rotors = [Rotor.rotor_for_name(ENIGMA_I_ROTOR_III),
                         rotor2,
                         Rotor.rotor_for_name(ENIGMA_I_ROTOR_I)])
        enigma.reflector = Rotor.rotor_for_name(REFLECTOR_B)
        ciphered = enigma.encrypt_string('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        self.assertEqual(ciphered, 'BDZGOWCXLTKSBTMCDLPBMUQOFXYHCXTGYJFLINHNXSHIUNTHEORXPQPKOVHCBUBTZSZSOOSTGOTFSODBBZZLXLCYZXIFGWFDZEEQ')

    def test_third_turnover(self):

        rotor2 = Rotor.rotor_for_name(ENIGMA_I_ROTOR_II)
        rotor3 = Rotor.rotor_for_name(ENIGMA_I_ROTOR_I)
        enigma = Enigma(rotors = [Rotor.rotor_for_name(ENIGMA_I_ROTOR_III),
                         rotor2,
                         rotor3])
        enigma.reflector = Rotor.rotor_for_name(REFLECTOR_B)
        ciphered = enigma.encrypt_string('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        self.assertEqual(ciphered, 'BDZGOWCXLTKSBTMCDLPBMUQOFXYHCXTGYJFLINHNXSHIUNTHEORXPQPKOVHCBUBTZSZSOOSTGOTFSODBBZZLXLCYZXIFGWFDZEEQI')

    def test_third_turnover_twice(self):

        rotor2 = Rotor.rotor_for_name(ENIGMA_I_ROTOR_II)
        rotor3 = Rotor.rotor_for_name(ENIGMA_I_ROTOR_I)
        enigma = Enigma(rotors = [Rotor.rotor_for_name(ENIGMA_I_ROTOR_III),
                         rotor2,
                         rotor3])
        enigma.reflector = Rotor.rotor_for_name(REFLECTOR_B)
        ciphered = enigma.encrypt_string('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        self.assertEqual(ciphered, 'BDZGOWCXLTKSBTMCDLPBMUQOFXYHCXTGYJFLINHNXSHIUNTHEORXPQPKOVHCBUBTZSZSOOSTGOTFSODBBZZLXLCYZXIFGWFDZEEQIBMGFJBWZFCKPFMGBXQCIVIBBRNCOCJUVYDKMVJPFMDRMTGLWFOZLXGJEYYQPVPBWNCKVKLZTCBDLDCTSNRCOOVPTGBVBBISGJSOYHDENCTNUUKCUGHREVWBDJCTQXXOGLEBZMDBRZOSXDTZSZBGDCFPRBZYQGSNCCHGYEWOHVJBYZGKDGYNNEUJIWCTYCYTUUMBOYVUNNQUKKSOBSCORSUOSCNVROQLHEUDSUKYMIGIBSXPIHNTUVGGHIFQTGZXLGYQCNVNSRCLVPYOSVRBKCEXRNLGDYWEBFXIVKKTUGKPVMZOTUOGMHHZDREKJHLEFKKPOXLWBWVBYUKDTQUHDQTREVRQJMQWNDOVWLJHCCXCFXRPPXMSJEZCJUFTBRZZMCSSNJNYLCGLOYCITVYQXPDIYFGEFYVXSXHKEGXKMMDSWBCYRKIZOCGMFDDTMWZTLSSFLJMOOLUUQJMIJSCIQVRUISTLTGNCLGKIKTZHRXENRXJHYZTLXICWWMYWXDYIBLERBFLWJQYWONGIQQCUUQTPPHBIEHTUVGCEGPEYMWICGKWJCUFKLUIDMJDIVPJDMPGQPWITKGVIBOOMTNDUHQPHGSQRJRNOOVPWMDNXLLVFIIMKIEYIZMQUWYDPOULTUWBUKVMMWRLQLQSQPEUGJRCXZWPFYIYYBWLOEWROUVKPOZTCE')

    def test_different_starting_position(self):
        rotor1 = Rotor.rotor_for_name(ENIGMA_I_ROTOR_III)
        rotor2 = Rotor.rotor_for_name(ENIGMA_I_ROTOR_II)
        rotor3 = Rotor.rotor_for_name(ENIGMA_I_ROTOR_I)
        rotor3.set_starting_position('J')
        rotor2.set_starting_position('G')
        rotor1.set_starting_position('V')
        enigma = Enigma(rotors = [rotor1,
                         rotor2,
                         rotor3])
        enigma.reflector = Rotor.rotor_for_name(REFLECTOR_B)
        ciphered = enigma.encrypt_string('AAAAA')
        self.assertEqual(ciphered, 'XVUYV')

