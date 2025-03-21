# Medical Insurance Cost Prediction Using Multiple Linear Regression

## Project Overview

This project aims to predict individual medical insurance costs using machine learning techniques. By analyzing factors such as age, gender, BMI, number of children, smoking status, and region, the model provides insights into how these variables influence insurance charges.

## Dataset

The dataset includes the following features:

- **Age**: Age of the individual.
- **Gender**: Male or female.
- **BMI (Body Mass Index)**: A measure of body fat based on height and weight.
- **Children**: Number of children/dependents covered by the insurance.
- **Smoker**: Smoking status of the individual (yes/no).
- **Region**: Residential area in the U.S. (northeast, southeast, southwest, northwest).
- **Charges**: Medical insurance costs billed to the individual.

## Objective

The primary goal is to develop a predictive model that estimates medical insurance charges based on the individual's demographic and lifestyle attributes.

## Approach

- **Data Preprocessing**: Handling missing values, encoding categorical variables, and scaling numerical features.
- **Exploratory Data Analysis (EDA)**: Identifying patterns and correlations between features and insurance charges.
- **Model Development**: Implementing regression models such as Linear Regression and Random Forest Regressor.
- **Model Evaluation**: Assessing model performance using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² score.

## Key Findings

- **Smoking Status**: Smokers are charged significantly higher premiums compared to non-smokers.
- **BMI**: Individuals with higher BMI tend to have increased insurance costs.
- **Age**: Older individuals generally incur higher medical expenses.
- **Region**: The region has a relatively minor impact on insurance charges compared to other factors.

## Future Enhancements

- Incorporating additional features such as medical history and lifestyle habits for more accurate predictions.
- Exploring advanced machine learning algorithms and hyperparameter tuning to improve model performance.
- Developing a user-friendly web application to provide real-time insurance cost predictions.
