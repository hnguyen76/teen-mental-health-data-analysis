import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Teen_Mental_Health_Dataset.csv")

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

text_cols = ["gender", "platform_usage", "social_interaction_level"]

for col in text_cols:
    df[col] = df[col].str.strip().str.lower()

df = df.drop_duplicates()

missing_summary = (
    df.isna()
    .sum()
    .rename("missing_count")
    .to_frame()
)

missing_summary["missing_pct"] = (
    missing_summary["missing_count"] / len(df) * 100
).round(2)

print("Shape:", df.shape)
print("Duplicate rows:", df.duplicated().sum())
print(missing_summary)

df.to_csv("teen_mental_health_cleaned.csv", index=False)