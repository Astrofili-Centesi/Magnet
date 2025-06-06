import pandas as pd
import sys

d=pd.read_csv(sys.argv[1])
d.drop(columns=[d.columns[0],"result","table"],inplace=True)
#d=d.pivot(index="_time",columns="_field",values="_value").reset_index()
d=d.set_index("_time")
d.columns=["magnet"]
d.index.name="time"
print(d)
d.to_json(sys.argv[2])
