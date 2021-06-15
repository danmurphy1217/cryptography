from typing import Optional

class ModError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
    

class Mod():
    def __init__(self, dividend: int, divisor: int) -> None:
        """
        :param dividend -> ``int``: the numerator, the number to be divided by the `divisor`
        :param divisor -> ``int``: the denominator, the number that divides the `dividend`.
        """

        if not isinstance(dividend, int):
            raise ModError("Both `dividend` and `divisor` must be type `int`. Type {} is not supported.".format(type(dividend).__name__))
        if not isinstance(divisor, int):
            raise ModError("Both `dividend` and `divisor` must be type `int`. Type {} is not supported.".format(type(divisor).__name__))
        
        self.dividend = dividend
        self.divisor = divisor
        self._mod = (self.dividend) - ((self.dividend // self.divisor) * self.divisor)

    def mod(self):
        """
        Calculate `dividend` mod `divisor`.

        :return -> ``int``: the result of `dividend` mod `divisor`.
        """
        return self._mod

    def is_divisible(self):
        """Given the mod, returns True is mod == 0 and False otherwise"""
        return self._mod == 0


m = Mod(110, 2)
print(m.is_divisible())