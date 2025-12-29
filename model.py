import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
df = pd.read_csv("final_dataset.csv")

# Create dropout label
df["dropout"] = df["final_result"].apply(
    lambda x: 1 if x == "Withdrawn" else 0
)

# Select features
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

# Encode categorical variables
X = pd.get_dummies(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
