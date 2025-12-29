import pandas as pd

# Load dataset (same folder)
df = pd.read_csv("final_dataset.csv")

# Create dropout label
df["dropout"] = df["final_result"].apply(
    lambda x: 1 if x == "Withdrawn" else 0
)

features = [
    "num_of_prev_attempts",
    "studied_credits",
    "imd_band",
    "age_band",
    "highest_education",
    "gender"
]

X = df[features]
y = df["dropout"]

print("FEATURES (X):")
print(X.head())

print("\nLABEL (y):")
print(y.head())
