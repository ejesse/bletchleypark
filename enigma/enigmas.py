

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
        ciphered = letter
        local_rotors = list(self.rotors)
        for rotor in local_rotors:
            ciphered = rotor.right_to_left(ciphered)
            print(ciphered)
        ciphered = self.reflector.right_to_left(ciphered)
        print(ciphered)
        local_rotors.reverse()
        for rotor in local_rotors:
            ciphered = rotor.left_to_right(ciphered)
            print(ciphered)
        return ciphered