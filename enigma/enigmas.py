from enigma import rotors


class Enigma:

    def __init__(self):
        self.model_name = None
        self.rotors = []
        self.reflector = None

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
        cipher = letter
        for rotor in self.rotors:
            cipher = rotor.right_to_left(cipher)
        cipher = self.reflector.reflect(cipher)
        for i in range(len(self.rotors)-1,-1,-1):
            rotor = self.rotors[i]
            cipher = rotor.left_to_right(cipher)
        return cipher

    def encrypt_string(self, plaintext):
        cipher = ''
        for c in plaintext:
            cipher += self.encrypt_letter(c)
        return cipher