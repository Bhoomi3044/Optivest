# Optivest
Optivest is an end-to-end, data-driven platform that helps retail investors optimize their portfolios and receive personalized investment recommendations. The system combines historical market data, statistical risk analysis, Markowitz Modern Portfolio Theory (MPT) optimization, and risk prediction models to generate actionable suggestions and visual insights.

🔍 Key Features

Portfolio Management: Create and manage portfolios, add / update asset holdings, track current allocations and returns.

Data Ingestion: Fetch and store historical market data (CSV / API support).

Portfolio Optimization: Compute optimal weights using MPT (maximize Sharpe, minimize variance).

Risk Prediction & Analysis: Compute portfolio-level risk metrics (std dev, VaR, maximum drawdown) and classify portfolios (Low / Medium / High risk).

Recommendations: Suggest rebalancing actions and candidate assets based on user risk profile and optimization results.

Visualizations: Interactive charts for efficient frontier, allocation pie, performance over time, and risk dashboards.

Security & Authentication: Secure user registration and login (hashed passwords, session tokens).

Tested & Documented: Unit tests for core components and a full project report included in docs/.

📁 Repository Structure
Optivest-Portfolio-Optimization-System/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── src/
│   ├── authentication.py          # registration/login (sqlite or mock DB)
│   ├── database.py                # DB helpers (sqlite wrapper)
│   ├── data_fetch.py              # yfinance / CSV ingestion helpers
│   ├── optimization.py            # uses PyPortfolioOpt or cvxpy
│   ├── risk_prediction.py         # risk metrics, VaR, max drawdown, classification
│   ├── portfolio_management.py    # CRUD for portfolios and holdings
│   └── visualization.py           # plotting helpers for charts (matplotlib/plotly)
│
├── data/
│   ├── sample_portfolio.csv
│   └── sample_market_data.csv
│
├── docs/
│   ├── Optivest Report.pdf        # Full project report (uploaded)
│   ├── FlowGraph.png
│   ├── DFD_Level0.png
│   ├── DFD_Level1.png
│   ├── DFD_Level2.png
│   ├── ER_Diagram.png
│   ├── GanttChart.png
│   ├── TestCases.docx
│   └── Cyclomatic_Complexity.png
│
├── tests/
│   ├── test_authentication.py
│   ├── test_risk_prediction.py
│   └── test_portfolio_management.py
│
└── examples/
    ├── run_local_demo.sh
    └── demo_notebook.ipynb


Note: The full 51-page project report you uploaded is included in docs/ as Optivest Report.pdf. If you want the exact local file as included when you worked with me, it is available at:
/mnt/data/Optivest Report edited.pdf
(When you upload to GitHub, move the file into docs/ and rename to Optivest Report.pdf for clarity.)

🧰 Tech Stack & Dependencies

Language & Frameworks

Python 3.9+

Optional web UI: Flask or Streamlit

Main libraries

pandas, numpy — data processing

yfinance or alpha_vantage — market data (configurable)

matplotlib, plotly — visualizations

PyPortfolioOpt or cvxpy — portfolio optimization

scipy — numerical routines

bcrypt — password hashing

sqlite3 — local database (built-in)

pytest — unit tests

requirements.txt (example)

pandas
numpy
matplotlib
plotly
yfinance
PyPortfolioOpt
cvxpy
scipy
bcrypt
pytest
openpyxl
flask        # optional (remove if using streamlit)
streamlit    # optional

🚀 Quick Start (Local Development)

Clone the repo

git clone https://github.com/<your-username>/Optivest-Portfolio-Optimization-System.git
cd Optivest-Portfolio-Optimization-System


Create & activate a virtual environment

python -m venv venv
# Windows (CMD)
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate


Install dependencies

pip install -r requirements.txt
# or individually
pip install pandas numpy matplotlib yfinance PyPortfolioOpt bcrypt pytest


Run the demo or unit tests

Run demo script / notebook:

python src/data_fetch.py          # quick check data fetch
python src/risk_prediction.py     # run sample risk calculation
streamlit run examples/demo_notebook.ipynb  # or use Jupyter


Run tests:

pytest tests/

🔧 How Modules Work (short descriptions)

authentication.py — registration and login. Uses bcrypt for hashing and stores users in SQLite. Example functions:

register_user(username, email, password)

authenticate_user(username, password)

data_fetch.py — fetch historical adjusted close prices from Yahoo via yfinance. Also supports reading local CSVs.

optimization.py — builds expected returns and covariance and calls EfficientFrontier to compute optimal weights (max Sharpe / min variance).

risk_prediction.py — computes portfolio-level std_dev, VaR (historical and parametric), max_drawdown, and classification (Low/Medium/High).

visualization.py — functions to plot efficient frontier, allocation pie, time-series returns, and risk heatmaps.

✅ Testing & Coverage

Unit tests are stored under tests/ and use pytest.

Example tests provided:

test_risk_prediction.py — validates risk calculations on synthetic data

test_authentication.py — registration/login flow using temporary DB

🧾 Report & Documentation

The full project report (design, DFDs, ER diagram, data dictionaries, FP/effort, gantt, and all artifacts) is included in docs/.
Local path to the uploaded report:
/mnt/data/Optivest Report edited.pdf — move to docs/Optivest Report.pdf before pushing to GitHub.

🔐 Security & Privacy Notes

Never commit real API keys, credentials, or user data to GitHub. Use .env or GitHub secrets for production.

For demo and development, use mock or sample data stored in data/.

All passwords must be hashed using bcrypt before storage; session tokens should be time-limited.

📦 Deployment Notes

For a small web UI, Streamlit allows instant deployment: streamlit run src/visualization.py

For production web deployment, containerize the app with Docker and host on Heroku / AWS Elastic Beanstalk / DigitalOcean.

🧩 Contribution & License

This repository uses the MIT License (see LICENSE file). Contributions are welcome — fork the repo, create a branch, and open a pull request.
