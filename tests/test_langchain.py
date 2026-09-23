import langchain
import langgraph


def test_packages():
    assert langchain.__version__
    assert langgraph.__version__