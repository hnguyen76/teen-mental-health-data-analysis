# Visualization Report

## Objective

The visualization notebook explores patterns in the cleaned teen mental health dataset using pandas, Matplotlib, and Seaborn.

Notebook:

```text
teen_visiualize.ipynb
```

## Visualizations Included

### 1. Depression Label Count

Chart type: bar chart

Purpose:

- Show the number of records for each depression label.
- Identify label imbalance.

Interpretation:

- Label `0` is the majority class.
- Label `1` is a small minority class with 31 records.

### 2. Average Social Media Hours By Depression Label

Chart type: bar chart

Purpose:

- Compare average daily social media usage between depression labels.

Observed result:

| Depression Label | Average Daily Social Media Hours |
|---:|---:|
| 0 | 4.48 |
| 1 | 6.72 |

Interpretation:

- Records with label `1` show higher average daily social media hours.

### 3. Sleep Hours Distribution

Chart type: histogram

Purpose:

- Show how sleep hours are distributed across the dataset.

How to read it:

- The x-axis shows sleep hour ranges.
- The y-axis shows how many records fall into each range.
- A histogram groups numeric values into bins; it does not display individual records one by one.

Observed summary:

- Average sleep hours: 6.45
- Median sleep hours: 6.50
- 25th to 75th percentile range: 5.2 to 7.6

### 4. Stress vs Anxiety

Chart type: scatter plot

Purpose:

- Show the relationship between stress level and anxiety level.

How to read it:

- Each point represents one or more records.
- The x-axis is stress level.
- The y-axis is anxiety level.
- Since both features use integer scores from 1 to 10, many records overlap at the same points.

Recommended improvement:

```python
plt.scatter(df["stress_level"], df["anxiety_level"], alpha=0.3)
```

The `alpha` value makes overlapping points easier to interpret.

### 5. Stress vs Anxiety Heatmap

Chart type: heatmap

Purpose:

- Show how many records exist for each stress-anxiety score combination.

Recommended code:

```python
table = pd.crosstab(df["anxiety_level"], df["stress_level"])

sns.heatmap(table, cmap="Blues", annot=True, fmt="d")
plt.title("Stress vs Anxiety Count")
plt.xlabel("Stress Level")
plt.ylabel("Anxiety Level")
plt.show()
```

How to read it:

- Choose any cell.
- The x-axis gives the stress score.
- The y-axis gives the anxiety score.
- The number in the cell is the count of records with that exact combination.
- Darker color means more records.

### 6. Average Sleep Hours By Depression Label

Chart type: bar chart

Purpose:

- Compare average sleep duration between depression labels.

Recommended code with labels:

```python
avg_sleep = (
    df.groupby("depression_label")["sleep_hours"]
    .mean()
)

ax = avg_sleep.plot(kind="bar", edgecolor="black")
ax.bar_label(ax.containers[0], fmt="%.2f", padding=3)

plt.title("Average Sleep Hours by Depression")
plt.xlabel("Depression label")
plt.ylabel("Average Sleep Hours")
plt.ylim(0, avg_sleep.max() + 1)
plt.show()
```

Observed result:

| Depression Label | Average Sleep Hours |
|---:|---:|
| 0 | 6.49 |
| 1 | 4.76 |

## Visualization Best Practices Used

- Clear chart titles.
- Labeled x-axis and y-axis.
- Bar labels for exact values where helpful.
- Transparency for scatter plots with overlapping points.
- Heatmap annotations for easier count interpretation.

## Visualization Limitations

- Scatter plots can hide overlapping points.
- Bar charts show averages but not distribution shape.
- Small sample size for depression label `1` can make comparisons unstable.
- Visual patterns should be validated with summary statistics.

