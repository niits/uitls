from modulo import find_modular_inverse, find_modular_exponentiation
from utils import convert_message_to_number, convert_number_to_message

class RSA(object):
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.e = e
        Phi = (p - 1)*(q - 1)
        self.d = find_modular_inverse(self.e, Phi)
    
    def encode(self, message):
        number = convert_message_to_number(message)
        if number < self.p * self.q:
            return find_modular_exponentiation(number, self.e, self.p * self.q)
        else:
            return -1
            
    def decode(self, code):
        if code < self.p * self.q and code > -1:
            number =  find_modular_exponentiation(code, self.d, self.p * self.q)
            return convert_number_to_message(number)
        else:
            return None
    
if __name__ == "__main__":
    rsa = RSA(61, 53, 17)
    code = rsa.encode('TR')
    print(rsa.decode(code))