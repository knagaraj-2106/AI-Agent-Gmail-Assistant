"""
test_agent.py

Tests the complete LangGraph Gmail AI Agent.
"""

from langchain_core.messages import HumanMessage

from agents.graph import graph


def ask_agent(question: str):
    """
    Sends a user question to the LangGraph agent
    and prints the final response.
    """

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=question)
            ]
        }
    )

    print("\n" + "=" * 80)
    print(f"USER : {question}")
    print("=" * 80)

    print("\nAI RESPONSE:\n")

    # Print the final AI message
    print(result["messages"][-1].content)


if __name__ == "__main__":

    while True:

        question = input("\nAsk Gmail Agent (type 'exit' to quit): ")

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        ask_agent(question)