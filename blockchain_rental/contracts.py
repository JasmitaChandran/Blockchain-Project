"""Rental smart-contract inspired flows."""
from __future__ import annotations

from dataclasses import dataclass

from blockchain_rental.blockchain import Blockchain
from blockchain_rental.block import Transaction


@dataclass
class RentalProperty:
    property_id: str
    owner: str
    rent_amount: float


@dataclass
class RentalContract:
    blockchain: Blockchain
    property: RentalProperty

    def reserve(self, tenant: str) -> None:
        tx = Transaction(
            sender=tenant,
            recipient=self.property.owner,
            amount=self.property.rent_amount,
            action="reserve",
            metadata={"property_id": self.property.property_id},
        )
        self.blockchain.new_transaction(tx)

    def pay_rent(self, tenant: str) -> None:
        tx = Transaction(
            sender=tenant,
            recipient=self.property.owner,
            amount=self.property.rent_amount,
            action="rent_payment",
            metadata={"property_id": self.property.property_id},
        )
        self.blockchain.new_transaction(tx)

    def terminate(self, tenant: str) -> None:
        tx = Transaction(
            sender=self.property.owner,
            recipient=tenant,
            amount=0,
            action="terminate",
            metadata={"property_id": self.property.property_id},
        )
        self.blockchain.new_transaction(tx)
