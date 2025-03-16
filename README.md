# data-science-personalized-and-adaptative-learning

# Project Overview
This project analyzes student engagement and dropout likelihood using machine learning models. It includes data preprocessing, exploratory analysis, correlation studies, and predictive modeling.

# Folder Structure
```
project-root/
├── data/                 # Contains the original dataset
├── scripts/              # Contains all the analysis and modeling scripts
│   ├── 01_data_preprocessing.py
│   ├── 02_exploratory_analysis.py
│   ├── 03_correlation_analysis.py
│   ├── 04_prediction_model.py
│   ├── 05_results_visualization.py
├── outputs/              # Stores cleaned data, results, and visualizations
├── requirements.txt      # Python dependencies
├── README.md             # Documentation
```

# Usage

### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file:
```sh
pip install -r requirements.txt
```

### 2. Run Data Preprocessing:
```sh
python scripts/01_data_preprocessing.py
```
This step cleans the dataset and saves the preprocessed version in the `outputs/` folder.

### 3. Run Exploratory Analysis:
```sh
python scripts/02_exploratory_analysis.py
```
This generates summary statistics and visualizations, saved in `outputs/`.

### 4. Perform Correlation Analysis:
```sh
python scripts/03_correlation_analysis.py
```
This generates a heatmap showing feature correlations and saves it in `outputs/`.

### 5. Train the Prediction Model:
```sh
python scripts/04_prediction_model.py
```
This trains a machine learning model and saves performance metrics and the trained model in `outputs/`.

### 6. Visualize Results:
```sh
python scripts/05_results_visualization.py
```
This generates a confusion matrix and other evaluation reports, saved in `outputs/`.

# Requirements
- Python 3.x
- Required libraries listed in `requirements.txt`

# Acknowledgments
**Dataset Name:** Personalized Learning & Adaptive Education Dataset  
**Dataset Author:** Adil Shamim  
**Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/adilshamim8/personalized-learning-and-adaptive-education-dataset)