# src/logreturn_analysis.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import spearmanr
from sklearn.cluster import KMeans

def run_capm_regression(aligned_df: pd.DataFrame):
    summary = []

    for token in aligned_df.columns.difference(["Market"]):
        x = aligned_df["Market"].values.reshape(-1, 1)
        y = aligned_df[token].values

        reg = LinearRegression().fit(x, y)
        y_pred = reg.predict(x)
        residuals = y - y_pred

        alpha = reg.intercept_
        beta = reg.coef_[0]
        r2 = reg.score(x, y)
        residual_std = np.std(residuals)

        summary.append({
            "Token": token,
            "Alpha": alpha,
            "Beta": beta,
            "R²": r2,
            "Residual Std": residual_std
        })

    return pd.DataFrame(summary)

def compute_spearman_distance(df: pd.DataFrame) -> pd.DataFrame:
    tokens = df.columns.difference(["Market"])
    n = len(tokens)

    dist_matrix = pd.DataFrame(np.zeros((n, n)), index=tokens, columns=tokens)

    for i in tokens:
        for j in tokens:
            rho, _ = spearmanr(df[i], df[j])
            dist = 1 - rho
            dist_matrix.loc[i, j] = dist

    return dist_matrix

def cluster_tokens(df: pd.DataFrame, n_clusters: int = 4):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    features = df[["Alpha", "Beta", "Residual Std"]]
    df["Cluster"] = kmeans.fit_predict(features)
    return df
