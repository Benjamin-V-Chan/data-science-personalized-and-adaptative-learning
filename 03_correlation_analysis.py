import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../outputs/cleaned_dataset.csv")

# Compute correlation matrix
correlation_matrix = df.corr()

# Heatmap
plt.figure(figsize=(12,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Matrix")
plt.savefig("../outputs/correlation_heatmap.png")