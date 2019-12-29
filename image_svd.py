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

def svd_compression(data_original, topk):
    """ SVD compression for 2D image/matrix

    Do SVD on 2D matrix/image, and choose top k important singular values to reform it.

    Args:
        data_original: 2D matrix/image.
        topk: how many important singular to use.

    Returns:
        A matrix/image reform form top k singular.
    """

    # singular value decomposition
    U, s, V = np.linalg.svd(data_original)

    # choose top k important singular values (or eigens)
    Uk = U[:,0:topk]
    Sk = np.diag(s[0:topk])
    Vk = V[0:topk,:]

    # recover the image
    data_recovered = Uk * Sk * Vk

    return data_recovered


if __name__ == '__main__':

    filename = "images/pikachu.jpg"

    # read image from file
    image = io.imread(filename, as_gray=True)
    data_original = np.mat(image)

    # show orignal image
    plt.subplot(1,4,1)
    plt.imshow(data_original, cmap=plt.cm.gray)
    plt.xlabel('original image')

    # show recovered image
    plt.subplot(1,4,2)
    plt.imshow(svd_compression(data_original, 5), cmap=plt.cm.gray)
    plt.xlabel('svd image(k=5)')

    # show recovered image
    plt.subplot(1,4,3)
    plt.imshow(svd_compression(data_original, 15), cmap=plt.cm.gray)
    plt.xlabel('svd image(k=15)')

    # show recovered image
    plt.subplot(1,4,4)
    plt.imshow(svd_compression(data_original, 50), cmap=plt.cm.gray)
    plt.xlabel('svd image(k=50)')

    plt.show()
