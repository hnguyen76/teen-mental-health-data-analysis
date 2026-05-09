from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


APP_TITLE = "Teen Mental Health Dashboard"
AUTHOR_LINE = "Created by Hieu Nguyen"
APP_SUBTITLE = (
    "Exploratory view of teen social media habits, sleep, school performance, "
    "and mental-health-related indicators."
)

CARD_COLORS = ["#2563EB", "#0F766E", "#F97316", "#7C3AED", "#16A34A"]
ACCENT_RED = "#DC2626"
INK = "#172033"
MUTED = "#64748B"
GRID = "#E7ECF4"
PANEL_BG = "#FFFFFF"

DASHBOARD_CSS = """
<style>
    :root {
        --ink: #172033;
        --muted: #64748B;
        --line: #E2E8F0;
        --panel: #FFFFFF;
        --page: #F6F8FB;
        --blue: #2563EB;
        --teal: #0F766E;
        --orange: #F97316;
    }

    .stApp {
        background: var(--page);
        color: var(--ink);
    }

    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 2.5rem;
        max-width: 1280px;
    }

    [data-testid="stSidebar"] {
        background: var(--panel);
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: var(--ink);
    }

    .creator-bar {
        color: var(--muted);
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0;
        margin-bottom: 0.75rem;
        text-transform: uppercase;
    }

    .dashboard-hero {
        background: linear-gradient(135deg, #172033 0%, #245C6F 58%, #F97316 140%);
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 8px;
        color: #FFFFFF;
        padding: 1.4rem 1.5rem;
        margin-bottom: 1.1rem;
        box-shadow: 0 18px 40px rgba(15, 23, 42, 0.10);
    }

    .dashboard-hero h1 {
        font-size: clamp(1.7rem, 3vw, 2.45rem);
        line-height: 1.08;
        margin: 0 0 0.55rem 0;
        letter-spacing: 0;
    }

    .dashboard-hero p {
        color: rgba(255, 255, 255, 0.86);
        font-size: 1rem;
        max-width: 780px;
        margin: 0 0 1rem 0;
    }

    .hero-meta {
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
    }

    .hero-pill {
        background: rgba(255, 255, 255, 0.13);
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 999px;
        color: #FFFFFF;
        font-size: 0.82rem;
        font-weight: 700;
        padding: 0.36rem 0.7rem;
    }

    .section-title {
        color: var(--ink);
        font-size: 1.05rem;
        font-weight: 800;
        margin: 1.1rem 0 0.5rem 0;
    }

    .stat-card,
    .insight-card {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 8px;
        box-shadow: 0 10px 24px rgba(15, 23, 42, 0.05);
        min-height: 116px;
        padding: 0.95rem 1rem;
    }

    .stat-card {
        border-top: 4px solid var(--blue);
    }

    .stat-label {
        color: var(--muted);
        font-size: 0.78rem;
        font-weight: 800;
        letter-spacing: 0;
        margin-bottom: 0.45rem;
        text-transform: uppercase;
    }

    .stat-value {
        color: var(--ink);
        font-size: 1.7rem;
        font-weight: 850;
        line-height: 1.05;
        margin-bottom: 0.45rem;
        overflow-wrap: anywhere;
    }

    .stat-note,
    .insight-note {
        color: var(--muted);
        font-size: 0.82rem;
        line-height: 1.35;
    }

    .insight-card {
        min-height: 100px;
        margin-bottom: 0.65rem;
    }

    .insight-label {
        color: var(--ink);
        font-size: 0.92rem;
        font-weight: 800;
        margin-bottom: 0.25rem;
    }

    .risk-note {
        background: #FFF7ED;
        border: 1px solid #FED7AA;
        border-radius: 8px;
        color: #7C2D12;
        font-size: 0.9rem;
        line-height: 1.45;
        margin: 0.8rem 0 1rem 0;
        padding: 0.85rem 1rem;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 0.35rem;
    }

    .stTabs [data-baseweb="tab"] {
        background: #FFFFFF;
        border: 1px solid var(--line);
        border-radius: 8px 8px 0 0;
        color: var(--muted);
        font-weight: 700;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .stTabs [aria-selected="true"] {
        color: var(--ink);
        border-bottom-color: #FFFFFF;
    }

    div[data-testid="stDataFrame"] {
        border: 1px solid var(--line);
        border-radius: 8px;
        overflow: hidden;
    }
</style>
"""

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


def chart_palette(count: int) -> list[str]:
    return [CARD_COLORS[index % len(CARD_COLORS)] for index in range(count)]


def make_figure(figsize: tuple[float, float]):
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor(PANEL_BG)
    ax.set_facecolor(PANEL_BG)
    return fig, ax


def style_axis(ax, title: str, xlabel: str, ylabel: str) -> None:
    ax.set_title(title, loc="left", fontsize=12, fontweight="bold", color=INK, pad=14)
    ax.set_xlabel(xlabel, color=MUTED, labelpad=8)
    ax.set_ylabel(ylabel, color=MUTED, labelpad=8)
    ax.tick_params(colors=MUTED)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.grid(axis="x", visible=False)
    sns.despine(ax=ax)


def render_author_credit(st) -> None:
    st.markdown(f'<div class="creator-bar">{AUTHOR_LINE}</div>', unsafe_allow_html=True)


def render_header(st, df: pd.DataFrame, source_path: Path) -> None:
    records = len(df)
    label_one_rate = pct(int((df["depression_label"] == 1).sum()), records)
    sleep_under_rate = pct(int((df["sleep_hours"] < 8).sum()), records)

    st.markdown(
        f"""
        <section class="dashboard-hero">
            <h1>{APP_TITLE}</h1>
            <p>{APP_SUBTITLE}</p>
            <div class="hero-meta">
                <span class="hero-pill">{records:,} records</span>
                <span class="hero-pill">{len(df.columns):,} columns</span>
                <span class="hero-pill">Label 1 rate: {label_one_rate:.1f}%</span>
                <span class="hero-pill">Sleep under 8 hrs: {sleep_under_rate:.1f}%</span>
                <span class="hero-pill">Source: {source_path}</span>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def build_sidebar_filters(st, df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Dashboard Controls")
    st.sidebar.caption("Use filters to compare slices of the cleaned dataset.")

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
    st.sidebar.divider()
    st.sidebar.caption(AUTHOR_LINE)

    return apply_filters(df, age_range, category_filters, selected_labels)


def render_kpis(st, df: pd.DataFrame) -> None:
    records = len(df)
    label_one_count = int((df["depression_label"] == 1).sum())
    low_sleep_count = int((df["sleep_hours"] < 8).sum())
    high_social_count = int((df["daily_social_media_hours"] >= 6).sum())

    metrics = [
        (
            "Records",
            f"{records:,}",
            "Filtered sample size",
            CARD_COLORS[0],
        ),
        (
            "Label 1 rate",
            format_percent(pct(label_one_count, records)),
            f"{label_one_count:,} records in label 1",
            ACCENT_RED,
        ),
        (
            "Avg sleep",
            f"{df['sleep_hours'].mean():.2f} hrs",
            "Mean nightly sleep",
            CARD_COLORS[1],
        ),
        (
            "Avg social media",
            f"{df['daily_social_media_hours'].mean():.2f} hrs",
            "Mean daily platform use",
            CARD_COLORS[2],
        ),
        (
            "Sleep under 8 hrs",
            format_percent(pct(low_sleep_count, records)),
            f"{low_sleep_count:,} records below 8 hrs",
            CARD_COLORS[4],
        ),
        (
            "6+ hrs social media",
            format_percent(pct(high_social_count, records)),
            f"{high_social_count:,} records at or above 6 hrs",
            CARD_COLORS[3],
        ),
    ]

    for column, (label, value, note, color) in zip(st.columns(len(metrics)), metrics):
        column.markdown(
            f"""
            <div class="stat-card" style="border-top-color: {color};">
                <div class="stat-label">{label}</div>
                <div class="stat-value">{value}</div>
                <div class="stat-note">{note}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def add_bar_labels(ax) -> None:
    for container in ax.containers:
        ax.bar_label(container, fmt="%.2f", padding=3)


def plot_count_bar(df: pd.DataFrame, column: str, title: str, xlabel: str):
    counts = df[column].value_counts().sort_index()
    labels = [f"Label {int(value)}" if column == "depression_label" else str(value) for value in counts.index]
    fig, ax = make_figure((7, 4))
    sns.barplot(
        x=labels,
        y=counts.values,
        ax=ax,
        hue=labels,
        palette=chart_palette(len(labels)),
        legend=False,
    )
    style_axis(ax, title, xlabel, "Records")
    ax.bar_label(ax.containers[0], fmt="%d", padding=3)
    fig.tight_layout()
    return fig


def plot_platform_bar(df: pd.DataFrame):
    counts = df["platform_usage"].value_counts()
    labels = [label_title(value) for value in counts.index]
    fig, ax = make_figure((7, 4))
    sns.barplot(
        x=labels,
        y=counts.values,
        ax=ax,
        palette=chart_palette(len(labels)),
        hue=labels,
        legend=False,
    )
    style_axis(ax, "Platform Usage", "Platform", "Records")
    ax.bar_label(ax.containers[0], fmt="%d", padding=3)
    fig.tight_layout()
    return fig


def plot_sleep_histogram(df: pd.DataFrame):
    fig, ax = make_figure((8, 4))
    sns.histplot(df["sleep_hours"], bins=10, kde=True, ax=ax, color="#0F766E")
    ax.axvline(
        df["sleep_hours"].mean(),
        color=ACCENT_RED,
        linewidth=2,
        label="Mean",
    )
    ax.axvline(8, color="#F97316", linewidth=2, linestyle="--", label="8-hour reference")
    style_axis(ax, "Sleep Hours Distribution", "Sleep hours", "Records")
    ax.legend(frameon=False, labelcolor=MUTED)
    fig.tight_layout()
    return fig


def plot_social_sleep_scatter(df: pd.DataFrame):
    fig, ax = make_figure((8, 5))
    sns.scatterplot(
        data=df,
        x="daily_social_media_hours",
        y="sleep_hours",
        hue="depression_label",
        palette={0: "#2563EB", 1: ACCENT_RED},
        alpha=0.72,
        edgecolor="#FFFFFF",
        linewidth=0.35,
        ax=ax,
    )
    style_axis(
        ax,
        "Social Media Hours vs Sleep Hours",
        "Daily social media hours",
        "Sleep hours",
    )
    ax.legend(title="Depression label", frameon=False, labelcolor=MUTED)
    fig.tight_layout()
    return fig


def plot_stress_anxiety_heatmap(df: pd.DataFrame):
    table = pd.crosstab(df["anxiety_level"], df["stress_level"])
    fig, ax = make_figure((8, 5))
    sns.heatmap(
        table,
        cmap="mako_r",
        annot=True,
        fmt="d",
        ax=ax,
        linewidths=0.4,
        linecolor="#FFFFFF",
        cbar_kws={"label": "Records"},
    )
    ax.set_title("Stress vs Anxiety Count", loc="left", fontsize=12, fontweight="bold", color=INK, pad=14)
    ax.set_xlabel("Stress level", color=MUTED, labelpad=8)
    ax.set_ylabel("Anxiety level", color=MUTED, labelpad=8)
    ax.tick_params(colors=MUTED)
    fig.tight_layout()
    return fig


def plot_correlation_heatmap(df: pd.DataFrame):
    corr = df[NUMERIC_COLUMNS].corr(numeric_only=True)
    fig, ax = make_figure((9, 6))
    sns.heatmap(
        corr,
        cmap="vlag",
        center=0,
        annot=True,
        fmt=".2f",
        ax=ax,
        linewidths=0.35,
        linecolor="#FFFFFF",
        cbar_kws={"label": "Correlation"},
    )
    ax.set_title("Numeric Correlation Matrix", loc="left", fontsize=12, fontweight="bold", color=INK, pad=14)
    ax.tick_params(colors=MUTED)
    fig.tight_layout()
    return fig


def plot_group_comparison(df: pd.DataFrame, value_column: str, title: str, ylabel: str):
    grouped = (
        df.groupby("depression_label", as_index=False)[value_column]
        .mean()
        .sort_values("depression_label")
    )

    labels = [f"Label {int(value)}" for value in grouped["depression_label"]]
    fig, ax = make_figure((6, 4))
    sns.barplot(
        data=grouped,
        x=labels,
        y=value_column,
        ax=ax,
        hue=labels,
        palette=chart_palette(len(labels)),
        legend=False,
    )
    style_axis(ax, title, "Depression label", ylabel)
    add_bar_labels(ax)
    fig.tight_layout()
    return fig


def render_overview(st, df: pd.DataFrame) -> None:
    st.markdown('<div class="section-title">Population Overview</div>', unsafe_allow_html=True)
    left, right = st.columns(2)
    left.pyplot(plot_count_bar(df, "depression_label", "Depression Label Count", "Label"))
    right.pyplot(plot_platform_bar(df))
    st.pyplot(plot_sleep_histogram(df))


def render_lifestyle(st, df: pd.DataFrame) -> None:
    st.markdown('<div class="section-title">Lifestyle Signals</div>', unsafe_allow_html=True)
    left, right = st.columns(2)
    left.pyplot(plot_social_sleep_scatter(df))
    right.pyplot(plot_stress_anxiety_heatmap(df))
    st.pyplot(plot_correlation_heatmap(df))


def render_depression_comparison(st, df: pd.DataFrame) -> None:
    st.markdown('<div class="section-title">Label Comparison</div>', unsafe_allow_html=True)
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
    st.markdown('<div class="section-title">Filtered Dataset</div>', unsafe_allow_html=True)
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
        st.markdown(
            """
            <div class="risk-note">
                The current filter contains only one depression label group, so
                group-to-group comparison is unavailable for this slice.
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    grouped = df.groupby("depression_label").mean(numeric_only=True)
    social_gap = grouped.loc[1, "daily_social_media_hours"] - grouped.loc[
        0, "daily_social_media_hours"
    ]
    sleep_gap = grouped.loc[1, "sleep_hours"] - grouped.loc[0, "sleep_hours"]
    stress_gap = grouped.loc[1, "stress_level"] - grouped.loc[0, "stress_level"]

    st.markdown(
        '<div class="section-title">Current Slice Readout</div>',
        unsafe_allow_html=True,
    )

    cards = [
        (
            "Social media gap",
            f"{social_gap:+.2f} hrs",
            "Label 1 average minus label 0 average",
        ),
        (
            "Sleep gap",
            f"{sleep_gap:+.2f} hrs",
            "Label 1 average minus label 0 average",
        ),
        (
            "Stress gap",
            f"{stress_gap:+.2f} pts",
            "Label 1 average minus label 0 average",
        ),
    ]

    for column, (label, value, note) in zip(st.columns(3), cards):
        column.markdown(
            f"""
            <div class="insight-card">
                <div class="insight-label">{label}</div>
                <div class="stat-value">{value}</div>
                <div class="insight-note">{note}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="risk-note">
            These are descriptive differences only. The depression label is a
            dataset indicator, not a clinical diagnosis.
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    import streamlit as st

    st.set_page_config(page_title=APP_TITLE, layout="wide")
    sns.set_theme(style="whitegrid", rc={"axes.edgecolor": GRID, "axes.labelcolor": MUTED})
    st.markdown(DASHBOARD_CSS, unsafe_allow_html=True)
    render_author_credit(st)

    try:
        source_path = find_data_file()
        df = load_clean_data(source_path)
    except (FileNotFoundError, ValueError) as exc:
        st.error(str(exc))
        st.stop()

    render_header(st, df, source_path)
    filtered = build_sidebar_filters(st, df)

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
        f"{AUTHOR_LINE}. This dashboard is for exploratory analysis and learning. "
        "It should not be used as medical advice."
    )


if __name__ == "__main__":
    main()
