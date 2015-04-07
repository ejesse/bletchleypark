from enigma.rotors import ALPHABET


class Enigma:

    def __init__(self, rotors=[]):
        self.model_name = None
        self.rotors = rotors
        self.reflector = None
        self._rotors_initialized=False
        self._init_rotors()

    def _init_rotors(self):
        if self._rotors_initialized:
            return
        if len(self.rotors) > 0:
            for r in self.rotors:
                r._enigma = self
            r = self.rotors[0]
            r._is_first = True
            self._rotors_initialized=True

    def check_turnovers(self):
        for i in range(len(self.rotors)-1,-1,-1):
            rotor = self.rotors[i]
            rotor.check_turnover()

    def turnover_signal(self, sending_rotor):
        position = self.rotors.index(sending_rotor)
        if position < len(self.rotors):
            self.rotors[position+1].rotate()
        # the "double step"
        # the pawls and ratchets cause this to happen
        # when the last wheel turns over, making
        # the previous wheel also turnover
        if position == (len(self.rotors)-2):
            self.rotors[position].rotate()

    def encrypt_letter(self, letter):
        """
        The basic function, enter a letter and get
        a cipher letter.

        NOTE: for programming sanity sake, we will
        treat the rotor direction counting from
        right to left, such that the right-most rotor
        is self.rotors[0]. This is because the engima
        machine ran the circuit from right to left
        from the perspective of the operator
        """
        cipher = letter.upper()
        if cipher not in ALPHABET:
            return ''
        for rotor in self.rotors:
            cipher = rotor.right_to_left(cipher)
        cipher = self.reflector.reflect(cipher)
        for i in range(len(self.rotors)-1,-1,-1):
            rotor = self.rotors[i]
            cipher = rotor.left_to_right(cipher)
        self.check_turnovers()
        return cipher

    def encrypt_string(self, plaintext):
        self.check_turnovers()
        cipher = ''
        for c in plaintext:
            cipher += self.encrypt_letter(c)
        return cipher


