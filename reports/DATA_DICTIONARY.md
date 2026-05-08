# Data Dictionary

Dataset: `data/Teen_Mental_Health_cleaned.csv`

## Overview

The dataset contains 1,200 teen records and 13 columns. It includes demographic, digital behavior, lifestyle, academic, and mental health related variables.

## Columns

| Column | Type | Description | Example / Range |
|---|---:|---|---|
| `age` | integer | Teen age in years. | 13 to 19 |
| `gender` | categorical | Teen gender category after standardization. | `male`, `female` |
| `daily_social_media_hours` | float | Average daily social media usage in hours. | 1.0 to 8.0 |
| `platform_usage` | categorical | Main social media platform category. | `instagram`, `tiktok`, `both` |
| `sleep_hours` | float | Average sleep duration in hours. | 4.0 to 9.0 |
| `screen_time_before_sleep` | float | Screen time before sleep in hours. | 0.5 to 3.0 |
| `academic_performance` | float | Academic performance score. | 2.0 to 4.0 |
| `physical_activity` | float | Physical activity measure. | 0.0 to 2.0 |
| `social_interaction_level` | categorical | Level of social interaction. | `low`, `medium`, `high` |
| `stress_level` | integer | Stress score. | 1 to 10 |
| `anxiety_level` | integer | Anxiety score. | 1 to 10 |
| `addiction_level` | integer | Addiction score. | 1 to 10 |
| `depression_label` | integer | Binary dataset label for depression-related classification. | 0 or 1 |

## Categorical Value Counts

### Gender

| Gender | Count |
|---|---:|
| male | 615 |
| female | 585 |

### Platform Usage

| Platform | Count |
|---|---:|
| instagram | 411 |
| tiktok | 398 |
| both | 391 |

### Social Interaction Level

| Level | Count |
|---|---:|
| medium | 416 |
| low | 415 |
| high | 369 |

### Depression Label

| Label | Count | Percent |
|---:|---:|---:|
| 0 | 1,169 | 97.42% |
| 1 | 31 | 2.58% |

## Notes

- `depression_label` should be interpreted as a dataset label, not a clinical diagnosis.
- Numeric score columns should be interpreted as score-like variables, not precise clinical measurements.
- Because the label distribution is highly imbalanced, comparisons involving label `1` should be treated carefully.

