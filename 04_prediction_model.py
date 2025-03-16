import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
df = pd.read_csv("../outputs/cleaned_dataset.csv")
X = df.drop(columns=[col for col in df.columns if "Dropout_Likelihood" in col])
y = df[[col for col in df.columns if "Dropout_Likelihood" in col]]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train.values.ravel())

# Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

# Save results
with open("../outputs/classification_report.txt", "w") as f:
    f.write(report)
joblib.dump(model, "../outputs/dropout_model.pkl")