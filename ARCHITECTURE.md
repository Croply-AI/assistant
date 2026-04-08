# Croply — System Architecture

## Design Philosophy

Croply is built around two principles:

1. **Local-first AI** — crop intelligence runs on or near the farmer's device, not in a central server that owns their data
2. **Verifiable without visible** — farmers can prove facts about their farm to third parties without exposing the underlying records

These principles shape every architectural decision.

---

## System Overview

```
┌──────────────────────────────────────────────────────────────┐
│                      FARMER'S DEVICE                         │
│                                                              │
│  ┌──────────────────────┐    ┌────────────────────────────┐ │
│  │   AI Crop Assistant  │    │      Local Data Vault      │ │
│  │   (React Native)     │    │                            │ │
│  │                      │    │  Yield records             │ │
│  │  Pest detection      │    │  Field data                │ │
│  │  Crop planning       │    │  Farming activity logs     │ │
│  │  Weather alerts      │    │  Financial history         │ │
│  │  Market guidance     │    │                            │ │
│  └──────────────────────┘    └────────────┬───────────────┘ │
│                                           │                  │
│                              Proof Generator                 │
│                              (on-device)                     │
│                                           │                  │
└───────────────────────────────────────────┼──────────────────┘
                                            │
                                  Cryptographic Proof
                                  (raw data stays local)
                                            │
                                            ▼
                               ┌────────────────────────┐
                               │     Kusama Network     │
                               │                        │
                               │   Asset Hub            │
                               │   ink! Verifier        │
                               └────────────┬───────────┘
                                            │
                              ┌─────────────┴──────────────┐
                              │                            │
                         Micro-lenders             Insurers & Buyers
                         verify eligibility        verify claims
                         
                         No raw data. Ever.
```

---

## Core Components

### 1. AI Crop Assistant (Mobile)

The farmer-facing layer. Built in React Native, optimized for:
- Low-bandwidth rural connectivity
- Low-end Android devices (target: 2GB RAM, 4G/3G)
- Offline-first where possible

**Features:**
- Camera-based pest and disease identification
- Personalized crop planning (region, season, soil type, past yields)
- Weather-integrated recommendations
- Local market price tracking

### 2. Local Data Vault

All farm data is stored locally on the farmer's device by default. No centralized database holds raw farm records.

The vault manages:
- Yield and harvest records
- Field and location data
- Farming practice logs
- Financial history

Farmers control what is shared, with whom, and for how long.

### 3. Credential & Proof System

The privacy-preserving layer that lets farmers prove facts without exposing data.

**Credential Types:**

| Credential | Statement Proven | Data Kept Private |
|---|---|---|
| **Yield Credential** | "Harvest exceeded X kg/acre" | Exact yield, field location |
| **Land Credential** | "Actively farming this land" | GPS coordinates, acreage |
| **Practice Credential** | "Follows sustainable methods" | Specific inputs, costs |
| **Credit Credential** | "Meets lender criteria Y" | Full financial records |

**How it works:**
1. Farmer selects what to prove (e.g. "prove my yield to this lender")
2. Proof is generated locally using data from the vault
3. Only the proof — not the data — is submitted to Kusama
4. Lender verifies the proof on-chain via the ink! verifier contract

### 4. Kusama Verification Layer

On-chain infrastructure for anchoring and verifying farmer credentials.

- **Asset Hub** — stores verified credential commitments
- **ink! Verifier Contract** — accepts proof submissions, emits verification events
- **Developer SDK** — allows third parties (lenders, insurers) to request and verify credentials

---

## Backend (Python / FastAPI)

Server-side AI inference and aggregated insights:

```
backend/
├── api/
│   ├── crop.py          # Crop planning endpoints
│   ├── pest.py          # Pest detection endpoints
│   └── market.py        # Market data endpoints
├── models/
│   ├── vision/          # Computer vision models (pest detection)
│   └── planning/        # Crop planning models
└── utils/
    ├── weather.py       # Weather API integration
    └── preprocessing.py # Image preprocessing
```

AI models process anonymized, aggregated data only. Individual farm records never touch the backend.

---

## Data Flow

```
Farmer records yield data
         │
         ▼
Stored in local vault (device only)
         │
         ▼
Farmer requests credential
(e.g. "prove yield to lender")
         │
         ▼
Proof generated on-device
Raw data does not leave device
         │
         ▼
Proof submitted to Kusama
         │
         ▼
Lender queries on-chain verifier
Gets: ✓ verified / ✗ not verified
Gets: nothing else
```

---

## Phase Roadmap

### Phase 1 — AI MVP
- Python backend with crop planning and pest detection
- React Native mobile app (basic UI)
- Local data storage
- No chain integration

### Phase 2 — Verification Layer
- Credential proof system (on-device generation)
- Kusama testnet deployment
- ink! verifier smart contract
- Third-party SDK (lenders, insurers)
- Polkadot.js wallet integration

### Phase 3 — Autonomous Layer
- Automated insurance triggers (crop loss verified on-chain → payout triggered)
- Cross-chain interoperability with DeFi lending
- Autonomous farm management with verifiable outcomes
- Rust / Substrate smart contracts

---

## Security Principles

- **No raw data on-chain** — only cryptographic proofs
- **Local-first storage** — farmer's device is the source of truth
- **Open source** — all credential logic is publicly auditable
- **No vendor lock-in** — farmers can export their vault at any time
- **Credential contracts audited** before mainnet deployment

---

*See [CONTRIBUTING.md](CONTRIBUTING.md) to get involved, or open a [Discussion](https://github.com/Croply-AI/assistant/discussions) with questions.*
