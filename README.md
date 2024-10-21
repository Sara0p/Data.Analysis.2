# Diabetes Prediction Using Naïve Bayes and Random Forest Classifiers
  
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
