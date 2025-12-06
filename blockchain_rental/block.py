"""Lightweight blockchain primitives for rental property events."""
from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Transaction:
    """Represents a single action in the rental system."""

    sender: str
    recipient: str
    amount: float
    action: str
    metadata: Optional[dict] = None

    def serialize(self) -> str:
        """Return a deterministic string representation for hashing."""
        body = {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "action": self.action,
            "metadata": self.metadata or {},
        }
        return json.dumps(body, sort_keys=True)


@dataclass
class Block:
    """A minimal block that links rental transactions together."""

    index: int
    previous_hash: str
    transactions: List[Transaction]
    timestamp: float = field(default_factory=time.time)
    nonce: int = 0

    def compute_hash(self) -> str:
        """Compute the block hash using SHA-256."""
        block_string = json.dumps(
            {
                "index": self.index,
                "previous_hash": self.previous_hash,
                "transactions": [tx.serialize() for tx in self.transactions],
                "timestamp": self.timestamp,
                "nonce": self.nonce,
            },
            sort_keys=True,
        )
        return hashlib.sha256(block_string.encode()).hexdigest()
