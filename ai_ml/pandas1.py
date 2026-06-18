import pandas as pd

data = {
    "Name": ["Rahul", "Amit", "Neha"],
    "Age": [25, 30, 28],
    "City": ["Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print(df)