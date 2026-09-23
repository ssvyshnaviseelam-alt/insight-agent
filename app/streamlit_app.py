import requests
import streamlit as st
from app.utils.logger import get_logger


# --------------------------------------------------
# Configuration
# --------------------------------------------------

API_URL = "http://127.0.0.1:8000/chat"
logger = get_logger("InsightAgent.Streamlit")
def get_tool_label(tool_used: str) -> str:
    labels = {
        "search_knowledge_base": "📚 Knowledge Base",
        "web_search": "🌐 Web Search",
        "calculate": "🧮 Calculator",
        "mcp": "🔌 MCP",
        "direct": "🤖 Direct Answer",
    }

    return labels.get(
        tool_used,
        "🤖 InsightAgent",
    )

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="InsightAgent",
    page_icon="🤖",
    layout="centered",
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🤖 InsightAgent")
st.caption("Agentic AI Research & Knowledge Assistant")


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("⚙️ Session Settings")

    user_id = st.text_input(
        "User ID",
        value="user1",
        key="user_id",
    )

    session_id = st.text_input(
        "Session ID",
        value="session1",
        key="session_id",
    )

    st.divider()

    if st.button(
        "🧹 Clear Chat",
        use_container_width=True,
    ):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.subheader("🛠️ Capabilities")

    st.markdown(
        """
        📚 **Knowledge Base**  
        Search internal AI knowledge.

        🌐 **Web Search**  
        Search current information.

        🧮 **Calculator**  
        Perform calculations.

        🔌 **MCP**  
        Access project-specific tools.

        🧠 **LangGraph Agent**  
        Automatically chooses the appropriate action.
        """
    )

    st.divider()

    st.caption(
        f"User: `{user_id}`"
    )

    st.caption(
        f"Session: `{session_id}`"
    )


# --------------------------------------------------
# Initialize Chat History
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# Welcome Message
# --------------------------------------------------

if not st.session_state.messages:

    st.info(
        "👋 Welcome to InsightAgent! "
        "Ask a question to get started."
    )


# --------------------------------------------------
# Display Chat History
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        
        if message["role"] == "assistant":

            tool_used = message.get(
                "tool_used",
                "unknown",
            )

            tool_label = get_tool_label(
                tool_used
            )

            st.caption(
                f"Used: {tool_label}"
            )

            st.markdown(
                message["content"]
            )

            sources = message.get(
                "sources",
                []
            )

            if tool_used == "search_knowledge_base" and sources:

                st.markdown("### 📚 Sources")

                for source in sources:
                    st.markdown(
                        f"- {source}"
                    )

        else:
            st.markdown(
                message["content"]
            )


# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "Ask InsightAgent a question..."
)


# --------------------------------------------------
# Process Question
# --------------------------------------------------

if question:
 
    logger.info(
        "User question submitted | "
        f"user={user_id} | "
        f"session={session_id}"
    )
    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(question)

    # Generate assistant response
    with st.chat_message("assistant"):

        with st.spinner(
            "🤔 InsightAgent is thinking..."
        ):

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "question": question,
                        "user_id": user_id,
                        "session_id": session_id,
                    },
                    timeout=120,
                )

                if response.status_code == 200:

                    data = response.json()
                    logger.info(
                        "API response received | "
                        f"user={user_id} | "
                        f"session={session_id}"
                    )

                    answer = data.get(
                        "answer",
                        "No answer returned.",
                    )

                    tool_used = data.get(
                        "tool_used",
                        "unknown",
                    )

                    sources = data.get(
                        "sources",
                        [],
                    )

                    tool_label = get_tool_label(tool_used)

                    st.caption(
                        f"Used: {tool_label}"
                    )

                    st.markdown(answer)

                    if tool_used == "search_knowledge_base" and sources:

                        st.markdown("### 📚 Sources")

                        for source in sources:
                            st.markdown(
                                f"- {source}"
                            )

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer,
                            "tool_used": tool_used,
                            "sources": sources,
                        }
                    )
                else:

                    st.error(
                        f"API Error: {response.status_code}"
                    )

                    st.code(
                        response.text
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Unable to connect to FastAPI. "
                    "Please make sure the API server is running."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "⏱️ The request timed out. "
                    "Please try again."
                )

            except Exception as e:

                st.error(
                    f"❌ Unexpected error: {str(e)}"
                )