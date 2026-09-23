from app.rag.retriever import retrieve_documents_with_scores


TEST_CASES = [
    {
        "question": "What is an AI agent?",
        "expected_keyword": "AI agent",
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
]


def evaluate_retrieval():
    total = len(TEST_CASES)
    passed = 0

    print("\nRAG Retrieval Evaluation")
    print("========================")

    for index, test_case in enumerate(
        TEST_CASES,
        start=1,
    ):
        question = test_case["question"]
        expected_keyword = test_case["expected_keyword"]

        results = retrieve_documents_with_scores(
            question,
            k=3,
            score_threshold=1.0,
        )

        retrieved_text = " ".join(
            document.page_content
            for document, _ in results
        )

        success = (
            expected_keyword.lower()
            in retrieved_text.lower()
        )

        if success:
            passed += 1
            status = "PASS"
        else:
            status = "FAIL"

        print(f"\nTest {index}: {status}")
        print(f"Question: {question}")
        print(f"Expected keyword: {expected_keyword}")
        print(f"Results returned: {len(results)}")

    accuracy = (
        passed / total * 100
        if total > 0
        else 0
    )

    print("\n========================")
    print(f"Passed: {passed}/{total}")
    print(f"Retrieval Accuracy: {accuracy:.2f}%")


if __name__ == "__main__":
    evaluate_retrieval()