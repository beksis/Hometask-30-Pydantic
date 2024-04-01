from pydantic import BaseModel
from typing import List


class User(BaseModel):
    name: str
    mail: str
    address: List[str]


class Bank(BaseModel):
    name: str
    rating: float
    opened: int


class Card(BaseModel):
    cardholder: User
    which_bank: Bank
    opened: int


class Balance(BaseModel):
    card: Card
    amount: float
    currency: str


users = [
    User(name="Alice", mail="alice@example.com", address=["Almazar rayon", "street Qoraqamish"]),
    User(name="Bob", mail="bob@example.com", address=["Almazar rayon", "street Qorasaroy"]),
]

banks = [
    Bank(name="Bank A", rating=4.5, opened=2000),
    Bank(name="Bank B", rating=4.2, opened=1995),
]

cards = [
    Card(cardholder=users[0], which_bank=banks[0], opened=2020),
    Card(cardholder=users[1], which_bank=banks[1], opened=2015),
]

balances = [
    Balance(card=cards[0], amount=1000.0, currency="USD"),
    Balance(card=cards[1], amount=500.0, currency="EUR"),
]