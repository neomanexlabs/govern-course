from decimal import Decimal

from billing.invoice import Invoice, Line


def test_single_line_total():
    inv = Invoice("INV-1001", [Line("Setup fee", Decimal("50.00"))])
    assert inv.total() == Decimal("60.00")


def test_two_lines_total():
    inv = Invoice("INV-1002", [Line("Plan", Decimal("20.00")), Line("Seat", Decimal("5.00"))])
    assert inv.total() == Decimal("30.00")
