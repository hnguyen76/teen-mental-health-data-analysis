from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


APP_TITLE = "Teen Mental Health Dashboard"
AUTHOR_LINE = "Created by Hieu Nguyen"
APP_SUBTITLE = (
    "A polished exploratory dashboard for teen social media habits, sleep, "
    "school performance, stress, anxiety, and depression-label patterns."
)

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

PALETTE = {
    "page": "#F7F8FA",
    "panel": "#FFFFFF",
    "ink": "#182126",
    "muted": "#65726F",
    "line": "#DDE5E1",
    "teal": "#087E74",
    "coral": "#E35D43",
    "gold": "#D99A2B",
    "blue": "#3567B7",
    "green": "#4D8B45",
    "plum": "#7E557F",
    "sand": "#F2E9D8",
}

CHART_COLORS = [
    PALETTE["teal"],
    PALETTE["coral"],
    PALETTE["gold"],
    PALETTE["blue"],
    PALETTE["green"],
    PALETTE["plum"],
]

DASHBOARD_CSS = f"""
<style>
    :root {{
        --page: {PALETTE["page"]};
        --panel: {PALETTE["panel"]};
        --ink: {PALETTE["ink"]};
        --muted: {PALETTE["muted"]};
        --line: {PALETTE["line"]};
        --teal: {PALETTE["teal"]};
        --coral: {PALETTE["coral"]};
        --gold: {PALETTE["gold"]};
        --blue: {PALETTE["blue"]};
    }}

    .stApp {{
        background: var(--page);
        color: var(--ink);
    }}

    .block-container {{
        max-width: 1320px;
        padding-top: 1.1rem;
        padding-bottom: 2.4rem;
    }}

    [data-testid="stSidebar"] {{
        background: #FFFFFF;
        border-right: 1px solid var(--line);
    }}

    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {{
        color: var(--ink);
        letter-spacing: 0;
    }}

    div[data-testid="stVerticalBlock"] {{
        gap: 0.7rem;
    }}

    .creator-strip {{
        align-items: center;
        color: var(--muted);
        display: flex;
        font-size: 0.86rem;
        font-weight: 800;
        justify-content: flex-end;
        letter-spacing: 0;
        margin-bottom: 0.65rem;
        text-transform: uppercase;
    }}

    .hero-panel {{
        background: var(--ink);
        border: 1px solid rgba(24, 33, 38, 0.14);
        border-radius: 8px;
        box-shadow: 0 18px 42px rgba(24, 33, 38, 0.13);
        color: #FFFFFF;
        margin-bottom: 0.95rem;
        overflow: hidden;
        padding: 1.35rem 1.45rem;
        position: relative;
    }}

    .hero-panel::before {{
        background: linear-gradient(180deg, var(--teal), var(--coral), var(--gold));
        content: "";
        inset: 0 auto 0 0;
        position: absolute;
        width: 6px;
    }}

    .hero-kicker {{
        color: rgba(255, 255, 255, 0.72);
        font-size: 0.76rem;
        font-weight: 850;
        letter-spacing: 0;
        margin-bottom: 0.45rem;
        text-transform: uppercase;
    }}

    .hero-panel h1 {{
        color: #FFFFFF;
        font-size: clamp(1.85rem, 3vw, 2.8rem);
        font-weight: 900;
        letter-spacing: 0;
        line-height: 1.05;
        margin: 0 0 0.58rem 0;
    }}

    .hero-panel p {{
        color: rgba(255, 255, 255, 0.82);
        font-size: 1.02rem;
        line-height: 1.45;
        margin: 0;
        max-width: 860px;
    }}

    .hero-meta {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.48rem;
        margin-top: 1rem;
    }}

    .hero-pill {{
        background: rgba(255, 255, 255, 0.10);
        border: 1px solid rgba(255, 255, 255, 0.16);
        border-radius: 999px;
        color: #FFFFFF;
        font-size: 0.82rem;
        font-weight: 760;
        line-height: 1.1;
        padding: 0.42rem 0.74rem;
        white-space: nowrap;
    }}

    .metric-card {{
        background: #FFFFFF;
        border: 1px solid var(--line);
        border-left: 5px solid var(--teal);
        border-radius: 8px;
        box-shadow: 0 10px 24px rgba(24, 33, 38, 0.055);
        min-height: 124px;
        padding: 0.95rem 1rem;
    }}

    .metric-label {{
        color: var(--muted);
        font-size: 0.74rem;
        font-weight: 850;
        letter-spacing: 0;
        margin-bottom: 0.38rem;
        text-transform: uppercase;
    }}

    .metric-value {{
        color: var(--ink);
        font-size: 1.75rem;
        font-weight: 900;
        line-height: 1.05;
        margin-bottom: 0.48rem;
        overflow-wrap: anywhere;
    }}

    .metric-note {{
        color: var(--muted);
        font-size: 0.82rem;
        line-height: 1.35;
    }}

    .section-title {{
        color: var(--ink);
        font-size: 1.08rem;
        font-weight: 900;
        letter-spacing: 0;
        margin: 1.05rem 0 0.15rem 0;
    }}

    .slice-card {{
        background: #FFFFFF;
        border: 1px solid var(--line);
        border-radius: 8px;
        box-shadow: 0 10px 24px rgba(24, 33, 38, 0.045);
        min-height: 104px;
        padding: 0.9rem 1rem;
    }}

    .slice-label {{
        color: var(--ink);
        font-size: 0.88rem;
        font-weight: 860;
        margin-bottom: 0.2rem;
    }}

    .slice-note {{
        color: var(--muted);
        font-size: 0.82rem;
        line-height: 1.35;
    }}

    .notice-box {{
        background: #FFF7ED;
        border: 1px solid #F2D2A9;
        border-radius: 8px;
        color: #7A3C16;
        font-size: 0.9rem;
        line-height: 1.45;
        margin: 0.75rem 0 0.95rem 0;
        padding: 0.85rem 1rem;
    }}

    .stTabs [data-baseweb="tab-list"] {{
        gap: 0.35rem;
    }}

    .stTabs [data-baseweb="tab"] {{
        background: #FFFFFF;
        border: 1px solid var(--line);
        border-radius: 8px 8px 0 0;
        color: var(--muted);
        font-weight: 800;
        letter-spacing: 0;
        padding-left: 1rem;
        padding-right: 1rem;
    }}

    .stTabs [aria-selected="true"] {{
        color: var(--ink);
        border-bottom-color: #FFFFFF;
    }}

    div[data-testid="stDataFrame"] {{
        border: 1px solid var(--line);
        border-radius: 8px;
        overflow: hidden;
    }}

    div[data-testid="stDownloadButton"] button {{
        border-radius: 8px;
        font-weight: 800;
    }}
</style>
"""


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


def set_plot_theme() -> None:
    sns.set_theme(
        style="whitegrid",
        rc={
            "axes.edgecolor": PALETTE["line"],
            "axes.labelcolor": PALETTE["muted"],
            "axes.titlecolor": PALETTE["ink"],
            "grid.color": "#E8EEE9",
            "figure.facecolor": PALETTE["panel"],
            "font.family": "DejaVu Sans",
        },
    )


def make_figure(figsize: tuple[float, float]):
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor(PALETTE["panel"])
    ax.set_facecolor(PALETTE["panel"])
    return fig, ax


def style_axis(ax, title: str, xlabel: str = "", ylabel: str = "") -> None:
    ax.set_title(title, loc="left", fontsize=12, fontweight="bold", pad=14)
    ax.set_xlabel(xlabel, color=PALETTE["muted"], labelpad=8)
    ax.set_ylabel(ylabel, color=PALETTE["muted"], labelpad=8)
    ax.tick_params(colors=PALETTE["muted"], labelsize=9)
    ax.grid(axis="y", color="#E8EEE9", linewidth=0.8)
    ax.grid(axis="x", visible=False)
    sns.despine(ax=ax)


def compute_snapshot(df: pd.DataFrame) -> dict[str, float]:
    records = len(df)
    label_one_count = int((df["depression_label"] == 1).sum())
    low_sleep_count = int((df["sleep_hours"] < 8).sum())
    high_social_count = int((df["daily_social_media_hours"] >= 6).sum())
    high_stress_count = int((df["stress_level"] >= 8).sum())

    return {
        "records": records,
        "columns": len(df.columns),
        "age_min": int(df["age"].min()),
        "age_max": int(df["age"].max()),
        "avg_sleep": float(df["sleep_hours"].mean()),
        "avg_social": float(df["daily_social_media_hours"].mean()),
        "avg_stress": float(df["stress_level"].mean()),
        "avg_anxiety": float(df["anxiety_level"].mean()),
        "label_one_count": label_one_count,
        "label_one_rate": pct(label_one_count, records),
        "low_sleep_count": low_sleep_count,
        "low_sleep_rate": pct(low_sleep_count, records),
        "high_social_count": high_social_count,
        "high_social_rate": pct(high_social_count, records),
        "high_stress_count": high_stress_count,
        "high_stress_rate": pct(high_stress_count, records),
    }


def label_gaps(df: pd.DataFrame) -> dict[str, float] | None:
    label_counts = set(df["depression_label"].dropna().astype(int).unique())
    if not {0, 1}.issubset(label_counts):
        return None

    grouped = df.groupby("depression_label").mean(numeric_only=True)
    return {
        "social": grouped.loc[1, "daily_social_media_hours"]
        - grouped.loc[0, "daily_social_media_hours"],
        "sleep": grouped.loc[1, "sleep_hours"] - grouped.loc[0, "sleep_hours"],
        "stress": grouped.loc[1, "stress_level"] - grouped.loc[0, "stress_level"],
        "anxiety": grouped.loc[1, "anxiety_level"] - grouped.loc[0, "anxiety_level"],
    }


def render_author_credit(st) -> None:
    st.markdown(
        f'<div class="creator-strip">{AUTHOR_LINE}</div>',
        unsafe_allow_html=True,
    )


def render_header(st, df: pd.DataFrame, source_path: Path) -> None:
    snapshot = compute_snapshot(df)
    st.markdown(
        f"""
        <section class="hero-panel">
            <div class="hero-kicker">Exploratory Data Dashboard</div>
            <h1>{APP_TITLE}</h1>
            <p>{APP_SUBTITLE}</p>
            <div class="hero-meta">
                <span class="hero-pill">{snapshot["records"]:,.0f} clean records</span>
                <span class="hero-pill">Ages {snapshot["age_min"]:.0f}-{snapshot["age_max"]:.0f}</span>
                <span class="hero-pill">Label 1 rate {snapshot["label_one_rate"]:.1f}%</span>
                <span class="hero-pill">Avg sleep {snapshot["avg_sleep"]:.2f} hrs</span>
                <span class="hero-pill">Source: {source_path}</span>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def build_sidebar_filters(st, df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Dashboard Controls")
    st.sidebar.caption("Filter the cleaned dataset before comparing patterns.")

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

    st.sidebar.divider()
    st.sidebar.caption(
        "The depression label is a dataset indicator, not a clinical diagnosis."
    )
    st.sidebar.caption(AUTHOR_LINE)

    return apply_filters(df, age_range, category_filters, selected_labels)


def metric_card(label: str, value: str, note: str, color: str) -> str:
    return f"""
    <div class="metric-card" style="border-left-color: {color};">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-note">{note}</div>
    </div>
    """


def render_kpis(st, df: pd.DataFrame) -> None:
    snapshot = compute_snapshot(df)
    cards = [
        (
            "Records",
            f"{snapshot['records']:,.0f}",
            "Filtered sample size",
            PALETTE["teal"],
        ),
        (
            "Label 1 rate",
            format_percent(snapshot["label_one_rate"]),
            f"{snapshot['label_one_count']:,.0f} records with label 1",
            PALETTE["coral"],
        ),
        (
            "Average sleep",
            f"{snapshot['avg_sleep']:.2f} hrs",
            f"{snapshot['low_sleep_rate']:.1f}% sleep under 8 hours",
            PALETTE["blue"],
        ),
        (
            "Average social media",
            f"{snapshot['avg_social']:.2f} hrs",
            f"{snapshot['high_social_rate']:.1f}% at 6+ hours daily",
            PALETTE["gold"],
        ),
    ]

    for column, (label, value, note, color) in zip(st.columns(4), cards):
        column.markdown(metric_card(label, value, note, color), unsafe_allow_html=True)


def render_slice_readout(st, df: pd.DataFrame) -> None:
    gaps = label_gaps(df)
    st.markdown('<div class="section-title">Current Slice Readout</div>', unsafe_allow_html=True)

    if gaps is None:
        st.markdown(
            """
            <div class="notice-box">
                The current filter contains only one depression-label group, so
                label comparison is unavailable for this slice.
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    cards = [
        (
            "Social media gap",
            f"{gaps['social']:+.2f} hrs",
            "Label 1 average minus label 0 average",
            PALETTE["gold"],
        ),
        (
            "Sleep gap",
            f"{gaps['sleep']:+.2f} hrs",
            "Label 1 average minus label 0 average",
            PALETTE["blue"],
        ),
        (
            "Stress gap",
            f"{gaps['stress']:+.2f} pts",
            "Label 1 average minus label 0 average",
            PALETTE["coral"],
        ),
        (
            "Anxiety gap",
            f"{gaps['anxiety']:+.2f} pts",
            "Label 1 average minus label 0 average",
            PALETTE["plum"],
        ),
    ]

    for column, (label, value, note, color) in zip(st.columns(4), cards):
        column.markdown(
            f"""
            <div class="slice-card" style="border-top: 4px solid {color};">
                <div class="slice-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="slice-note">{note}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="notice-box">
            These differences are descriptive only. They do not prove causation
            and should not be interpreted as clinical guidance.
        </div>
        """,
        unsafe_allow_html=True,
    )


def plot_label_distribution(df: pd.DataFrame):
    counts = df["depression_label"].value_counts().sort_index()
    labels = [f"Label {int(label)}" for label in counts.index]
    colors = [
        PALETTE["blue"] if int(label) == 0 else PALETTE["coral"]
        for label in counts.index
    ]
    snapshot = compute_snapshot(df)

    fig, ax = make_figure((6.2, 4.7))
    wedges, _ = ax.pie(
        counts.values,
        colors=colors,
        startangle=90,
        counterclock=False,
        wedgeprops={"width": 0.38, "edgecolor": PALETTE["panel"], "linewidth": 3},
    )
    ax.text(
        0,
        0.05,
        f"{snapshot['label_one_rate']:.1f}%",
        ha="center",
        va="center",
        fontsize=24,
        fontweight="bold",
        color=PALETTE["ink"],
    )
    ax.text(
        0,
        -0.17,
        "Label 1 rate",
        ha="center",
        va="center",
        fontsize=9,
        color=PALETTE["muted"],
    )
    ax.set_title("Depression Label Mix", loc="left", fontsize=12, fontweight="bold", pad=12)
    legend_labels = [
        f"{label}: {count:,.0f} records"
        for label, count in zip(labels, counts.values)
    ]
    ax.legend(
        wedges,
        legend_labels,
        loc="lower center",
        bbox_to_anchor=(0.5, -0.1),
        frameon=False,
        ncol=max(1, len(labels)),
        fontsize=9,
    )
    fig.tight_layout()
    return fig


def plot_platform_distribution(df: pd.DataFrame):
    counts = df["platform_usage"].value_counts().sort_values(ascending=True)
    labels = [label_title(value) for value in counts.index]

    fig, ax = make_figure((7.4, 4.7))
    bars = ax.barh(labels, counts.values, color=CHART_COLORS[: len(labels)])
    style_axis(ax, "Platform Usage", "Records", "")
    ax.set_xlim(0, max(counts.values) * 1.18)
    for bar in bars:
        ax.text(
            bar.get_width() + max(counts.values) * 0.025,
            bar.get_y() + bar.get_height() / 2,
            f"{bar.get_width():,.0f}",
            va="center",
            color=PALETTE["muted"],
            fontsize=9,
            fontweight="bold",
        )
    fig.tight_layout()
    return fig


def plot_sleep_distribution(df: pd.DataFrame):
    fig, ax = make_figure((8, 4.8))
    sns.histplot(
        df["sleep_hours"],
        bins=12,
        kde=True,
        ax=ax,
        color=PALETTE["teal"],
        edgecolor=PALETTE["panel"],
        linewidth=1.0,
    )
    ax.axvline(
        df["sleep_hours"].mean(),
        color=PALETTE["coral"],
        linewidth=2.4,
        label="Mean",
    )
    ax.axvline(
        8,
        color=PALETTE["gold"],
        linewidth=2.2,
        linestyle="--",
        label="8-hour reference",
    )
    style_axis(ax, "Sleep Hours Distribution", "Sleep hours", "Records")
    ax.legend(frameon=False, labelcolor=PALETTE["muted"])
    fig.tight_layout()
    return fig


def plot_social_sleep_scatter(df: pd.DataFrame):
    fig, ax = make_figure((8, 5.1))
    sns.scatterplot(
        data=df,
        x="daily_social_media_hours",
        y="sleep_hours",
        hue="depression_label",
        size="stress_level",
        sizes=(20, 95),
        palette={0: PALETTE["blue"], 1: PALETTE["coral"]},
        alpha=0.72,
        edgecolor="#FFFFFF",
        linewidth=0.35,
        ax=ax,
    )
    style_axis(
        ax,
        "Social Media vs Sleep",
        "Daily social media hours",
        "Sleep hours",
    )
    ax.legend(
        title="Label / stress",
        frameon=False,
        labelcolor=PALETTE["muted"],
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
    )
    fig.tight_layout()
    return fig


def plot_stress_anxiety_heatmap(df: pd.DataFrame):
    table = pd.crosstab(df["anxiety_level"], df["stress_level"])
    fig, ax = make_figure((7.8, 5.1))
    sns.heatmap(
        table,
        cmap="rocket_r",
        annot=True,
        fmt="d",
        ax=ax,
        linewidths=0.45,
        linecolor="#FFFFFF",
        cbar_kws={"label": "Records"},
    )
    ax.set_title("Stress and Anxiety Density", loc="left", fontsize=12, fontweight="bold", pad=12)
    ax.set_xlabel("Stress level", color=PALETTE["muted"], labelpad=8)
    ax.set_ylabel("Anxiety level", color=PALETTE["muted"], labelpad=8)
    ax.tick_params(colors=PALETTE["muted"], labelsize=9)
    fig.tight_layout()
    return fig


def plot_age_lifestyle_trends(df: pd.DataFrame):
    trends = (
        df.groupby("age", as_index=False)[
            ["daily_social_media_hours", "sleep_hours", "stress_level"]
        ]
        .mean()
        .sort_values("age")
    )

    fig, ax = make_figure((8, 4.8))
    ax.plot(
        trends["age"],
        trends["daily_social_media_hours"],
        marker="o",
        color=PALETTE["gold"],
        linewidth=2.4,
        label="Social media hours",
    )
    ax.plot(
        trends["age"],
        trends["sleep_hours"],
        marker="o",
        color=PALETTE["blue"],
        linewidth=2.4,
        label="Sleep hours",
    )
    ax.plot(
        trends["age"],
        trends["stress_level"],
        marker="o",
        color=PALETTE["coral"],
        linewidth=2.4,
        label="Stress level",
    )
    style_axis(ax, "Average Lifestyle Signals by Age", "Age", "Average value")
    ax.legend(frameon=False, labelcolor=PALETTE["muted"], ncol=2)
    fig.tight_layout()
    return fig


def plot_metric_comparison(df: pd.DataFrame):
    value_columns = {
        "daily_social_media_hours": "Social media",
        "sleep_hours": "Sleep",
        "stress_level": "Stress",
        "anxiety_level": "Anxiety",
        "addiction_level": "Addiction",
        "academic_performance": "Academic",
    }
    summary = (
        df.groupby("depression_label")[list(value_columns)]
        .mean()
        .reset_index()
        .melt(
            id_vars="depression_label",
            var_name="metric",
            value_name="average",
        )
    )
    summary["metric"] = summary["metric"].map(value_columns)
    summary["label"] = summary["depression_label"].map(lambda value: f"Label {int(value)}")

    fig, ax = make_figure((9.2, 5.1))
    sns.barplot(
        data=summary,
        x="metric",
        y="average",
        hue="label",
        palette={"Label 0": PALETTE["blue"], "Label 1": PALETTE["coral"]},
        ax=ax,
    )
    style_axis(ax, "Average Metrics by Depression Label", "", "Average score / hours")
    ax.legend(title="", frameon=False, labelcolor=PALETTE["muted"])
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f", padding=2, fontsize=8, color=PALETTE["muted"])
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
    ax.set_title("Numeric Correlation Matrix", loc="left", fontsize=12, fontweight="bold", pad=12)
    ax.tick_params(colors=PALETTE["muted"], labelsize=8)
    fig.tight_layout()
    return fig


def render_overview(st, df: pd.DataFrame) -> None:
    st.markdown('<div class="section-title">Dataset Overview</div>', unsafe_allow_html=True)
    left, right = st.columns([0.45, 0.55])
    left.pyplot(plot_label_distribution(df), use_container_width=True)
    right.pyplot(plot_platform_distribution(df), use_container_width=True)
    st.pyplot(plot_sleep_distribution(df), use_container_width=True)


def render_signals(st, df: pd.DataFrame) -> None:
    st.markdown('<div class="section-title">Behavior Signals</div>', unsafe_allow_html=True)
    left, right = st.columns(2)
    left.pyplot(plot_social_sleep_scatter(df), use_container_width=True)
    right.pyplot(plot_age_lifestyle_trends(df), use_container_width=True)
    st.pyplot(plot_stress_anxiety_heatmap(df), use_container_width=True)


def render_comparison(st, df: pd.DataFrame) -> None:
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
    st.pyplot(plot_metric_comparison(df), use_container_width=True)
    st.pyplot(plot_correlation_heatmap(df), use_container_width=True)


def render_data_table(st, df: pd.DataFrame) -> None:
    st.markdown('<div class="section-title">Filtered Data</div>', unsafe_allow_html=True)
    st.dataframe(df, width="stretch", hide_index=True)
    st.download_button(
        "Download filtered CSV",
        df.to_csv(index=False).encode("utf-8"),
        file_name="teen_mental_health_filtered.csv",
        mime="text/csv",
    )


def main() -> None:
    import streamlit as st

    st.set_page_config(page_title=APP_TITLE, layout="wide")
    set_plot_theme()
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
    render_slice_readout(st, filtered)

    overview_tab, signals_tab, comparison_tab, data_tab = st.tabs(
        ["Overview", "Signals", "Label Comparison", "Data"]
    )

    with overview_tab:
        render_overview(st, filtered)

    with signals_tab:
        render_signals(st, filtered)

    with comparison_tab:
        render_comparison(st, filtered)

    with data_tab:
        render_data_table(st, filtered)

    st.caption(
        f"{AUTHOR_LINE}. Exploratory analysis only. Not medical advice."
    )


if __name__ == "__main__":
    main()
