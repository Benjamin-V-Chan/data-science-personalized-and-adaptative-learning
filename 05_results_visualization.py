import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import joblib

# Load data and model
df = pd.read_csv("../outputs/cleaned_dataset.csv")
model = joblib.load("../outputs/dropout_model.pkl")
X = df.drop(columns=[col for col in df.columns if "Dropout_Likelihood" in col])
y = df[[col for col in df.columns if "Dropout_Likelihood" in col]]

# Predictions
predictions = model.predict(X)

# Confusion Matrix
cm = confusion_matrix(y, predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix")
plt.savefig("../outputs/confusion_matrix.png")