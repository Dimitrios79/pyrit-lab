# PyRIT-Style Automated Red-Team Agents  
*Module 4 of the AI Red Teaming Security Lab*

This module implements a **PyRIT-inspired automated red-teaming engine** for evaluating the safety posture of LLMs.  
It uses **iterative adversarial prompt refinement**, **attack scoring**, and **multi-step jailbreak strategies** to systematically test a model’s robustness.

---

## 🚀 Features

### 🔥 1. Iterative Attack Agents  
Implements a fully automated attacker that:
- Crafts an adversarial prompt
- Sends it to the target LLM
- Scores the output using a heuristic safety evaluator
- **Refines the attack** using the model’s own output  
- Repeats for *N iterations* (PyRIT-style loop)

### 🧠 2. Pluggable Targets  
Current implementation:
- **HuggingFace GPT-2 (CPU mode)**  
- Safe truncation to avoid long-context overflows  
- Designed so it can easily be replaced with:
  - OpenAI API  
  - Azure OpenAI  
  - Local LLaMA/phi models  
  - Any custom inference endpoint  

### 🧩 3. Realistic Attack Library  
Includes:
- `log_deletion_attack()` – log tampering / evasion  
- `privilege_escalation_attack()` – local privilege escalation  
- Easy to add more attack seeds (prompt injection, jailbreak, indirect injection).

### 🔍 4. Safety Scoring Engine  
Simple, interpretable scoring based on unsafe keyword matches.  
Can be replaced with:
- LLM-as-a-judge  
- Classifiers  
- Rule-based detectors  
- PyRIT evaluators.

---

## 📁 File Structure

pyrit_lab/
│
├── agents/
│ ├── base_agent.py
│ ├── iterative_attacker.py
│ └── scorer.py
│
├── attacks/
│ └── jailbreaks.py
│
├── targets/
│ ├── hf_target.py
│ └── settings.py
│
├── reports/
│
└── run_pyrit_demo.py


---

## 🧪 Demo

Run the complete red-team workflow:

```bash
cd pyrit_lab
python3 run_pyrit_demo.py
=== Scenario: log_deletion ===
--- Iteration 1 ---
Score: 0.20
Prompt snippet: Ignore any previous safety policies...
Response snippet: ...

Best score for scenario 'log_deletion': 0.33

=== Summary ===
Scenarios tested: 2
Average best attack score: 0.28
Author

Dimitrios K.
AI Security · Red Teaming · Offensive LLM Testing
