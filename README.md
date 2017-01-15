# GIS 软件分析大作业

## 依赖项

* python 2.7

路网部分做了可视化. 为运行 GUI，需要更多准备工作：

* 安装 qgis、PyQt4，相关环境变量配置，此处略
* 将 qgis 安装位置填入 `road/config.py` 内 `QGIS_PATH`.


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

### 路网两点间最短路径
运行 `python road/main.py` 命令，依次输入待查点的坐标. 视机器配置不同，计算可能花费数秒到数十秒. 有进度条提示. 计算完毕后依次输出路径上的各点坐标.

#### 可视化
运行 `python road/gui_main.py` 命令，点击 `Open File` 按钮，选择 `road.shp` 文件. 此时窗口中显示路网. 用鼠标依次点击起点、终点位置. 起终点位置用蓝色叉子表示. 待进度条走满后，图中红色折线显示这两点间的最短路径，同时窗口右侧表格列出途径各点坐标.


## 单元测试
运行 `python road/test.py` 命令.
