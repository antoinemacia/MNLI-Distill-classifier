import pandas as pd
from pathlib import Path
import json

TRAINING_DATASET_PATH = './embold_train.json'
CSV_OUTPUT_PATH = 'unlabelled_titles_simple.csv'


def json_to_df(path):
    with open(path) as json_file:
        parsed_file = json.load(json_file)

    return pd.DataFrame(parsed_file)


filepath = Path(TRAINING_DATASET_PATH)

df = json_to_df(filepath)
df["text"] = df["title"]
df.to_csv(CSV_OUTPUT_PATH, index=False, columns = ["text"])
