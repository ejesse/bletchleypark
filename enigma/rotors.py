

ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Rotor:

    def __init__(self, key=''):
        self.rotor_number = None
        self.enigma_model = None
        self.initial_mapping = ALPHABET
        self.offset = 0
        self.ring_setting = 0
        self._right_state = ALPHABET
        self.key = key
        self.__turnover_position = 0
        self._stepping = 0
        self._left_circuit = ALPHABET

    @property
    def turnover_position(self):
        return self.__turnover_position

    @turnover_position.setter
    def turnover_position(self, turnover_position):
        try:
            turnover_position = turnover_position.upper()
            self.__turnover_position = ALPHABET.find(turnover_position)
        except AttributeError:
            self.__turnover_position = turnover_position

    def _its_a_circle(self, position):
        if position > 25:
            position = position - 25
        return position

    def step(self):
        self._stepping = self._stepping + 1
        if self._stepping > self.__turnover_position:
            self.offset = self.offset + 1
            self._stepping = 0
            carryover = self.key[0]
            self.key = self.key[1:] + carryover
            carryover = self._left_circuit[0]
            self._left_circuit = self._left_circuit[1:] + carryover


    def right_to_left(self, letter):
        self.step()
        position = self.initial_mapping.find(letter)
        return self.key[position]

    def left_to_right(self, letter):
        position = self.key.find(letter)
        position = position - self.offset
        position = self._its_a_circle(position)
        return self.initial_mapping[position]


ENIGMA_I_ROTOR_I = Rotor(key='EKMFLGDQVZNTOWYHXUSPAIBRCJ')
ENIGMA_I_ROTOR_I.turnover_position = 17
ENIGMA_I_ROTOR_II = Rotor(key='AJDKSIRUXBLHWTMCQGZNPYFVOE')
ENIGMA_I_ROTOR_II.turnover_position = 5
ENIGMA_I_ROTOR_III = Rotor(key='BDFHJLCPRTXVZNYEIWGAKMUSQO')
ENIGMA_I_ROTOR_III.turnover_position = 0
ENIGMA_I_ROTOR_IV = Rotor(key='ESOVPZJAYQUIRHXLNFTGKDCMWB')
ENIGMA_I_ROTOR_V = Rotor(key='VZBRGITYUPSDNHLXAWMJQOFECK')

# reflectors

REFLECTOR_BETA = Rotor(key='LEYJVCNIXWPBQMDRTAKZGFUHOS')
REFLECTOR_GAMMA = Rotor(key='FSOKANUERHMBTIYCWLQPZXVGJD')
REFLECTOR_A = Rotor(key='EJMZALYXVBWFCRQUONTSPIKHGD')
REFLECTOR_B = Rotor(key='YRUHQSLDPXNGOKMIEBFZCWVJAT')
REFLECTOR_C = Rotor(key='FVPJIAOYEDRZXWGCTKUQSBNMHL')
REFLECTOR_B_THIN = Rotor(key='ENKQAUYWJICOPBLMDXZVFTHRGS')
REFLECTOR_C_THIN = Rotor(key='RDOBJNTKVEHMLFCWZAXGYIPSUQ')
REFLECTOR_ETW = Rotor(key='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
