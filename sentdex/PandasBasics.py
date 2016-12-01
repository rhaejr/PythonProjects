import pandas as pd
import matplotlib as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats)

# df = df.set_index('Day')
# df.set_index('Day', inplace=True)
# print(df.Visitors)

# print(df[["Bounce Rate","Visitors"]])
print(df.Visitors.tolist())
print(np.array(df[["Bounce Rate","Visitors"]]))