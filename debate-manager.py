from llm import generate_response


def ask_agent(agent, topic, previous_message=""):

    prompt = f"""
You are participating in a debate.

Your name:
{agent.name}

Your role:
{agent.role}

Topic:
{topic}

Your belief:
{agent.stance}

Opponent said:
{previous_message}

Rules:
- Stay loyal to your belief
- Speak naturally
- Keep response concise
"""

    response = generate_response(prompt)

    return response