from modulo import find_modular_inverse, find_modular_exponentiation
from utils import convert_message_to_number, convert_number_to_message

class RSA(object):
    def __init__(self, p, q, e, with_manual):
        self.p = p
        self.q = q
        self.e = e
        Phi = (p - 1)*(q - 1)
        if with_manual:
            print('Phi: {Phi}'.format(Phi=Phi))
            print('Find d:')
        self.d = find_modular_inverse(self.e, Phi, True)

        if with_manual:
            print('d= {d}'.format(d=self.d))
    
    def encode(self, message, with_manual):
        number = convert_message_to_number(message)
        number = number % (self.p * self.q)
        if with_manual:
            print('Message to number: {number}'.format(number=number))
        if number < self.p * self.q:
            if with_manual:
                print('Encode:')
            return find_modular_exponentiation(number, self.e, self.p * self.q, with_manual)
        else:
            return -1
            
    def decode(self, code, with_manual):
        if code < (self.p * self.q) and code > -1 and self.d:
            if with_manual:
                print('Decode:')
            number =  find_modular_exponentiation(code, self.d, self.p * self.q, with_manual)
            return convert_number_to_message(number)
        else:
            return None
    
if __name__ == "__main__":
    rsa = RSA(27644437, 479001599, 27092003, True)
    code = rsa.encode('TRANDUCTRUNG', True)
    print('Code: {code}'.format(code=code))
    mesage = rsa.decode(code, True)
    print('Message: {mesage}'.format(mesage=mesage))