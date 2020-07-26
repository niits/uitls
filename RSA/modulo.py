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
            print(str(module).ljust(12), str(number).ljust(12), str(r).ljust(12), str(q).ljust(12), str(y0).ljust(18),str(y1).ljust(18),str(y).ljust(18))

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
            print(str(base).ljust(18), str(exponent).ljust(18), str(d).ljust(18))
        
        exponent = exponent // 2
        base = (base * base) % module
    
    return d


if __name__ == "__main__":
    print(find_modular_inverse(202005091905, 1073807359, True))