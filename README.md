# 机器视觉算法宝箱

### 1. 图像的SVD分解（Singular Value Decomposition）
<img src="https://latex.codecogs.com/svg.latex?\Large&space;M=U*\Sigma*V^{t}" />

<img src="https://latex.codecogs.com/svg.latex?\Large&space;M" /> : 任意的二维图像/矩阵<br/>
#### 可以分解为：
<img src="https://latex.codecogs.com/svg.latex?\Large&space;U" /> : 经过变换后的新标准正交基<br/>
<img src="https://latex.codecogs.com/svg.latex?\Large&space;\Sigma" /> : V中的向量与U中相对应向量之间的比例关系<br/>
<img src="https://latex.codecogs.com/svg.latex?\Large&space;V" /> : 原始域的标准正交基<br/>
#### 使用SVD做数据信息提取或压缩时，一般往往依据一些策略，例如，设定只提取∑中的前k项，或者保留矩阵中一定百分比的能量信息<br/>

[跳转并查阅示例代码](./image_svd.py)
