# Statement of Work: Teen Mental Health EDA

## 1. Project Title

Teen Mental Health Exploratory Data Analysis

## 2. Objective

The objective of this project is to perform a structured exploratory data analysis on a teen mental health dataset. The analysis focuses on understanding patterns across social media usage, sleep hours, screen time before sleep, academic performance, physical activity, stress, anxiety, addiction level, and depression label.

## 3. Scope

In scope:

- Load and inspect raw CSV data.
- Standardize column names and categorical values.
- Validate missing values, duplicate records, and numeric ranges.
- Export a cleaned CSV file.
- Perform descriptive statistical analysis.
- Create visualizations for distributions and relationships.
- Summarize findings in GitHub-ready reports.

Out of scope:

- Clinical diagnosis or medical recommendations.
- Predictive machine learning models.
- Causal inference.
- External data enrichment.
- Deployment of a web application or dashboard.

## 4. Dataset

Primary raw dataset:

```text
data/Teen_Mental_Health_Dataset.csv
```

Cleaned output dataset:

```text
data/Teen_Mental_Health_cleaned.csv
```

Dataset size after cleaning:

- Rows: 1,200
- Columns: 13
- Missing values: 0
- Duplicate rows: 0

## 5. Deliverables

| Deliverable | File |
|---|---|
| Project README | `README.md` |
| Cleaning notebook | `EDA_teen_cleaning_data.ipynb` |
| Visualization notebook | `teen_visiualize.ipynb` |
| Cleaned dataset | `data/Teen_Mental_Health_cleaned.csv` |
| Data dictionary | `reports/DATA_DICTIONARY.md` |
| Data cleaning report | `reports/DATA_CLEANING_REPORT.md` |
| EDA report | `reports/EDA_REPORT.md` |
| Visualization report | `reports/VISUALIZATION_REPORT.md` |

## 6. Methodology

1. Data ingestion
   - Load the CSV file with pandas.
   - Review shape, columns, data types, and sample records.

2. Data quality review
   - Check missing values.
   - Check duplicate records.
   - Inspect categorical value consistency.
   - Validate numeric ranges.

3. Data cleaning
   - Standardize column names.
   - Standardize categorical values to lowercase.
   - Convert relevant columns to numeric values where needed.
   - Export the cleaned dataset.

4. Exploratory data analysis
   - Generate summary statistics.
   - Compare group averages by `depression_label`.
   - Analyze academic performance thresholds.
   - Review selected correlations.

5. Visualization
   - Build bar charts for category counts and averages.
   - Build histograms for numeric distributions.
   - Build scatter plots and heatmaps for variable relationships.

## 7. Success Criteria

The project is complete when:

- The cleaned dataset is saved and reproducible.
- All reports are readable from GitHub.
- EDA findings are supported by dataset metrics.
- Visualizations are interpretable.
- Limitations are clearly documented.

## 8. Assumptions

- The source dataset is already anonymized.
- `depression_label` is a binary label where `0` and `1` represent two dataset classes.
- Numeric scales such as stress, anxiety, and addiction are treated as ordinal score-like features.
- The analysis is descriptive and does not establish causation.

## 9. Risks And Limitations

- The depression label is highly imbalanced: only 31 of 1,200 records are label `1`.
- Small group size for label `1` may make averages unstable.
- Self-reported behavioral data can contain measurement bias.
- The dataset does not provide enough context to make clinical conclusions.

## 10. Tools

- Python
- pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

