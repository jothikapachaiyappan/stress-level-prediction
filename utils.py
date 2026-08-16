import streamlit as st


# ==========================================
# GLOBAL PREMIUM CSS
# ==========================================

def load_css():

    st.markdown("""
    <style>

    /* =========================================
       MAIN APP
       ========================================= */

    .stApp {
        background: linear-gradient(
            135deg,
            #081229 0%,
            #0f172a 40%,
            #111827 100%
        );
        color: white;
    }


    /* =========================================
       SIDEBAR
       ========================================= */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #111827,
            #1e293b
        );
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }


    /* =========================================
       TITLES
       ========================================= */

    h1 {
        color: white !important;
        font-weight: 700 !important;
        letter-spacing: 1px;
    }

    h2,
    h3 {
        color: #e2e8f0 !important;
    }


    /* =========================================
       HOME PAGE - 4 METRIC CARDS
       ========================================= */

    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.18) !important;
        border-radius: 18px !important;
        padding: 18px !important;
        box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.25);
    }

    div[data-testid="stMetricLabel"] {
        color: #ffffff !important;
        font-size: 17px !important;
        font-weight: 700 !important;
        letter-spacing: 0.3px !important;
    }

    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 32px !important;
        font-weight: 800 !important;
        text-shadow: 0px 2px 5px rgba(0, 0, 0, 0.8);
    }

    div[data-testid="stMetricDelta"] {
        color: #ffffff !important;
        font-size: 15px !important;
        font-weight: 600 !important;
    }


    /* =========================================
       INPUT LABELS
       Height, Weight, Anxiety, Meditation,
       Smoking, Alcohol, Heart Rate, etc.
       ========================================= */

    .stSelectbox label,
    .stNumberInput label,
    .stSlider label,
    .stTextInput label,
    .stTextArea label {

        color: #ffffff !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        letter-spacing: 0.4px !important;

        text-shadow:
            0px 2px 3px rgba(0, 0, 0, 0.8);
    }


    /* =========================================
       INPUT TEXT
       ========================================= */

    .stNumberInput input,
    .stTextInput input,
    .stTextArea textarea {
        font-size: 16px !important;
    }


    /* =========================================
       BUTTONS
       ========================================= */

    .stButton > button {

        width: 100%;
        border: none;
        border-radius: 14px;
        padding: 14px;

        font-weight: 600;
        color: white !important;

        background: linear-gradient(
            135deg,
            #2563eb,
            #7c3aed
        );

        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: scale(1.02);

        box-shadow:
            0px 8px 25px rgba(
                59,
                130,
                246,
                0.45
            );
    }


    /* =========================================
       DATAFRAME
       ========================================= */

    .stDataFrame {
        border-radius: 20px;
        overflow: hidden;
    }


    /* =========================================
       INPUT CONTAINERS
       ========================================= */

    .stSelectbox,
    .stNumberInput,
    .stSlider,
    .stTextInput,
    .stTextArea {
        border-radius: 12px;
    }


    /* =========================================
       ALERT / SUCCESS
       ========================================= */

    div[data-testid="stAlert"] {
        border-radius: 15px;
    }


    /* =========================================
       EXPANDER
       ========================================= */

    .streamlit-expanderHeader {
        font-size: 18px;
        font-weight: 600;
        color: white !important;
    }


    /* =========================================
       GENERAL TEXT
       ========================================= */

    .stMarkdown,
    .stText,
    p,
    li {
        color: #ffffff;
    }


    /* =========================================
       SCROLLBAR
       ========================================= */

    ::-webkit-scrollbar {
        width: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background: #3b82f6;
        border-radius: 10px;
    }


    /* =========================================
       HORIZONTAL LINE
       ========================================= */

    hr {
        border: 1px solid rgba(
            255,
            255,
            255,
            0.08
        );
    }

    </style>
    """, unsafe_allow_html=True)


# ==========================================
# HERO BANNER
# ==========================================

def hero_banner():

    st.markdown("""
    <div style="
        padding: 35px;
        border-radius: 25px;
        background: linear-gradient(
            135deg,
            #2563eb,
            #7c3aed
        );
        text-align: center;
        color: white;
        margin-bottom: 20px;
    ">

        <h1>
            🧠 Stress Level Detection Using Machine Learning
        </h1>

        <h4>
            Predict • Analyze • Prevent Stress
        </h4>

    </div>
    """, unsafe_allow_html=True)


# ==========================================
# KPI CARDS
# ==========================================

def kpi_cards():

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📄 Dataset Records",
        "100K+"
    )

    c2.metric(
        "📊 Features",
        "20"
    )

    c3.metric(
        "🎯 Accuracy",
        "95%"
    )

    c4.metric(
        "⚙ Modules",
        "4"
    )


# ==========================================
# PROJECT FEATURES
# ==========================================

def feature_section():

    st.subheader(
        "🚀 Key Features"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
### 📊 Dataset Insights

Interactive visual analytics and trend analysis.
""")

        st.info("""
### 🤖 Stress Prediction

Predict stress levels instantly.
""")

    with col2:

        st.info("""
### ⚠ Risk Analysis

Identify major stress factors.
""")

        st.info("""
### 📈 Recommendations

AI powered wellness suggestions.
""")


# ==========================================
# NAVIGATION
# ==========================================

def navigation_buttons():

    st.subheader(
        "🔗 Quick Navigation"
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        if st.button(
            "📊 Dataset Insights"
        ):

            st.switch_page(
                "pages/2_Dataset_Insights.py"
            )

    with c2:

        if st.button(
            "🤖 Stress Prediction"
        ):

            st.switch_page(
                "pages/3_Stress_Prediction.py"
            )

    with c3:

        if st.button(
            "ℹ About Project"
        ):

            st.switch_page(
                "pages/4_About_Project.py"
            )


# ==========================================
# FOOTER
# ==========================================

def footer():

    st.divider()

    st.markdown("""
    <center>

        <span style="
            color: #cbd5e1;
            font-size: 15px;
        ">

            Developed with ❤️ using
            Python • Streamlit • Machine Learning

        </span>

    </center>
    """, unsafe_allow_html=True)
