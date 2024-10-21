# Diabetes Prediction using Machine Learning

## Overview

This project aims to predict diabetes using two classification models: Random Forest Classifier and Naive Bayes Classifier. It utilizes the "Pima Indians Diabetes Database" dataset for training and testing.

## Dataset

The dataset used in this project is the "Pima Indians Diabetes Database." It contains various medical predictor variables and an outcome variable indicating whether the patient has diabetes or not.

## Methodology

1. **Data Loading and Preprocessing:** The dataset is loaded, explored, and preprocessed to handle missing values and ensure data quality.
2. **Exploratory Data Analysis (EDA):** EDA techniques are used to gain insights into the dataset, including histograms, correlation heatmaps, and scatter plots.
3. **Model Selection:** Two classification models are chosen:
    - Random Forest Classifier
    - Naive Bayes Classifier
4. **Model Training and Evaluation:** The selected models are trained on the training data and evaluated on the testing data using metrics such as accuracy, confusion matrix, and classification report.
5. **Results and Conclusion:** The results are presented, and conclusions are drawn regarding the performance of the models in predicting diabetes.

## Requirements

- Python 3.x
- Libraries: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn
- Google Colab (optional)


## Usage

1. Upload the dataset "diabetes.csv" to your Google Drive (optional).
2. Open the code file in Google Colab or any Python environment.
3. Install the required libraries if necessary.
4. Run the code cells sequentially to execute the analysis and prediction.


## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to suggest improvements or enhancements.

## License

This project is licensed under the [MIT License](LICENSE).
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Fake News Detection

This project aims to detect fake news articles using machine learning techniques. It utilizes a dataset of news articles labeled as real or fake and trains a model to classify new articles.

## Dataset

The dataset used in this project consists of two CSV files:

- `train[1].csv`: Contains the training data with news articles and their corresponding labels (real or fake).
- `test[1].csv`: Contains the testing data with news articles to be classified.


## Preprocessing

The following preprocessing steps are applied to the data:

- Handling missing data: Missing values are filled with spaces.
- Combining text features: The title, author, and text of each article are combined into a single "total" column.
- Tokenization: The text is tokenized into individual words.
- Stop word removal: Common words that do not carry significant meaning are removed.
- Lemmatization: Words are reduced to their base form using lemmatization.

## Feature Extraction

TF-IDF (Term Frequency-Inverse Document Frequency) is used to extract features from the preprocessed text. This technique assigns weights to words based on their importance in the document and the corpus.

## Model Training

Two machine learning models are trained:

- Naive Bayes: A probabilistic classifier based on Bayes' theorem.
- SVM (Support Vector Machine): A discriminative classifier that finds an optimal hyperplane to separate data points.

## Evaluation

The models are evaluated using accuracy score and classification report metrics. The results show the performance of each model in terms of precision, recall, F1-score, and support.

## Usage

To use this project, follow these steps:

1. Install the necessary libraries:
