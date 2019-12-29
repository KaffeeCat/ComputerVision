#############################################################
# File name : image_svd.py
# File purpose : demonstate image SVD composition
# Author : Wang Kang
# Date : 2019/12
# Email : price.love@live.cn
#############################################################
import numpy as np
import matplotlib.pyplot as plt  # install matplotlib
from sklearn import datasets     # install scikit-learn
from skimage import io           # install scikit-image

filename = "images/pikachu.jpg"
topk = 200

# read image from file
image = io.imread(filename, as_gray=True)
data_original = np.mat(image)

# singular value decomposition
U, s, V = np.linalg.svd(data_original)

# choose top k important singular values (or eigens)
Uk = U[:,0:topk]
Sk = np.diag(s[0:topk])
Vk = V[0:topk,:]

# recover the image
data_recovered = Uk * Sk * Vk

# show orignal image
plt.subplot(1,2,1)
plt.imshow(data_original, cmap=plt.cm.gray)
plt.subplot(1,2,2)
plt.imshow(data_recovered, cmap=plt.cm.gray)
plt.show()
