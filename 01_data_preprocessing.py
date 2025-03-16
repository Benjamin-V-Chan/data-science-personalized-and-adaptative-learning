import pandas as pd
import os

# Load dataset
df = pd.read_csv("../data/personalized_learning_dataset.csv")

# Check for missing values
df = df.dropna()

# Encode categorical variables
df = pd.get_dummies(df, columns=["Gender", "Education_Level", "Course_Name", "Engagement_Level", "Learning_Style", "Dropout_Likelihood"], drop_first=True)

# Save cleaned dataset
os.makedirs("../outputs", exist_ok=True)
df.to_csv("../outputs/cleaned_dataset.csv", index=False)
