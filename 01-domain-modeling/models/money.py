from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    currency: str
    value: int

    def __add__(self, other) -> "Money":
        if other.currency != self.currency:
            raise ValueError(f"Cannot add {self.currency} to {other.currency}")
        return Money(self.currency, self.value + other.value)

    def __sub__(self, other) -> "Money":
        if other.currency != self.currency:
            raise ValueError(f"Cannot add {self.currency} to {other.currency}")
        return Money(self.currency, self.value - other.value)

    def __mul__(self, other) -> "Money":
        if not (isinstance(other, float) or isinstance(other, int)):
            raise TypeError(f"Cannot multiply {type(other)}")
        return Money(self.currency, self.value * other)
