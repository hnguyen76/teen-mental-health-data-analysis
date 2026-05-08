# Exploratory Data Analysis Report

## Objective

This report summarizes exploratory findings from the teen mental health dataset. The goal is to understand basic distributions and relationships between lifestyle, social media usage, sleep, academic performance, stress, anxiety, addiction level, and depression label.

## Dataset Summary

| Metric | Value |
|---|---:|
| Rows | 1,200 |
| Columns | 13 |
| Missing values | 0 |
| Duplicate rows | 0 |
| Age range | 13 to 19 |

## Numeric Summary

| Variable | Mean | Std | Min | Median | Max |
|---|---:|---:|---:|---:|---:|
| `age` | 15.93 | 2.02 | 13.00 | 16.00 | 19.00 |
| `daily_social_media_hours` | 4.54 | 2.03 | 1.00 | 4.50 | 8.00 |
| `sleep_hours` | 6.45 | 1.44 | 4.00 | 6.50 | 9.00 |
| `screen_time_before_sleep` | 1.74 | 0.72 | 0.50 | 1.80 | 3.00 |
| `academic_performance` | 2.99 | 0.58 | 2.00 | 2.99 | 4.00 |
| `physical_activity` | 1.01 | 0.58 | 0.00 | 1.00 | 2.00 |
| `stress_level` | 5.45 | 2.90 | 1.00 | 5.00 | 10.00 |
| `anxiety_level` | 5.64 | 2.86 | 1.00 | 6.00 | 10.00 |
| `addiction_level` | 5.57 | 2.83 | 1.00 | 6.00 | 10.00 |

## Depression Label Distribution

| Depression Label | Count | Percent |
|---:|---:|---:|
| 0 | 1,169 | 97.42% |
| 1 | 31 | 2.58% |

The dataset is highly imbalanced. Only 31 records belong to label `1`, so any comparison involving this group should be interpreted carefully.

## Sleep Insights

Average sleep duration is approximately 6.45 hours.

| Sleep Segment | Percent |
|---|---:|
| Under 6 hours | 40.00% |
| 6 to 8 hours | 42.83% |
| Under 8 hours | 80.17% |

Interpretation:

- Most teens in the dataset sleep below 8 hours.
- The central range from the 25th to 75th percentile is approximately 5.2 to 7.6 hours.

## Depression Label Group Comparison

### Average Daily Social Media Hours

| Depression Label | Average Daily Social Media Hours |
|---:|---:|
| 0 | 4.48 |
| 1 | 6.72 |

### Average Sleep Hours

| Depression Label | Average Sleep Hours |
|---:|---:|
| 0 | 6.49 |
| 1 | 4.76 |

### Average Stress, Anxiety, And Addiction Scores

| Depression Label | Stress | Anxiety | Addiction |
|---:|---:|---:|---:|
| 0 | 5.37 | 5.56 | 5.57 |
| 1 | 8.48 | 8.61 | 5.32 |

Interpretation:

- Label `1` has higher average daily social media use than label `0`.
- Label `1` has lower average sleep hours than label `0`.
- Label `1` has higher average stress and anxiety scores than label `0`.
- Addiction score is similar across labels in this dataset.

Because the label `1` group has only 31 records, these findings should be treated as descriptive signals, not final conclusions.

## Academic Performance Insights

Academic performance has:

- Mean: 2.99
- Median: 2.99
- Min: 2.00
- Max: 4.00
- 75th percentile: 3.48

Records with academic performance above 3.5:

| Metric | Value |
|---|---:|
| Count | 285 |
| Percent | 23.75% |

Gender distribution for academic performance above 3.5:

| Gender | Count |
|---|---:|
| female | 151 |
| male | 134 |

Age distribution for academic performance above 3.5:

| Age | Count |
|---:|---:|
| 13 | 52 |
| 14 | 41 |
| 15 | 36 |
| 16 | 32 |
| 17 | 43 |
| 18 | 37 |
| 19 | 44 |

## Correlation Highlights

Selected correlations with `depression_label`:

| Feature | Correlation |
|---|---:|
| `daily_social_media_hours` | 0.175 |
| `sleep_hours` | -0.191 |
| `stress_level` | 0.170 |
| `anxiety_level` | 0.170 |
| `addiction_level` | -0.014 |
| `academic_performance` | 0.001 |

Interpretation:

- Depression label has a small positive correlation with daily social media hours, stress level, and anxiety level.
- Depression label has a small negative correlation with sleep hours.
- Academic performance has almost no linear relationship with depression label in this dataset.
- These correlations are weak and descriptive; they do not prove causation.

## Recommendations For Next Analysis

- Use boxplots to compare sleep and social media hours by depression label.
- Use heatmaps or crosstabs to understand stress and anxiety combinations.
- Consider label imbalance before building any predictive model.
- If modeling is added later, evaluate with metrics suitable for imbalanced data, such as precision, recall, F1-score, and ROC-AUC.

## Conclusion

The dataset suggests that teens labeled with depression label `1` tend to have lower sleep hours and higher social media usage, stress, and anxiety scores. However, the label `1` group is small, so findings should be treated as early EDA observations rather than definitive conclusions.

