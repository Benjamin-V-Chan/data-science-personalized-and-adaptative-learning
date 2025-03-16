import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../outputs/cleaned_dataset.csv")

# Summary statistics
summary = df.describe()
summary.to_csv("../outputs/summary_statistics.csv")

# Histograms
plt.figure(figsize=(10,6))
df.hist(bins=20, figsize=(12,10))
plt.savefig("../outputs/histograms.png")

# Boxplots
plt.figure(figsize=(10,6))
sns.boxplot(data=df)
plt.xticks(rotation=90)
plt.savefig("../outputs/boxplots.png")