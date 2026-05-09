from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


APP_TITLE = "Teen Mental Health Dashboard"

DATA_CANDIDATES = (
    Path("Teen_Mental_Health_Cleaned.csv"),
    Path("teen_mental_health_cleaned.csv"),
    Path("data") / "Teen_Mental_Health_cleaned.csv",
    Path("data") / "Teen_Mental_Health_Cleaned.csv",
)

REQUIRED_COLUMNS = {
    "age",
    "gender",
    "daily_social_media_hours",
    "platform_usage",
    "sleep_hours",
    "screen_time_before_sleep",
    "academic_performance",
    "physical_activity",
    "social_interaction_level",
    "stress_level",
    "anxiety_level",
    "addiction_level",
    "depression_label",
}

CATEGORY_COLUMNS = ["gender", "platform_usage", "social_interaction_level"]
FILTER_COLUMNS = {
    "gender": "Gender",
    "platform_usage": "Platform",
    "social_interaction_level": "Social interaction",
}
NUMERIC_COLUMNS = [
    "age",
    "daily_social_media_hours",
    "sleep_hours",
    "screen_time_before_sleep",
    "academic_performance",
    "physical_activity",
    "stress_level",
    "anxiety_level",
    "addiction_level",
    "depression_label",
]


def find_data_file() -> Path:
    for path in DATA_CANDIDATES:
        if path.exists():
            return path

    candidates = ", ".join(str(path) for path in DATA_CANDIDATES)
    raise FileNotFoundError(f"No cleaned dataset found. Checked: {candidates}")


def load_clean_data(path: Path | None = None) -> pd.DataFrame:
    csv_path = path or find_data_file()
    df = pd.read_csv(csv_path)

    missing_columns = REQUIRED_COLUMNS.difference(df.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Dataset is missing required columns: {missing}")

    for column in CATEGORY_COLUMNS:
        df[column] = df[column].astype(str).str.strip().str.lower()

    df["depression_label"] = df["depression_label"].astype(int)
    return df.drop_duplicates().reset_index(drop=True)


def apply_filters(
    df: pd.DataFrame,
    age_range: tuple[int, int],
    category_filters: dict[str, list[str]],
    depression_labels: list[int],
) -> pd.DataFrame:
    filtered = df[df["age"].between(age_range[0], age_range[1])]

    for column, selected_values in category_filters.items():
        if selected_values:
            filtered = filtered[filtered[column].isin(selected_values)]

    if depression_labels:
        filtered = filtered[filtered["depression_label"].isin(depression_labels)]

    return filtered.reset_index(drop=True)


def pct(value: float, total: float) -> float:
    if total == 0:
        return 0.0
    return value / total * 100


def format_percent(value: float) -> str:
    return f"{value:.1f}%"


def label_title(value: object) -> str:
    return str(value).replace("_", " ").title()


def build_sidebar_filters(st, df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Filters")

    min_age = int(df["age"].min())
    max_age = int(df["age"].max())
    age_range = st.sidebar.slider("Age range", min_age, max_age, (min_age, max_age))

    category_filters: dict[str, list[str]] = {}
    for column, label in FILTER_COLUMNS.items():
        options = sorted(df[column].dropna().unique().tolist())
        category_filters[column] = st.sidebar.multiselect(
            label,
            options=options,
            default=options,
            format_func=label_title,
        )

    label_options = sorted(df["depression_label"].dropna().unique().astype(int).tolist())
    selected_labels = st.sidebar.multiselect(
        "Depression label",
        options=label_options,
        default=label_options,
        format_func=lambda value: f"Label {value}",
    )

    st.sidebar.caption(
        "The depression label is a dataset indicator, not a clinical diagnosis."
    )

    return apply_filters(df, age_range, category_filters, selected_labels)


def render_kpis(st, df: pd.DataFrame) -> None:
    records = len(df)
    label_one_count = int((df["depression_label"] == 1).sum())
    low_sleep_count = int((df["sleep_hours"] < 8).sum())

    metrics = [
        ("Records", f"{records:,}"),
        ("Label 1 rate", format_percent(pct(label_one_count, records))),
        ("Avg sleep", f"{df['sleep_hours'].mean():.2f} hrs"),
        ("Avg social media", f"{df['daily_social_media_hours'].mean():.2f} hrs"),
        ("Sleep under 8 hrs", format_percent(pct(low_sleep_count, records))),
    ]

    for column, (label, value) in zip(st.columns(len(metrics)), metrics):
        column.metric(label, value)


def add_bar_labels(ax) -> None:
    for container in ax.containers:
        ax.bar_label(container, fmt="%.2f", padding=3)


def plot_count_bar(df: pd.DataFrame, column: str, title: str, xlabel: str):
    counts = df[column].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(x=counts.index.astype(str), y=counts.values, ax=ax, color="#4C78A8")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Records")
    ax.bar_label(ax.containers[0], fmt="%d", padding=3)
    sns.despine()
    fig.tight_layout()
    return fig


def plot_platform_bar(df: pd.DataFrame):
    counts = df["platform_usage"].value_counts()
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(
        x=[label_title(value) for value in counts.index],
        y=counts.values,
        ax=ax,
        palette=["#4C78A8", "#F58518", "#54A24B"],
        hue=[label_title(value) for value in counts.index],
        legend=False,
    )
    ax.set_title("Platform Usage")
    ax.set_xlabel("Platform")
    ax.set_ylabel("Records")
    ax.bar_label(ax.containers[0], fmt="%d", padding=3)
    sns.despine()
    fig.tight_layout()
    return fig


def plot_sleep_histogram(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df["sleep_hours"], bins=10, kde=True, ax=ax, color="#72B7B2")
    ax.axvline(df["sleep_hours"].mean(), color="#E45756", linewidth=2, label="Mean")
    ax.set_title("Sleep Hours Distribution")
    ax.set_xlabel("Sleep hours")
    ax.set_ylabel("Records")
    ax.legend()
    sns.despine()
    fig.tight_layout()
    return fig


def plot_social_sleep_scatter(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="daily_social_media_hours",
        y="sleep_hours",
        hue="depression_label",
        palette={0: "#4C78A8", 1: "#E45756"},
        alpha=0.65,
        ax=ax,
    )
    ax.set_title("Social Media Hours vs Sleep Hours")
    ax.set_xlabel("Daily social media hours")
    ax.set_ylabel("Sleep hours")
    ax.legend(title="Depression label")
    sns.despine()
    fig.tight_layout()
    return fig


def plot_stress_anxiety_heatmap(df: pd.DataFrame):
    table = pd.crosstab(df["anxiety_level"], df["stress_level"])
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(table, cmap="YlGnBu", annot=True, fmt="d", ax=ax)
    ax.set_title("Stress vs Anxiety Count")
    ax.set_xlabel("Stress level")
    ax.set_ylabel("Anxiety level")
    fig.tight_layout()
    return fig


def plot_correlation_heatmap(df: pd.DataFrame):
    corr = df[NUMERIC_COLUMNS].corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.heatmap(corr, cmap="RdBu_r", center=0, annot=True, fmt=".2f", ax=ax)
    ax.set_title("Numeric Correlation Matrix")
    fig.tight_layout()
    return fig


def plot_group_comparison(df: pd.DataFrame, value_column: str, title: str, ylabel: str):
    grouped = (
        df.groupby("depression_label", as_index=False)[value_column]
        .mean()
        .sort_values("depression_label")
    )

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(
        data=grouped,
        x="depression_label",
        y=value_column,
        ax=ax,
        hue="depression_label",
        palette={0: "#4C78A8", 1: "#E45756"},
        legend=False,
    )
    ax.set_title(title)
    ax.set_xlabel("Depression label")
    ax.set_ylabel(ylabel)
    add_bar_labels(ax)
    sns.despine()
    fig.tight_layout()
    return fig


def render_overview(st, df: pd.DataFrame) -> None:
    left, right = st.columns(2)
    left.pyplot(plot_count_bar(df, "depression_label", "Depression Label Count", "Label"))
    right.pyplot(plot_platform_bar(df))
    st.pyplot(plot_sleep_histogram(df))


def render_lifestyle(st, df: pd.DataFrame) -> None:
    left, right = st.columns(2)
    left.pyplot(plot_social_sleep_scatter(df))
    right.pyplot(plot_stress_anxiety_heatmap(df))
    st.pyplot(plot_correlation_heatmap(df))


def render_depression_comparison(st, df: pd.DataFrame) -> None:
    comparison_columns = [
        "daily_social_media_hours",
        "sleep_hours",
        "stress_level",
        "anxiety_level",
        "addiction_level",
        "academic_performance",
    ]
    summary = df.groupby("depression_label")[comparison_columns].mean().round(2)
    summary["records"] = df.groupby("depression_label").size()

    st.dataframe(summary, width="stretch")

    left, right = st.columns(2)
    left.pyplot(
        plot_group_comparison(
            df,
            "daily_social_media_hours",
            "Average Social Media Hours by Label",
            "Average hours",
        )
    )
    right.pyplot(
        plot_group_comparison(
            df,
            "sleep_hours",
            "Average Sleep Hours by Label",
            "Average hours",
        )
    )

    left, right = st.columns(2)
    left.pyplot(
        plot_group_comparison(
            df,
            "stress_level",
            "Average Stress Level by Label",
            "Average score",
        )
    )
    right.pyplot(
        plot_group_comparison(
            df,
            "anxiety_level",
            "Average Anxiety Level by Label",
            "Average score",
        )
    )


def render_data_table(st, df: pd.DataFrame) -> None:
    st.dataframe(df, width="stretch", hide_index=True)
    st.download_button(
        "Download filtered CSV",
        df.to_csv(index=False).encode("utf-8"),
        file_name="teen_mental_health_filtered.csv",
        mime="text/csv",
    )


def render_context_notes(st, df: pd.DataFrame) -> None:
    label_one = int((df["depression_label"] == 1).sum())
    label_zero = int((df["depression_label"] == 0).sum())

    if label_one == 0 or label_zero == 0:
        st.info("The current filter contains only one depression label group.")
        return

    grouped = df.groupby("depression_label").mean(numeric_only=True)
    social_gap = grouped.loc[1, "daily_social_media_hours"] - grouped.loc[
        0, "daily_social_media_hours"
    ]
    sleep_gap = grouped.loc[1, "sleep_hours"] - grouped.loc[0, "sleep_hours"]
    stress_gap = grouped.loc[1, "stress_level"] - grouped.loc[0, "stress_level"]

    st.info(
        "In the current filter, label 1 averages "
        f"{social_gap:+.2f} more social media hours, "
        f"{sleep_gap:+.2f} sleep hours, and "
        f"{stress_gap:+.2f} stress score points compared with label 0. "
        "These are descriptive differences only."
    )


def main() -> None:
    import streamlit as st

    st.set_page_config(page_title=APP_TITLE, layout="wide")
    sns.set_theme(style="whitegrid")

    st.title(APP_TITLE)
    st.caption(
        "Interactive EDA dashboard for teen social media, sleep, academic, and "
        "mental-health-related indicators."
    )

    try:
        source_path = find_data_file()
        df = load_clean_data(source_path)
    except (FileNotFoundError, ValueError) as exc:
        st.error(str(exc))
        st.stop()

    filtered = build_sidebar_filters(st, df)
    st.caption(f"Source: `{source_path}`")

    if filtered.empty:
        st.warning("No records match the selected filters.")
        st.stop()

    render_kpis(st, filtered)
    render_context_notes(st, filtered)

    overview_tab, lifestyle_tab, comparison_tab, data_tab = st.tabs(
        ["Overview", "Lifestyle Signals", "Label Comparison", "Data"]
    )

    with overview_tab:
        render_overview(st, filtered)

    with lifestyle_tab:
        render_lifestyle(st, filtered)

    with comparison_tab:
        render_depression_comparison(st, filtered)

    with data_tab:
        render_data_table(st, filtered)

    st.caption(
        "This dashboard is for exploratory analysis and learning. It should not "
        "be used as medical advice."
    )


if __name__ == "__main__":
    main()
