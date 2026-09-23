from app.rag.rag_pipeline import ask_rag


TEST_CASES = [
    {
        "question": "What is an AI agent?",
        "expected_keyword": "agent",
    },
    {
        "question": "What is retrieval-augmented generation?",
        "expected_keyword": "retrieval",
    },
    {
        "question": "What is an embedding?",
        "expected_keyword": "embedding",
    },
    {
        "question": "What is LangGraph?",
        "expected_keyword": "LangGraph",
    },
    {
        "question": "What is MCP?",
        "expected_keyword": "MCP",
    },
       {
        "question": "What is the capital of France?",
        "expected_keyword": "I don't have enough information",
    },
]


def evaluate_answers():
    total = len(TEST_CASES)
    passed = 0

    print("\nRAG Answer Quality Evaluation")
    print("============================")

    for index, test_case in enumerate(
        TEST_CASES,
        start=1,
    ):
        question = test_case["question"]
        expected_keyword = test_case["expected_keyword"]

        result = ask_rag(
            question,
            k=3,
            score_threshold=1.0,
        )

        answer = result["answer"]

        success = (
            expected_keyword.lower()
            in answer.lower()
        )

        if success:
            passed += 1
            status = "PASS"
        else:
            status = "FAIL"

        print(f"\nTest {index}: {status}")
        print(f"Question: {question}")
        print(f"Expected keyword: {expected_keyword}")
        print(f"Answer: {answer}")

    accuracy = (
        passed / total * 100
        if total > 0
        else 0
    )

    print("\n============================")
    print(f"Passed: {passed}/{total}")
    print(f"Answer Quality: {accuracy:.2f}%")


if __name__ == "__main__":
    evaluate_answers()