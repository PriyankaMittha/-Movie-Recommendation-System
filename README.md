# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using **Python and Machine Learning** that suggests similar movies based on user input by analyzing movie metadata.

---

## 📌 Project Overview

The Movie Recommendation System recommends movies by measuring the similarity between movies using text-based features such as **genres, overview, and keywords**.  
It uses **Natural Language Processing (NLP)** techniques and **cosine similarity** to provide personalized recommendations.

---

## 🚀 Features

- Content-based filtering approach  
- Text vectorization using ** CountVectorizer **
- Similarity calculation using **Cosine Similarity**
- User-friendly and easy-to-run Jupyter Notebook
- Scalable for large movie datasets  

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib & Seaborn  
- Jupyter Notebook  

---


---

## 📊 Dataset

The dataset contains movie-related information such as:
- Movie Title
- Genres
- Overview / Description
- Keywords

**Dataset Source:** Kaggle / TMDB  
*([Dataset can be replaced or extended easily](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata))*

---

## ⚙️ How It Works

1. Load and preprocess the movie dataset  
2. Combine important textual features  
3. Convert text data into numerical vectors  
4. Compute similarity using cosine similarity  
5. Recommend top N similar movies based on input  

---

## ▶️ How to Run the Project

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
pip install -r requirements.txt
jupyter notebook


