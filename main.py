import ollama

# =========================
# MULTI AGENT DEBATE SYSTEM
# =========================

TOPIC = "What if YouTube was banned in India?"


def ask_agent(name, role, stance, previous_message=""):

    prompt = f"""
You are participating in a live debate.

Your name:
{name}

Your role:
{role}

Debate topic:
{TOPIC}

Your belief:
{stance}

Previous speaker said:
{previous_message}

Rules:
- Stay loyal to your belief
- Disagree if necessary
- Speak naturally
- Keep response concise
- Sound human
"""

    response = ollama.generate(
        model="gpt-oss:120b-cloud",
        prompt=prompt
    )

    return response["response"]


# =========================
# MODERATOR INTRODUCTION
# =========================

print("\n" + "=" * 50)
print("        MULTI AGENT DEBATE")
print("=" * 50)

moderator_intro = f"""
Welcome everyone to tonight's debate.

Topic:
{TOPIC}

Each participant will present their views and respond to others.
Please keep arguments concise and meaningful.
"""

print("\nMODERATOR:\n")
print(moderator_intro)


# =========================
# AGENT DEFINITIONS
# =========================

agents = [
    {
        "name": "Dr. Ananya Sharma",
        "role": "Technology Policy Scholar",
        "stance": "Opposes banning YouTube in India because it supports education, business, and free expression."
    },

    {
        "name": "Ravi Patel",
        "role": "Digital Minimalism Activist",
        "stance": "Supports banning YouTube in India because it spreads addiction, misinformation, and algorithmic manipulation."
    },

    {
        "name": "Aarav Mehta",
        "role": "Startup Founder",
        "stance": "Believes banning YouTube would damage India's creator economy and digital innovation."
    },

    {
        "name": "Nisha Verma",
        "role": "School Teacher",
        "stance": "Believes YouTube helps learning but excessive consumption harms student focus and discipline."
    }
]


# =========================
# ROUND 1
# =========================

conversation_history = []

print("\n" + "-" * 50)
print("ROUND 1")
print("-" * 50)

for agent in agents:

    response = ask_agent(
        agent["name"],
        agent["role"],
        agent["stance"]
    )

    conversation_history.append(
        f'{agent["name"]}: {response}'
    )

    print(f"\n{agent['name']} ({agent['role']}):\n")
    print(response)


# =========================
# ROUND 2 (REBUTTALS)
# =========================

print("\n" + "-" * 50)
print("ROUND 2 — REBUTTALS")
print("-" * 50)

for index, agent in enumerate(agents):

    opponent_argument = conversation_history[(index - 1)]

    response = ask_agent(
        agent["name"],
        agent["role"],
        agent["stance"],
        opponent_argument
    )

    print(f"\n{agent['name']} ({agent['role']}):\n")
    print(response)


# =========================
# JUDGE AGENT
# =========================

judge_prompt = f"""
You are an unbiased debate judge.

Topic:
{TOPIC}

Debate transcript:
{conversation_history}

Task:
- Analyze the debate
- Decide who presented the strongest argument
- Explain why briefly
"""

judge_response = ollama.generate(
    model="gpt-oss:120b-cloud",
    prompt=judge_prompt
)

print("\n" + "=" * 50)
print("JUDGE ANALYSIS")
print("=" * 50)

print("\nJUDGE:\n")
print(judge_response["response"])