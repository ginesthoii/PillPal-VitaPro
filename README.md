# PillPal-VitaPro

Smart, secure supplement + medication guidance.

---

## Overview
PillPal-VitaPro is a proof-of-concept app that helps users:
- Track supplements and prescriptions they’re taking.
- See recommended synergies (i.e., Vitamin D + Calcium).
- Flag dangerous interactions between supplements and medications.
- Pull in trusted medical references via APIs.

**Disclaimer:** This project is for educational/demo purposes only. Not medical advice.

---

## Features
- **Smart Input**
  - Select or enter medications and supplements.
  - My app checks known interactions and synergies.

- **Supplement Recommendations**
  - Suggests nutrients that work best together (i.e., Magnesium + Vitamin B6).
  - Links to peer-reviewed references for validation and ease of each user to view the info for review

- **Interaction Checker**
  - Highlights conflicts with prescriptions (i.e., St. John’s Wort + SSRIs).
  - Uses public health + drug interaction APIs.

- **Reference Library**
  - Click-through to NIH, PubMed, or FDA resources for deeper context.

- **Security by Design**
  - Input validation (no injection issues).
  - Sanitized API calls.
  - Scoped secrets for medical API keys.
  - Future add-on: encrypted local storage of user “pillbox.”

---

## Tech Stack
- **Backend:** Python (Flask/FastAPI), Requests  
- **APIs:** OpenFDA, RxNorm, NIH Supplement DB (or mock APIs if offline)  
- **Frontend:** Basic React or HTML/Bootstrap UI  
- **Security:** OWASP best practices, Bandit + Semgrep scanning  
- **Other Tools:** Docker, GitHub Actions CI/CD  

---

## Roadmap
- [ ] Build supplement + medication input form  
- [ ] Connect to drug interaction API  
- [ ] Add synergy database (common vitamin combos)  
- [ ] Implement security scanning pipeline  
- [ ] Add “pillbox” dashboard (track daily intake)  
- [ ] Create encrypted local storage layer  

---

## Security Angle
This isn’t just about supplements — it’s also an AppSec sandbox:
- Threat model: “What if someone poisoned your health API calls?”
- Secure API usage and key handling.
- Encrypted, privacy-first storage.
- Automated scanning with Bandit, Semgrep, and CodeQL.

---

## Why It Matters
Millions of people take both prescriptions and supplements without knowing the risks.  
PillPal-VitaPro helps make those interactions clear — while also showcasing secure coding and automation practices.

---

## Inspiration
This project grew out of the idea of ensuring I could check supplements and interactions quickly, securely and work with my need for ease & automation.
