import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
df = pd.read_json("https://www.opendata.go.ke/resource/p452-xb7c.json")
print(df.head(5))