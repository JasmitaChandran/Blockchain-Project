# Blockchain Rental Property System (Easy Demo)

This repo contains a tiny, self-contained example of a blockchain-inspired rental property workflow. It is intentionally simple so you can run it without special tooling or dependencies.

## Features
- Minimal blockchain that links property events together using proof-of-work hashing
- Sample smart-contract style flows for reserving, paying rent, and terminating a lease
- Generates a JSON file that shows the chain contents and verifies validity

## Prerequisites
- Python 3.11+ (no external packages needed)

## Quick start
1. Create and activate a virtual environment (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Run the demo:
   ```bash
   python main.py
   ```
3. Inspect the output:
   - `demo_chain.json` contains the serialized chain and a `valid_chain` flag.
   - The console shows each block and transaction, demonstrating how rental events are linked.

## How it works
- `blockchain_rental/block.py` defines the block and transaction objects and how they are hashed.
- `blockchain_rental/blockchain.py` holds a tiny proof-of-work blockchain implementation.
- `blockchain_rental/contracts.py` mimics on-chain rental interactions (reserve, pay rent, terminate).
- `main.py` wires everything together, mints two example blocks, and saves the chain as JSON.

Feel free to tweak the transactions in `main.py` to model your own scenario—the blockchain will automatically rebuild and validate the chain structure.
