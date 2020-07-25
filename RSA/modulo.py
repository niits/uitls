def find_modular_inverse(number, module, with_manual=False):
    y0 = 0
    y1 = 1
    temp = module

    while number > 0:
        r = module % number
        if r == 0:
            break

        q = module // number
        y = y0 - y1 * q

        if with_manual:
            print(str(module).rjust(4), str(number).rjust(4), str(r).rjust(4), str(q).rjust(4), str(y0).rjust(4),str(y1).rjust(4),str(y).rjust(4))

        y0 = y1
        y1 = y
        module = number
        number = r

    if number > 1:
        return None
    else:
        if y < 0:
            y = y + temp
        return y

def find_modular_exponentiation(base, exponent, module, with_manual=False):
    d = 1
    while exponent != 0:
        if exponent % 2 != 0:
            d = (d * base) % module

        if with_manual:
            print(str(base).rjust(8), str(exponent).rjust(8), str(d).rjust(8))
        
        exponent = exponent // 2
        base = (base * base) % module
    
    return d


if __name__ == "__main__":
    find_modular_inverse(30, 101, True)