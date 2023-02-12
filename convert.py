import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from pathlib import Path 
import json

def json_to_df(path):
    with open(path) as json_file:
        parsed_file = json.load(json_file)

    return pd.DataFrame(parsed_file)


filepath = Path('./embold_train.json')

df = json_to_df(filepath)
df["text"] = df["title"] + "-" + df["body"]
df.to_csv('embold_train.csv', index=False, columns = ["text"])
