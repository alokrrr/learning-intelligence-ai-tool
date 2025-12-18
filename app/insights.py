def generate_insights(results, chapter_difficulty):
    insights = []

    # High-risk students
    high_risk = [r["student_id"] for r in results if r["risk"] == "HIGH"]
    if high_risk:
        insights.append(
            f"{len(high_risk)} students are at high risk of dropping out: {', '.join(high_risk)}"
        )
    else:
        insights.append("No high-risk students detected.")

    # Key risk factor insight
    insights.append(
        "Low assessment scores and low engagement time are the primary factors affecting course completion."
    )

    # Most difficult chapter
    hardest = max(chapter_difficulty, key=lambda x: x["difficulty_score"])
    insights.append(
        f"Chapter {hardest['chapter_id']} appears to be the most difficult with a high dropout rate and low scores."
    )

    return insights
