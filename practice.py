import pandas as pd

df = pd.read_csv("data.csv")

emotions = df["clasification"].value_counts()
emotions['happy']

n_happy = int(emotions['happy'])
n_neutral = emotions['neutral']
n_bad = emotions['bad']

print(type(n_happy))



