# 🛡️ Kcolg IDOR Scanner (v0.4)

**Kcolg** is an offensive security assistant developed in Python, focused on automated detection of **IDOR** (Insecure Direct Object Reference) vulnerabilities in APIs.

This project was born from the need for a lightweight, modular, and educational tool for **Bug Bounty** beginners.

---

## ⚖️ Legal Disclaimer

**For educational and ethical testing purposes only.** 
The use of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. The developer assumes no liability and is not responsible for any misuse or damage caused by this program.

---

## ✨ Features (v0.4)
- **Smart URL Handling:** Automatic cleaning and validation of target endpoints.
- **Input Shield:** Prevents crashes from invalid user inputs.
- **Substitution Engine:** Automatic ID swapping in REST endpoints.
- **Authentication Simulation:** Support for custom Headers (Bearer Tokens).
- **Response Preview:** Real-time JSON data preview for quick analysis.

## 🚀 Getting Started

1.  **Ensure you have [Python 3.x](https://www.python.org) installed.**
2.  **Clone the repository:**
    ```bash
    git clone https://github.com
    cd Kcolg
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the scanner:**
    ```bash
 python main.py
    ```



    
