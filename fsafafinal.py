import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="Financial & Forensic Dashboard", layout="wide")

# --------------------------------------------------
# LOAD EXCEL FILE
# --------------------------------------------------
FILE_PATH = "FSAFAWAIExcel_Final.xlsx"

@st.cache_data
def load_data():
    try:
        xls = pd.ExcelFile(FILE_PATH)
        data = {sheet: pd.read_excel(xls, sheet_name=sheet) for sheet in xls.sheet_names}
        return data
    except Exception as e:
        st.error(f"Error loading Excel file: {e}")
        return None

data = load_data()

# --------------------------------------------------
# HELPER FUNCTION
# --------------------------------------------------
def get_clean_data(df, keyword):
    if df is None or df.empty:
        return None, None

    label_col = df.columns[0]
    mask = df[label_col].astype(str).str.contains(keyword, case=False, na=False)
    row = df[mask]

    if row.empty:
        return None, None

    year_cols = [c for c in df.columns[1:] if "Unnamed" not in str(c)]
    values = pd.to_numeric(row[year_cols].iloc[0], errors="coerce")

    return year_cols, values


# --------------------------------------------------
# MAIN DASHBOARD
# --------------------------------------------------
if data:

    company_sheets = list(data.keys())
    st.title("📊 Financial & Forensic Analysis Dashboard")

    # --------------------------------------------------
    # FORENSIC ANALYSIS
    # --------------------------------------------------
    st.header("Forensic Accounting Analysis")

    st.subheader("Accrual Trend (2014–2025)")
    fig1, ax1 = plt.subplots(figsize=(10, 4))

    for company in company_sheets:
        x, y = get_clean_data(data[company], "Accrual")
        if y is not None:
            ax1.plot(x, y, marker="o", label=company)

    ax1.set_ylabel("Accrual Value")
    ax1.legend()
    st.pyplot(fig1)

    # ---------------------------
    # SCORE TABS
    # ---------------------------
    st.subheader("Forensic Score Comparison")
    tab1, tab2, tab3 = st.tabs(["M-Score", "Z-Score", "F-Score"])

    with tab1:
        fig, ax = plt.subplots(figsize=(10, 4))
        for company in company_sheets:
            x, y = get_clean_data(data[company], "M Score")
            if y is not None:
                ax.plot(x, y, marker="o", label=company)
        ax.set_title("Beneish M-Score")
        ax.legend()
        st.pyplot(fig)

    with tab2:
        fig, ax = plt.subplots(figsize=(10, 4))
        for company in company_sheets:
            x, y = get_clean_data(data[company], "Z Score")
            if y is not None:
                ax.plot(x, y, marker="o", label=company)
        ax.set_title("Altman Z-Score")
        ax.legend()
        st.pyplot(fig)

    with tab3:
        fig, ax = plt.subplots(figsize=(10, 4))
        for company in company_sheets:
            x, y = get_clean_data(data[company], "F Score")
            if y is not None:
                ax.plot(x, y, marker="o", label=company)
        ax.set_title("Piotroski F-Score")
        ax.legend()
        st.pyplot(fig)

    # --------------------------------------------------
    # FINANCIAL PERFORMANCE
    # --------------------------------------------------
    st.header("Financial Performance Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Revenue Trend")
        fig, ax = plt.subplots(figsize=(8, 5))
        for company in company_sheets:
            x, y = get_clean_data(data[company], "Revenue")
            if y is not None:
                ax.plot(x, y, marker="o", label=company)
        ax.legend()
        st.pyplot(fig)

    with col2:
        st.subheader("Net Profit Trend")
        fig, ax = plt.subplots(figsize=(8, 5))
        for company in company_sheets:
            x, y = get_clean_data(data[company], "Net Profit")
            if y is not None:
                ax.plot(x, y, marker="o", label=company)
        ax.legend()
        st.pyplot(fig)

    # --------------------------------------------------
    # FINAL INTERPRETATION
    # --------------------------------------------------
    st.header("Analyst Interpretation")

    st.text_area(
        "Enter your qualitative analysis and conclusions:",
        value="Based on forensic indicators and financial trends, the company shows the following performance characteristics...",
        height=200
    )

else:
    st.error("Excel file not found. Please ensure 'FSAFAWAIExcel_Final.xlsx' is in the project folder.")
