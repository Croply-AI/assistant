# Croply Verification Layer

This module handles how Croply lets farmers prove facts about their farms to third parties — without exposing underlying raw data.

## The Problem This Solves

A farmer wants a micro-loan. The lender needs to know the farm is productive. Currently the farmer has two options: hand over all their records (and lose leverage), or provide nothing (and get rejected).

Croply's verification layer creates a third path: the farmer proves their yield exceeded a threshold. The lender gets the answer they need. The farmer's records stay on their device.

## How It Works

```
Farmer selects what to prove
         │
         ▼
Proof generated locally
using data from their vault
         │
         ▼
Only the proof goes to Kusama
Raw data never leaves the device
         │
         ▼
Third party verifies on-chain
Gets: verified ✓ or not ✗
Gets: nothing else
```

## Credential Types

| Credential | Proves | Keeps Private |
|---|---|---|
| **Yield** | "Harvest exceeded X kg/acre" | Exact figures, location |
| **Land** | "Actively farming this land" | GPS, coordinates |
| **Practice** | "Follows sustainable methods" | Specific inputs, costs |
| **Credit** | "Meets lender criteria" | Full financial records |

## Directory Structure

```
verification/
├── proofs/          # Credential proof types
│   ├── yield/
│   ├── land/
│   ├── practice/
│   └── credit/
├── verifier/        # ink! smart contracts (on-chain verification)
│   └── src/
├── sdk/             # SDK for third-party integrators (lenders, insurers)
│   └── src/
└── tests/
```

## Status

🚧 **Active design phase** — implementation not yet started.

Current focus:
- [ ] Finalizing credential data models
- [ ] Designing proof generation pipeline
- [ ] ink! verifier contract specification
- [ ] SDK interface design for third-party integrators

## Contributing

This is our highest-priority development area right now. If you have experience in cryptographic systems, privacy-preserving technology, or ink! smart contracts — please open a [Discussion](https://github.com/Croply-AI/assistant/discussions).

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for full guidelines.
