import streamlit as st

st.title("Age prediction & Employee Classification")
st.divider()
st.header("A. Classification Task")

st.markdown("""
The task at hand is to estimate wether the employee would 
seek help or not, making it a binary classification task, 
therefore the following models can be used to classfiy the employees:
- Logistic Regression
- Random Forest Classification
- Support Vector Classification
- XGBoosting Classification
""")

st.divider()
st.subheader("Logisitic Regression")

st.markdown("""
In order to train a good Logistic Regression model the following hyperparameters can be tuned using `GridSearchCV`
with 3 Cross Validation folds to prevent overfitting the model to the training data.

The tuned hyperparameters are:
- *C*: penalty coefficient -- 10
- *penalty*: type of penalty to apply (`l1` or `l2`) -- 'l2'
- *solver*: binary classification optimization algorithm to use for training the model -- 'saga'

The classification report for the test dataset with tuned model is:
""")

st.code("print('Hello, World!')")

st.code("""
               precision    recall  f1-score   support

          No       0.74      0.78      0.76       124
         Yes       0.78      0.73      0.75       127

    accuracy                           0.76       251
   macro avg       0.76      0.76      0.76       251
weighted avg       0.76      0.76      0.76       251

ROC-AUC: 0.8215011430022859
""")

st.subheader("Random Forest Classification")
st.markdown("""
The RandomForestClassifier model has a lot of hyper parameters 
and for this datasets, these can be tuned for the highest score, 
while looking out for overfitting using cross validation. 

The hyper parameters are tuned as:
- *max_depth*: maximum tree depth before it is cutoff -- `10`
- *min_samples_leaf*:  minimum no. of leaf nodes the decision trees need to have -- `1`
- *min_samples_split*: minimum no. of samples to consider for each split -- `5`
- *n_estimators*: no. of ensemble decision trees to use for modelling the data -- `200`

The classification report and ROC-AUC score for the RFC model are:
""")

st.code("""
               precision    recall  f1-score   support

          No       0.77      0.79      0.78       124
         Yes       0.79      0.76      0.78       127

    accuracy                           0.78       251
   macro avg       0.78      0.78      0.78       251
weighted avg       0.78      0.78      0.78       251

ROC-AUC: 0.861252222504445
""")

st.subheader("Support Vector Classifier")
st.markdown("""
The Support Vector Classifier (or SVC) is a heuristic algorithm, 
selecting certain data points as pivots (or support vectors) to 
form classification boundary (or hyperplanes), but suffer from slow convergence in the iterative method.

The tuned hyper parameters for the SVC model are:
- C: regularization coefficient for the penalty -- 1
- gamma: kernel coefficient for 'rbf' -- 'scale' 
- kernel: type of kernel to use for projection -- 'rbf'
            
The classification report and ROC-AUC score for the SVC model are:
""")

st.code("""
              precision    recall  f1-score   support

           0       0.51      0.48      0.50       124
           1       0.52      0.54      0.53       127

    accuracy                           0.51       251
   macro avg       0.51      0.51      0.51       251
weighted avg       0.51      0.51      0.51       251

ROC-AUC Score: 0.5071755143510287
""")

st.subheader("XGBoosting Classifier")
st.markdown("""
XGBoosting is an ensemble algorithm using various smaller regressor 
estimators to compute the regression/classification objective. 

The various parameters for the tuned model are:
- colsample_bytree: fraction samples to train for in each tree -- 1.0
- learning_rate: learning rate for the stochastic gradient descent optimizer -- 0.01
- max_depth: maximum depth the ensemble trees can grow to -- 3
- n_estimators: no. of estimator for the ensemble model -- 200
- subsample: fraction of sample to train for -- 1.0
            
Classification report and ROC-AUC score for the XGB model are:
""")

st.code("""
               precision    recall  f1-score   support

           0       0.77      0.79      0.78       124
           1       0.79      0.77      0.78       127

    accuracy                           0.78       251
   macro avg       0.78      0.78      0.78       251
weighted avg       0.78      0.78      0.78       251

ROC-AUC Score: 0.8401701803403607
""")


st.divider()
st.header("Classification model comparision")

st.markdown("Ploting the receiver operating characteristic curves "
"for each model can help us compare their performance")
st.image("images/model-roc-curves.png")

st.divider()
st.header("B. Regression Task")

st.markdown("""
The regression task aims to predict the `Age` of employees using various regression models. Below are the models used, their tuned hyperparameters, and evaluation results.
""")

st.subheader("Linear Regression")
st.markdown("""
Linear Regression is a simple and interpretable model that fits a linear relationship between the features and the target variable.
""")
st.code("""
MAE: 5.12
RMSE: 6.45
R² Score: 0.32
""")

st.subheader("Random Forest Regression")
st.markdown("""
Random Forest Regressor is an ensemble method that builds multiple decision trees and averages their predictions for better accuracy and robustness.

Tuned hyperparameters:
- n_estimators: 200
- max_depth: 10
- min_samples_split: 2
- min_samples_leaf: 1
""")
st.code("""
Random Forest Regression Performance:
MAE: 4.85
RMSE: 6.12
R² Score: 0.38
""")

st.subheader("Random Forest Regression (Log-Transformed Target)")
st.markdown("""
Applying a log transformation to the target variable can help stabilize variance and improve model performance, especially when the target is skewed.
""")
st.code("""
MAE: 4.72
RMSE: 5.98
R²: 0.41
""")

st.subheader("XGBoost Regression")
st.markdown("""
XGBoost is a powerful gradient boosting algorithm that often achieves state-of-the-art results on structured data.

Tuned hyperparameters:
- n_estimators: 200
- max_depth: 5
- learning_rate: 0.1
- subsample: 1.0
- colsample_bytree: 1.0
""")
st.code("""
✅ Best Params: {'regressor__colsample_bytree': 1.0, 'regressor__learning_rate': 0.1, 'regressor__max_depth': 5, 'regressor__n_estimators': 200, 'regressor__subsample': 1.0}
MAE: 4.68
RMSE: 5.90
R² Score: 0.43
""")

st.divider()
st.header("Regression Model Comparison")
st.markdown("A summary of the regression model performances is shown below:")
st.markdown("""
| Model                        | MAE  | RMSE | R² Score |
|------------------------------|------|------|----------|
| Linear Regression            | 5.12 | 6.45 | 0.32     |
| Random Forest                | 4.85 | 6.12 | 0.38     |
| Random Forest (Log-Transformed) | 4.72 | 5.98 | 0.41     |
| XGBoost Regression           | 4.68 | 5.90 | 0.43     |
""")