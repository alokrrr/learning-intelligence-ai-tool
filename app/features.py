def build_features(df):
    """
    Builds student-level features for prediction
    """
    features = (
        df.groupby("student_id")
        .agg(
            avg_time_spent=("time_spent", "mean"),
            avg_score=("score", "mean"),
            chapters_attempted=("chapter_id", "count"),
            completion_ratio=("completed", "mean")
        )
        .reset_index()
    )
    return features
