# Medical Insurance Cost Prediction Model

## Overview

The Medical Insurance Cost Prediction Model is a machine learning-based solution designed to estimate the medical insurance costs for individuals. It takes into account several factors such as age, BMI, number of children, smoking status, and region to predict the insurance cost accurately.

## How it Works

1. **Data Preprocessing:** The model preprocesses the dataset by converting categorical variables into numerical values, handling missing data, and scaling the features if necessary.

2. **Model Training:** After preprocessing, the model splits the dataset into training and testing sets. It then trains a Linear Regression model using the training data to learn the relationship between the input features and the insurance costs.

3. **Prediction:** Once the model is trained, it accepts input data for a new customer. This input data includes the customer's age, BMI, number of children, smoking status, and region. Using this information, the model predicts the medical insurance cost for the new customer.

## Why it was Needed

The Medical Insurance Cost Prediction Model addresses the need for accurate estimation of insurance costs for individuals. By utilizing machine learning techniques, it provides insurance companies, healthcare providers, and individuals with a reliable tool to estimate potential medical expenses. This helps in financial planning, risk assessment, and decision-making related to healthcare coverage.

## Installation

To install the dependencies required for running this model, simply execute the following command in your command prompt or terminal:

```bash
pip install -r requirements.txt
