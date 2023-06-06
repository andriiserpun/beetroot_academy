class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return self.numerator * other.denominator == other.numerator * self.denominator

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))