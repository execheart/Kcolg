# 🛡️ Kcolg IDOR Scanner (MVP v0.2)

**Kcolg** is an offensive security assistant developed in Python, focused on automated detection of **IDOR** (Insecure Direct Object Reference) vulnerabilities in APIs.

This project was born from the need for a lightweight, modular, and educational tool for **Bug Bounty** beginners.

---

## ⚖️ Legal Disclaimer

**For educational and ethical testing purposes only.**
The use of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. The developer assumes no liability and is not responsible for any misuse or damage caused by this program.

---

## ✨ Current Features (MVP)
- **Substitution Engine:** Automatic ID swapping in REST endpoints.
- **Authentication Simulation:** Support for custom Headers (Bearer Tokens).
- **Response Analysis:** Identification of status codes and JSON data preview.
- **Scanning Loop:** Sequential testing of multiple objects in a single execution.

## 🚀 Getting Started

1. Ensure you have [Python 3.x](https://www.python.org) installed.
2. Clone the repository:
   ```bash
   git clone https://github.com
   cd Kcolg
