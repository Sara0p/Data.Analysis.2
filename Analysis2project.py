{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1BQo_q3yMDxwkuCrPxtgVE1mtvI3TgwTA",
      "authorship_tag": "ABX9TyOWsRoUiWho6s4kR4Q9meao",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sara0p/Data.Analysis.2/blob/main/Analysis2project.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "W7km0v-YMBSJ"
      },
      "outputs": [],
      "source": [
        "#this  is an application for data analyise project it's about classifing and we will you 2 types\n",
        "# of classification the random classfier and the naiieve classifier\n",
        "# the data are used is Naive Bayes Classifier\n",
        "#Objective: Build a Naive Bayes classifier to predict a target variable."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import statistics\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.metrics import accuracy_score"
      ],
      "metadata": {
        "id": "D3wJxpYXP_ET"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bPNksRIbQhvn",
        "outputId": "f2c4ee9c-b285-4c64-a9e8-adcf2e26b545"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df=pd.read_csv('/content/drive/MyDrive/diabetes.csv')"
      ],
      "metadata": {
        "id": "zrzcO4ZxNYqB"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()\n",
        "\n"
      ],
      "metadata": {
        "id": "4QDVR8kISR5q",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "outputId": "c0dc8e97-3372-4cad-c6ef-0f42d3b1ea3f"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
              "0            6      148             72             35        0  33.6   \n",
              "1            1       85             66             29        0  26.6   \n",
              "2            8      183             64              0        0  23.3   \n",
              "3            1       89             66             23       94  28.1   \n",
              "4            0      137             40             35      168  43.1   \n",
              "\n",
              "   DiabetesPedigreeFunction  Age  Outcome  \n",
              "0                     0.627   50        1  \n",
              "1                     0.351   31        0  \n",
              "2                     0.672   32        1  \n",
              "3                     0.167   21        0  \n",
              "4                     2.288   33        1  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-7d7f357a-5ca5-4f03-b2ac-06e16447f05a\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Pregnancies</th>\n",
              "      <th>Glucose</th>\n",
              "      <th>BloodPressure</th>\n",
              "      <th>SkinThickness</th>\n",
              "      <th>Insulin</th>\n",
              "      <th>BMI</th>\n",
              "      <th>DiabetesPedigreeFunction</th>\n",
              "      <th>Age</th>\n",
              "      <th>Outcome</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>6</td>\n",
              "      <td>148</td>\n",
              "      <td>72</td>\n",
              "      <td>35</td>\n",
              "      <td>0</td>\n",
              "      <td>33.6</td>\n",
              "      <td>0.627</td>\n",
              "      <td>50</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>85</td>\n",
              "      <td>66</td>\n",
              "      <td>29</td>\n",
              "      <td>0</td>\n",
              "      <td>26.6</td>\n",
              "      <td>0.351</td>\n",
              "      <td>31</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>8</td>\n",
              "      <td>183</td>\n",
              "      <td>64</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>23.3</td>\n",
              "      <td>0.672</td>\n",
              "      <td>32</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>89</td>\n",
              "      <td>66</td>\n",
              "      <td>23</td>\n",
              "      <td>94</td>\n",
              "      <td>28.1</td>\n",
              "      <td>0.167</td>\n",
              "      <td>21</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0</td>\n",
              "      <td>137</td>\n",
              "      <td>40</td>\n",
              "      <td>35</td>\n",
              "      <td>168</td>\n",
              "      <td>43.1</td>\n",
              "      <td>2.288</td>\n",
              "      <td>33</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-7d7f357a-5ca5-4f03-b2ac-06e16447f05a')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-7d7f357a-5ca5-4f03-b2ac-06e16447f05a button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-7d7f357a-5ca5-4f03-b2ac-06e16447f05a');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-795c728a-99a3-4334-b534-3e9cdf11b426\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-795c728a-99a3-4334-b534-3e9cdf11b426')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-795c728a-99a3-4334-b534-3e9cdf11b426 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 768,\n  \"fields\": [\n    {\n      \"column\": \"Pregnancies\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3,\n        \"min\": 0,\n        \"max\": 17,\n        \"num_unique_values\": 17,\n        \"samples\": [\n          6,\n          1,\n          3\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Glucose\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 31,\n        \"min\": 0,\n        \"max\": 199,\n        \"num_unique_values\": 136,\n        \"samples\": [\n          151,\n          101,\n          112\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"BloodPressure\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 19,\n        \"min\": 0,\n        \"max\": 122,\n        \"num_unique_values\": 47,\n        \"samples\": [\n          86,\n          46,\n          85\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"SkinThickness\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 15,\n        \"min\": 0,\n        \"max\": 99,\n        \"num_unique_values\": 51,\n        \"samples\": [\n          7,\n          12,\n          48\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Insulin\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 115,\n        \"min\": 0,\n        \"max\": 846,\n        \"num_unique_values\": 186,\n        \"samples\": [\n          52,\n          41,\n          183\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"BMI\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 7.884160320375446,\n        \"min\": 0.0,\n        \"max\": 67.1,\n        \"num_unique_values\": 248,\n        \"samples\": [\n          19.9,\n          31.0,\n          38.1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"DiabetesPedigreeFunction\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.3313285950127749,\n        \"min\": 0.078,\n        \"max\": 2.42,\n        \"num_unique_values\": 517,\n        \"samples\": [\n          1.731,\n          0.426,\n          0.138\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 11,\n        \"min\": 21,\n        \"max\": 81,\n        \"num_unique_values\": 52,\n        \"samples\": [\n          60,\n          47,\n          72\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Outcome\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(df.columns)\n",
        "missing_values = df.isnull().sum()\n",
        "print(missing_values)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ONRDddg-D-Jk",
        "outputId": "8fd3eff6-fed0-4a4e-9183-a28bd1cbbfae"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Index(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',\n",
            "       'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],\n",
            "      dtype='object')\n",
            "Pregnancies                 0\n",
            "Glucose                     0\n",
            "BloodPressure               0\n",
            "SkinThickness               0\n",
            "Insulin                     0\n",
            "BMI                         0\n",
            "DiabetesPedigreeFunction    0\n",
            "Age                         0\n",
            "Outcome                     0\n",
            "dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X = df.iloc[:, :-1]\n",
        "y = df.iloc[:, -1]\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)"
      ],
      "metadata": {
        "collapsed": true,
        "id": "ymF9caDOEB_i"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# import Random Forest classifier\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "\n",
        "# instantiate the classifier\n",
        "rfc = RandomForestClassifier(random_state=0)\n",
        "\n",
        "\n",
        "# fit the model\n",
        "rfc.fit(X_train, y_train)\n",
        "\n",
        "\n",
        "# Predict the Test set results\n",
        "y_pred = rfc.predict(X_test)\n",
        "\n",
        "\n",
        "# Check accuracy score\n",
        "\n",
        "from sklearn.metrics import accuracy_score\n",
        "\n",
        "# Evaluate the model\n",
        "accuracy = accuracy_score(y_test, y_pred)\n",
        "\n",
        "\n",
        "# Print the results\n",
        "print(f\"Accuracy: {accuracy * 100:.2f}%\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R48jYvbBFRb3",
        "outputId": "c24d334d-2a6e-44d8-a330-e54409598484"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy: 75.32%\n",
            "Classification Report:\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.naive_bayes import GaussianNB\n",
        "gnb = GaussianNB()\n",
        "gnb.fit(X_train, y_train)\n",
        "# Make predictions on the test set\n",
        "y_pred = gnb.predict(X_test)\n",
        "\n",
        "# Evaluate the model\n",
        "accuracy = accuracy_score(y_test, y_pred)\n",
        "\n",
        "\n",
        "# Print the results\n",
        "print(f\"Accuracy: {accuracy * 100:.2f}%\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kkUExHJTGZrF",
        "outputId": "bf7e9b4d-7859-4e48-955d-50a9ae205806"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy: 74.46%\n"
          ]
        }
      ]
    }
  ]
}