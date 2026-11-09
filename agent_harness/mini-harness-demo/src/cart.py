from decimal import Decimal, ROUND_HALF_UP


def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def calculate_total(items, user_type="normal"):
    """
    items: [{"price": "60.00", "qty": 2}]
    rules:
    - subtotal >= 100: minus 10
    - vip user: 5% off after threshold discount
    - return Decimal with 2 decimal places
    """
    total = Decimal("0.00")

    for item in items:
        price = Decimal(str(item["price"]))
        qty = int(item["qty"])

        if price < 0:
            raise ValueError("price must not be negative")

        if qty < 0:
            raise ValueError("qty must not be negative")

        total += price * qty

    if total >= Decimal("100.00"):
        total -= Decimal("10.00")

    if user_type == "vip":
        total = total * Decimal("0.95")

    return money(total)
