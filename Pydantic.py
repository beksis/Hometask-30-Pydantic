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
    User(name="Maksim", mail="maksim_ex@gmail.com", address=["Mirabad distr.", "Nukus str, 66"]),
    User(name="Bobur", mail="bobur668@mail.ru", address=["Almazar distr.", "Qorasaroy str"]),
]

banks = [
    Bank(name="Kapital Bank ", rating=4.5, opened=1998),
    Bank(name="Davr Bank", rating=4.2, opened=2000),
]

cards = [
    Card(cardholder=users[0], which_bank=banks[0], opened=2020),
    Card(cardholder=users[1], which_bank=banks[1], opened=2015),
]

balances = [
    Balance(card=cards[0], amount=1000.0, currency="USD"),
    Balance(card=cards[1], amount=500.0, currency="EUR"),
]
