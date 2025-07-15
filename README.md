#  Crypto Token Clustering & CAPM Classification

## Overview

This repository presents a complete pipeline to **analyze, classify, and cluster top crypto tokens** using **market-neutral financial modeling techniques**. The goal is to support:

-  Tactical Asset Allocation
-  Index Construction (Market & Sector)
-  Shortable, Liquid Token Screening
-  Production-ready Clustering Data for Quant Strategies

By leveraging return-based models, statistical clustering, and CAPM regressions, we categorize tokens into groups based on their alpha, beta, and idiosyncratic risk. We also account for **rank-based statistical distances** like **Spearman's rho** to handle crypto market outliers.

> Future extensions include integrating sentiment signals (e.g. StockTwits) for tactical allocation overlays.

---

##  Repository Structure

```
crypto-token-clustering/
├── data/
│   ├── top40_price_data/              # Raw CSVs for each token (OHLC prices)
│   ├── aligned_top40_logreturns.csv   # Daily log returns aligned to index
│   ├── index_timeseries.csv           # Market index time series
│   ├── token_capm_summary.csv         # Alpha, Beta, R², Residual Volatility
│   └── token_capm_clusters.csv        # Cluster labels assigned to tokens
│
├── notebooks/
│   └── crypto_project.ipynb           # Jupyter Notebook with full workflow
│
├── output/
│   └── token_cluster_pairplot.png     # Cluster visualization
│
├── src/
│   ├── data_loader.py                 # Load, normalize, and preprocess prices
│   └── logreturn_analysis.py          # CAPM regression and clustering pipeline
│
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Ignored files & folders
└── README.md                          # Project overview and instructions
```

---

##  Analysis Workflow

### 1. Universe Selection

- Fetched top tokens by **market cap** using CoinGecko.
- Applied a **volume threshold** (e.g., > $50M 24h vol) to filter shortable & liquid tokens.
- Saved filtered universe as `token_universe_filtered_top40.csv`.

### 2. Data Pipeline

- Historical OHLC data collected for each token.
- Stored in `/data/raw/top40_price_data/`.
- Merged and converted to **daily log returns** in `aligned_top40_logreturns.csv`.

### 3. Market Index

- Constructed a market-level index stored in `index_timeseries.csv`.
- Used for computing market exposure (β) in CAPM.

### 4. CAPM Regression

For each token:
- Regressed daily returns on market returns.
- Extracted:
  - **Alpha** (excess return)
  - **Beta** (market sensitivity)
  - **R²**
  - **Residual Std Dev** (volatility unexplained by market)

### 5. Clustering

- Applied **KMeans** on the features: Alpha, Beta, Residual Std.
- Used **Spearman’s correlation** distance to account for rank-based relationships.
- Saved cluster assignments to `token_capm_clusters.csv`.
- Visualized using `token_cluster_pairplot.png`.

---

##  Outputs

| File | Description |
|------|-------------|
| `token_capm_summary.csv` | Token-wise CAPM alpha, beta, R², residual volatility |
| `token_capm_clusters.csv` | Clustering labels for each token |
| `aligned_top40_logreturns.csv` | Daily log returns aligned with index |
| `hedgeable_crypto_index.csv` | Prototype index construction |
| `token_cluster_pairplot.png` | Cluster visualization chart |

---

##  Future Work

- Integrate [StockTwits Sentiment](https://stocktwits.com/symbol/BTC.X/sentiment) for alpha signals
- Expand to 100 tokens with scalable architecture
- Incorporate volatility-adjusted weights in index design
- Deploy cluster classification as an API/dataset

---

##  Installation

```bash
git clone https://github.com/your-org/crypto-classification-project.git
cd crypto-classification-project
pip install -r requirements.txt

