%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from skimage import data, color, feature
import skimage.data
plt.rcParams['font.sans-serif']=['SimHei']
plt.rc('font', size=15)
image = color.rgb2gray(data.chelsea())
hog_vec, hog_vis = feature.hog(image, visualize=True)
fig, ax = plt.subplots(1, 2, figsize=(12, 6),
subplot_kw=dict(xticks=[], yticks=[]))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('输入图片')
ax[1].imshow(hog_vis)
ax[1].set_title('HOG 要素');
plt.show()


