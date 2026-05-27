from agent import Agent
from debate_manager import run_debate
from topics import DEFAULT_TOPIC

AGENTS = [
    Agent(
        name="Dr. Ananya Sharma",
        role="Technology Policy Scholar",
        stance="Opposes banning YouTube — supports education, business, and free expression.",
        behavior="Speaks formally with data-backed arguments. Calm and analytical tone."
    ),
    Agent(
        name="Ravi Patel",
        role="Digital Minimalism Activist",
        stance="Supports banning YouTube — spreads addiction and misinformation.",
        behavior="Passionate and emotional. Uses real-world examples to make points."
    ),
    Agent(
        name="Aarav Mehta",
        role="Startup Founder",
        stance="Banning YouTube would damage India's creator economy.",
        behavior="Confident and business-focused. Talks in numbers and market impact."
    ),
    Agent(
        name="Nisha Verma",
        role="School Teacher",
        stance="YouTube helps learning but harms student focus when overused.",
        behavior="Balanced and empathetic. Speaks from classroom experience."
    ),
]

if __name__ == "__main__":
    run_debate(AGENTS, DEFAULT_TOPIC)
