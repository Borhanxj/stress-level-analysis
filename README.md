# **Stress Level Analysis Based on Socioeconomic and Environmental Factors**

A data science project analyzing the relationship between stress levels and socioeconomic & environmental factors such as temperature, rainfall, unemployment rates, salary distribution, demographics, and more. Using statistical analysis and machine learning to uncover patterns and predictive insights.

---

## **Project Overview**
This project explores how external factors—including economic indicators and climate conditions—impact stress levels. By analyzing data from multiple sources, I aim to identify key contributors to stress and develop predictive insights.

### **Key Research Questions**
- How do unemployment rates and salary distribution impact reported stress levels?
- Do environmental conditions (temperature, rainfall, pollution) correlate with higher stress levels?
- Are there regional or demographic differences in stress patterns?

---

## **Motivation**
Stress is a major public health issue worldwide. Recent surveys have highlighted increasing stress levels, particularly among younger populations. Countries like South Korea and Turkey report some of the highest stress levels globally. Economic instability and climate conditions might play a role, and this project aims to explore these connections.
([Statista](https://www.statista.com/statistics/1057961/the-most-stressed-out-populations-worldwide/?utm_source=chatgpt.com))

---

## **Data Sources & Collection Plan**
I will collect and combine publicly available datasets to analyze stress factors.

### **Planned Datasets:**
1. **Stress-related statistics**
   - Global stress indices (e.g., WHO, Gallup)
   - Mental health surveys

2. **Weather Conditions**
   - Temperature, precipitation, pollution (NOAA, NASA, local meteorological data)

3. **Economic Indicators**
   - Unemployment rates (World Bank, IMF)
   - Salary distribution (OECD, National Statistics)
   - Cost of living indices

### **Data Enrichment Plan**
- Cross-referencing stress levels with socioeconomic and weather data.
- Aggregating data at regional/national levels.
- Handling missing values and inconsistencies.

---

## **Methodology**
1. **Exploratory Data Analysis (EDA)**
   - Data cleaning, preprocessing, and visualization.
   - Correlation analysis to identify patterns.

2. **Hypothesis Testing & Statistical Analysis**
   - T-tests, ANOVA, and regression models.

3. **Machine Learning Approaches**
   - Clustering (e.g., K-Means) for stress pattern grouping.
   - Regression (e.g., Random Forest, XGBoost) for predicting stress levels.

---

## **Project Timeline**
| Date | Task |
|------|------|
| **March 10** | Submit project proposal (GitHub README) |
| **April 18** | Collect and clean data, perform EDA |
| **May 23** | Implement machine learning models |
| **May 30** | Final submission (GitHub repository) |

---

## **Tools & Technologies**
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
- **Version Control:** GitHub  
- **Data Sources:** WHO, NOAA, World Bank, OECD, NASA  

---

## **Reproducibility**
- **Data Format:** CSV files stored in `/data/` directory.
- **Code Structure:**
/stress-level-analysis ├── data/ # Raw & processed datasets ├── notebooks/ # Jupyter notebooks for EDA & modeling ├── src/ # Python scripts for data processing ├── models/ # Saved ML models ├── README.md # Project documentation ├── requirements.txt # List of dependencies

- **Setup Instructions:**
1. Clone the repository:
   ```
   git clone https://github.com/Borhanxj/stress-level-analysis.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run initial analysis:
   ```
   python src/data_preprocessing.py
   ```

---

_"This README was structured with guidance from ChatGPT to ensure clarity and completeness."_
