from app.agents.graph_agent import create_agent_graph


def main():
    graph = create_agent_graph()

    questions = [
        "What is 125 * 8?",
        "What is an AI agent?",
        "What are the latest developments in AI agents?",
    ]

    for question in questions:
        print("\n==============================")
        print("Question:", question)

        result = graph.invoke(
            {
                "question": question,
                "decision": "",
                "tool_input": "",
                "tool_result": "",
                "answer": "",
            }
        )

        print("Decision:", result["decision"])
        print("Tool Result:")
        print(result["tool_result"])


if __name__ == "__main__":
    main()