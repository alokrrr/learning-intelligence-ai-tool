def detect_chapter_difficulty(df):
    """
    Returns chapter-level difficulty insights
    """
    chapter_stats = (
        df.groupby("chapter_id")
        .agg(
            avg_time_spent=("time_spent", "mean"),
            avg_score=("score", "mean"),
            dropout_rate=("completed", lambda x: 1 - x.mean())
        )
        .reset_index()
    )

    # Simple difficulty score
    chapter_stats["difficulty_score"] = (
        chapter_stats["avg_time_spent"] * 0.4 +
        (100 - chapter_stats["avg_score"]) * 0.4 +
        chapter_stats["dropout_rate"] * 100 * 0.2
    )

    return chapter_stats
