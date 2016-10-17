import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as style

plt.style.use('ggplot')

web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 53, 34, 45, 64, 34],
             'Bounce_Rate': [65, 72, 62, 64, 54, 66]}

df = pd.DataFrame(web_stats)
#
# print(df)
# print(df.head())
# print(df.tail())
# print(df.head(2))
df2 = df.set_index('Day')
print(df2.head())


