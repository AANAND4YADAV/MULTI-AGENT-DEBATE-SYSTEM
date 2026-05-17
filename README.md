# Multi-Agent Debate Simulator

A lightweight experimental project that simulates debates between multiple AI agents using local and cloud-based language models.

The project explores how different AI agents interact when given:
- different roles
- different beliefs
- shared context
- opponent arguments

Instead of building a simple chatbot, this project focuses on:
- multi-agent interaction
- prompt behavior
- context flow
- orchestration logic
- modular AI system design

---

# Features

- Multiple AI debate agents
- Role-based responses
- Context-aware rebuttals
- Judge analysis system
- Modular project structure
- Support for Ollama models
- Local + cloud model experimentation

---

# Project Structure

```bash
multi-agent-debate/
│
├── main.py
│
├── core/
│   ├── llm.py
│   └── debate_manager.py
│
├── agents/
│   └── agent.py
│
├── data/
│   └── topics.py
│
├── .env.example
├── requirements.txt
└── README.md
```

---

# Concepts Explored

This project helped explore and experiment with:

- Prompt engineering
- Multi-agent interaction
- Context passing
- Role conditioning
- Debate orchestration
- Local LLM inference
- Modular architecture
- Separation of concerns
- Basic OOP design

Several interesting behaviors were also observed:
- response imitation
- behavioral drift
- prompt sensitivity
- instruction conflicts
- context-dependent reasoning

---

# Early Experiments & Observations

## Experiment 1 — Small Local Models

Initial testing was done using:

- gemma:2b

### Observations

- lightweight and easy to run locally
- struggled with stance consistency
- agents sometimes accidentally agreed
- long prompts reduced debate quality
- concise prompts produced better interactions

Example observation:
> shorter prompts often created more natural debates than overly detailed prompts.

---

## Experiment 2 — Stronger Models

Later testing was performed using:

- gpt-oss:120b-cloud

### Observations

- stronger reasoning quality
- more coherent rebuttals
- better role consistency
- emergent moderator/judge-like behavior
- improved contextual understanding

The model occasionally introduced:
- self-generated structure
- nuanced arguments
- implicit judging logic

without explicit hardcoded instructions.

---

# Why This Project Exists

The goal of this project is not only to generate AI debates, but also to learn:

- how AI systems are structured
- how context affects model behavior
- how orchestration layers work
- how modular software architecture is designed

This project is being developed incrementally as a learning-focused engineering experiment.

---

# Future Plans

- Multi-round debates
- Debate memory system
- Async agent execution
- Real-time streaming responses
- Agent scoring system
- Debate visualization
- Web interface
- Multiple concurrent debate rooms

---

# Example Debate Topics

- Should AI replace teachers?
- What if YouTube was banned in India?
- Is remote work better than office culture?
- Should social media require age verification?
- Will AI create more jobs than it destroys?

---

# Installation

## Clone Repository

```bash
git clone <your-repo-url>
cd multi-agent-debate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

---

# Tech Stack

- Python
- Ollama
- Local LLMs
- Cloud-hosted LLMs

---
# Architecture

```text
                        ┌────────────────────┐
                        │      main.py       │
                        │  Entry Point       │
                        └─────────┬──────────┘
                                  │
                                  ▼
                  ┌──────────────────────────┐
                  │   debate_manager.py      │
                  │  Debate Orchestration    │
                  └─────────┬────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼

┌────────────────┐  ┌────────────────┐  ┌────────────────┐
│    agent.py    │  │    topics.py   │  │     llm.py     │
│ Agent Objects  │  │ Debate Topics  │  │ Model Interface│
└────────────────┘  └────────────────┘  └────────┬───────┘
                                                  │
                                                  ▼
                                      ┌────────────────────┐
                                      │   Ollama / LLM     │
                                      │ gpt-oss:120b-cloud │
                                      └────────────────────┘
```

---

## Component Responsibilities

### `main.py`
- Starts the debate system
- Loads agents and topics
- Controls debate execution flow

---

### `debate_manager.py`
Core orchestration layer responsible for:
- prompt construction
- context passing
- rebuttal handling
- round management
- debate coordination

---

### `agent.py`
Defines AI debate agents using OOP principles.

Each agent contains:
- name
- role
- stance

---

### `topics.py`
Stores structured debate topics and stances.

Separates:
- data
from
- orchestration logic

---

### `llm.py`
Handles all communication with the language model.

Responsibilities:
- sending prompts
- receiving responses
- abstracting model interaction

This allows future model switching without changing debate logic.

---

## System Flow

1. `main.py` initializes debate agents
2. Topic data is loaded from `topics.py`
3. `debate_manager.py` creates prompts
4. Prompts are sent through `llm.py`
5. LLM generates responses
6. Responses are passed between agents as context
7. Judge agent analyzes the final debate

# Final Note

This project started as a simple single-file experiment and gradually evolved into a modular multi-agent system.

The main objective is continuous experimentation, learning, and understanding how intelligent systems behave under different prompting and orchestration strategies.
