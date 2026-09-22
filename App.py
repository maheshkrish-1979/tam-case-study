import streamlit as st
import pandas as pd
import duckdb
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & STYLING
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Acceldata Case Study | TAM Interview Presentation",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Executive Deck Aesthetics
st.markdown("""
<style>
    .main-title {
        font-size: 28px;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 15px;
        color: #475569;
        margin-bottom: 25px;
    }
    .slide-card {
        background-color: #F8FAFC;
        border-left: 5px solid #0284C7;
        padding: 18px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .slide-header {
        font-size: 20px;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 10px;
    }
    .highlight-box {
        background-color: #EFF6FF;
        border: 1px solid #BFDBFE;
        padding: 15px;
        border-radius: 8px;
        color: #1E40AF;
        font-weight: 500;
    }
    .talking-point-title {
        font-weight: 700;
        color: #0F172A;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
st.sidebar.image("https://img.icons8.com/color/96/shield.png", width=55)
st.sidebar.title("Navigation Deck")

app_mode = st.sidebar.radio(
    "Select Deck Page / Module:",
    [
        "📌 Executive Summary & CTO Challenge",
        "🔮 Q1: Where is the Industry Heading?",
        "⚖️ Q2: Why Data Observability over AI Scripts?",
        "🔄 Q3: How Observability Evolves with AI Agents",
        "🧪 Live Demo Sandbox (Streamlit Interactive App)",
        "🏗️ Architecture & Buy vs Build Matrix"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Interview Details")
st.sidebar.text("Candidate: Mahesh")
st.sidebar.text("Role: Technical Account Manager")
st.sidebar.text("Panel: Ashok, Lokesh, Shash")

# -----------------------------------------------------------------------------
# PAGE 1: EXECUTIVE SUMMARY & CTO CHALLENGE
# -----------------------------------------------------------------------------
if app_mode == "📌 Executive Summary & CTO Challenge":
    st.markdown('<p class="main-title">🛡️ Data Observability in the Age of AI</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Executive Thesis & Strategic Counter-Positioning for Acceldata Case Study</p>', unsafe_allow_html=True)
    
    col_cto, col_thesis = st.columns(2)
    
    with col_cto:
        st.markdown("""
        <div class="slide-card">
            <div class="slide-header">❓ The CTO Challenge Statement</div>
            <p style="font-style: italic; color: #334155;">
            "My engineers can use AI (Claude/Cursor) to build monitoring for our data pipelines in a day. We already have logs, metrics, and cloud monitoring. Why should I pay for a Data Observability platform?"
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🎯 Core Objections Decoded")
        st.markdown("""
        * **Perceived Cost:** Writing validation code with LLMs feels "free."
        * **Telemetry Confusion:** Conflating infrastructure uptime (CloudWatch/Datadog logs) with **data truth and semantic quality**.
        * **Short-Term Bias:** Focusing on Day 1 creation speed instead of Day 2 maintenance debt.
        """)

    with col_thesis:
        st.markdown("""
        <div class="slide-card" style="border-left-color: #059669;">
            <div class="slide-header">💡 Our Strategic Counter-Thesis</div>
            <p style="color: #065F46; font-weight: 500;">
            "AI assistants make building scripts trivial, but exponentially compound management debt at enterprise scale. Building a check takes 10 minutes; maintaining 10,000 fragmented custom checks across multi-cloud environments turns engineering teams into maintenance vendors."
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🗣️ Presenter Talking Points")
        st.markdown("""
        1. **Script Proliferation vs. Platform Governance:** Point scripts lead to fragmented alert fatigue, zero cross-system lineage, and unmonitored blind spots.
        2. **Multidimensional Correlation:** Isolated logs cannot correlate Data Quality + Schema Drift + Compute Cost + Lineage in a single pane.
        3. **Opportunity Cost:** Engineers should build customer-facing business logic, not maintain in-house pipeline monitoring software.
        """)

    st.markdown("---")
    st.subheader("Visual Framework: Day 1 Creation Speed vs. Day 2 Scale")
    
    # Visual Chart: Day 1 vs Day 2 Overhead
    df_cost = pd.DataFrame({
        "Pipelines Monitored": [10, 50, 100, 500, 1000],
        "Custom AI Scripts Maintenance ($/yr)": [5000, 35000, 120000, 650000, 1400000],
        "Enterprise Observability Platform ($/yr)": [20000, 45000, 70000, 150000, 250000]
    })
    fig_cost = px.line(
        df_cost, x="Pipelines Monitored", 
        y=["Custom AI Scripts Maintenance ($/yr)", "Enterprise Observability Platform ($/yr)"],
        markers=True, title="TCO Shift: Script Maintenance Debt at Enterprise Scale",
        labels={"value": "Total Cost of Ownership ($)", "variable": "Approach"}
    )
    st.plotly_chart(fig_cost, use_container_width=True)

# -----------------------------------------------------------------------------
# PAGE 2: Q1 - WHERE IS THE INDUSTRY HEADING?
# -----------------------------------------------------------------------------
elif app_mode == "🔮 Q1: Where is the Industry Heading?":
    st.markdown('<p class="main-title">🔮 Question 1: Industry Trajectory (12–24 Months)</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">How AI & AI Agents are Changing Enterprise Data Infrastructure Reliability</p>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="slide-card">
            <div class="slide-header">1. Agentic Pipelines</div>
            <p>From static, human-written ETL to dynamic, autonomous agent loops that generate queries, transform schemas, and execute workflows in real time.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        st.markdown("""
        <div class="slide-card">
            <div class="slide-header">2. Silent Corruptions</div>
            <p>Failures shift from hard crashes (500 errors) to non-deterministic silent failures: hallucinated data, semantic drift, and infinite query retry loops.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="slide-card">
            <div class="slide-header">3. Strict Reliability SLAs</div>
            <p>RAG pipelines, LLM fine-tuning, and operational AI agents require 100% trustworthy data. Bad data directly triggers flawed autonomous business actions.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Shift in Pipeline Failure Modes")
    
    # Comparison Bar Chart
    df_failures = pd.DataFrame({
        "Failure Mode Category": ["Pipeline Hard Crash", "Schema Drift", "Data Hallucination / Semantic Drift", "Compute Cost Spikes"],
        "Traditional ETL Era (%)": [70, 20, 5, 5],
        "Agentic AI Era (%)": [15, 30, 35, 20]
    })
    fig_fail = px.bar(
        df_failures, x="Failure Mode Category", y=["Traditional ETL Era (%)", "Agentic AI Era (%)"],
        barmode="group", title="Evolution of Pipeline Reliability Risk Profiles"
    )
    st.plotly_chart(fig_fail, use_container_width=True)

    st.markdown("### 🗣️ Speaker Script & Key Points")
    st.markdown("""
    * *"Historically, data pipelines were deterministic—a job succeeded or failed with a clear error code. In the age of AI agents, pipelines are probabilistic."*
    * *"Agents dynamically alter schemas and fill missing values with plausible-looking hallucinations. Traditional logs show `200 OK`, but the data is garbage."*
    * *"Observability must transition from post-mortem debugging to proactive continuous validation before data enters AI context windows."*
    """)

# -----------------------------------------------------------------------------
# PAGE 3: Q2 - WHY DATA OBSERVABILITY OVER AI SCRIPTS?
# -----------------------------------------------------------------------------
elif app_mode == "⚖️ Q2: Why Data Observability over AI Scripts?":
    st.markdown('<p class="main-title">⚖️ Question 2: Custom AI Scripts vs. Dedicated Platform</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Where Enterprise Data Observability Platforms Provide Differentiated & Enduring Value</p>', unsafe_allow_html=True)

    st.subheader("Multidimensional Correlation Matrix")
    st.write("Point-solution AI scripts evaluate isolated variables. Enterprise platforms correlate all four operational pillars simultaneously.")

    # 4 Pillars Grid
    p1, p2, p3, p4 = st.columns(4)
    p1.metric("1. Data Quality", "Accuracy & Completeness", "Anomalies")
    p2.metric("2. Schema & Lineage", "End-to-End Mapping", "Drift Tracking")
    p3.metric("3. Pipeline Performance", "Latency & SLA Durations", "Bottlenecks")
    p4.metric("4. Compute & Cost", "Warehouse Consumption", "Spike Detection")

    st.markdown("---")
    col_comp1, col_comp2 = st.columns(2)

    with col_comp1:
        st.markdown("### 🤖 The Custom AI Script Blindspots")
        st.error("❌ **No Cross-System Lineage:** A script running on Databricks cannot trace upstream Kafka or downstream Snowflake dependencies.")
        st.error("❌ **Compute Insensibility:** Data quality scripts don't monitor query retry cost spikes in cloud warehouses.")
        st.error("❌ **Governance Void:** Lacks centralized RBAC, SOC2 compliance, audit logging, and team-wide alert routing.")

    with col_comp2:
        st.markdown("### 🌐 The Acceldata Platform Advantage")
        st.success("🟢 **Out-of-the-Box Connectors:** Zero-code integration across Databricks, Snowflake, Kafka, and Hadoop.")
        st.success("🟢 **Automated ML Baselines:** Automatically learns data distributions without manual threshold coding.")
        st.success("🟢 **Unified Telemetry:** Links data volume drops directly to underlying compute cost spikes and job delays.")

# -----------------------------------------------------------------------------
# PAGE 4: Q3 - HOW OBSERVABILITY EVOLVES WITH AI AGENTS
# -----------------------------------------------------------------------------
elif app_mode == "🔄 Q3: How Observability Evolves with AI Agents":
    st.markdown('<p class="main-title">🔄 Question 3: The Evolution of Observability in the Agentic Era</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">When AI Agents become both Consumers and Operators of Enterprise Data</p>', unsafe_allow_html=True)

    col_cons, col_oper = st.columns(2)

    with col_cons:
        st.markdown("""
        <div class="slide-card">
            <div class="slide-header">📥 Agents as Consumers</div>
            <p>Observability acts as the <b>Trust & Safety Guardrail</b> before raw data enters an LLM context window or RAG vector database.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        * **Pre-Execution Sanity Checks:** Prevents agent hallucinations by blocking corrupted context inputs.
        * **Semantic Drift Detection:** Ensures vector embeddings reflect true enterprise data semantics over time.
        * **Data Privacy Guardrails:** Prevents PII or sensitive columns from leaking into agent prompt contexts.
        """)

    with col_oper:
        st.markdown("""
        <div class="slide-card" style="border-left-color: #8B5CF6;">
            <div class="slide-header">⚙️ Agents as Operators</div>
            <p>Observability platforms evolve from passive alerting dashboards into <b>Closed-Loop API Control Planes</b> for self-healing infrastructure.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        * **Automated Remediation APIs:** Observability platforms trigger API callbacks so AI agents can quarantine bad records.
        * **Self-Healing Pipelines:** Agents read observability anomaly payloads to dynamically rewrite broken SQL queries or reroute jobs.
        * **Autonomic Cost Throttling:** Agents automatically terminate rogue query loops based on real-time cost alerts.
        """)

    st.markdown("---")
    st.subheader("Closed-Loop Agentic Observability Workflow")
    
    # Diagram simulation
    st.info("🔄 **Raw Data Lakehouse** ➔ 🛡️ **Acceldata Observability Gate** ➔ 🚨 **Anomaly Payload API** ➔ 🤖 **AI Repair Agent** ➔ ⚡ **Self-Healed Pipeline**")

# -----------------------------------------------------------------------------
# PAGE 5: LIVE DEMO SANDBOX
# -----------------------------------------------------------------------------
elif app_mode == "🧪 Live Demo Sandbox (Streamlit Interactive App)":
    # (Embedded database engine and interactive scenario sandbox)
    @st.cache_resource
    def get_db():
        conn = duckdb.connect(database=':memory:', read_only=False)
        conn.execute("""
            CREATE TABLE silver_transactions (
                tx_id INTEGER,
                customer_id VARCHAR,
                amount DOUBLE,
                status VARCHAR,
                processing_cost_usd DOUBLE,
                tx_time TIMESTAMP
            );
            INSERT INTO silver_transactions VALUES
                (101, 'CUST_1001', 450.00, 'COMPLETED', 0.12, '2026-09-22 10:00:00'),
                (102, 'CUST_1002', 1250.50, 'COMPLETED', 0.15, '2026-09-22 10:05:00'),
                (103, 'CUST_1003', 85.20, 'COMPLETED', 0.10, '2026-09-22 10:10:00'),
                (104, 'CUST_1004', 310.00, 'PENDING', 0.11, '2026-09-22 10:15:00');
        """)
        return conn

    conn = get_db()

    st.markdown('<p class="main-title">🧪 Interactive Sandbox: Custom AI Scripts vs. Acceldata</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Simulating Data Quality, Schema Drift, and Compute Cost Anomaly Scenarios Live</p>', unsafe_allow_html=True)

    # Scenario Selector
    scenario = st.selectbox(
        "Select Pipeline Scenario to Inject:",
        [
            "🟢 Baseline (Normal Operational Flow)",
            "🔴 Agent Failure 1: Schema Drift & Data Corruption",
            "🟡 Agent Failure 2: Query Retry Loop (Compute Cost Spike)"
        ]
    )

    # Dynamic KPI Metrics
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    if scenario == "🟢 Baseline (Normal Operational Flow)":
        col_m1.metric("Pipeline Health", "HEALTHY", "100% Up")
        col_m2.metric("Data Quality Score", "99.8%", "0.0%")
        col_m3.metric("Compute Overhead", "$0.48 / run", "Optimal")
        col_m4.metric("Active Alerts", "0 Active", "None")
    elif scenario == "🔴 Agent Failure 1: Schema Drift & Data Corruption":
        col_m1.metric("Pipeline Health", "CRITICAL", "-40% Drift", delta_color="inverse")
        col_m2.metric("Data Quality Score", "42.1%", "-57.7%", delta_color="inverse")
        col_m3.metric("Compute Overhead", "$0.52 / run", "Normal")
        col_m4.metric("Active Alerts", "2 Alerts", "Schema + Quality", delta_color="inverse")
    else:
        col_m1.metric("Pipeline Health", "DEGRADED", "Cost Spike", delta_color="off")
        col_m2.metric("Data Quality Score", "98.5%", "-1.3%", delta_color="normal")
        col_m3.metric("Compute Overhead", "$18.40 / run", "+3,733%", delta_color="inverse")
        col_m4.metric("Active Alerts", "1 Alert", "Compute Loop", delta_color="inverse")

    st.markdown("---")

    # Data Table Rendering
    if scenario == "🟢 Baseline (Normal Operational Flow)":
        df = conn.execute("SELECT * FROM silver_transactions").df()
    elif scenario == "🔴 Agent Failure 1: Schema Drift & Data Corruption":
        df = pd.DataFrame({
            "tx_id": [101, 102, 103, 104],
            "client_guid": ["CUST_1001", "CUST_1002", "CUST_1003", "CUST_1004"],
            "amount": [450.00, -9999.00, 85.20, 310.00],
            "status": ["COMPLETED", "COMPLETED", "COMPLETED", "PENDING"],
            "processing_cost_usd": [0.12, 0.15, 0.10, 0.11]
        })
    else:
        df = pd.DataFrame({
            "tx_id": [101, 102, 103, 104],
            "customer_id": ["CUST_1001", "CUST_1002", "CUST_1003", "CUST_1004"],
            "amount": [450.00, 1250.50, 85.20, 310.00],
            "status": ["COMPLETED", "COMPLETED", "COMPLETED", "PENDING"],
            "processing_cost_usd": [0.12, 18.40, 0.10, 0.11]
        })

    tab_data, tab_chart = st.tabs(["📋 Ingested Lakehouse Data", "📊 Telemetry Trends"])
    with tab_data:
        st.dataframe(df, use_container_width=True)
    with tab_chart:
        fig = px.bar(
            df, x="tx_id", y="amount", color="processing_cost_usd",
            title="Transaction Value vs Processing Cost Breakdown",
            color_continuous_scale="Reds" if scenario != "🟢 Baseline (Normal Operational Flow)" else "Viridis"
        )
        st.plotly_chart(fig, use_container_width=True)

    # Comparative Engine
    col_left, col_right = st.columns(2)
    with col_left:
        st.markdown("### 🤖 Custom AI Script (Claude/Cursor)")
        if scenario == "🟢 Baseline (Normal Operational Flow)":
            st.success("✅ **PASSED**: All basic unit assertions executed successfully.")
        elif scenario == "🔴 Agent Failure 1: Schema Drift & Data Corruption":
            st.error("❌ **SCRIPT CRASHED**: `KeyError: 'customer_id' not found`. Upstream field rename broke downstream script.")
        else:
            st.warning("⚠️ **FALSE POSITIVE**: Script checked row values but was completely blind to the $18.40 compute cost spike!")

    with col_right:
        st.markdown("### 🌐 Enterprise Observability Platform (Acceldata)")
        if scenario == "🟢 Baseline (Normal Operational Flow)":
            st.success("🟢 **PLATFORM HEALTH: 100%**: Zero anomalies detected across compute, data, and schema layers.")
        elif scenario == "🔴 Agent Failure 1: Schema Drift & Data Corruption":
            st.error("🔴 **SCHEMA DRIFT DETECTED**: `customer_id` auto-mapped to `client_guid`. Downstream lineage preserved.")
            st.error("🔴 **DATA ANOMALY DETECTED**: Value `-9999.00` quarantined.")
        else:
            st.error("🚨 **COMPUTE SPIKE DETECTED**: Warehouse query execution loop flagged (+3,733% cost variance).")

# -----------------------------------------------------------------------------
# PAGE 6: ARCHITECTURE & BUY VS BUILD MATRIX
# -----------------------------------------------------------------------------
elif app_mode == "🏗️ Architecture & Buy vs Build Matrix":
    st.markdown('<p class="main-title">🏗️ Architectural Evaluation: Buy vs. Build Decision</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Where Custom AI Scripts Work vs. Where They Break Down at Enterprise Scale</p>', unsafe_allow_html=True)

    st.subheader("1. Scale Breakdown Breakdown Curve")
    st.markdown("""
    * **1-5 Pipelines (Startup Phase):** Custom AI scripts built via Cursor work great. Low complexity, single team.
    * **5-50 Pipelines (Growth Phase):** Maintenance burden starts competing with feature delivery. Schema drift breaks weekly.
    * **50+ Pipelines (Enterprise Scale):** Custom scripts completely break down. Siloed context, zero unified lineage, alert fatigue, and massive engineering overhead.
    """)

    st.markdown("---")
    st.subheader("2. Enterprise Buy vs. Build Evaluation Matrix")

    st.markdown("""
    | Evaluation Criteria | Custom-Built AI Scripts | Enterprise Data Observability Platform |
    | :--- | :--- | :--- |
    | **Time to First Alert** | ⚡ Fast (10 mins) | 🔌 Fast (Pre-built Delta/Snowflake Connectors) |
    | **Ongoing Maintenance** | ❌ High ($O(N)$ ongoing script updates) | 🟢 Zero (Automated baseline ML profiling) |
    | **Cross-System Lineage** | ❌ Non-existent | 🟢 Column-level lineage across multi-cloud |
    | **Compute & Cost Linkage**| ❌ Isolated in CloudWatch/Datadog logs | 🟢 Correlated directly to pipeline runs & quality |
    | **Security & RBAC** | ❌ Hardcoded in repository scripts | 🟢 Centralized Enterprise Access & Audit Logging |
    | **SLA Management** | ❌ Basic threshold checks | 🟢 Business-level SLA tracking & alerting |
    """)

    st.markdown("---")
    st.subheader("3. Executive Closing Pitch")
    st.markdown("""
    <div class="highlight-box">
    "Paying for an Enterprise Data Observability platform isn't about paying for checks your engineers <i>could</i> write. It is about buying zero-maintenance coverage, enterprise-wide lineage, multidimensional cost correlation, and freeing your talent to build core product features."
    </div>
    """, unsafe_allow_html=True)