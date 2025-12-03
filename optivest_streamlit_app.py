import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------
# PAGE SETTINGS
# -------------------------------------
st.set_page_config(
    page_title="OptiVest - Easy Portfolio Optimizer",
    page_icon="📈",
    layout="wide"
)

st.title("📈 OptiVest – Simple Portfolio Optimization for Retail Investors")
st.write("""
Welcome to **OptiVest** – a simple and friendly tool that helps you build a smart investment portfolio.
You can upload your stock price data OR use sample data.  
Everything is explained in **very simple language**, so even a beginner can understand!
""")

# -------------------------------------
# SAMPLE DATA
# -------------------------------------
def load_sample_data():
    dates = pd.date_range("2023-01-01", periods=300)
    np.random.seed(42)

    data = pd.DataFrame({
        "AAPL": np.cumprod(1 + np.random.normal(0.0005, 0.02, 300)),
        "MSFT": np.cumprod(1 + np.random.normal(0.0004, 0.018, 300)),
        "GOOG": np.cumprod(1 + np.random.normal(0.0006, 0.022, 300)),
        "AMZN": np.cumprod(1 + np.random.normal(0.0003, 0.019, 300)),
    }, index=dates)

    return data

# -------------------------------------
# FILE UPLOAD SECTION
# -------------------------------------
st.sidebar.header("📂 Upload Your Stock Prices")
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, index_col=0)
    df.index = pd.to_datetime(df.index)
    st.success("Custom dataset uploaded successfully!")
else:
    st.info("Using sample stock data because no file was uploaded.")
    df = load_sample_data()

# Show data preview
st.subheader("📊 Stock Price Data Preview")
st.dataframe(df.head())

# -------------------------------------
# CALCULATE DAILY RETURNS
# -------------------------------------
returns = df.pct_change().dropna()

st.subheader("📉 Daily Returns")
st.write("These are the percentage changes in price every day.")
st.dataframe(returns.head())

# -------------------------------------
# PORTFOLIO OPTIMIZATION
# -------------------------------------
st.header("🎯 Portfolio Optimization Made Simple")

st.write("""
We try different combinations of weights for the stocks.  
Then we pick the portfolio with:

- **Highest Return**
- **Lowest Risk**
- **Best Risk–Return Balance (Sharpe Ratio)**  
""")

num_portfolios = 5000
results = np.zeros((3, num_portfolios))
weights_record = []

for i in range(num_portfolios):
    weights = np.random.random(len(df.columns))
    weights /= np.sum(weights)
    weights_record.append(weights)

    portfolio_return = np.sum(returns.mean() * weights) * 252
    portfolio_vol = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    sharpe = portfolio_return / portfolio_vol

    results[0, i] = portfolio_vol
    results[1, i] = portfolio_return
    results[2, i] = sharpe

results_df = pd.DataFrame(results.T, columns=["Risk", "Return", "Sharpe"])

# Best portfolios
best_sharpe_idx = results_df["Sharpe"].idxmax()
lowest_risk_idx = results_df["Risk"].idxmin()

best_sharpe_weights = weights_record[best_sharpe_idx]
lowest_risk_weights = weights_record[lowest_risk_idx]

# -------------------------------------
# SHOW RESULTS
# -------------------------------------
st.subheader("🏆 Best Portfolios")

col1, col2 = st.columns(2)

with col1:
    st.write("### ⭐ Best Risk–Return Portfolio (Highest Sharpe Ratio)")
    st.write("This portfolio gives the **best balance** of return and safety.")
    st.write(pd.DataFrame(best_sharpe_weights, index=df.columns, columns=["Weight"]))

with col2:
    st.write("### 🛡️ Safest Portfolio (Lowest Risk)")
    st.write("This portfolio focuses on **minimum volatility** (least ups & downs).")
    st.write(pd.DataFrame(lowest_risk_weights, index=df.columns, columns=["Weight"]))

# -------------------------------------
# PLOT
# -------------------------------------
st.subheader("📈 Risk vs. Return Chart")

fig, ax = plt.subplots(figsize=(10, 5))
scatter = ax.scatter(results_df["Risk"], results_df["Return"], alpha=0.3)

ax.scatter(
    results_df.loc[best_sharpe_idx, "Risk"],
    results_df.loc[best_sharpe_idx, "Return"],
    s=200
)

ax.set_xlabel("Risk (Volatility)")
ax.set_ylabel("Expected Return")
ax.set_title("Efficient Frontier – Risk vs Return")

st.pyplot(fig)

# -------------------------------------
# RECOMMENDATION ENGINE
# -------------------------------------
st.header("💡 Investment Recommendation (Simple Language)")

risk_choice = st.selectbox(
    "What type of investor are you?",
    ["Very Safe", "Moderate", "Aggressive"]
)

if risk_choice == "Very Safe":
    st.success("🛡️ Recommended: **Lowest Risk Portfolio** (More stable, less return)")
    rec_weights = lowest_risk_weights
elif risk_choice == "Moderate":
    st.info("⚖️ Recommended: **Mix of Low Risk + Sharpe Portfolio**")
    rec_weights = (lowest_risk_weights + best_sharpe_weights) / 2
else:
    st.warning("🔥 Recommended: **Highest Sharpe Ratio Portfolio** (Higher return, higher risk)")
    rec_weights = best_sharpe_weights

st.write("### Your Suggested Weights")
st.dataframe(pd.DataFrame(rec_weights, index=df.columns, columns=["Weight"]))

st.write("""
### 📘 Explanation (Easy Language)

- **Return** = How much profit you may earn  
- **Risk** = How much the price goes up and down  
- **Sharpe Ratio** = How much return you get *for the amount of risk*  
- **Efficient Frontier** = Best possible portfolios at different risk levels  
""")

