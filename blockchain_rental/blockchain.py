"""Simple proof-of-concept blockchain for rental property events."""
from __future__ import annotations

import itertools
from typing import List

from blockchain_rental.block import Block, Transaction


class Blockchain:
    """Extremely small blockchain that stores rental transactions."""

    difficulty_prefix: str = "00"

    def __init__(self) -> None:
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self._counter = itertools.count()
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        genesis_block = Block(index=0, previous_hash="0", transactions=[])
        genesis_block.nonce, genesis_block_hash = self.proof_of_work(genesis_block)
        self.chain.append(genesis_block)
        self.last_hash = genesis_block_hash

    def new_transaction(self, transaction: Transaction) -> None:
        self.pending_transactions.append(transaction)

    def proof_of_work(self, block: Block) -> tuple[int, str]:
        """Brute-force until the hash starts with the difficulty prefix."""
        for nonce in self._counter:
            block.nonce = nonce
            guess_hash = block.compute_hash()
            if guess_hash.startswith(self.difficulty_prefix):
                return nonce, guess_hash
        raise RuntimeError("Proof of work search exhausted")

    def mine(self) -> Block:
        """Create a block from pending transactions and attach it to the chain."""
        if not self.pending_transactions:
            raise ValueError("No transactions to mine")

        new_block = Block(
            index=len(self.chain),
            previous_hash=self.last_hash,
            transactions=self.pending_transactions.copy(),
        )
        nonce, block_hash = self.proof_of_work(new_block)
        new_block.nonce = nonce
        self.chain.append(new_block)
        self.last_hash = block_hash
        self.pending_transactions.clear()
        return new_block

    def is_valid(self) -> bool:
        """Verify each block links correctly and matches its proof."""
        for prev, current in zip(self.chain, self.chain[1:]):
            if current.previous_hash != prev.compute_hash():
                return False
            if not current.compute_hash().startswith(self.difficulty_prefix):
                return False
        return True

    def to_dict(self) -> dict:
        return {
            "length": len(self.chain),
            "chain": [
                {
                    "index": block.index,
                    "previous_hash": block.previous_hash,
                    "nonce": block.nonce,
                    "timestamp": block.timestamp,
                    "transactions": [tx.serialize() for tx in block.transactions],
                }
                for block in self.chain
            ],
        }
