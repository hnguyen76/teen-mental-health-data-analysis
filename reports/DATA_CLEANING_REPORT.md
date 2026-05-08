# Data Cleaning Report

## Objective

The goal of the cleaning process was to prepare the teen mental health dataset for exploratory data analysis and visualization.

## Input And Output Files

Input:

```text
data/Teen_Mental_Health_Dataset.csv
```

Output:

```text
data/Teen_Mental_Health_cleaned.csv
```

## Initial Dataset Profile

| Metric | Value |
|---|---:|
| Rows | 1,200 |
| Columns | 13 |
| Missing values | 0 |
| Duplicate rows | 0 |

## Cleaning Steps

### 1. Column Name Standardization

Column names were standardized to a consistent snake_case style.

Examples:

- `Daily Social Media Hours` becomes `daily_social_media_hours`
- `Sleep Hours` becomes `sleep_hours`
- `Depression Label` becomes `depression_label`

### 2. Duplicate Review

Duplicate rows were checked with:

```python
df.duplicated().sum()
```

Result:

```text
0 duplicate rows
```

No duplicate rows needed to be removed.

### 3. Missing Value Review

Missing values were checked with:

```python
df.isnull().sum()
```

Result:

```text
0 missing values across all columns
```

No imputation was required for the teen dataset.

### 4. Categorical Standardization

Text categories were standardized by stripping whitespace and converting values to lowercase.

Columns cleaned:

- `gender`
- `platform_usage`
- `social_interaction_level`

Example:

```python
df["gender"] = df["gender"].str.strip().str.lower()
```

### 5. Numeric Range Validation

The following checks were performed:

```python
df[df["age"] <= 0]
df[df["daily_social_media_hours"] <= 0]
df[df["sleep_hours"] <= 0]
df[~df["depression_label"].isin([0, 1])]
```

No invalid values were found based on these checks.

## Final Dataset Profile

| Metric | Value |
|---|---:|
| Rows | 1,200 |
| Columns | 13 |
| Missing values | 0 |
| Duplicate rows | 0 |

## Export Command

The cleaned dataset was exported with:

```python
df.to_csv("data/Teen_Mental_Health_cleaned.csv", index=False)
```

Using `index=False` prevents pandas from writing the DataFrame index as an extra CSV column.

## Cleaning Conclusion

The dataset was already mostly clean. The main cleaning work involved standardizing text categories and validating that the data had no missing values, duplicate rows, or invalid numeric ranges.

