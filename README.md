# 🌱 Croply — Farm Smarter. Own Your Data.

> AI-powered crop guidance for smallholder farmers — with full control over their farm data.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Built on Kusama](https://img.shields.io/badge/Built%20on-Kusama-E6007A)](https://kusama.network)
[![Status: Early Stage](https://img.shields.io/badge/Status-Early%20Stage-yellow)]()
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org)

---

## The Problem

500 million smallholder farmers produce 70% of the world's food — yet they make critical decisions with almost no data infrastructure.

When farmers need access to credit, insurance, or premium markets, they're forced to hand over sensitive farm data: exact yields, field locations, financial records. This data is then used against them — by lenders setting unfavorable terms, by buyers negotiating prices down, by insurers finding reasons to deny claims.

**Farmers face an impossible choice: share everything and lose leverage, or share nothing and lose access.**

---

## What Croply Does

Croply is a mobile-first farming assistant that gives smallholder farmers two things they've never had together:

### 🤖 AI Crop Guidance
- **Pest & disease detection** — take a photo, get an instant diagnosis and treatment plan
- **Crop planning** — personalized planting schedules based on your region, season, and soil
- **Weather-aware recommendations** — irrigation timing, harvest windows, frost alerts
- **Market insights** — price trends and optimal selling windows

### 🔐 Data Sovereignty
Farmers shouldn't have to expose their raw data to access financial services. Croply lets farmers **prove what matters** — to lenders, insurers, and buyers — without handing over their entire farm records.

A farmer can prove their harvest exceeded a threshold to qualify for a loan. A buyer can verify sustainable practices were followed. An insurer can confirm crop loss occurred. **All without the farmer ever sharing the underlying data.**

This is built on cryptographic verification — not trust.

---

## How It Works

```
                    FARMER'S PHONE
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼
   AI Farming Assistant         Data Vault (local)
   • Crop planning              • Yield records
   • Pest detection             • Field data
   • Weather alerts             • Farming logs
   • Market guidance                   │
                                       │
                              Cryptographic Proof
                              (data stays on device)
                                       │
                                       ▼
                            ┌─────────────────────┐
                            │   Kusama Network     │
                            │  (verification layer)│
                            └─────────────────────┘
                                       │
                            ┌──────────┴──────────┐
                            │                     │
                       Lenders             Insurers / Buyers
                    (verify eligibility)   (verify claims)
                    
                    Neither party ever sees raw farm data.
```

---

## Who Benefits

| Stakeholder | What They Get |
|---|---|
| **Smallholder Farmer** | AI crop guidance + control over their own data |
| **Micro-lender** | Verified farm credentials without compliance overhead |
| **Crop Insurer** | Verifiable loss claims without fraud risk |
| **Market Buyer** | Verified sustainable/organic practice claims |
| **NGO / Aid Org** | Reach verified farmers without centralised registries |

---

## Tech Stack

### Phase 1 — MVP (Current)
- **Backend:** Python (FastAPI)
- **AI:** Image-based pest/disease detection, crop planning models
- **Mobile:** React Native (optimized for low-bandwidth, low-end Android)
- **Data:** Local-first, farmer-controlled storage

### Phase 2 — Verification Layer
- **Cryptographic proofs:** Privacy-preserving credential verification
- **Chain:** Kusama / Asset Hub for on-chain verification
- **SDK:** Polkadot.js for wallet and chain interaction
- **Smart Contracts:** ink! (Substrate) for credential logic

### Phase 3 — Autonomous Farming Layer
- Automated crop insurance triggers based on verified on-chain data
- Cross-chain interoperability with DeFi lending protocols
- Fully autonomous farm management with verifiable outcomes

---

## Repository Structure

```
assistant/
├── backend/               # Python FastAPI — AI inference & crop logic
│   ├── api/               # REST endpoints
│   ├── models/            # AI models (pest detection, crop planning)
│   └── utils/
├── src/
│   ├── verification/      # Cryptographic proof generation & verification
│   │   ├── proofs/        # Credential proof types
│   │   ├── verifier/      # On-chain verifier contracts (ink!)
│   │   └── sdk/           # Developer SDK
│   ├── mobile/            # React Native farmer app
│   ├── api/               # Node.js API gateway
│   └── web/               # Web dashboard
├── docs/                  # Architecture, design docs
├── ARCHITECTURE.md
├── CONTRIBUTING.md
└── LICENSE
```

---

## Roadmap

- [x] Project concept & architecture
- [x] Python backend scaffold
- [ ] MVP AI assistant (crop planning + pest detection)
- [ ] Farmer data vault (local-first storage)
- [ ] Cryptographic credential system
- [ ] Kusama testnet deployment
- [ ] Farmer pilot (10 smallholder farmers)
- [ ] Mainnet launch on Kusama

---

First on Kusama

Kusama's permissionless, experimental infrastructure is the right foundation for Croply:

- Fast iteration — we can test and refine the verification layer without Polkadot's stability constraints
- Asset Hub — stable settlement layer for verified farmer credentials
- Smart contracts — ink! contracts handle credential verification logic
- Aligned values — Kusama's decentralized, censorship-resistant ethos matches our mission of giving power back to farmers

---

## Contributing

We're actively looking for contributors with expertise in:

- React Native / mobile development (low-bandwidth environments)
- Rust / ink! smart contracts
- Cryptographic systems and privacy-preserving technology

See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

---

## Team

Built by farmers, developers, and Web3 builders.

- **Anda** (https://x.com/dgreatanda) - Founder & Business Development, Polkadot Ambassador
- **Hope Clary** (https://x.com/Hopeioum) — CTO, Polkadot Veteran (United States)
- **AbeCryp** (https://x.com/Claris_write) — Content Lead
- *Open roles: Mobile Developer, AI/ML Engineer*
---

## Links

- 🌐 Website: coming soon
- 💬 [GitHub Discussions](https://github.com/Croply-AI/assistant/discussions)
- 📄 [Architecture](ARCHITECTURE.md)
- 📋 [Contributing](CONTRIBUTING.md)

---

*Croply is an early-stage project building toward a future where every farmer — regardless of location or resources — can access intelligent crop guidance and fair financial services.*
