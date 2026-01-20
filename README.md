# End-to-End Sentiment Analysis System for User Reviews

## Project Overview
This project is an end-to-end sentiment analysis system designed to analyze user reviews and present actionable insights through a web-based interface. The system processes textual data stored in a spreadsheet, applies machine learning models for sentiment classification, and delivers results via a simple UI for non-technical users.

This project was developed as my undergraduate thesis and demonstrates the complete data analytics workflow—from data ingestion and preprocessing to model deployment and user-facing visualization.

---

## Objectives
- Automate sentiment classification of user reviews
- Transform unstructured text data into actionable insights
- Provide an accessible interface for stakeholders without technical background
- Support data-driven decision making for service improvement

---

## Dataset
- **Source:** Google Spreadsheet (user reviews dataset)
- **Data Type:** Textual data (reviews, ratings)
- **Size:** Thousands of user reviews
- **Target Group:** Users aged 19–33

> *Note: Due to data privacy, this repository includes a sample dataset only.*

---

## Tools & Technologies

### Data Analysis & Modeling
- Python  
- Pandas  
- Scikit-learn  
- TF-IDF Vectorization  
- Random Forest Classifier  
- Google Colab

### Deployment & Interface
- Flask (Backend API)
- HTML & CSS (Frontend UI)
- Google Spreadsheet (Data Storage)

---

## Methodology

1. **Data Collection**
   - Imported user reviews from Google Spreadsheet

2. **Data Preprocessing**
   - Text cleaning (lowercasing, punctuation removal, stopword removal)
   - Tokenization and vectorization using TF-IDF

3. **Model Development**
   - Trained and evaluated machine learning models
   - Selected Random Forest based on performance metrics

4. **Model Evaluation**
   - Accuracy, precision, recall
   - Achieved **95% accuracy** on the target age group

5. **Deployment**
   - Integrated trained model into a Flask API
   - Developed a web interface to display sentiment predictions

---

## System Architecture

