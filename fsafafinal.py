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
# Ensure this matches your exact filename
FILE_PATH = "FSAFAWAIExcel.xlsx"

@st.cache_data
def load_data():
    try:
        xls = pd.ExcelFile(FILE_PATH)
        data = {}
        for sheet in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet)
            data[sheet] = df
        return data
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

data = load_data()

if data:
    company_sheets = list(data.keys())[:5]   # First 5 sheets = companies

    # --------------------------------------------------
    # TITLE
    # --------------------------------------------------
    st.title("📊 Financial and Forensic Analysis Dashboard")

    # --------------------------------------------------
    # FORENSIC ANALYSIS (ACCRUALS)
    # --------------------------------------------------
    st.header("🔍 Forensic Accounting Analysis")
    st.subheader("Accrual Trend (2014-2025)")

    fig1, ax1 = plt.subplots(figsize=(10, 5))
    for company in company_sheets:
        df = data[company]
        label_col = df.columns[0]
        # Find row containing 'accrual'
        accrual_row = df[df[label_col].astype(str).str.contains("accrual", case=False, na=False)]
        
        if not accrual_row.empty:
            year_cols = [c for c in df.columns[1:] if "Unnamed" not in str(c)]
            y_values = pd.to_numeric(accrual_row[year_cols].iloc[0], errors='coerce')
            ax1.plot(year_cols, y_values, marker="o", label=company)

    ax1.set_xlabel("Year")
    ax1.set_ylabel("Accruals")
    plt.xticks(rotation=45) # Prevents X-axis overlap
    ax1.legend()
    st.pyplot(fig1)

    # --------------------------------------------------
    # SEPARATE FORENSIC SCORES
    # --------------------------------------------------
    st.subheader("Forensic Score Breakdowns")
    score_tabs = st.tabs(["M-Score", "Z-Score", "F-Score"])
    score_names = ["M Score", "Z Score", "F Score"]

    for i, tab in enumerate(score_tabs):
        with tab:
            fig, ax = plt.subplots(figsize=(10, 4))
            target_score = score_names[i]
            for company in company_sheets:
                df = data[company]
                label_col = df.columns[0]
                # Match exact score name
                row = df[df[label_col].astype(str).str.strip() == target_score]
                if not row.empty:
                    year_cols = [c for c in df.columns[1:] if "Unnamed" not in str(c)]
                    y_values = pd.to_numeric(row[year_cols].iloc[0], errors='coerce')
                    ax.plot(year_cols, y_values, marker="o", label=company)
            
            ax.set_title(f"{target_score} Comparison")
            ax.set_ylabel("Score Value")
            plt.xticks(rotation=45)
            ax.legend()
            st.pyplot(fig)

    # --------------------------------------------------
    # FINANCIAL PERFORMANCE
    # --------------------------------------------------
    st.header("📈 Financial Performance Analysis")

    col_rev, col_prof = st.columns(2)

    with col_rev:
        st.subheader("Revenue Trend")
        fig3, ax3 = plt.subplots(figsize=(8, 5))
        for company in company_sheets:
            df = data[company]
            label_col = df.columns[0]
            revenue = df[df[label_col].astype(str).str.contains("revenue|sales", case=False, na=False)]
            if not revenue.empty:
                year_cols = [c for c in df.columns[1:] if "Unnamed" not in str(c)]
                y_values = pd.to_numeric(revenue[year_cols].iloc[0], errors='coerce')
                ax3.plot(year_cols, y_values, marker="o", label=company)
        plt.xticks(rotation=45)
        ax3.legend()
        st.pyplot(fig3)

    with col_prof:
        st.subheader("Profit Trend")
        fig4, ax4 = plt.subplots(figsize=(8, 5))
        for company in company_sheets:
            df = data[company]
            label_col = df.columns[0]
            profit = df[df[label_col].astype(str).str.contains("profit", case=False, na=False)]
            if not profit.empty:
                year_cols = [c for c in df.columns[1:] if "Unnamed" not in str(c)]
                y_values = pd.to_numeric(profit[year_cols].iloc[0], errors='coerce')
                ax4.plot(year_cols, y_values, marker="o", label=company)
        plt.xticks(rotation=45)
        ax4.legend()
        st.pyplot(fig4)

    # --------------------------------------------------
    # USER INTERPRETATION
    # --------------------------------------------------
    st.header("📝 Analyst Interpretation")
    st.text_area("Write your analysis, observations, and conclusions here:", height=200)

else:
    st.error("Please ensure the Excel file is named correctly and uploaded.")
