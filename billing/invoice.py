from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class Line:
    description: str
    unit_price: Decimal
    quantity: int = 1


@dataclass
class Invoice:
    number: str
    lines: list[Line] = field(default_factory=list)
    tax_rate: Decimal = Decimal("0.20")

    def subtotal(self) -> Decimal:
        return sum((line.unit_price for line in self.lines), Decimal("0"))

    def tax(self) -> Decimal:
        return (self.subtotal() * self.tax_rate).quantize(Decimal("0.01"))

    def total(self) -> Decimal:
        return self.subtotal() + self.tax()
