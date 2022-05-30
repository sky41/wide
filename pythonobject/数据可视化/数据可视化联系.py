import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
sns.set_style("darkgrid")
plt.plot(np.arange(10))
df_iris = pd.read_csv('iris.csv')
fig, axes = plt.subplots(1, 2)
sns.distplot(df_iris['petal length'], ax=axes[0],
             kde=True, rug=True)        # kde 密度曲线  rug 边际毛毯
sns.kdeplot(df_iris['petal length'], ax=axes[1], shade=True)
plt.show()
