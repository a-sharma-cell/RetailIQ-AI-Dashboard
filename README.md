# RetailIQ: AI-Powered Retail Sales Intelligence Dashboard

> An end-to-end analytics solution that transforms raw retail transaction data into actionable business intelligence — combining a structured data pipeline, an executive dashboard, and a conversational AI layer for self-serve insight generation.

---

## Executive Summary

RetailIQ analyzes four years (2015–2018) of retail transaction data (~10,000 orders) to surface profitability drivers, regional performance gaps, and discount-related margin erosion. The project delivers three things a stakeholder actually needs: a clean, trustworthy data foundation; a visual dashboard for at-a-glance monitoring; and a natural-language interface so non-technical users can interrogate the data without writing a query.

---

## 1. Problem Statement

Retail organizations routinely collect granular transactional data — orders, discounts, regional sales, customer-level profitability — but this data rarely reaches decision-makers in a usable form. It typically sits in raw exports, requires SQL or BI fluency to interpret, and creates a dependency on analysts for even basic questions ("which region is underperforming?", "are our discounts profitable?"). This bottleneck slows down operational decisions and limits data access to a technical few.

## 2. Business Objective

Design and deliver a self-service retail analytics solution that:

- Establishes a **reliable, query-ready data layer** from messy source data
- Surfaces **key performance indicators and trends** through an interactive dashboard
- Enables **natural-language querying** so any stakeholder — regardless of technical background — can ask business questions and receive immediate, data-grounded answers

## 3. Methodology

The project follows a standard analytics engineering pipeline, with each stage designed to be auditable and reproducible.

### 3.1 Data Acquisition & Cleaning
The source export contained 10,800 rows, of which 806 were corrupted — the result of an unrelated dataset being inadvertently appended during a prior export (evidenced by non-numeric values in identifier fields). These were programmatically identified and removed, yielding a clean base of **9,994 verified transaction records**.

Critically, **1,871 orders (18.7% of the dataset) carry negative profit**. Rather than treating this as a data quality issue, these records were deliberately retained — they represent a legitimate business signal indicating margin erosion, most likely tied to discounting behavior (analyzed further below).

Data types were standardized (dates parsed, numeric fields cast appropriately), and column names normalized to `snake_case` for downstream consistency.

### 3.2 Data Storage
The cleaned dataset was loaded into **MySQL**, establishing a structured, queryable single source of truth in place of flat-file analysis — the standard pattern for production-grade reporting.

### 3.3 Business Intelligence Layer
An interactive **Power BI** dashboard was built on top of the cleaned data, featuring:
- KPI cards (Total Sales, Total Profit, Total Orders, Average Discount)
- Regional sales comparison (bar chart)
- Monthly sales trend analysis (line chart)
- Category and sub-category sales composition (treemap)
- Top 10 customers by profitability (ranked table)
- Interactive slicers (Region, Year, Category) for ad-hoc filtering

### 3.4 Conversational Analytics Layer
To remove the technical barrier to data access, the dataset was connected to **Google's Gemini model via PandasAI**, allowing plain-English queries to be translated into data operations in real time. This was wrapped in a lightweight **Streamlit** application with a free-text query box and a curated set of sample questions for quick demonstration.

---

## 4. Tools & Technology Stack

| Layer | Technology |
|---|---|
| Data Cleaning & Transformation | Python, Pandas |
| Data Storage | MySQL |
| Business Intelligence | Power BI |
| Natural Language Querying | PandasAI, Google Gemini (via LiteLLM) |
| Application Layer | Streamlit |
| Version Control | Git, GitHub |

---

## 5. Key Findings

| Finding | Detail |
|---|---|
| **Top-performing region** | West generated the highest profit (~$108,418), outperforming East, Central, and South |
| **Leading category by revenue** | Technology recorded the highest total sales (~$836,154), ahead of Office Supplies and Furniture |
| **Margin risk concentration** | Furniture carries an average discount of ~17.4% — the highest among major categories |
| **Profitability leakage** | 18.7% of all orders were unprofitable, a pattern concentrated in heavily discounted categories |

## 6. Business Recommendations

1. **Review discount policy in Furniture and other high-discount categories.** The correlation between elevated discounting and unprofitable orders suggests current promotional thresholds may be eroding margin without proportional volume gains.
2. **Replicate West region's commercial strategy** in underperforming regions — its profit lead likely reflects pricing discipline, product mix, or operational efficiencies worth codifying and transferring.
3. **Leverage Technology's revenue strength for cross-category bundling**, using its demand pull to lift attachment rates in lower-performing categories.
4. **Institute a discount-to-profit guardrail** in future pricing decisions, flagging orders where discount depth historically correlates with negative margin.

---

## 7. Deliverables

- **Power BI Dashboard:** Included in this repository as `retail dashboard.pbix` — open in Power BI Desktop to explore.
- **Streamlit AI Assistant:** Runs locally via `streamlit run app.py` (see setup instructions below).

---

## 8. Repository Structure

RetailIQ-AI-Dashboard/

├── app.py                  # Streamlit application (conversational AI interface)

├── clean_data.py           # Data cleaning and transformation pipeline

├── load_to_mysql.py        # MySQL database loading script

├── superstore_cleaned.csv  # Cleaned, analysis-ready dataset

├── retail dashboard.pbix   # Power BI dashboard

├── requirements.txt        # Python dependencies

└── README.md

## 9. Reproducing This Project

```bash
# 1. Clone the repository
git clone https://github.com/a-sharma-cell/RetailIQ-AI-Dashboard.git
cd RetailIQ-AI-Dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
# Create a .env file in the root directory:
# GEMINI_API_KEY=your_api_key_here

# 4. Run the data pipeline
python clean_data.py
python load_to_mysql.py

# 5. Launch the application
streamlit run app.py
```

---

## Author

**Atharva Sharma**
