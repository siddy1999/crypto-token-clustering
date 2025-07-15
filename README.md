# Crypto Token Clustering & Residual Market Model

This repository contains the codebase and data for a factor-model-based analysis of crypto tokens. The goal is to construct a market index, regress token returns to extract residuals, and use those residuals for clustering-based classification of tokens.

## ?? Key Goals

- Construct a robust **volume-weighted crypto market index**
- Perform **CAPM-style regression** to decompose returns
- Analyze residuals for **clustering and sector inference**
- Enable **classification of top tokens** into interpretable groups
- Support shortable-token universe selection
- Prepare ground for tactical asset allocation signals using community sentiment

## ?? Folder Structure

\\\
crypto-token-clustering/
+-- data/
¦   +-- top40_price_data/     # Raw token OHLCV data (1 CSV per token)
+-- output/                   # Generated datasets: log returns, regressions, residuals
+-- notebooks/                # Jupyter Notebooks (analysis, clustering, diagnostics)
+-- src/                      # Python scripts and modules
+-- README.md
+-- requirements.txt
+-- .gitignore
\\\

## ?? How to Run

1. Install packages:
   \\\
   pip install -r requirements.txt
   \\\

2. Run the notebooks or scripts in src/.

3. All outputs will be saved in the output/ directory.

## ?? Data Overview

- Raw price data for 40 tokens saved under data/top40_price_data/
- Each CSV contains columns: date, price, or close
- Market index stored in data/index_timeseries.csv
- Aligned log returns computed and saved in:
  - output/aligned_top40_logreturns.csv
  - output/token_capm_summary.csv
  - output/residual_clusters.csv

## ?? Methods Used

- CAPM-style regression: \_i = alpha + beta * r_m + e\
- Residual extraction and Spearman-distance based clustering
- KMeans and distance-matrix based alternatives
- Cluster labeling based on volatility & alpha patterns

## ?? Next Steps

- Add more tokens (targeting top 100–150)
- Incorporate sentiment (e.g., from Stocktwits)
- Refine cluster logic using more features
- Productionize classification dataset

## ?? License

MIT License

