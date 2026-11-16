
import pytest

from vending_machine import select_item, make_change, purchase

def test_invalid_item():
    assert select_item("water", {}, 100) == "invalid"


def test_sold_out_item():
    assert select_item("cola", {}, 200) == "sold_out"


def test_insufficient_credit():
    stock = {"cola": 5}
    assert select_item("cola", stock, 100) == "insufficient"


def test_valid_item_selection():
    stock = {"cola": 5}
    assert select_item("cola", stock, 200) == "ok"


def test_no_change_needed():
    assert make_change(0) == []


def test_negative_change():
    with pytest.raises(ValueError):
        make_change(-10)


def test_valid_change():
    assert make_change(85) == [50, 25, 10]


def test_unreturnable_change():
    assert make_change(3) is None

def test_purchase_invalid_item():
    stock = {}
    assert purchase("water", stock, 200) == ("invalid", [])


def test_purchase_sold_out_item():
    stock = {}
    assert purchase("cola", stock, 200) == ("sold_out", [])


def test_purchase_insufficient_credit():
    stock = {"cola": 5}
    assert purchase("cola", stock, 100) == ("insufficient", [])


def test_purchase_no_exact_change():
    stock = {"cola": 5}

    result = purchase("cola", stock, 153)

    assert result == ("no_exact_change", [])
    assert stock["cola"] == 5


def test_successful_purchase():
    stock = {"cola": 5}

    result = purchase("cola", stock, 200)

    assert result == ("dispensed", [50])
    assert stock["cola"] == 4


def test_purchase_with_exact_payment():
    stock = {"chips": 3}

    result = purchase("chips", stock, 100)

    assert result == ("dispensed", [])
    assert stock["chips"] == 2
