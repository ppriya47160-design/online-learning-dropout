import pandas as pd

# Load dataset (same folder)
df = pd.read_csv("final_dataset.csv")

# Create dropout column
df["dropout"] = df["final_result"].apply(
    lambda x: 1 if x == "Withdrawn" else 0
)

# Verify output
print(df[["final_result", "dropout"]].head())
print("\nDropout count:")
print(df["dropout"].value_counts())
