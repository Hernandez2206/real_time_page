import pandas as pd
import numpy as np
import time

df = pd.read_csv("data.csv")
emotions = ["happy", "neutral", "bad"]



for seconds in range(200):
    random_value = np.random.randint(1,5)
    random_emotion = np.random.choice(emotions)
    df = df.append({"tweet":random_value, "username":random_value, "clasification": random_emotion}, ignore_index=True)
    df.to_csv("data1.csv")
    time.sleep(5)
