Here is a clear, professional, and well-structured rewritten version of your requirements, keeping everything intact but expressed more formally and clearly:

---

I am planning to build a **static dashboard using Python**, which will be deployed using **GitHub and Streamlit**. The entire dashboard will be driven strictly by the **Excel file that I upload**, and no external or dynamic data sources will be used.

### **Dashboard Structure and Requirements**

#### **1. Data Source**

* The Excel file contains **five sheets**, which include:

  * Financial statements of the company
  * Forensic accounting and financial analysis data
* All visualizations and calculations must strictly use data from these sheets.
* Sheet names and structure must be used exactly as they appear in the Excel file.

---

### **2. Dashboard Layout**

The dashboard should be divided into **two main horizontal sections**:

---

## **A. Upper Section – Financial Statement Analysis**

### **1. Company Selection**

* A dropdown selector to choose a specific company.
* All visuals update based on the selected company.

### **2. Company Snapshot (Left Panel)**

This section should include:

* A line graph showing:

  * Revenue
  * Profit
  * Cash Flow from Operations (CFO)
* The **X-axis must represent years (2014–2025)**.
* The **Y-axis should represent financial values**.

### **3. DuPont Analysis (Right Panel)**

* Display the **DuPont Analysis table** exactly as given in the Financial Statement Analysis sheet.
* The table should be shown for the selected company without altering its structure.

---

### **4. Efficiency Analysis (Below Company Snapshot)**

* Graphs showing:

  * Days Sales Outstanding (DSO)
  * Days Payable Outstanding (DPO)
  * Days Inventory Outstanding (DIO)
  * Cash Conversion Cycle (CCC)
* Years should be on the horizontal axis.
* Data should be sourced from the Financial Statement Analysis sheet.

---

### **5. Liquidity Analysis (Right of Efficiency Section)**

* Graphs for:

  * Working Capital Ratio (WCR)
  * Cash Ratio
* Again, years must be on the horizontal axis.

---

## **B. Lower Section – Forensic Accounting Analysis**

### **1. Forensic Indicators Visualization**

Display bar charts for:

* M-Score
* F-Score
* Z-Score
* Accruals

(All values should be taken directly from the respective company sheets.)

### **2. Final Forensic Verdict**

* Provide a concise analytical conclusion based on:

  * Accrual behavior
  * Earnings manipulation indicators
  * Financial distress signals
* The verdict should clearly state the financial quality and risk level of the company.

---

### **Additional Requirements**

* The dashboard must be **static** (no real-time or API-based data).
* Use **Python + Streamlit** only.
* Provide a `requirements.txt` file listing all necessary libraries.
* Follow clean layout principles with readable charts and proper spacing.
* Apply thoughtful visual design to improve clarity and interpretation.

---

If you want, I can next help you with:

* Folder structure for the project
* Complete Streamlit code
* `requirements.txt` file
* Recommended chart types and color themes

Just tell me what you want next.
