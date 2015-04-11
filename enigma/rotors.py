

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


def get_next_alpha(letter):
    letter = letter.upper()
    if letter == 'Z':
        return 'A'
    position = ALPHABET.find(letter)
    return ALPHABET[position+1]


class Rotor:

    def __init__(self, key=''):
        self.display_state = 'A'
        self.name = None
        self.rotor_number = None
        self.enigma_model = None
        self.offset = 0
        self.ring_setting = 0
        self._right_circuit = ALPHABET
        self.key = key
        self.turnover_position = 'A'
        self._stepping = 0
        self._left_circuit = None
        self._enigma = None
        self._is_first = False

    def _carryover(self, item):
        carryover = item[0]
        return item[1:] + carryover

    def set_starting_position(self, letter):
        for i in range(0,ALPHABET.find(letter)):
            self.rotate()

    def check_turnover(self):
        if self.display_state == self.turnover_position:
            self._enigma.turnover_signal(self)

    def rotate(self):
        if self._left_circuit is None:
            self._left_circuit = str(ALPHABET)
        self._left_circuit = self._carryover(self._left_circuit)
        self.key = self._carryover(self.key)
        self.display_state = get_next_alpha(self.display_state)

    def right_to_left(self, letter):
        if self._is_first:
            self.rotate()
        position = self._right_circuit.find(letter)
        if self._left_circuit is not None:
            cipher = self.key[position]
            position = self._left_circuit.find(cipher)
            return ALPHABET[position]
        return self.key[position]

    def reflect(self, letter):
        raise NotImplemented("Rotors do not relflect!")

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
            r.name = 'ENIGMA_I_ROTOR_I'
            r.turnover_position = 'Q'
            return r
        elif name is 'ENIGMA_I_ROTOR_II':
            r = Rotor(key='AJDKSIRUXBLHWTMCQGZNPYFVOE')
            r.name = 'ENIGMA_I_ROTOR_II'
            r.turnover_position = 'E'
            return r
        elif name is 'ENIGMA_I_ROTOR_III':
            r = Rotor(key='BDFHJLCPRTXVZNYEIWGAKMUSQO')
            r.name = 'ENIGMA_I_ROTOR_III'
            r.turnover_position = 'V'
            return r
        elif name is 'ENIGMA_I_ROTOR_IV':
            r = Rotor(key='ESOVPZJAYQUIRHXLNFTGKDCMWB')
            r.name = 'ENIGMA_I_ROTOR_IV'
            r.turnover_position = 'J'
            return r
        elif name is 'ENIGMA_I_ROTOR_V':
            r = Rotor(key='VZBRGITYUPSDNHLXAWMJQOFECK')
            r.name = 'ENIGMA_I_ROTOR_V'
            r.turnover_position = 'Z'
            return r
        elif name is 'REFLECTOR_BETA':
            r = Reflector(key='LEYJVCNIXWPBQMDRTAKZGFUHOS')
            r.name = 'REFLECTOR_BETA'
            return r
        elif name is 'REFLECTOR_GAMMA':
            r = Reflector(key='FSOKANUERHMBTIYCWLQPZXVGJD')
            r.name = 'REFLECTOR_GAMMA'
            return r
        elif name is 'REFLECTOR_A':
            r = Reflector(key='EJMZALYXVBWFCRQUONTSPIKHGD')
            r.name = 'REFLECTOR_A'
            return r
        elif name is 'REFLECTOR_B':
            r = Reflector(key='YRUHQSLDPXNGOKMIEBFZCWVJAT')
            r.name = 'REFLECTOR_B'
            return r
        elif name is 'REFLECTOR_C':
            r = Reflector(key='FVPJIAOYEDRZXWGCTKUQSBNMHL')
            r.name = 'REFLECTOR_C'
            return r
        elif name is 'REFLECTOR_B_THIN':
            r = Reflector(key='ENKQAUYWJICOPBLMDXZVFTHRGS')
            r.name = 'REFLECTOR_B_THIN'
            return r
        elif name is 'REFLECTOR_C_THIN':
            r = Reflector(key='RDOBJNTKVEHMLFCWZAXGYIPSUQ')
            r.name = 'REFLECTOR_C_THIN'
            return r
        elif name is 'REFLECTOR_ETW':
            r = Reflector(key='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            r.name = 'REFLECTOR_ETW'
            return r
        else:
            return None


class Reflector(Rotor):

    def __init__(self, key=''):
        Rotor.__init__(self, key=key)

    def reflect(self, letter):
        position = ALPHABET.find(letter)
        return self.key[position]

    def right_to_left(self, letter):
        raise NotImplemented('Relfectors only reflect')

    def left_to_right(self, letter):
        raise NotImplemented('Relfectors only reflect')

