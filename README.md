# Titanic Dataset Analysis

## 📊 Project Overview  
This project performs an exploratory data analysis (EDA) on the Titanic dataset using Python libraries such as **Pandas**, **Matplotlib**, and **Seaborn**. It covers steps from data preprocessing to visualizations that uncover key survival trends based on demographic and class-based factors.

---

## 🛠️ Dependencies

Make sure you have the following dependencies installed:

- Python 3.x  
- pandas  
- matplotlib  
- seaborn

You can install all dependencies via pip:

```bash
pip install pandas matplotlib seaborn
```

---


## 🔍 Features & Code Highlights

- ✅ **Dataset Loading**  
   Loads the Titanic dataset from a CSV file using `pandas.read_csv()`.

- 🔧 **Data Cleaning**  
   Handles missing values in key columns:
   - `Age`: Imputed using median values.
   - `Cabin`: Column dropped due to high missing data.
   - `Embarked`: Filled with the most common port of embarkation.

- 📊 **Data Visualization**  
   Utilizes `matplotlib` and `seaborn` to create insightful visualizations:
   - Survival rates by **age group**
   - Survival distribution by **sex**
   - Analysis by **passenger class (Pclass)**
   - Impact of **family size** on survival
   - Correlation heatmaps

---

## 📈 Results & Insights

Explore the visualizations to uncover patterns in survival based on:

- Gender: Females had a higher survival rate.
- Class: First-class passengers had better chances of survival.
- Age: Younger passengers showed better survival rates.
- Embarked Port: Location also had an influence on survival.

These findings help illustrate the factors that influenced survival during the Titanic disaster.

---


## 📌 Notes

- Make sure the Titanic CSV file is available in the same directory as the script or adjust the file path accordingly.
- You can use [Kaggle Titanic dataset](https://www.kaggle.com/c/titanic/data) for input data.
