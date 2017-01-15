# GIS 软件分析大作业

## 环境

* python 2.7
* Windows 7，32 位系统

路网部分做了可视化. 为运行 GUI，需要更多准备工作：

* 安装 qgis、PyQt4，相关环境变量配置，此处略去.
* 将 qgis 安装位置填入 `road/config.py` 内 `QGIS_PATH`.
* 编译 Qt 界面文件
```
cd road
pyuic4 gui_ui.ui > gui_ui.py
cd ..
```


## 数据
请放在 `data/` 下，使用英文文件名.
```
data
├── soil.shx
├── soil.shp
├── soil.dbf
├── road.shx
├── road.shp
└── road.dbf
```
或手动修改 `config.py` 文件中 `FILENAME` 的值.


## 运行方法
### 土壤数据最小包围矩形
运行 `python soil/main.py` 命令，输入图元编号（从 0 开始，以在 shapefile 中的顺序计），输出 MBR.

由于数据量太大造成的困难，未进行可视化展现.

运行结果示意：

    Loaded 94303 shapes.
    shape id> 0
    [121.03072579191806, 45.62512161618308, 135.10151647685353, 53.562097119050215]
    shape id> 233
    [122.32846933652685, 51.31733376179446, 122.84917610237606, 51.78162842182464]
    shape id> 233333
    shape # 233333 does not exist!
    shape id> exit


### 路网两点间最短路径
运行 `python road/main.py` 命令，依次输入待查点的坐标. 视机器配置不同，计算可能花费数秒到数十秒. 有进度条提示. 计算完毕后依次输出路径上的各点坐标.

运行结果示意：

    Loaded 15996 shapes.
    starting point x> 200
    starting point y> 600
    ending point x> 400
    ending point y> 300
    ...
    [(209.81703186035156, 589.093017578125), ..., (397.1900634765625, 298.99798583984375)]




#### 可视化
运行 `python road/gui_main.py` 命令，启动图形界面. 点击 `Open File` 按钮，选择 `road.shp` 文件. 此时窗口中显示路网，可利用鼠标滚轮进行缩放、平移.

用鼠标依次点击起点、终点位置. 起终点位置用蓝色叉子表示. 待进度条走满后，图中红色折线显示这两点间的最短路径，同时窗口右侧表格列出途径各点坐标.

运行时屏幕截图：
![已输入起止点，正在计算](http://lizy14.github.io/GIS-assignments/screenshots/calculating.png)

![计算结果展现](http://lizy14.github.io/GIS-assignments/screenshots/result.png)


## 单元测试
运行 `python road/test.py` 命令.


## 实现说明
### 土壤数据最小包围矩形
实现了平凡的算法. 遍历多边形各个顶点，分别记录诸顶点 x、y 坐标的最大、最小值，其组成的矩形即是.

### 路网拓扑检验
_TODO_

### 路网两点间最短路径
#### 数学建模
采用__加权无向图__对路网建模. 路口（即表示路段的折线段的端点）作为图的__节点__. 如果两个路口间有路段相连，则相应两个节点之间有__边__. 边的权重是路段的长度，即两端点间的折线段的各段线段的欧式距离之和. 如果两个路口间有多个路段，则取其中最小者.

注意到在这样的模型下，路段的形状信息丢失了. 因此在抽象的最短路径问题求解完成后，需要一个额外的步骤来获得原实际问题的解.

之所以将折线段的端点而非每一个顶点作为节点，是出于降低节点数量、降低计算量的考虑. 因只考虑了路口到路口的最短路径. 故对于用户输入的起止点不在路口的情况需要特别处理，此处均用附近的路口作为近似.


#### 数据结构
点的坐标是浮点数二元组，采用 Python 内建 `tuple`. 路口等同于点的坐标. 路段作为折线段则是由点的坐标组成的 `list`. 路网是路段组成的 `list`.  

图的节点编号采用相应路口点的坐标. 图的节点集是上述二元组的集合，采用 `set`.

边和邻接关系保存了两份，其一是邻接矩阵，采用 `dict`，键是由节点编号组成的二元组，值是该边的权重. 其二是邻接集，同为 `dict`，键是节点编号，值是节点编号组成的 `list`.

#### 算法
* 根据 shapefile 包含的折线段集构建图
* 根据用户输入的任意坐标找到图上节点：最近邻搜索. 平凡的遍历法.
* 加权无向图中求节点对最短路径：Dijkstra 算法. 此处略去.
* 把图的最短路径还原为原路网的最短路径

## 代码结构

* I/O 相关
    * `config.py` 保存易变的文件路径等信息，需要由用户手工修改.
    * `shapefile.py` 实现 `shp` 格式文件读取.
    * `dao.py` 是封装的数据访问对象，调用第三方库导入 `shp` 文件.
* 算法实现
    * `mbr.py` 实现求 MBR 的算法.
    * `geometry.py` 集中了和几何度量有关的若干函数，如求路段长度、求最近邻.
    * `graph.py` 是图的数据结构定义及其有关算法的实现.
* 用户界面
    * `progress.py` 实现了一个命令行界面的进度条.
    * `gui_main` 是图形界面的程序的入口.
    * `gui_ui.ui` 是界面文件. `gui_ui.py` 由其编译得到.
* 入口点
    * `main.py` 是命令行界面的程序的入口.
    * `test.py` 含有单元测试.

## 讨论
最短路径计算耗时太长. 在笔者进行实验的 i7-6600U 上，使用 CPython 解释器，计算一个节点对耗时接近 20 秒. 尽管加了进度条以挽回用户体验，不得不说这样的时长并不能满足图形图形界面上实时交互的要求. 有优化空间. 可以考虑重新设计图的数据结构，空间换时间. 必要时可考虑将算法替换为 C 语言实现.

为加快最近邻搜索，可考虑采用 R 树等索引结构. 由于最近邻搜索在总运行时间中所占比例甚小，未实施此项优化.

## 非原创部分
* `shp` 格式文件的解析和导入使用了现有的库 [pyshp](https://pypi.python.org/pypi/pyshp) (`shapefile.py`).
* Dijkstra 算法的 Python 实现参考了 GitHub 用户 [econchick 的代码](https://gist.github.com/econchick/4666413).
* 一个命令行界面的进度条 (`progress.py`) 来自[爆栈网上的回答](https://stackoverflow.com/a/34325723).
