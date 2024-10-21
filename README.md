# Diabetes Prediction Using Naïve Bayes and Random Forest Classifiers
  
Overview
This project implements two machine learning algorithms, Naïve Bayes and Random Forest, to predict diabetes based on patient data. The models are trained on a dataset containing several medical and demographic features, including pregnancies, glucose levels, blood pressure, skin thickness, insulin levels, BMI, diabetes pedigree function, and age.

Dataset
The dataset includes the following features:

Pregnancies: Number of times the patient has been pregnant.
Glucose: Plasma glucose concentration after a glucose tolerance test.
Blood Pressure: Diastolic blood pressure (mm Hg).
Skin Thickness: Triceps skinfold thickness (mm).
Insulin: 2-hour serum insulin (µU/mL).
BMI: Body mass index.
Diabetes Pedigree Function: Likelihood of diabetes based on family history.
Age: The age of the patient.
Outcome: Diabetes diagnosis result (1 = positive, 0 = negative).
Models
1. Naïve Bayes Classifier
Naïve Bayes is a supervised learning algorithm that applies probability theory for classification. It assumes that the features are conditionally independent, which makes it simple yet effective for certain types of datasets.

Performance: The Naïve Bayes model achieves around 76% accuracy, making it a reasonably good fit for this dataset.
Comparison: Naïve Bayes performs similarly to Random Forest in this task, though the choice of model depends on factors like interpretability and computational efficiency.
2. Random Forest Classifier
Random Forest is a meta-estimator that builds multiple decision trees and averages their predictions to improve accuracy and reduce overfitting.

Performance: This model achieves approximately 77% accuracy.
Interpretability: Feature importance can be analyzed to identify which factors most influence predictions.
Tuning: Hyperparameters such as the number of trees and maximum tree depth can be adjusted to optimize performance.
Confusion Matrix: Key metrics like true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN) are used to evaluate model accuracy.
Key Insights
Feature Importance: Random Forest allows for analyzing which features contribute most to diabetes prediction.
Hyperparameter Tuning: Adjusting the number of trees, depth, and other hyperparameters can improve both models' performance.
Data Imbalance: Techniques like oversampling or undersampling may be necessary if the dataset is imbalanced between positive and negative diabetes cases.
Conclusion
Both Naïve Bayes and Random Forest classifiers show good performance on this dataset, with Random Forest slightly outperforming Naïve Bayes. The choice of classifier can depend on specific use cases, computational requirements, and interpretability needs.

