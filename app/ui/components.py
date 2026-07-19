import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# PAGE TITLE
# ==========================================================

def page_title():

    st.markdown(
        """
# 🧠 ResearchMind AI

### Industry-Grade Multi-Agent Research Paper Analysis Platform

Analyze IEEE, Springer, ACM, Elsevier and arXiv papers using an AI-powered multi-agent workflow.

---
"""
    )

    st.divider()


# ==========================================================
# SIDEBAR
# ==========================================================

def sidebar():

    with st.sidebar:

        st.header("🧠 ResearchMind AI")

        st.markdown(
            """
### Pipeline

✅ Metadata

✅ Analyzer

✅ Reviewer

✅ Summarizer

✅ Citation Extraction

✅ Insights

✅ Fact Checking

✅ Hallucination Detection

✅ Confidence Scoring

✅ Report Generation

✅ Export Reports
"""
        )

        st.divider()

        uploaded_file = st.file_uploader(
            "Choose Research Paper",
            type=["pdf"],
        )

        analyze = st.button(
            "🚀 Analyze Paper",
            use_container_width=True,
        )

        st.divider()

        st.info(
            "Upload a research paper to begin analysis."
        )

    return uploaded_file, analyze


# ==========================================================
# AGENT STATUS
# ==========================================================

def show_agent_status(agent_name):

    st.success(f"✅ {agent_name} completed")


# ==========================================================
# SCORE CARDS
# ==========================================================

def metrics(
    review_score,
    confidence,
    approved,
):

    c1, c2, c3 = st.columns(3)

    # -------------------------
    # Review Score
    # -------------------------

    if review_score >= 8:
        score_delta = "Excellent 🟢"
    elif review_score >= 7:
        score_delta = "Good 🟡"
    else:
        score_delta = "Needs Improvement 🔴"

    c1.metric(
        label="⭐ Review Score",
        value=f"{review_score:.1f}/10",
        delta=score_delta,
    )

    # -------------------------
    # Confidence
    # -------------------------

    if confidence >= 80:
        conf_delta = "High 🟢"
    elif confidence >= 60:
        conf_delta = "Medium 🟡"
    else:
        conf_delta = "Low 🔴"

    c2.metric(
        label="📊 Confidence",
        value=f"{confidence:.0f}%",
        delta=conf_delta,
    )

    # -------------------------
    # Approval
    # -------------------------

    c3.metric(
        label="✅ Approval",
        value="Approved" if approved else "Rejected",
        delta="Passed" if approved else "Failed",
    )


# ==========================================================
# METADATA
# ==========================================================

def metadata_card(metadata):

    st.subheader("📄 Paper Metadata")

    c1, c2 = st.columns(2)

    with c1:

        st.markdown(f"**Title**")
        st.write(metadata.get("title", "-"))

        st.markdown("**Authors**")
        authors = metadata.get("authors", [])
        st.write(", ".join(authors) if authors else "Not specified")

        st.markdown("**Institution**")
        st.write(metadata.get("institution", "-"))

        st.markdown("**Department**")
        st.write(metadata.get("department", "-"))

        st.markdown("**Year**")
        st.write(metadata.get("year", "-"))

    with c2:

        st.markdown("**Domain**")
        st.write(metadata.get("domain", "-"))

        st.markdown("**Venue**")
        st.write(metadata.get("venue", "-"))

        st.markdown("**DOI**")
        st.write(metadata.get("doi", "-"))

        st.markdown("**Keywords**")

        keywords = metadata.get("keywords", [])

        if keywords:
            st.write(", ".join(keywords))
        else:
            st.write("Not specified")

        st.markdown("**Emails**")

        emails = metadata.get("emails", [])

        if emails:
            st.write(", ".join(emails))
        else:
            st.write("Not specified")

    st.markdown("---")

    st.markdown("### 📑 Abstract")

    st.write(
        metadata.get(
            "abstract",
            "Not specified.",
        )
    )


# ==========================================================
# ANALYSIS
# ==========================================================

def analysis_card(analysis):

    st.subheader("🔬 Research Analysis")

    st.markdown("### 🎯 Problem Statement")
    st.write(
        analysis.get(
            "problem_statement",
            "Not specified."
        )
    )

    st.markdown("---")

    st.markdown("### ⚙ Methodology")
    st.write(
        analysis.get(
            "methodology",
            "Not specified."
        )
    )

    st.markdown("---")

    left, right = st.columns(2)

    with left:

        st.markdown("### 🧪 Experiments")
        st.write(
            analysis.get(
                "experiments",
                "Not specified."
            )
        )

        st.markdown("### 📊 Results")
        st.write(
            analysis.get(
                "results",
                "Not reported."
            )
        )

    with right:

        st.markdown("### 🗂 Datasets")

        datasets = analysis.get(
            "datasets",
            [],
        )

        if datasets:

            for dataset in datasets:

                st.write(f"• {dataset}")

        else:

            st.write("Not specified.")

        st.markdown("### ⚠ Limitations")

        st.write(
            analysis.get(
                "limitations",
                "Not specified."
            )
        )


# ==========================================================
# SUMMARY
# ==========================================================

def summary_card(summary):

    st.subheader("📝 Research Summary")

    with st.expander(
        "📄 Executive Summary",
        expanded=True,
    ):

        st.write(
            summary.get(
                "executive_summary",
                "Not available.",
            )
        )

    with st.expander(
        "🔬 Technical Summary",
        expanded=False,
    ):

        st.write(
            summary.get(
                "technical_summary",
                "Not available.",
            )
        )

    with st.expander(
        "👨‍🎓 Beginner Summary",
        expanded=False,
    ):

        st.write(
            summary.get(
                "beginner_summary",
                "Not available.",
            )
        )


# ==========================================================
# INSIGHTS
# ==========================================================

def insight_card(insights):

    st.subheader("💡 Research Insights")

    # ==========================================
    # Key Insights
    # ==========================================

    st.markdown("### 💡 Key Insights")

    key_insights = insights.get(
        "key_insights",
        [],
    )

    if key_insights:

        for i, item in enumerate(key_insights, start=1):

            st.info(f"**Insight {i}**\n\n{item}")

    else:

        st.warning("No insights generated.")

    st.divider()

    # ==========================================
    # Future Work
    # ==========================================

    st.markdown("### 🚀 Future Work")

    future = insights.get(
        "future_work",
        "Not specified in the paper.",
    )

    st.write(future)

    st.divider()

    # ==========================================
    # Applications
    # ==========================================

    st.markdown("### 🌍 Applications")

    apps = insights.get(
        "applications",
        [],
    )

    if apps:

        for app in apps:

            st.success(f"✅ {app}")

    else:

        st.warning("No applications specified.")


# ==========================================================
# REVIEW
# ==========================================================

def review_card(review):

    st.subheader("⭐ AI Review")

    score = review.get("score", 0)
    approved = review.get("approved", False)
    feedback = review.get("feedback", "No feedback available.")

    # ==========================================
    # Top Metrics
    # ==========================================

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Review Score",
            f"{score:.1f}/10",
        )

    with c2:

        if approved:

            st.success("✅ Approved")

        else:

            st.error("❌ Not Approved")

    st.divider()

    # ==========================================
    # Feedback
    # ==========================================

    st.markdown("### 📝 Reviewer Feedback")

    st.write(feedback)

    st.divider()

    # ==========================================
    # Progress Bar
    # ==========================================

    st.markdown("### 📊 Quality Score")

    st.progress(min(score / 10, 1.0))

    if score >= 8:

        st.success("Excellent quality analysis.")

    elif score >= 7:

        st.info("Good quality analysis.")

    elif score >= 5:

        st.warning("Average quality. Some improvements recommended.")

    else:

        st.error("Low quality. Significant improvements recommended.")


# ==========================================================
# FACT CHECK
# ==========================================================

def fact_check_card(fact_check):

    st.subheader("✔ Fact Verification")

    status = fact_check.get(
        "overall_status",
        "Unknown",
    )

    if status.lower() == "verified":

        st.success(f"Overall Status: {status}")

    else:

        st.warning(f"Overall Status: {status}")

    st.divider()

    # ==========================================
    # Supported Claims
    # ==========================================

    st.markdown("### ✅ Supported Claims")

    supported = fact_check.get(
        "supported_claims",
        [],
    )

    if supported:

        for claim in supported:

            st.success(claim)

    else:

        st.info("No supported claims identified.")

    st.divider()

    # ==========================================
    # Unsupported Claims
    # ==========================================

    st.markdown("### ❌ Unsupported Claims")

    unsupported = fact_check.get(
        "unsupported_claims",
        [],
    )

    if unsupported:

        for claim in unsupported:

            st.error(claim)

    else:

        st.success("No unsupported claims detected.")

    st.divider()

    # ==========================================
    # Hallucinations
    # ==========================================

    st.markdown("### 🚨 Hallucinations")

    hallucinations = fact_check.get(
        "hallucinations",
        [],
    )

    if hallucinations:

        for item in hallucinations:

            st.error(item)

    else:

        st.success("No hallucinations detected.")


# ==========================================================
# HALLUCINATION
# ==========================================================

def hallucination_card(hallucination):

    st.subheader("🚨 Hallucination Detection")

    detected = hallucination.get(
        "hallucination_detected",
        False,
    )

    severity = hallucination.get(
        "severity",
        "Unknown",
    )

    recommendation = hallucination.get(
        "recommendation",
        "No recommendation available.",
    )

    # ==========================================
    # Status
    # ==========================================

    if detected:

        st.error("🚨 Hallucinations Detected")

    else:

        st.success("✅ No Hallucinations Detected")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Severity",
            severity,
        )

    with c2:

        st.metric(
            "Detection",
            "Yes" if detected else "No",
        )

    st.divider()

    # ==========================================
    # Hallucinated Statements
    # ==========================================

    st.markdown("### 📋 Hallucinated Statements")

    hallucinations = hallucination.get(
        "hallucinations",
        [],
    )

    if hallucinations:

        for item in hallucinations:

            st.error(item)

    else:

        st.success("No hallucinated content found.")

    st.divider()

    # ==========================================
    # Recommendation
    # ==========================================

    st.markdown("### 💡 Recommendation")

    st.info(recommendation)


# ==========================================================
# CONFIDENCE
# ==========================================================

def confidence_card(confidence):

    st.subheader("📊 Confidence Analytics")

    overall = confidence.get(
        "overall_confidence",
        0,
    )

    st.metric(
        "Overall Confidence",
        f"{overall:.0f}%",
    )

    st.progress(
        min(overall / 100, 1.0)
    )

    st.divider()

    # ==========================================
    # Section Scores
    # ==========================================

    st.markdown("### 📈 Section Confidence")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Analysis",
            f"{confidence.get('analysis_confidence',0):.0f}%"
        )

        st.metric(
            "Summary",
            f"{confidence.get('summary_confidence',0):.0f}%"
        )

        st.metric(
            "Citation",
            f"{confidence.get('citation_confidence',0):.0f}%"
        )

    with c2:

        st.metric(
            "Insights",
            f"{confidence.get('insight_confidence',0):.0f}%"
        )

        st.metric(
            "Review",
            f"{confidence.get('review_confidence',0):.0f}%"
        )

    st.divider()

    # ==========================================
    # Weak Sections
    # ==========================================

    st.markdown("### ⚠ Weak Sections")

    weak = confidence.get(
        "weak_sections",
        [],
    )

    if weak:

        for section in weak:

            st.warning(section)

    else:

        st.success("No weak sections detected.")

    st.divider()

    # ==========================================
    # Recommendation
    # ==========================================

    st.markdown("### 💡 AI Recommendation")

    st.info(
        confidence.get(
            "recommendation",
            "No recommendation."
        )
    )


# ==========================================================
# REPORT
# ==========================================================

def report_card(report):

    st.subheader("📑 AI Generated Research Report")

    with st.expander(
        "📄 Open Full Report",
        expanded=True,
    ):

        st.markdown(report["markdown"])

    st.info(
        "💡 This report was automatically generated by ResearchMind AI using multiple specialized AI agents."
    )


# ==========================================================
# DOWNLOADS
# ==========================================================

def download_buttons(report):

    st.subheader("⬇ Downloads")

    c1, c2 = st.columns(2)

    with c1:

        st.download_button(
            "Markdown",
            report["markdown"],
            file_name="research_report.md",
        )

    with c2:

        st.download_button(
            "JSON",
            str(report["report_json"]),
            file_name="research_report.json",
        )


# ==========================================================
# DATAFRAME
# ==========================================================

def dataframe(data, title):

    st.subheader(title)

    if isinstance(data, list):

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True,
        )

    else:

        st.json(data)
# ==========================================================
# LIVE WORKFLOW STATUS
# ==========================================================

# ==========================================================
# LIVE WORKFLOW STATUS
# ==========================================================

def workflow_progress(completed_agents):

    st.subheader("⚙ Workflow Progress")

    pipeline = [
        "metadata",
        "analyzer",
        "reviewer",
        "summarizer",
        "citation",
        "insight",
        "fact_checker",
        "hallucination",
        "confidence",
        "report_generator",
        "exporter",
    ]

    left, right = st.columns(2)

    for i, agent in enumerate(pipeline):

        column = left if i % 2 == 0 else right

        with column:

            if agent in completed_agents:

                st.success(
                    f"✅ {agent.replace('_', ' ').title()}"
                )

            else:

                st.info(
                    f"⏳ {agent.replace('_', ' ').title()}"
                )
# ==========================================================
# ANALYSIS TIMELINE
# ==========================================================

def analysis_timeline():

    st.subheader("📌 Analysis Timeline")

    timeline = [
        "📄 PDF Uploaded",
        "🧠 Metadata Extracted",
        "🔬 Paper Analyzed",
        "⭐ Review Completed",
        "📝 Summary Generated",
        "📚 Citations Extracted",
        "💡 Insights Generated",
        "✔ Fact Checking Completed",
        "🚨 Hallucination Detection Completed",
        "📊 Confidence Calculated",
        "📑 Report Generated",
        "💾 Export Completed",
    ]

    for item in timeline:

        st.markdown(f"✅ {item}")
# ==========================================================
# ANALYTICS DASHBOARD
# ==========================================================

def analytics_dashboard(result):

    st.subheader("📈 Research Analytics")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Agents",
            len(result.completed_agents),
        )

    with c2:

        st.metric(
            "Review Score",
            f"{result.review_score:.1f}",
        )

    with c3:

        st.metric(
            "Confidence",
            f"{result.confidence.get('overall_confidence',0):.0f}%",
        )

    with c4:

        st.metric(
            "Approval",
            "Yes" if result.approved else "No",
        )
# ==========================================================
# CONFIDENCE CHART
# ==========================================================

def confidence_chart(confidence):

    scores = {
        "Analysis": confidence.get("analysis_confidence", 0),
        "Summary": confidence.get("summary_confidence", 0),
        "Citation": confidence.get("citation_confidence", 0),
        "Insights": confidence.get("insight_confidence", 0),
        "Review": confidence.get("review_confidence", 0),
    }

    fig = px.bar(
        x=list(scores.keys()),
        y=list(scores.values()),
        labels={
            "x": "Section",
            "y": "Confidence (%)",
        },
        title="Confidence by Section",
    )

    fig.update_layout(
        height=400,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )
# ==========================================================
# REVIEW STATUS CHART
# ==========================================================

def review_status_chart(review):

    approved = review.get("approved", False)

    values = [1, 0] if approved else [0, 1]

    labels = [
        "Approved",
        "Not Approved",
    ]

    fig = px.pie(
        values=values,
        names=labels,
        hole=0.65,
        title="Review Status",
    )

    fig.update_traces(
        textinfo="label+percent",
    )

    fig.update_layout(
        height=400,
        showlegend=True,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )
# ==========================================================
# AGENT PERFORMANCE DASHBOARD
# ==========================================================

def agent_performance_chart(result):

    import pandas as pd
    import plotly.express as px

    agents = [
        "Metadata",
        "Analyzer",
        "Reviewer",
        "Summarizer",
        "Citation",
        "Insight",
        "Fact Checker",
        "Hallucination",
        "Confidence",
        "Report",
        "Exporter",
    ]

    completed = result.completed_agents

    status = []

    for agent in agents:

        if agent.lower().replace(" ", "_") in completed:

            status.append(100)

        else:

            status.append(0)

    df = pd.DataFrame(
        {
            "Agent": agents,
            "Completion": status,
        }
    )

    fig = px.bar(
        df,
        x="Agent",
        y="Completion",
        text="Completion",
        title="AI Agent Execution Status",
    )

    fig.update_layout(
        height=450,
        yaxis_range=[0, 100],
    )

    fig.update_traces(
        texttemplate="%{text}%",
        textposition="outside",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )
# ==========================================================
# AI HEALTH DASHBOARD
# ==========================================================

def ai_health_chart(confidence):

    import plotly.graph_objects as go

    categories = [
        "Analysis",
        "Summary",
        "Citation",
        "Insights",
        "Review",
    ]

    values = [
        confidence.get("analysis_confidence", 0),
        confidence.get("summary_confidence", 0),
        confidence.get("citation_confidence", 0),
        confidence.get("insight_confidence", 0),
        confidence.get("review_confidence", 0),
    ]

    # Close the radar chart
    categories.append(categories[0])
    values.append(values[0])

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill="toself",
            name="AI Health",
        )
    )

    fig.update_layout(
        title="AI Health Dashboard",
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
            )
        ),
        showlegend=False,
        height=500,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )
# ==========================================================
# EXECUTIVE DASHBOARD
# ==========================================================

def executive_dashboard(result):

    st.subheader("🏆 Executive Overview")

    score = result.review_score
    confidence = result.confidence.get(
        "overall_confidence",
        0,
    )
    agents = len(result.completed_agents)
    approved = result.approved

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "🤖 Agents",
            agents,
        )

    with c2:

        st.metric(
            "⭐ Review",
            f"{score:.1f}/10",
        )

    with c3:

        st.metric(
            "📊 Confidence",
            f"{confidence:.0f}%",
        )

    with c4:

        if approved:

            st.success("✅ APPROVED")

        else:

            st.error("❌ NOT APPROVED")

    st.divider()

    if confidence >= 80:

        st.success(
            "🟢 High confidence analysis."
        )

    elif confidence >= 60:

        st.warning(
            "🟡 Medium confidence analysis."
        )

    else:

        st.error(
            "🔴 Low confidence analysis."
        )
# ==========================================================
# PAPER CHAT UI
# ==========================================================


def paper_chat():

    st.subheader("💬 Chat with this Research Paper")

    st.info(
        "Ask any question about the uploaded paper."
    )

    question = st.text_input(
        "Ask a question",
        placeholder="Example: What dataset was used?",
    )

    ask = st.button(
        "Ask AI",
        use_container_width=True,
    )

    return question, ask