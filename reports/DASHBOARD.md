# Teen Mental Health Dashboard

This is a GitHub-friendly static dashboard generated from `Teen_Mental_Health_Cleaned.csv`. GitHub cannot run Streamlit apps inside the repository file view, so this page saves the dashboard charts as PNG images that can be viewed directly on GitHub.

## KPI Summary

| Metric | Value |
|---|---:|
| Records | 1,200 |
| Columns | 13 |
| Average daily social media hours | 4.54 |
| Average sleep hours | 6.45 |
| Sleep under 8 hours | 80.17% |
| Depression label 1 records | 31 |
| Depression label 1 rate | 2.58% |
| Academic performance above 3.5 | 285 (23.75%) |

## Label Comparison

| Depression label | Records | Avg social media hours | Avg sleep hours | Avg stress | Avg anxiety |
|---:|---:|---:|---:|---:|---:|
| 0 | 1,169 | 4.48 | 6.49 | 5.37 | 5.56 |
| 1 | 31 | 6.72 | 4.76 | 8.48 | 8.61 |

## Overview Charts

![Depression label count](figures/depression_label_count.png)

![Platform usage](figures/platform_usage.png)

![Sleep distribution](figures/sleep_distribution.png)

## Lifestyle Signals

![Stress vs anxiety heatmap](figures/stress_anxiety_heatmap.png)

![Correlation heatmap](figures/correlation_heatmap.png)

## Depression Label Differences

![Average social media hours by label](figures/avg_social_media_by_label.png)

![Average sleep hours by label](figures/avg_sleep_by_label.png)

![Average stress level by label](figures/avg_stress_by_label.png)

![Average anxiety level by label](figures/avg_anxiety_by_label.png)

## Notes

- This dashboard is descriptive exploratory analysis only.
- The `depression_label` column is a dataset label, not a clinical diagnosis.
- The label 1 group is small, so comparisons should be interpreted carefully.
- Run the interactive version locally with `streamlit run dashboard.py`.
