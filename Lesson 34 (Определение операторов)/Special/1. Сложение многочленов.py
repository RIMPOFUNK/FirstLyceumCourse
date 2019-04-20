class Polynomial:
    def __init__(self, coeff):
        self.coeff = coeff[:]

    def __call__(self, val):
        ret = self.coeff[0]

        for i in range(1, len(self.coeff)):
            ret += self.coeff[i] * val**i
        return ret

    def __add__(self, add):
        m = max(self.coeff, add.coeff, key=lambda x: len(x))

        if m is self.coeff:
            ret = add.coeff[:]
        else:
            ret = self.coeff[:]

        for i in range(len(m)):
            if i >= len(ret):
                ret.append(m[i])
            else:
                ret[i] += m[i]

        return Polynomial(ret[:])

