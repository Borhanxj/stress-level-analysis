# **Stress Level Analysis Based on Socioeconomic and Environmental Factors**

A data science project analyzing the relationship between **stress levels** and **socioeconomic & environmental factors** such as temperature, unemployment rates, salary distribution, cost of living, and demographics. Using statistical analysis and machine learning to uncover patterns and predictive insights.

---

## **📌 Project Overview**
This project explores how external factors—including **economic indicators and climate conditions**—impact stress levels. By analyzing data from multiple sources, I aim to **identify key contributors to stress and develop predictive models**.

### **Key Research Questions**
- How do **unemployment rates and salary distribution** impact reported stress levels?
- Do **environmental conditions** (temperature, rainfall, pollution) correlate with higher stress levels?
- Are there **regional or demographic differences** in stress patterns?
- Does the **cost of living** influence mental health outcomes?

---

## **📌 Motivation**
Stress is something many of us experience, but it's also becoming a major public health issue worldwide.  
A recent survey ranked it just behind **cancer and mental health** as one of the biggest concerns, with countries like **South Korea and Turkey** reporting especially high levels.  
Younger people are often more affected, but even a significant number of older adults struggle with stress.  
This makes me wonder—**what’s driving this rise in stress?**  
Could factors like **economic instability or climate conditions** play a role?  
**That’s what I want to explore in this project.**  
([Statista](https://www.statista.com/statistics/1057961/the-most-stressed-out-populations-worldwide/?utm_source=chatgpt.com))

---

## **📌 Project Scope**
### **Country as a Parameter**
Instead of limiting the analysis to specific countries, this project considers **all available regions** in the dataset and uses **country as a parameter** in analysis. However, **comparisons will focus on**:
- 🇺🇸 **United States**
- 🇩🇪 **Germany**
- 🇰🇷 **South Korea**

This approach provides **flexibility** while still allowing deeper regional insights.

### **Comparison Factors**
- **Economic Factors:** Salary distribution, unemployment, cost of living.
- **Environmental Factors:** Temperature, precipitation, air pollution.
- **Demographic Trends:** Stress levels by age, gender, and location.

This ensures a **broad but structured** analysis.

---

## **📌 Datasets & Parameters**
This project integrates multiple datasets to analyze stress levels in relation to external factors.

### **1️⃣ Mental Health & Stress Dataset**
📂 **File:** `Stress_Data.csv`  
📌 **Source:** Kaggle Mental Health Dataset  
📌 **Includes:** Stress levels, mental health conditions, work-life balance.  
📌 **Covers:** Multiple countries (Country is a parameter).  

### **2️⃣ Gallup Stress Survey**
📂 **File:** `Gallup_Stress_Report_2024.pdf`  
📌 **Source:** Gallup Global Emotions Report  
📌 **Includes:** Global stress trends based on survey data.  
📌 **Covers:** Multiple countries.  

### **3️⃣ Weather & Climate Dataset**
📂 **File:** `Weather_Data.csv`  
📌 **Source:** Kaggle Weather Dataset  
📌 **Includes:** Temperature, precipitation, pollution levels.  
📌 **Covers:** Multiple countries (Country is a parameter).  

### **4️⃣ Economic Indicators**
#### **a. Quality of Life (U.S. Specific)**
📂 **File:** `Quality_of_Life_US.csv`  
📌 **Source:** Kaggle - U.S. Statewise Quality of Life Index  
📌 **Includes:** Cost of living, employment rates, and economic conditions.  
📌 **Covers:** United States (state-level).  

#### **b. Global Economic Data**
📂 **File:** `World_Economic_Data.csv`  
📌 **Source:** Kaggle - World Data 2023  
📌 **Includes:** GDP, income levels, unemployment rates.  
📌 **Covers:** Multiple countries (Country is a parameter).  

#### **c. Income Distribution (OECD)**
📂 **File:** `OECD_Income_Data.pdf`  
📌 **Source:** OECD Income Distribution Database  
📌 **Includes:** Salary distribution, income inequality.  
📌 **Covers:** Multiple countries (requires data extraction).  

---

## 📌 Hypotheses based on visualizations

### 1️⃣ Social Media Expression Mirrors Psychological Strain  
📂 **Dataset:** `social_media_stress.csv`  
📊 **Visualization:** Violin plots — Likes, Comments & DMs vs Emotion

> Users who express **anxiety** or **sadness** tend to engage more through **DMs and comments** rather than passive actions like liking.  
> This may indicate a higher **emotional need for interaction**, suggesting that the **type of engagement**, not just frequency, reflects underlying stress.

---

### 2️⃣ Culture May Buffer Against Economic Stress  
📂 **Dataset:** `gallup_emotion_data_2023.csv`, `oecd_income_sample.csv`  
📊 **Visualization:** Emotion Heatmap + OECD Income Overlay

> Some **low-income countries** (e.g., **Vietnam**) report **high positive emotional scores**, indicating that **cultural or social resilience** may **offset the psychological impact** of economic hardship.  
> This suggests that **income alone does not predict stress**, and **cultural context plays a critical role** in emotional well-being.

---

## **📊 Data Collection & EDA**

### 🧼 Data Cleaning Summary

Before performing exploratory data analysis (EDA), we applied structured cleaning operations across all datasets to ensure consistency and reliability:

#### ✅ `social_media_stress.csv`
- Converted `Age` column to numeric format
- Removed rows with missing or invalid age values
- Cleaned dataset used to analyze usage time and engagement patterns by emotion

#### ✅ `Stress_Data.csv`
- Preserved full data but grouped by `Country` to calculate proportions of stress levels (`Low`, `Medium`, `High`)
- Used for country-level comparisons and merged with economic indicators

#### ✅ `World_Economic_Data.csv`
- Removed percentage symbols and commas from fields such as `Unemployment rate`, `CPI`, `Life expectancy`, and `Tax revenue (%)`
- Converted cleaned columns to numeric types
- Prepared for merging with stress summaries to enable correlation analysis

#### ✅ `Gallup_Stress_Report_2024.pdf`
- Extracted emotional indicators like `Stress`, `Worry`, `Anger`, `Sadness`, `Loneliness` and global experience indices
- Manually converted structured values into tabular form
- Saved as `gallup_emotion_data_2023.csv` for further use

#### ✅ `OECD_Income_Data.pdf`
- Sample disposable income values were extracted for selected countries
- Used to support high-level comparison between income and emotional health patterns

---

### 🔗 Merged Dataset Overview

We created a merged dataset combining **country-level stress proportions** from `Stress_Data.csv` with **economic indicators** from `World_Economic_Data.csv`.

📄 **File:** `merged_stress_economics.csv`  
🧩 **Purpose:** To analyze how **economic and healthcare metrics** (e.g., life expectancy, unemployment, physician density) correlate with the **proportion of people reporting high stress**.

This merged dataset was the foundation for our **correlation heatmap** and multiple cross-variable analyses.


---

### 📊 EDA: Daily Usage Time vs Dominant Emotion

📂 **Dataset used:** `social_media_stress.csv`

We explored how much time users spend on social media and how it relates to their dominant emotional state.

![Boxplot: Daily Usage Time by Emotion](eda/boxplot_usage_emotion.png)

---

### 🧪 EDA: Likes, Comments & DMs vs Emotion

📂 **Dataset used:** `social_media_stress.csv`

We explored how different types of social media engagement (likes, comments, and messages) vary based on users' dominant emotional state using violin plots.

📄 **Code file**: [`eda_social_engagement.py`](eda/eda_social_engagement.py)

🧠 **Insights:**
- **Happiness** and **Anxiety** show broader spread in likes and message counts
- **Anger** and **Sadness** are associated with more DMs and comment activity
- Emotional state is reflected in the quantity and variability of online engagement

![Violin Plot - Engagement vs Emotion](eda/violin_engagement_emotion.png)

---

### 🌍 EDA: Stress Level Distribution by Country

📂 **Dataset used:** `Stress_Data.csv`

We examined which countries in the dataset have the highest concentration of individuals reporting **high stress levels**.

📄 **Code file**: [`eda_country_stress_fixed.py`](eda/eda_country_stress_fixed.py)

🧠 **Insights:**
- Countries like **India**, **USA**, and **Germany** report the highest number of high-stress individuals
- Most countries also show a fairly even distribution across all stress levels
- Cultural or socioeconomic factors may be influencing this spread

![Country Stress Bar Chart](eda/country_stress_distribution_fixed.png)

---

### 🔗 EDA: Correlation Between Stress and Economic Indicators

📂 **Datasets used:** `Stress_Data.csv` + `World_Economic_Data.csv`  
📄 **Merged file:** `merged_stress_economics.csv`

We analyzed how the proportion of people reporting **high stress** correlates with various economic and health indicators across countries.

📄 **Code file**: [`eda_stress_correlation.py`](eda/eda_stress_correlation.py)

🧠 **Insights:**
- High stress levels show **negative correlation** with **life expectancy** and **physician availability**
- Stress is **positively correlated** with **unemployment** and **CPI (inflation)**
- Strong economic and healthcare systems may contribute to reduced national stress

![Stress Correlation Heatmap](eda/stress_correlation_heatmap.png)

---

### 🧠 EDA: Emotional Metrics by Country (Gallup 2023)

📂 **Dataset used:** `Gallup_Stress_Report_2024.pdf` → structured as `gallup_emotion_data_2023.csv`

We visualized five key emotional indicators from Gallup’s global survey: **stress, worry, anger, sadness, and loneliness**.

📄 **Code file**: [`eda_emotion_heatmap.py`](eda/eda_emotion_heatmap.py)

🧠 **Insights:**
- **Israel** and **Guinea** show high levels across multiple emotions
- **Vietnam** and **Canada** report notably low emotional negativity
- The heatmap allows easy country-to-country emotional comparison

![Emotion Heatmap Table](eda/emotion_heatmap_table.png)

---

## **📌 Project Timeline**
| Date | Task |
|------|------|
| **March 10** | Submit project proposal (GitHub README) |
| **April 18** | Collect and clean data, perform EDA |
| **May 23** | Implement machine learning models |
| **May 30** | Final submission (GitHub repository) |

---

📌 _**This README was structured with guidance from ChatGPT to ensure clarity and completeness.**_
