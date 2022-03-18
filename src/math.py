class Math:
    def get_precision(x):
        max_digits = 14
        int_part = int(abs(x))
        magnitude = 1 if int_part == 0 else int(Math.log10(int_part)) + 1
        if magnitude >= max_digits:
            return 0
        frac_part = abs(x) - int_part
        multiplier = 10 ** (max_digits - magnitude)
        frac_digits = multiplier + int(multiplier * frac_part + 0.5)
        while frac_digits % 10 == 0:
            frac_digits /= 10
        scale = int(Math.log10(frac_digits))
        return scale

    def log(n, r):
        return  1 + Math.log(n / r, r) if (n > r - 1) else 0
     
    def log10(x):
        return Math.log(x, 10)

    def sqrt(x):
        if x < 0:
            return 0
        else:
            return x ** 0.5