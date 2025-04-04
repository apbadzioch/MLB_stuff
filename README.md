# Pitch Predictor: Machine Learning for Pitch Type Prediction

## Project Overview
This project started as a way to practice data science skills for my Python Data Science class at Houston Community College (Fall 2024). While working with various datasets, I realized that baseball is built on data and statistics, and since I was watching the MLB playoffs at the time, it became the perfect insperation.

The goal: Predict the type of pitch a pitcher is most likely to throw, based on their tendencies and handedness. Over time, this will evole into a flexable ML tool using logistic regression, random forests, and plans to extend into reinforcement learning for strategic sequencing.

## Features
- Supervised learning models:
    - Logistic Regression
    - Random Forest
- Optional SMOTE for handling imbalanced data
- Custom feature enginering: pitch ratios, variety, handedness
**In-progress**
- Train and evaluate with <code>train_model()</code>
- Predict new pitch types using <code>predict()</code>
- Save and load trained models for reuse
- Reinforcement Learning environment to simulate pitch sequences

## Technologies Used
- Python
- Pandas, NumPy
- matplotlib
- tkinter
- Flask/Django
- scikit-learn
- joblib
- Gym and stable-baselines3 for RL
