from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.patches import FancyBboxPatch

from dashboard import (
    APP_SUBTITLE,
    APP_TITLE,
    AUTHOR_LINE,
    CHART_COLORS,
    NUMERIC_COLUMNS,
    PALETTE,
    compute_snapshot,
    find_data_file,
    label_gaps,
    label_title,
    load_clean_data,
    set_plot_theme,
    style_axis,
)


REPORT_PATH = Path("reports") / "DASHBOARD.md"
FIGURE_DIR = Path("reports") / "figures"


def save_figure(fig, filename: str) -> str:
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    path = FIGURE_DIR / filename
    fig.savefig(path, dpi=170, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    return f"figures/{filename}"


def format_percent(value: float) -> str:
    return f"{value:.2f}%"


def add_panel(
    fig,
    x: float,
    y: float,
    width: float,
    height: float,
    facecolor: str = "#FFFFFF",
    edgecolor: str = "#DDE5E1",
    zorder: int = 1,
) -> None:
    panel = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.006,rounding_size=0.012",
        linewidth=1.0,
        facecolor=facecolor,
        edgecolor=edgecolor,
        transform=fig.transFigure,
        zorder=zorder,
    )
    fig.patches.append(panel)


def add_metric_card(
    fig,
    x: float,
    y: float,
    width: float,
    height: float,
    label: str,
    value: str,
    note: str,
    color: str,
) -> None:
    add_panel(fig, x, y, width, height, zorder=1)
    fig.patches.append(
        FancyBboxPatch(
            (x, y),
            0.008,
            height,
            boxstyle="round,pad=0,rounding_size=0.01",
            linewidth=0,
            facecolor=color,
            transform=fig.transFigure,
            zorder=2,
        )
    )
    fig.text(x + 0.022, y + height - 0.034, label.upper(), fontsize=10, fontweight="bold", color=PALETTE["muted"], zorder=3)
    fig.text(x + 0.022, y + 0.056, value, fontsize=24, fontweight="bold", color=PALETTE["ink"], zorder=3)
    fig.text(x + 0.022, y + 0.024, note, fontsize=9.5, color=PALETTE["muted"], zorder=3)


def draw_summary_dashboard(df: pd.DataFrame, source_path: Path):
    snapshot = compute_snapshot(df)
    gaps = label_gaps(df) or {"social": 0, "sleep": 0, "stress": 0, "anxiety": 0}

    fig = plt.figure(figsize=(16, 9), facecolor=PALETTE["page"])

    add_panel(fig, 0.035, 0.715, 0.93, 0.225, facecolor=PALETTE["ink"], edgecolor=PALETTE["ink"])
    fig.patches.append(
        FancyBboxPatch(
            (0.035, 0.715),
            0.012,
            0.225,
            boxstyle="round,pad=0,rounding_size=0.012",
            linewidth=0,
            facecolor=PALETTE["teal"],
            transform=fig.transFigure,
            zorder=2,
        )
    )
    fig.text(0.065, 0.885, "EXPLORATORY DATA DASHBOARD", fontsize=11, fontweight="bold", color="#AAB8B3", zorder=3)
    fig.text(0.065, 0.825, APP_TITLE, fontsize=33, fontweight="bold", color="#FFFFFF", zorder=3)
    fig.text(0.065, 0.775, APP_SUBTITLE, fontsize=13.5, color="#D7DEDB", zorder=3)
    fig.text(0.935, 0.892, AUTHOR_LINE, fontsize=12, fontweight="bold", color="#FFFFFF", ha="right", zorder=3)
    fig.text(0.935, 0.752, f"Source: {source_path}", fontsize=10, color="#B7C4BF", ha="right", zorder=3)

    cards = [
        (
            "Records",
            f"{snapshot['records']:,.0f}",
            f"Ages {snapshot['age_min']:.0f}-{snapshot['age_max']:.0f}",
            PALETTE["teal"],
        ),
        (
            "Label 1 Rate",
            f"{snapshot['label_one_rate']:.1f}%",
            f"{snapshot['label_one_count']:,.0f} records",
            PALETTE["coral"],
        ),
        (
            "Avg Sleep",
            f"{snapshot['avg_sleep']:.2f} hrs",
            f"{snapshot['low_sleep_rate']:.1f}% under 8 hours",
            PALETTE["blue"],
        ),
        (
            "Avg Social",
            f"{snapshot['avg_social']:.2f} hrs",
            f"{snapshot['high_social_rate']:.1f}% at 6+ hours",
            PALETTE["gold"],
        ),
    ]
    card_width = 0.218
    for index, card in enumerate(cards):
        add_metric_card(fig, 0.04 + index * 0.235, 0.555, card_width, 0.125, *card)

    add_panel(fig, 0.04, 0.08, 0.285, 0.425)
    add_panel(fig, 0.355, 0.08, 0.285, 0.425)
    add_panel(fig, 0.67, 0.08, 0.29, 0.425)

    ax_platform = fig.add_axes([0.065, 0.16, 0.235, 0.265], zorder=3)
    platform_counts = df["platform_usage"].value_counts().sort_values(ascending=True)
    platform_labels = [label_title(value) for value in platform_counts.index]
    ax_platform.barh(platform_labels, platform_counts.values, color=CHART_COLORS[: len(platform_labels)])
    style_axis(ax_platform, "Platform Mix", "Records", "")
    for spine in ax_platform.spines.values():
        spine.set_visible(False)

    ax_gap = fig.add_axes([0.38, 0.16, 0.235, 0.265], zorder=3)
    gap_values = [gaps["social"], gaps["sleep"], gaps["stress"], gaps["anxiety"]]
    gap_labels = ["Social", "Sleep", "Stress", "Anxiety"]
    gap_colors = [PALETTE["gold"], PALETTE["blue"], PALETTE["coral"], PALETTE["plum"]]
    ax_gap.axhline(0, color=PALETTE["line"], linewidth=1.2)
    bars = ax_gap.bar(gap_labels, gap_values, color=gap_colors)
    style_axis(ax_gap, "Label 1 vs Label 0 Gap", "", "Delta")
    for bar, value in zip(bars, gap_values):
        ax_gap.text(
            bar.get_x() + bar.get_width() / 2,
            value + (0.16 if value >= 0 else -0.18),
            f"{value:+.2f}",
            ha="center",
            va="bottom" if value >= 0 else "top",
            fontsize=9,
            fontweight="bold",
            color=PALETTE["muted"],
        )

    ax_sleep = fig.add_axes([0.695, 0.16, 0.235, 0.265], zorder=3)
    sns.histplot(df["sleep_hours"], bins=12, color=PALETTE["teal"], edgecolor="#FFFFFF", ax=ax_sleep)
    ax_sleep.axvline(df["sleep_hours"].mean(), color=PALETTE["coral"], linewidth=2.2)
    ax_sleep.axvline(8, color=PALETTE["gold"], linewidth=2.0, linestyle="--")
    style_axis(ax_sleep, "Sleep Distribution", "Hours", "Records")

    return fig


def draw_overview_board(df: pd.DataFrame):
    snapshot = compute_snapshot(df)
    fig, axes = plt.subplots(2, 2, figsize=(16, 10), facecolor=PALETTE["page"])
    fig.subplots_adjust(top=0.86, hspace=0.38, wspace=0.28)
    fig.suptitle("Teen Mental Health Dashboard: Overview", x=0.05, ha="left", fontsize=24, fontweight="bold", color=PALETTE["ink"])
    fig.text(0.95, 0.945, AUTHOR_LINE, ha="right", fontsize=11, fontweight="bold", color=PALETTE["muted"])

    counts = df["depression_label"].value_counts().sort_index()
    labels = [f"Label {int(value)}" for value in counts.index]
    colors = [PALETTE["blue"] if int(value) == 0 else PALETTE["coral"] for value in counts.index]
    axes[0, 0].pie(
        counts.values,
        labels=[f"{label}\n{count:,.0f}" for label, count in zip(labels, counts.values)],
        colors=colors,
        startangle=90,
        counterclock=False,
        wedgeprops={"width": 0.42, "edgecolor": "#FFFFFF", "linewidth": 2},
        textprops={"color": PALETTE["muted"], "fontsize": 10, "fontweight": "bold"},
    )
    axes[0, 0].text(0, 0, f"{snapshot['label_one_rate']:.1f}%\nLabel 1", ha="center", va="center", fontsize=18, fontweight="bold", color=PALETTE["ink"])
    axes[0, 0].set_title("Depression Label Mix", loc="left", fontsize=13, fontweight="bold", color=PALETTE["ink"], pad=12)

    platform_counts = df["platform_usage"].value_counts().sort_values(ascending=True)
    platform_labels = [label_title(value) for value in platform_counts.index]
    axes[0, 1].barh(platform_labels, platform_counts.values, color=CHART_COLORS[: len(platform_labels)])
    style_axis(axes[0, 1], "Platform Usage", "Records", "")

    sns.histplot(df["sleep_hours"], bins=12, color=PALETTE["teal"], edgecolor="#FFFFFF", ax=axes[1, 0])
    axes[1, 0].axvline(df["sleep_hours"].mean(), color=PALETTE["coral"], linewidth=2.3, label="Mean")
    axes[1, 0].axvline(8, color=PALETTE["gold"], linewidth=2.0, linestyle="--", label="8-hour reference")
    style_axis(axes[1, 0], "Sleep Hours Distribution", "Sleep hours", "Records")
    axes[1, 0].legend(frameon=False, labelcolor=PALETTE["muted"])

    sns.scatterplot(
        data=df,
        x="daily_social_media_hours",
        y="sleep_hours",
        hue="depression_label",
        palette={0: PALETTE["blue"], 1: PALETTE["coral"]},
        alpha=0.72,
        edgecolor="#FFFFFF",
        linewidth=0.35,
        ax=axes[1, 1],
    )
    style_axis(axes[1, 1], "Social Media vs Sleep", "Daily social media hours", "Sleep hours")
    legend = axes[1, 1].legend(title="Label", frameon=True, loc="upper right")
    legend.get_frame().set_facecolor("#FFFFFF")
    legend.get_frame().set_edgecolor(PALETTE["line"])
    legend.get_frame().set_alpha(0.9)
    return fig


def draw_risk_profile_board(df: pd.DataFrame):
    fig, axes = plt.subplots(2, 2, figsize=(16, 10), facecolor=PALETTE["page"])
    fig.subplots_adjust(top=0.86, hspace=0.38, wspace=0.26)
    fig.suptitle("Teen Mental Health Dashboard: Signal Profile", x=0.05, ha="left", fontsize=24, fontweight="bold", color=PALETTE["ink"])
    fig.text(0.95, 0.945, AUTHOR_LINE, ha="right", fontsize=11, fontweight="bold", color=PALETTE["muted"])

    table = pd.crosstab(df["anxiety_level"], df["stress_level"])
    sns.heatmap(
        table,
        cmap="rocket_r",
        annot=True,
        fmt="d",
        linewidths=0.4,
        linecolor="#FFFFFF",
        cbar_kws={"label": "Records"},
        ax=axes[0, 0],
    )
    axes[0, 0].set_title("Stress and Anxiety Density", loc="left", fontsize=13, fontweight="bold", color=PALETTE["ink"], pad=12)
    axes[0, 0].set_xlabel("Stress level", color=PALETTE["muted"])
    axes[0, 0].set_ylabel("Anxiety level", color=PALETTE["muted"])

    value_columns = {
        "daily_social_media_hours": "Social",
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
        .melt(id_vars="depression_label", var_name="metric", value_name="average")
    )
    summary["metric"] = summary["metric"].map(value_columns)
    summary["label"] = summary["depression_label"].map(lambda value: f"Label {int(value)}")
    sns.barplot(
        data=summary,
        x="metric",
        y="average",
        hue="label",
        palette={"Label 0": PALETTE["blue"], "Label 1": PALETTE["coral"]},
        ax=axes[0, 1],
    )
    style_axis(axes[0, 1], "Average Metrics by Label", "", "Average")
    axes[0, 1].legend(title="", frameon=False, labelcolor=PALETTE["muted"])

    trends = (
        df.groupby("age", as_index=False)[
            ["daily_social_media_hours", "sleep_hours", "stress_level"]
        ]
        .mean()
        .sort_values("age")
    )
    axes[1, 0].plot(trends["age"], trends["daily_social_media_hours"], marker="o", color=PALETTE["gold"], linewidth=2.3, label="Social media")
    axes[1, 0].plot(trends["age"], trends["sleep_hours"], marker="o", color=PALETTE["blue"], linewidth=2.3, label="Sleep")
    axes[1, 0].plot(trends["age"], trends["stress_level"], marker="o", color=PALETTE["coral"], linewidth=2.3, label="Stress")
    style_axis(axes[1, 0], "Average Signals by Age", "Age", "Average")
    axes[1, 0].legend(frameon=False, labelcolor=PALETTE["muted"], ncol=3)

    corr = df[NUMERIC_COLUMNS].corr(numeric_only=True)
    sns.heatmap(
        corr,
        cmap="vlag",
        center=0,
        annot=False,
        linewidths=0.25,
        linecolor="#FFFFFF",
        cbar_kws={"label": "Correlation"},
        ax=axes[1, 1],
    )
    axes[1, 1].set_title("Numeric Correlation Map", loc="left", fontsize=13, fontweight="bold", color=PALETTE["ink"], pad=12)
    axes[1, 1].tick_params(colors=PALETTE["muted"], labelsize=8)
    return fig


def build_markdown(df: pd.DataFrame, source_path: Path, figures: dict[str, str]) -> str:
    snapshot = compute_snapshot(df)
    gaps = label_gaps(df) or {"social": 0, "sleep": 0, "stress": 0, "anxiety": 0}
    label_counts = df["depression_label"].value_counts().sort_index()
    grouped = df.groupby("depression_label").mean(numeric_only=True)
    label_rows = []

    for label, row in grouped.iterrows():
        label_rows.append(
            "| "
            f"{int(label)} | "
            f"{int(label_counts.get(label, 0)):,} | "
            f"{row['daily_social_media_hours']:.2f} | "
            f"{row['sleep_hours']:.2f} | "
            f"{row['stress_level']:.2f} | "
            f"{row['anxiety_level']:.2f} |"
        )

    return f"""<p align="right"><strong>{AUTHOR_LINE}</strong></p>

# {APP_TITLE}

![Teen mental health dashboard summary]({figures['summary']})

## Executive Snapshot

| Metric | Value |
|---|---:|
| Records | {snapshot['records']:,.0f} |
| Columns | {snapshot['columns']:,.0f} |
| Average daily social media hours | {snapshot['avg_social']:.2f} |
| Average sleep hours | {snapshot['avg_sleep']:.2f} |
| Sleep under 8 hours | {format_percent(snapshot['low_sleep_rate'])} |
| 6+ daily social media hours | {snapshot['high_social_count']:,.0f} ({format_percent(snapshot['high_social_rate'])}) |
| Depression label 1 records | {snapshot['label_one_count']:,.0f} |
| Depression label 1 rate | {format_percent(snapshot['label_one_rate'])} |

## Label 1 vs Label 0

| Comparison | Difference |
|---|---:|
| Daily social media hours | {gaps['social']:+.2f} |
| Sleep hours | {gaps['sleep']:+.2f} |
| Stress level | {gaps['stress']:+.2f} |
| Anxiety level | {gaps['anxiety']:+.2f} |

## Visual Dashboard Boards

![Overview dashboard board]({figures['overview']})

![Signal profile dashboard board]({figures['risk_profile']})

## Label Comparison Table

| Depression label | Records | Avg social media hours | Avg sleep hours | Avg stress | Avg anxiety |
|---:|---:|---:|---:|---:|---:|
{chr(10).join(label_rows)}

## Notes

- Generated from `{source_path}`.
- This dashboard is descriptive exploratory analysis only.
- The `depression_label` column is a dataset label, not a clinical diagnosis.
- Run the interactive version locally with `streamlit run dashboard.py`.
"""


def main() -> None:
    set_plot_theme()
    source_path = find_data_file()
    df = load_clean_data(source_path)

    figures = {
        "summary": save_figure(
            draw_summary_dashboard(df, source_path),
            "dashboard_summary.png",
        ),
        "overview": save_figure(
            draw_overview_board(df),
            "dashboard_overview.png",
        ),
        "risk_profile": save_figure(
            draw_risk_profile_board(df),
            "dashboard_signal_profile.png",
        ),
    }

    REPORT_PATH.write_text(build_markdown(df, source_path, figures), encoding="utf-8")
    print(f"Wrote {REPORT_PATH}")
    print(f"Wrote {len(figures)} dashboard figures to {FIGURE_DIR}")


if __name__ == "__main__":
    main()
