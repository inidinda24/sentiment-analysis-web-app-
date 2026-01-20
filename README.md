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
- **Data Type:** Textual data (name, age, and reviews)
- **Size:** 462 of user reviews

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
   - Accuracy, precision, recall, F1-Score
   - Achieved **95% accuracy** on the target age group

5. **Deployment**
   - Integrated trained model into a Flask API
   - Developed a web interface to display sentiment predictions

---

## System Architecture
<img width="181" height="242" alt="Systhematic Architecture drawio" src="https://github.com/user-attachments/assets/89902a6c-7727-4628-ad0a-33c06c45d93d" />

---

## Key Results
- Random Forest sentiment classification model achieved high accuracy across user age segments
- Highest model performance recorded in early adult users (19–33 years) with 95% accuracy
- Model accuracy varied by age group:
  * Teenagers: 85%
  * Middle-aged adults: 80%
  * Older adults: 75%
- Sentiment classification performance was influenced by language style, sentence complexity, and emotional expression
- Successfully implemented an end-to-end web-based sentiment analysis system using Flask for real-time prediction

---

## Business Insights & Recommendations
- User feedback behavior differs significantly by age group and should be analyzed using age-based segmentation
- Early adult users provide clearer and more consistent sentiment signals, making them ideal for automated sentiment monitoring
- Older user segments may require complementary qualitative analysis due to more complex language patterns
- Service improvement initiatives should be prioritized based on dominant sentiment trends per age segment
- Sentiment analysis can be used as a continuous KPI for monitoring service quality in digital health platforms
- The deployed system demonstrates scalability for real-time customer feedback analysis

---

## Model Development
- Google Colab Notebook:  
  Remaja: https://colab.research.google.com/drive/12PvbFaweRmphyiS5kT4fk2BZTGDw2OXE?usp=sharing
  Dewasa Awal: https://colab.research.google.com/drive/1mgcTf_eL0vUi9GsLHCks8aiu6Fn5uBzw?usp=sharing
  Dewasa Menengah: https://colab.research.google.com/drive/1NQNsazADqD4mZMZScs161ffQe5fP7oaj?usp=sharing
  Dewasa Lanjut: https://colab.research.google.com/drive/1W9aXaLD1l2V4w348G6DGQ59kdcuY5jaG?usp=sharing

  ## Dataset
- Source: Google Spreadsheet  
  https://docs.google.com/spreadsheets/d/1YXubBT5NeTp2ik0sQ4D3QeuSbFWwU7J3ZgHC0L4cjAY/edit?usp=sharing

  

  
  





