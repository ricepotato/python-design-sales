import os
import dotenv
import pytest
from pay.credit_card import CreditCard
from pay.processor import PaymentProcessor, luhn_checksum


dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY") or ""


def test_invalid_api_key(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        payment_processor = PaymentProcessor("")
        payment_processor.charge(card, 100)


def test_card_number_valid_date(card: CreditCard):
    payment_processor = PaymentProcessor(API_KEY)
    assert payment_processor.validate_card(card)


def test_card_number_invalid_date(card: CreditCard):
    payment_processor = PaymentProcessor(API_KEY)
    card.expiry_year = 1900
    assert not payment_processor.validate_card(card)


def test_card_number_invalid_luhn():
    assert not luhn_checksum("1249190007575068")


def test_card_number_valid_luhn():
    assert luhn_checksum("1249190007575069")


def test_charge_card_valid(card: CreditCard):
    payment_processor = PaymentProcessor(API_KEY)
    payment_processor.charge(card, 100)


def test_charge_card_invalid(card: CreditCard):
    card.number = "1249190007575068"
    with pytest.raises(ValueError):
        payment_processor = PaymentProcessor(API_KEY)
        payment_processor.charge(card, 100)
