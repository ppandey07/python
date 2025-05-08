# Existing imports
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor  # Import XGBoost
from catboost import CatBoostRegressor  # Import CatBoost
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import Binarizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

# Load your dataset
dataset = pd.read_csv('insurance.csv')

# Preprocess the dataset (dropping non-numeric columns and getting dummies)
dataset_encoded = pd.get_dummies(data=dataset, drop_first=True)

# Split the dataset into features and target variable
x = dataset_encoded.drop(columns='charges')
y = dataset_encoded['charges']

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
regressor_lr = LinearRegression()
regressor_lr.fit(x_train, y_train)

# Create and train the Random Forest model
regressor_rf = RandomForestRegressor(n_estimators=10, random_state=0)
regressor_rf.fit(x_train, y_train)

# Create and train the XGBoost model
regressor_xgb = XGBRegressor()
regressor_xgb.fit(x_train, y_train)

# Create and train the CatBoost model
# regressor_cat = CatBoostRegressor(silent=True)
# regressor_cat.fit(x_train, y_train)
# Convert charges into categories (e.g., Low: 0, High: 1)
threshold = dataset_encoded['charges'].median()
dataset_encoded['charges_category'] = (dataset_encoded['charges'] > threshold).astype(int)

# Update target variable for classification
y_classification = dataset_encoded['charges_category']

# Split dataset
x_train_cls, x_test_cls, y_train_cls, y_test_cls = train_test_split(x, y_classification, test_size=0.2, random_state=42)

# Train Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(x_train_cls, y_train_cls)

# Make predictions
y_pred_rf = rf_classifier.predict(x_test_cls)

# Compute Confusion Matrix
cm = confusion_matrix(y_test_cls, y_pred_rf)

# Display Confusion Matrix in Streamlit
st.subheader("Confusion Matrix (Random Forest Classifier)")
fig, ax = plt.subplots()
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Low", "High"], yticklabels=["Low", "High"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
st.pyplot(fig)

# Display Classification Report
st.subheader("Classification Report")
st.text(classification_report(y_test_cls, y_pred_rf))

st.title('Insurance Cost Prediction')

st.sidebar.header('User Input')

# Create input fields for user input
age = st.sidebar.number_input('Age', min_value=1, max_value=100, value=30)
bmi = st.sidebar.number_input('BMI', min_value=10.0, max_value=50.0, value=25.0)
children = st.sidebar.number_input('Number of Children', min_value=0, max_value=10, value=0)
sex = st.sidebar.radio('Sex', ['male', 'female'])
smoker = st.sidebar.radio('Smoker', ['yes', 'no'])
region = st.sidebar.selectbox('Region', ['northeast', 'northwest', 'southeast', 'southwest'])

# Function to preprocess user input
def preprocess_input(age, bmi, children, sex, smoker, region):
    # One-hot encoding for user input
    input_data = pd.DataFrame({
        'age': [age],
        'bmi': [bmi],
        'children': [children],
        'sex_male': [1 if sex == 'male' else 0],
        'smoker_yes': [1 if smoker == 'yes' else 0],
        'region_northwest': [1 if region == 'northwest' else 0],
        'region_northeast': [1 if region == 'northeast' else 0],
        'region_southeast': [1 if region == 'southeast' else 0],
        'region_southwest': [1 if region == 'southwest' else 0],
    })
    return input_data

user_input = preprocess_input(age, bmi, children, sex, smoker, region)

# Ensure the user input has the same columns as the training data
user_input = user_input.reindex(columns=x.columns, fill_value=0)

# Function to make predictions
def predict_charges(model, user_input):
    return model.predict(user_input)

# Calculate predictions for all models
lr_prediction = predict_charges(regressor_lr, user_input)
rf_prediction = predict_charges(regressor_rf, user_input)
xgb_prediction = predict_charges(regressor_xgb, user_input)
# cat_prediction = predict_charges(regressor_cat, user_input)

st.sidebar.header('Prediction')

st.sidebar.write('Linear Regression Model Prediction: \u20B9', round(lr_prediction[0], 2))
st.sidebar.write('Random Forest Model Prediction: \u20B9', round(rf_prediction[0], 2))
st.sidebar.write('XGBoost Model Prediction: \u20B9', round(xgb_prediction[0], 2))
# st.sidebar.write('CatBoost Model Prediction: \u20B9', round(cat_prediction[0], 2))

# Function to recommend insurance company based on predicted charges
def recommend_insurance_company(predicted_charge):
    closest_row = dataset.iloc[(dataset['charges'] - predicted_charge).abs().idxmin()]
    return closest_row['company']  # Return the company name from the closest match

# Get recommendations based on the predictions
lr_recommendation = recommend_insurance_company(lr_prediction[0])
rf_recommendation = recommend_insurance_company(rf_prediction[0])
xgb_recommendation = recommend_insurance_company(xgb_prediction[0])
# cat_recommendation = recommend_insurance_company(cat_prediction[0])

st.sidebar.header('Insurance Company Recommendation')
st.sidebar.write('Linear Regression Model Recommendation: ', lr_recommendation)
st.sidebar.write('Random Forest Model Recommendation: ', rf_recommendation)
st.sidebar.write('XGBoost Model Recommendation: ', xgb_recommendation)
# st.sidebar.write('CatBoost Model Recommendation: ', cat_recommendation)

# Create a Reset button to clear user input
if st.sidebar.button('Reset'):
    st.experimental_rerun()

# Display model comparison
st.write('Comparing Models')
st.markdown("<div>Linear Regression R^2 Score: <b>{:.2f}</b></div>".format(r2_score(y_test, regressor_lr.predict(x_test))), unsafe_allow_html=True)
st.markdown("<div>Random Forest R^2 Score: <b>{:.2f}</b></div>".format(r2_score(y_test, regressor_rf.predict(x_test))), unsafe_allow_html=True)
st.markdown("<div>XGBoost R^2 Score: <b>{:.2f}</b></div>".format(r2_score(y_test, regressor_xgb.predict(x_test))), unsafe_allow_html=True)
# st.markdown("<div>CatBoost R^2 Score: <b>{:.2f}</b></div>".format(r2_score(y_test, regressor_cat.predict(x_test))), unsafe_allow_html=True)

# Create a section to display a comparison graph of model predictions
st.subheader('Model Predictions Comparison')


# Create a DataFrame with the model predictions
comparison_df = pd.DataFrame({
    'Model': ['Linear Regression', 'Random Forest', 'XGBoost'],
    'Prediction (₹)': [lr_prediction[0], rf_prediction[0], xgb_prediction[0]]
})
# Selecting only relevant columns for correlation matrix
selected_features = ['age', 'bmi', 'children', 'sex_male', 'smoker_yes', 
                     'region_northwest', 'region_southeast', 'region_southwest']

correlation_matrix = dataset_encoded[selected_features].corr()

# Plot correlation heatmap
st.subheader("Feature Correlation Matrix (Selected Features)")

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)

# Display the heatmap in Streamlit
st.pyplot(fig)

st.subheader("ROC Curve for Model Comparison")

# Convert regression problem into binary classification (High vs. Low charges)
threshold = dataset['charges'].median()  # Median split
y_train_bin = (y_train > threshold).astype(int)
y_test_bin = (y_test > threshold).astype(int)

# Train classifiers instead of regressors
regressor_lr.fit(x_train, y_train_bin)
regressor_rf.fit(x_train, y_train_bin)
regressor_xgb.fit(x_train, y_train_bin)

# Get predicted probabilities
lr_probs = regressor_lr.predict(x_test)
rf_probs = regressor_rf.predict(x_test)
xgb_probs = regressor_xgb.predict(x_test)

# Compute ROC curve and AUC
fpr_lr, tpr_lr, _ = roc_curve(y_test_bin, lr_probs)
roc_auc_lr = auc(fpr_lr, tpr_lr)

fpr_rf, tpr_rf, _ = roc_curve(y_test_bin, rf_probs)
roc_auc_rf = auc(fpr_rf, tpr_rf)

fpr_xgb, tpr_xgb, _ = roc_curve(y_test_bin, xgb_probs)
roc_auc_xgb = auc(fpr_xgb, tpr_xgb)

# Plot ROC Curves
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(fpr_lr, tpr_lr, label=f"Linear Regression (AUC = {roc_auc_lr:.2f})", linestyle='--')
ax.plot(fpr_rf, tpr_rf, label=f"Random Forest (AUC = {roc_auc_rf:.2f})", linestyle='-.')
ax.plot(fpr_xgb, tpr_xgb, label=f"XGBoost (AUC = {roc_auc_xgb:.2f})", linestyle='-')

# Reference Line (No Skill)
ax.plot([0, 1], [0, 1], color='gray', linestyle=":")

ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")
ax.set_title("ROC Curve Comparison")
ax.legend()

# Display in Streamlit
st.pyplot(fig)

# Add a section to display the dataset
st.write('Insurance Dataset')
st.write(dataset)

# Plot the comparison using Streamlit's bar chart
st.bar_chart(comparison_df.set_index('Model'))

