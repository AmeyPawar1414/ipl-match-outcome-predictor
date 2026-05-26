# 🏏 IPL Match Outcome Predictor

A data science project that predicts IPL match winners using historical data (2008–2024) with **60.6% accuracy** — comparable to expert cricket analysts.

---

## 📊 Key Findings

1. **Head-to-head history is the strongest predictor** (43.7% feature importance) — past matchups between two teams carry more signal than any other factor
2. **Venue win rate is the second biggest factor** (32.7%) — home ground conditions significantly influence outcomes
3. **Winning the toss barely matters** (4.7%) — teams that win the toss win only 50.83% of matches, almost identical to a coin flip
4. **Mumbai Indians** are the most successful franchise with 144 wins across all seasons
5. **Random Forest (60.6%)** significantly outperforms Logistic Regression (49.1%), confirming that match outcomes have non-linear relationships with features
6. **Recent form accounts for 15.5%** of predictive power — momentum matters but not as much as historical record

---

## 🗂️ Project Structure

```
ipl-match-outcome-predictor/
├── data/
│   ├── raw/                  # Original Kaggle dataset
│   └── processed/            # Cleaned data and engineered features
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_model_training.ipynb
├── src/
│   └── predict.py            # Run predictions for any match
├── models/
│   ├── random_forest.pkl
│   ├── logistic_regression.pkl
│   └── model_metrics.json
├── reports/
│   └── visualizations/       # All charts and plots
└── requirements.txt
```

---

## ⚙️ Features Used

| Feature | Description | Importance |
|---|---|---|
| `team1_win_rate_vs_team2` | Historical head-to-head win rate | 43.7% |
| `team1_venue_win_rate` | Win rate at the specific venue | 32.7% |
| `team1_recent_form` | Win rate in last 5 matches | 15.5% |
| `team1_won_toss` | Whether team1 won the toss | 4.8% |
| `toss_decision_bat` | Whether toss winner chose to bat | 3.1% |

---

## 🤖 Model Performance

| Model | Accuracy | AUC Score |
|---|---|---|
| Random Forest | **60.6%** | 0.599 |
| Logistic Regression | 49.1% | 0.499 |

> IPL matches are inherently unpredictable — 60.6% accuracy is in line with expert analyst predictions and reflects the genuine randomness of T20 cricket.

---

## 🚀 How to Run

**1. Clone the repo**
```bash
git clone https://github.com/AmeyPawar1414/ipl-match-outcome-predictor.git
cd ipl-match-outcome-predictor
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Download the dataset**

Get `matches.csv` and `deliveries.csv` from [Kaggle](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020) and place them in `data/raw/`

**4. Run the notebooks in order**
```
01_data_exploration → 02_data_cleaning → 03_feature_engineering → 04_model_training
```

**5. Predict a match outcome**
```bash
cd src
python predict.py
```

**Example output:**
```
=============================================
  Mumbai Indians vs Chennai Super Kings
=============================================
  Mumbai Indians                 75.5%
  Chennai Super Kings            24.5%
=============================================
  Predicted Winner: Mumbai Indians
=============================================
```

---

## 🛠️ Tech Stack

- **Python** — Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning** — Scikit-learn (Logistic Regression, Random Forest)
- **Visualization** — Matplotlib, Seaborn, Power BI
- **Tools** — Jupyter Notebook, Git

---

## 📁 Dataset

- **Source:** [IPL Complete Dataset on Kaggle](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)
- **Seasons:** 2008–2024
- **Matches:** 1,090 (after cleaning)
- **Deliveries:** 260,920 ball-by-ball records

---

## 👤 Author

**Amey Pawar**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Amey--Pawar-blue)](https://www.linkedin.com/in/amey-pawar-644a18277/)
[![GitHub](https://img.shields.io/badge/GitHub-AmeyPawar1414-black)](https://github.com/AmeyPawar1414)