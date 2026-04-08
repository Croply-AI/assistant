# Contributing to Croply

Thanks for your interest in Croply. We're building AI-powered crop guidance for smallholder farmers — with real data ownership baked in from day one.

We're early-stage and building in public. Every contribution matters.

---

## What We're Building

Two things working together:

**An AI farming assistant** that helps smallholder farmers make better decisions — pest identification, crop planning, weather-aware recommendations, market insights.

**A farmer data layer** that lets farmers prove things about their farms to lenders, insurers, and buyers — without handing over raw records. Built on cryptographic verification, on Kusama.

---

## Where You Can Help

| Area | What's Needed |
|---|---|
| 📱 **Mobile (React Native)** | Low-bandwidth UX, offline-first features, camera integration |
| 🐍 **AI / ML (Python)** | Computer vision for pest detection, crop planning models |
| 🔐 **Cryptographic Systems** | Privacy-preserving credential generation and verification |
| 🦀 **Rust / ink!** | Smart contracts for on-chain credential verification |
| 🌍 **Agricultural Domain** | Crop knowledge, farming systems, regional context |
| 📝 **Docs & DX** | Developer experience, technical writing, guides |

---

## Getting Started

### Fork & Clone

```bash
git clone https://github.com/YOUR_USERNAME/assistant.git
cd assistant
```

### Run the Backend

```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Explore the Codebase

```
backend/        ← Start here for AI and crop logic (Python)
src/mobile/     ← React Native app
src/verification/ ← Credential and proof system (active development)
src/api/        ← API gateway
```

---

## How to Contribute

### Found a bug?
Open an [Issue](https://github.com/Croply-AI/assistant/issues) with as much detail as possible.

### Have a feature idea?
Start a [Discussion](https://github.com/Croply-AI/assistant/discussions) — especially for anything touching the credential or verification system, since these decisions have downstream security implications.

### Ready to submit code?
1. Branch off `main`: `git checkout -b feature/your-feature-name`
2. Make focused, well-described commits
3. Open a Pull Request referencing any related issues
4. Be ready for review — we take security and farmer privacy seriously

---

## Code Standards

- **Python:** PEP8, type hints preferred, docstrings for public functions
- **Rust/ink!:** `cargo fmt` before every commit
- **JavaScript/TypeScript:** Prettier defaults
- **Commits:** Use conventional commits — `feat:`, `fix:`, `docs:`, `chore:`

---

## A Note on the Verification System

The `src/verification/` layer handles how farmers prove credentials to third parties. This is security-critical code — farmer privacy depends on it being correct.

If you're contributing here:
- Open a Discussion before writing code — design decisions matter
- Document what each proof type proves, what stays private, what's revealed
- Include test cases with your PRs
- Reference any prior work or relevant research

---

## Community

- 💬 [GitHub Discussions](https://github.com/Croply-AI/assistant/discussions) — ideas, design, Q&A
- 🐛 [GitHub Issues](https://github.com/Croply-AI/assistant/issues) — bugs and tasks

---

## License

By contributing, you agree your work will be licensed under [MIT](LICENSE).

---

*We're building for farmers who have historically had the least access to tools that work for them. That responsibility shapes how we build.*
