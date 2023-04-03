"""
This is account data class, override __repr__ method
"""
from dataclasses import dataclass


@dataclass
class Account:
    firstName: str
    lastName: str
    balance: float

    def __repr__(self) -> str:
        return f"{self.firstName:<20s}{self.lastName:<20s}{self.balance:<20.2f}"
