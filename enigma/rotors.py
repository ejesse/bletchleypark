

ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ENIGMA_I_ROTOR_I = 'ENIGMA_I_ROTOR_I'
ENIGMA_I_ROTOR_II = 'ENIGMA_I_ROTOR_II'
ENIGMA_I_ROTOR_III = 'ENIGMA_I_ROTOR_III'
ENIGMA_I_ROTOR_IV = 'ENIGMA_I_ROTOR_IV'
ENIGMA_I_ROTOR_V = 'ENIGMA_I_ROTOR_V'

# reflectors

REFLECTOR_BETA = 'REFLECTOR_BETA'
REFLECTOR_GAMMA = 'REFLECTOR_GAMMA'
REFLECTOR_A = 'REFLECTOR_A'
REFLECTOR_B = 'REFLECTOR_B'
REFLECTOR_C = 'REFLECTOR_C'
REFLECTOR_B_THIN = 'REFLECTOR_B_THIN'
REFLECTOR_C_THIN = 'REFLECTOR_C_THIN'
REFLECTOR_ETW = 'REFLECTOR_ETW'

class Rotor:

    def __init__(self, key=''):
        self.rotor_number = None
        self.enigma_model = None
        self.offset = 0
        self.ring_setting = 0
        self._right_circuit = ALPHABET
        self.key = key
        self.__turnover_position = 0
        self._stepping = 0
        self._left_circuit = None

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

    def _carryover(self, item):
        carryover = item[0]
        return item[1:] + carryover

    def _rotate(self):
        if self._left_circuit is None:
            self._left_circuit = str(ALPHABET)
        self._left_circuit = self._carryover(self._left_circuit)
        self.key = self._carryover(self.key)

    def step(self):
        self._stepping+=1
        if self._stepping > self.__turnover_position:
            self._stepping = 0
            self._rotate()

    def right_to_left(self, letter):
        self.step()
        position = self._right_circuit.find(letter)
        if self._left_circuit is not None:
            cipher = self.key[position]
            position = self._left_circuit.find(cipher)
            return ALPHABET[position]
        return self.key[position]

    def reflect(self, letter):
        position = ALPHABET.find(letter)
        return self.key[position]

    def left_to_right(self, letter):
        if self._left_circuit is not None:
            position = ALPHABET.find(letter)
            cipher = self._left_circuit[position]
            position = self.key.find(cipher)
        else:
            position = self.key.find(letter)
        return self._right_circuit[position]

    @staticmethod
    def rotor_for_name(name):
        if name is 'ENIGMA_I_ROTOR_I':
            r = Rotor(key='EKMFLGDQVZNTOWYHXUSPAIBRCJ')
            r.turnover_position = 17
            return r
        elif name is 'ENIGMA_I_ROTOR_II':
            r = Rotor(key='AJDKSIRUXBLHWTMCQGZNPYFVOE')
            r.turnover_position = 5
            return r
        elif name is 'ENIGMA_I_ROTOR_III':
            r = Rotor(key='BDFHJLCPRTXVZNYEIWGAKMUSQO')
            r.turnover_position = 0
            return r
        elif name is 'ENIGMA_I_ROTOR_III':
            r = Rotor(key='BDFHJLCPRTXVZNYEIWGAKMUSQO')
            return r
        elif name is 'ENIGMA_I_ROTOR_IV':
            r = Rotor(key='ESOVPZJAYQUIRHXLNFTGKDCMWB')
            return r
        elif name is 'ENIGMA_I_ROTOR_V':
            r = Rotor(key='VZBRGITYUPSDNHLXAWMJQOFECK')
            return r
        elif name is 'REFLECTOR_BETA':
            r = Rotor(key='LEYJVCNIXWPBQMDRTAKZGFUHOS')
            return r
        elif name is 'REFLECTOR_GAMMA':
            r = Rotor(key='FSOKANUERHMBTIYCWLQPZXVGJD')
            return r
        elif name is 'REFLECTOR_A':
            r = Rotor(key='EJMZALYXVBWFCRQUONTSPIKHGD')
            return r
        elif name is 'REFLECTOR_B':
            r = Rotor(key='YRUHQSLDPXNGOKMIEBFZCWVJAT')
            return r
        elif name is 'REFLECTOR_C':
            r = Rotor(key='FVPJIAOYEDRZXWGCTKUQSBNMHL')
            return r
        elif name is 'REFLECTOR_B_THIN':
            r = Rotor(key='ENKQAUYWJICOPBLMDXZVFTHRGS')
            return r
        elif name is 'REFLECTOR_C_THIN':
            r = Rotor(key='RDOBJNTKVEHMLFCWZAXGYIPSUQ')
            return r
        elif name is 'REFLECTOR_ETW':
            r = Rotor(key='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            return r
        else:
            return None

