from llm import generate
from agent import Agent

def ask_agent(agent: Agent, topic: str, previous_message: str = "") -> str:
    prompt = f"""
You are participating in a live debate.
Your name: {agent.name}
Your role: {agent.role}
Debate topic: {topic}
Your belief: {agent.stance}
Previous speaker said: {previous_message}

Rules:
- Stay loyal to your belief
- Disagree if necessary
- Speak naturally
- Keep response concise
- Sound human
"""
    return generate(prompt)


def run_debate(agents: list[Agent], topic: str):
    print("\n" + "=" * 50)
    print(" MULTI AGENT DEBATE")
    print("=" * 50)
    print(f"\nMODERATOR:\n\nWelcome to tonight's debate.\nTopic: {topic}\n")

    # Round 1
    conversation_history = []
    print("\n" + "-" * 50 + "\nROUND 1\n" + "-" * 50)
    for agent in agents:
        response = ask_agent(agent, topic)
        conversation_history.append(f"{agent.name}: {response}")
        print(f"\n{agent.name} ({agent.role}):\n{response}")

    # Round 2 — Rebuttals
    print("\n" + "-" * 50 + "\nROUND 2 — REBUTTALS\n" + "-" * 50)
    for i, agent in enumerate(agents):
        opponent_arg = conversation_history[i - 1]
        response = ask_agent(agent, topic, opponent_arg)
        print(f"\n{agent.name} ({agent.role}):\n{response}")

    # Judge
    judge_prompt = f"""
You are an unbiased debate judge.
Topic: {topic}
Debate transcript: {conversation_history}
Analyze the debate, decide who had the strongest argument, and explain briefly.
"""
    verdict = generate(judge_prompt)
    print("\n" + "=" * 50 + "\nJUDGE ANALYSIS\n" + "=" * 50)
    print(f"\nJUDGE:\n{verdict}")
