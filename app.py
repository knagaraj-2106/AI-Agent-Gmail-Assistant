"""
app.py

Streamlit interface for AI Gmail Assistant.

Features:
- Gmail account information
- Unread email count
- Recent emails quick action
- Latest email summarization
- Natural-language Gmail assistant
- LangGraph agent
- Conversation memory
- New conversation support
"""

import uuid

import streamlit as st
from langchain_core.messages import HumanMessage

from agents.graph import graph
from services.gmail_service import GmailService


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Gmail Assistant",
    page_icon="📧",
    layout="wide",
)


# =========================================================
# SESSION STATE
# =========================================================

# ---------------------------------------------------------
# Conversation Thread ID
# ---------------------------------------------------------

if "thread_id" not in st.session_state:

    st.session_state.thread_id = str(
        uuid.uuid4()
    )


# ---------------------------------------------------------
# Chat Messages
# ---------------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# ---------------------------------------------------------
# Quick Prompt
# ---------------------------------------------------------

if "quick_prompt" not in st.session_state:

    st.session_state.quick_prompt = None


# =========================================================
# GMAIL SERVICE
# =========================================================

gmail = GmailService()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("📧 Gmail Account")

    # -----------------------------------------------------
    # Gmail Connection
    # -----------------------------------------------------

    try:

        profile = gmail.get_profile()

        st.success("Connected")

        st.write("**Email:**")

        st.write(
            profile["emailAddress"]
        )

        st.divider()

        # -------------------------------------------------
        # Gmail Statistics
        # -------------------------------------------------

        st.subheader("📊 Gmail Statistics")

        st.metric(
            "Unread Emails",
            gmail.get_unread_count()
        )

        st.metric(
            "Total Emails",
            profile["messagesTotal"]
        )

        st.metric(
            "Threads",
            profile["threadsTotal"]
        )

        st.divider()

        # -------------------------------------------------
        # Quick Actions
        # -------------------------------------------------

        st.subheader("⚡ Quick Actions")

        if st.button(
            "📬 Unread Count",
            use_container_width=True
        ):

            st.session_state.quick_prompt = (
                "How many unread emails do I have?"
            )

        if st.button(
            "📩 Recent Emails",
            use_container_width=True
        ):

            st.session_state.quick_prompt = (
                "Show my latest 5 emails."
            )

        if st.button(
            "📝 Summarize Latest",
            use_container_width=True
        ):

            st.session_state.quick_prompt = (
                "Summarize my latest email."
            )

        if st.button(
            "🔎 Search Emails",
            use_container_width=True
        ):

            st.session_state.quick_prompt = (
                "Show me my latest emails from Google."
            )

        if st.button(
            "⚡ Find Action Items",
            use_container_width=True
        ):

            st.session_state.quick_prompt = (
                "Find important action items from my recent emails."
            )

        if st.button(
            "📅 Find Deadlines",
            use_container_width=True
        ):

            st.session_state.quick_prompt = (
                "Find upcoming deadlines and meetings in my emails."
            )

        st.divider()

        # -------------------------------------------------
        # New Conversation
        # -------------------------------------------------

        st.subheader("💬 Conversation")

        if st.button(
            "🆕 New Conversation",
            use_container_width=True
        ):

            # Create a completely new thread ID
            st.session_state.thread_id = str(
                uuid.uuid4()
            )

            # Clear visible chat history
            st.session_state.messages = []

            # Clear pending quick prompt
            st.session_state.quick_prompt = None

            # Refresh Streamlit
            st.rerun()

        st.divider()

        # -------------------------------------------------
        # Current Thread
        # -------------------------------------------------

        st.caption(
            "Current Conversation ID"
        )

        st.code(
            st.session_state.thread_id,
            language="text"
        )

    except Exception as e:

        st.error(
            "Unable to connect to Gmail"
        )

        st.write(
            str(e)
        )


# =========================================================
# MAIN TITLE
# =========================================================

st.title("📧 AI Gmail Assistant")

st.write(
    "Ask anything about your Gmail inbox using natural language."
)


# =========================================================
# DISPLAY CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# =========================================================
# CHAT INPUT
# =========================================================

prompt = st.chat_input(
    "Ask about your emails..."
)


# =========================================================
# QUICK ACTION PROMPT
# =========================================================

if (
    prompt is None
    and st.session_state.quick_prompt
):

    prompt = st.session_state.quick_prompt

    st.session_state.quick_prompt = None


# =========================================================
# PROCESS USER REQUEST
# =========================================================

if prompt:

    # -----------------------------------------------------
    # Store User Message
    # -----------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    # -----------------------------------------------------
    # Display User Message
    # -----------------------------------------------------

    with st.chat_message("user"):

        st.markdown(
            prompt
        )

    # -----------------------------------------------------
    # LangGraph Configuration
    # -----------------------------------------------------

    config = {
        "configurable": {
            "thread_id": st.session_state.thread_id
        }
    }

    # -----------------------------------------------------
    # Execute LangGraph
    # -----------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "🤔 Checking your Gmail..."
        ):

            try:

                result = graph.invoke(
                    {
                        "messages": [
                            HumanMessage(
                                content=prompt
                            )
                        ]
                    },
                    config=config
                )

                # -----------------------------------------
                # Get Messages From LangGraph
                # -----------------------------------------

                messages = result.get(
                    "messages",
                    []
                )

                # -----------------------------------------
                # Get Final Response
                # -----------------------------------------

                if messages:

                    final_message = messages[-1]

                    response = (
                        final_message.content
                    )

                else:

                    response = (
                        "I couldn't generate a response."
                    )

                # -----------------------------------------
                # Handle Empty Response
                # -----------------------------------------

                if not response:

                    response = (
                        "I couldn't generate a response "
                        "from the Gmail assistant."
                    )

            except Exception as e:

                response = (
                    "Sorry, I encountered an error "
                    "while processing your request."
                )

                st.error(
                    str(e)
                )

        # -------------------------------------------------
        # Display Assistant Response
        # -------------------------------------------------

        st.markdown(
            response
        )

    # -----------------------------------------------------
    # Store Assistant Response
    # -----------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )