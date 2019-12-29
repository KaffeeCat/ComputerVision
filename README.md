# 机器视觉算法宝箱

### 1. 图像的SVD分解（Singular Value Decomposition）
<img src="https://latex.codecogs.com/svg.latex?\Large&space;M=U*\Sigma*V^{t}" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;M" /> : 任意的二维图像/矩阵<br/>
#### 可以分解为：
<img src="https://latex.codecogs.com/svg.latex?\Large&space;U" /> : 经过变换后的新标准正交基<br/>
<img src="https://latex.codecogs.com/svg.latex?\Large&space;\Sigma" /> : V中的向量与U中相对应向量之间的比例关系<br/>
<img src="https://latex.codecogs.com/svg.latex?\Large&space;V" /> : 原始域的标准正交基<br/>
#### SVD可以将图像或矩阵通过更小更精简的几个子矩阵相乘来表达，这些小矩阵的是原矩阵的重要特性。使用SVD做数据信息提取或压缩时，一般往往依据一些策略，例如，设定只提取奇异值<img src="https://latex.codecogs.com/svg.latex?\Large&space;\Sigma" />中的前k项，或者保留矩阵中一定百分比的能量信息(如下所示，图像在<img src="https://latex.codecogs.com/svg.latex?\Large&space;\Sigma" />中选择前5,15,50奇异值进行信息提取的时候，逐渐变的清晰)

![image](/images/svd_figure.jpeg)

[跳转并查阅示例代码](./image_svd.py)
