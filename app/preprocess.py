import pandas as pd

def preprocess_records(records):
    """
    Converts raw learning records into a clean DataFrame
    """
    df = pd.DataFrame([r.dict() for r in records])
    return df
