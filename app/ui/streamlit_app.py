import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
import tempfile

from app.graph.state import create_initial_state
from app.graph.workflow import run_workflow
from app.services.pdf_service import pdf_service
from app.services.chat_service import chat_service
from app.services.chunk_service import chunk_service
from app.ui.styles import load_css
from app.ui.components import *


st.set_page_config(
    page_title="ResearchMind AI",
    page_icon="🧠",
    layout="wide",
)
st.markdown(
    load_css(),
    unsafe_allow_html=True,
)
# =====================================================
# HEADER
# =====================================================

page_title()

# =====================================================
# SIDEBAR
# =====================================================

uploaded_file, analyze = sidebar()

# =====================================================
# MAIN
# =====================================================

if uploaded_file and analyze:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf",
    ) as tmp:

        tmp.write(uploaded_file.read())

        pdf_path = tmp.name

    paper = pdf_service.extract_text(pdf_path)

    paper_chunks = chunk_service.split(paper)

    state = create_initial_state(
        paper_text=paper,
        pdf_path=pdf_path,
    )

    progress = st.progress(0)

    status = st.empty()

    steps = [
        ("Metadata", 10),
        ("Analyzer", 20),
        ("Reviewer", 30),
        ("Summarizer", 40),
        ("Citation", 50),
        ("Insights", 60),
        ("Fact Checker", 70),
        ("Hallucination", 80),
        ("Confidence", 90),
        ("Report", 95),
        ("Export", 100),
    ]

    for name, percent in steps:

        status.info(f"⚙ Preparing {name}...")

        progress.progress(percent)

    result = run_workflow(state)

    progress.progress(100)

    status.success("✅ Analysis Completed Successfully!")

    left, right = st.columns([2, 1])

    with left:

        workflow_progress(result.completed_agents)

    with right:

        analysis_timeline()

    report = result.final_report

    st.divider()

    # =====================================================
    # METRICS
    # =====================================================

    executive_dashboard(result)

    st.divider()

    analytics_dashboard(result)

    st.divider()

    agent_performance_chart(result)
    # =====================================================
    # REPORT
    # =====================================================

    tabs = st.tabs(
[
    "📄 Metadata",
    "🔬 Analysis",
    "📝 Summary",
    "💡 Insights",
    "⭐ Review",
    "✔ Fact Check",
    "🚨 Hallucination",
    "📊 Confidence",
    "📑 Report",
    "💬 Chat",
]
)

    with tabs[0]:
        metadata_card(result.metadata)

    with tabs[1]:
        analysis_card(result.analysis)

    with tabs[2]:
        summary_card(result.summary)

    with tabs[3]:
        insight_card(result.insights)

    with tabs[4]:

        review_card(result.review)

        st.divider()

        review_status_chart(result.review)

    with tabs[5]:
        fact_check_card(result.fact_check)

    with tabs[6]:
        hallucination_card(result.hallucination)

    with tabs[7]:

        confidence_card(result.confidence)

        st.divider()
        confidence_chart(result.confidence)
        st.divider()
        ai_health_chart(result.confidence)

    with tabs[8]:
        report_card(report)

    with tabs[9]:

        question, ask = paper_chat()

        if ask:

            if question.strip():

                with st.spinner("🤖 Thinking..."):

                    answer = chat_service.ask(
                        paper,
                        question,
                    )

                st.success("Answer")

                st.write(answer)

            else:

                st.warning(
                    "Please enter a question."
                )

    # =====================================================
    # DOWNLOADS
    # =====================================================

    download_buttons(report)

else:

    st.info(
        "Upload a research paper and click Analyze."
    )