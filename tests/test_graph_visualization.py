from app.agents.graph_agent import create_agent_graph


def main():
    graph = create_agent_graph()

    print("\nInsightAgent LangGraph")
    print("======================")

    print("\nGraph structure:")
    print(graph.get_graph().draw_ascii())


if __name__ == "__main__":
    main()