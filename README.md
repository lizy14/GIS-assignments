# GIS 软件分析大作业

## 依赖项
* python 2.7
* pyshp 1.2: `pip install -r requirements.txt`


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
运行 `python road/main.py` 命令，依次输入待查点的坐标. 视机器配置不同，计算可能花费十秒到一分钟，有进度条提示. 计算完毕后依次输出路径上的各点坐标.



## 单元测试
运行 `python road/test.py` 命令.
