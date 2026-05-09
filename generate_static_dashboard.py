from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from dashboard import (
    find_data_file,
    load_clean_data,
    plot_correlation_heatmap,
    plot_count_bar,
    plot_group_comparison,
    plot_platform_bar,
    plot_sleep_histogram,
    plot_stress_anxiety_heatmap,
)


REPORT_PATH = Path("reports") / "DASHBOARD.md"
FIGURE_DIR = Path("reports") / "figures"


def save_figure(fig, filename: str) -> str:
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    path = FIGURE_DIR / filename
    fig.savefig(path, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return f"figures/{filename}"


def format_percent(value: float) -> str:
    return f"{value:.2f}%"


def build_markdown(df: pd.DataFrame, source_path: Path, figures: dict[str, str]) -> str:
    records = len(df)
    label_counts = df["depression_label"].value_counts().sort_index()
    label_one_count = int(label_counts.get(1, 0))
    label_one_rate = label_one_count / records * 100
    low_sleep_rate = (df["sleep_hours"] < 8).mean() * 100
    high_academic_count = int((df["academic_performance"] > 3.5).sum())
    high_academic_rate = high_academic_count / records * 100

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

    return f"""# Teen Mental Health Dashboard

This is a GitHub-friendly static dashboard generated from `{source_path}`. GitHub cannot run Streamlit apps inside the repository file view, so this page saves the dashboard charts as PNG images that can be viewed directly on GitHub.

## KPI Summary

| Metric | Value |
|---|---:|
| Records | {records:,} |
| Columns | {len(df.columns):,} |
| Average daily social media hours | {df['daily_social_media_hours'].mean():.2f} |
| Average sleep hours | {df['sleep_hours'].mean():.2f} |
| Sleep under 8 hours | {format_percent(low_sleep_rate)} |
| Depression label 1 records | {label_one_count:,} |
| Depression label 1 rate | {format_percent(label_one_rate)} |
| Academic performance above 3.5 | {high_academic_count:,} ({format_percent(high_academic_rate)}) |

## Label Comparison

| Depression label | Records | Avg social media hours | Avg sleep hours | Avg stress | Avg anxiety |
|---:|---:|---:|---:|---:|---:|
{chr(10).join(label_rows)}

## Overview Charts

![Depression label count]({figures['depression_count']})

![Platform usage]({figures['platform_usage']})

![Sleep distribution]({figures['sleep_distribution']})

## Lifestyle Signals

![Stress vs anxiety heatmap]({figures['stress_anxiety']})

![Correlation heatmap]({figures['correlation']})

## Depression Label Differences

![Average social media hours by label]({figures['social_by_label']})

![Average sleep hours by label]({figures['sleep_by_label']})

![Average stress level by label]({figures['stress_by_label']})

![Average anxiety level by label]({figures['anxiety_by_label']})

## Notes

- This dashboard is descriptive exploratory analysis only.
- The `depression_label` column is a dataset label, not a clinical diagnosis.
- The label 1 group is small, so comparisons should be interpreted carefully.
- Run the interactive version locally with `streamlit run dashboard.py`.
"""


def main() -> None:
    source_path = find_data_file()
    df = load_clean_data(source_path)

    figures = {
        "depression_count": save_figure(
            plot_count_bar(df, "depression_label", "Depression Label Count", "Label"),
            "depression_label_count.png",
        ),
        "platform_usage": save_figure(
            plot_platform_bar(df),
            "platform_usage.png",
        ),
        "sleep_distribution": save_figure(
            plot_sleep_histogram(df),
            "sleep_distribution.png",
        ),
        "stress_anxiety": save_figure(
            plot_stress_anxiety_heatmap(df),
            "stress_anxiety_heatmap.png",
        ),
        "correlation": save_figure(
            plot_correlation_heatmap(df),
            "correlation_heatmap.png",
        ),
        "social_by_label": save_figure(
            plot_group_comparison(
                df,
                "daily_social_media_hours",
                "Average Social Media Hours by Label",
                "Average hours",
            ),
            "avg_social_media_by_label.png",
        ),
        "sleep_by_label": save_figure(
            plot_group_comparison(
                df,
                "sleep_hours",
                "Average Sleep Hours by Label",
                "Average hours",
            ),
            "avg_sleep_by_label.png",
        ),
        "stress_by_label": save_figure(
            plot_group_comparison(
                df,
                "stress_level",
                "Average Stress Level by Label",
                "Average score",
            ),
            "avg_stress_by_label.png",
        ),
        "anxiety_by_label": save_figure(
            plot_group_comparison(
                df,
                "anxiety_level",
                "Average Anxiety Level by Label",
                "Average score",
            ),
            "avg_anxiety_by_label.png",
        ),
    }

    REPORT_PATH.write_text(build_markdown(df, source_path, figures), encoding="utf-8")
    print(f"Wrote {REPORT_PATH}")
    print(f"Wrote {len(figures)} figures to {FIGURE_DIR}")


if __name__ == "__main__":
    main()
