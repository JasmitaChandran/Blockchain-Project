"""Tiny demo for the blockchain rental property system."""
from __future__ import annotations

import json
from pathlib import Path

from blockchain_rental.blockchain import Blockchain
from blockchain_rental.contracts import RentalContract, RentalProperty


def build_demo_chain() -> Blockchain:
    """Create a blockchain with a couple of rental events."""
    blockchain = Blockchain()
    property_one = RentalProperty(property_id="APT-101", owner="Landlord", rent_amount=1200)
    contract = RentalContract(blockchain=blockchain, property=property_one)

    contract.reserve(tenant="Alice")
    contract.pay_rent(tenant="Alice")
    contract.terminate(tenant="Alice")
    blockchain.mine()

    property_two = RentalProperty(property_id="APT-202", owner="Bob", rent_amount=950)
    contract_two = RentalContract(blockchain=blockchain, property=property_two)
    contract_two.reserve(tenant="Charlie")
    contract_two.pay_rent(tenant="Charlie")
    blockchain.mine()

    return blockchain


def save_demo(blockchain: Blockchain, output_path: Path) -> None:
    output = {
        "valid_chain": blockchain.is_valid(),
        "blockchain": blockchain.to_dict(),
    }
    output_path.write_text(json.dumps(output, indent=2))


def main() -> None:
    print("Building a sample blockchain ...")
    chain = build_demo_chain()
    output_file = Path("demo_chain.json")
    save_demo(chain, output_file)
    print(f"Saved demo chain to {output_file.resolve()}")
    print("First block details:")
    print(json.dumps(chain.to_dict()["chain"], indent=2))


if __name__ == "__main__":
    main()
