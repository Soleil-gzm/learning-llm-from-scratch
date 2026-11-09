from decimal import Decimal
import pytest

from src.cart import calculate_total


def test_normal_user_threshold_discount():
    items = [{"price": "60.00", "qty": 2}]
    assert calculate_total(items) == Decimal("110.00")


def test_vip_discount_after_threshold_discount():
    items = [{"price": "60.00", "qty": 2}]
    assert calculate_total(items, user_type="vip") == Decimal("104.50")


def test_no_float_precision_issue():
    items = [
        {"price": "0.10", "qty": 3},
        {"price": "0.20", "qty": 1},
    ]
    assert calculate_total(items) == Decimal("0.50")


def test_negative_price_rejected():
    items = [{"price": "-1.00", "qty": 1}]
    with pytest.raises(ValueError):
        calculate_total(items)