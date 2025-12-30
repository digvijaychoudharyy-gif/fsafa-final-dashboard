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

# Function to extract data by looking at the first column (Metric/Year)
def get_clean_data(df, keyword):
    if df is None or df.empty:
        return None, None
    
    # Identify the first column regardless of its name
    label_col = df.columns[0]
    
    # Find row where label contains the keyword
    mask = df[label_col].astype(str).str.contains(keyword, case=False, na=False)
    row = df[mask]
    
    if row.empty:
        return None, None
    
    # Get columns that represent years (skipping the label column)
    valid_cols = [c for c in df.columns[1:] if "Unnamed" not in str(c)]
    
    # Convert years to strings and values to numeric
    years = [str(c) for c in valid_cols]
    values = pd.to_numeric(row[valid_cols].iloc[0], errors='coerce')
    
    return years, values

if data:
    company_sheets = list(data.keys())[:5]
    
    st.title("Financial and Forensic Analysis Dashboard")

    # --------------------------------------------------
    # FORENSIC ANALYSIS SECTION
    # --------------------------------------------------
    st.header("Forensic Accounting Analysis")
    
    # Accrual Trend
    st.subheader("Accrual Trend (2014-2025)")
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    for company in company_sheets:
        x, y = get_clean_data(data[company], "Accrual")
        if y is not None:
            ax1.plot(x, y, marker="o", label=company)
    
    plt.xticks(rotation=45)
    ax1.set_ylabel("Value")
    ax1.legend()
    st.pyplot(fig1)

    # Separate Score Graphs in Tabs
    st.subheader("Forensic Score Comparison")
    tab1, tab2, tab3 = st.tabs(["M-Score", "Z-Score", "F-Score"])
    
    with tab1:
        figM, axM = plt.subplots(figsize=(10, 4))
        for company in company_sheets:
            x, y = get_clean_data(data[company], "M Score")
            if y is not None:
                axM.plot(x, y, marker="o", label=company)
        plt.xticks(rotation=45)
        axM.set_title("Beneish M-Score (2014-2025)")
        axM.legend()
        st.pyplot(figM)

    with tab2:
        figZ, axZ = plt.subplots(figsize=(10, 4))
        for company in company_sheets:
            x, y = get_clean_data(data[company], "Z Score")
            if y is not None:
                axZ.plot(x, y, marker="o", label=company)
        plt.xticks(rotation=45)
        axZ.set_title("Altman Z-Score (2014-2025)")
        axZ.legend()
        st.pyplot(figZ)

    with tab3:
        figF, axF = plt.subplots(figsize=(10, 4))
        for company in company_sheets:
            x, y = get_clean_data(data[company], "F Score")
            if y is not None:
                axF.plot(x, y, marker="o", label=company)
        plt.xticks(rotation=45)
        axF.set_title("Piotroski F-Score (2014-2025)")
        axF.legend()
        st.pyplot(figF)

    # --------------------------------------------------
    # FINANCIAL PERFORMANCE SECTION
    # --------------------------------------------------
    st.header("Financial Performance Analysis")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Revenue Trend")
        fig_rev, ax_rev = plt.subplots(figsize=(8, 5))
        for company in company_sheets:
            x, y = get_clean_data(data[company], "Sales")
            if y is not None:
                ax_rev.plot(x, y, marker="o", label=company)
        plt.xticks(rotation=45)
        ax_rev.legend()
        st.pyplot(fig_rev)

    with col2:
        st.subheader("Net Profit Trend")
        fig_prof, ax_prof = plt.subplots(figsize=(8, 5))
        for company in company_sheets:
            x, y = get_clean_data(data[company], "Net Profit")
            if y is not None:
                ax_prof.plot(x, y, marker="o", label=company)
        plt.xticks(rotation=45)
        ax_prof.legend()
        st.pyplot(fig_prof)

    # --------------------------------------------------
    # USER INTERPRETATION
    # --------------------------------------------------
    st.header("Analyst Interpretation")
    st.text_area(
        label="Enter findings below:",
        value="Write your analysis and conclusions here.",
        height=200
    )

else:
    st.error("Excel file not found. Ensure 'FSAFA WAI Excel.xlsx' is in the app folder.")
