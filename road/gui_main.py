# created by 201411172039 Zheng Liangyu
# Shirley Zheng all right reserved


from config import FILENAME, QGIS_PATH
from dao import *
from graph import *
from progress import printProgress

from qgis.core import *
from qgis.gui import *
import qgis
from PyQt4.QtGui import *
from PyQt4 import QtCore
import gui_ui as createGUI
import sys
import os

guiPath = os.getcwd()
sys.path.append(guiPath)

def progress(iter, total):
    printProgress(iter, total)
    bar = main_win.progressBar
    if iter >= total:
        bar.hide()
    else:
        bar.show()
    main_win.progressBar.setRange(0, total)
    main_win.progressBar.setValue(iter)
    QApplication.processEvents()

class PointTool(QgsMapTool):

    waiting_for_end = False
    last_start_marker = None
    last_end_marker = None


    def __init__(self, canvas):
        QgsMapTool.__init__(self, canvas)
        self.canvas = canvas

    def canvasPressEvent(self, event):
        pass

    def get_point(self, event):
        x = event.pos().x()
        y = event.pos().y()
        point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
        return point

    def canvasMoveEvent(self, event):
        point = self.get_point(event)

    def canvasReleaseEvent(self, event):
        point = self.get_point(event)
        print(point)

        def add_new_marker(point):
            m = QgsVertexMarker(self.canvas)
            m.setCenter(point)
            m.setColor(QColor(0, 0, 255))
            m.setIconSize(10)
            m.setPenWidth(2)
            return m

        if not self.waiting_for_end:
            print('START')
            main_win.start = point
            waiting_for_end = True
            if self.last_start_marker is not None:
                self.canvas.scene().removeItem(self.last_start_marker)
            self.last_start_marker = add_new_marker(point)
            main_win.please('click on the ending point')

        else:
            print('END')
            main_win.end = point
            if self.last_end_marker is not None:
                self.canvas.scene().removeItem(self.last_end_marker)
            self.last_end_marker = add_new_marker(point)
            main_win.update()

        self.waiting_for_end = not self.waiting_for_end



class zlyShow(QDialog, createGUI.Ui_dlgShape):

    start = None
    end = None
    last_rubber = None

    def __init__(self):
        QDialog.__init__(self)
        super(zlyShow, self).__init__()

        self.setupUi(self)
        self.map_canvas = QgsMapCanvas()
        self.map_canvas.setCanvasColor(QColor(233, 233, 233))

        self.grid.addWidget(self.map_canvas, 0, 0, 1, 1)
        self.progressBar.hide()
        self.table.hide()

        tool = PointTool(self.map_canvas)
        self.map_canvas.setMapTool(tool)
        self.please('click the button to choose a shapefile')



    def please(self, verb):
        self.prompt.setText("" if not verb else "Please {}.".format(verb))

    def update(self):

        print(self.start)
        print(self.end)
        main_win.please('wait while the calculation is underway ...')
        path = shortest_path_wrapped(self.shapes, self.graph, self.start, self.end, progress=progress)
        print(path)

        points = map(lambda x: QgsPoint(x[0], x[1]), path)

        if self.last_rubber is not None:
            self.map_canvas.scene().removeItem(self.last_rubber)

        r = QgsRubberBand(self.map_canvas, False)  # False = not a polygon
        r.setColor(QColor(255, 0, 0))
        r.setWidth(2)
        r.setToGeometry(QgsGeometry.fromPolyline(points), None)

        self.last_rubber = r

        model = QStandardItemModel()
        model.setHorizontalHeaderItem(0, QStandardItem('x'))
        model.setHorizontalHeaderItem(1, QStandardItem('y'))

        for i, p in enumerate(path):
            model.setItem(i, 0, QStandardItem(str(p[0])))
            model.setItem(i, 1, QStandardItem(str(p[1])))

        self.table.setModel(model)
        self.table.show()

        main_win.please('click on the starting point')

    def openFile(self):
        '''
        fileName = QFileDialog.getOpenFileName(
            self, 'Open File', '/', 'shapefile(*.shp)')
'''
        fileName = FILENAME
        if not fileName:
            return

        self.label.setText(fileName)

        main_win.please('wait while shapefile being loaded ...')

        try:
            layer = QgsVectorLayer(fileName, 'roads', 'ogr')
            self.layer = layer
            assert(layer.isValid())
        except:
            msg = "Failed to open file {}.".format(filename)
            QMessageBox.warning(self, 'PyQt', msg, QMessageBox.Ok)
            return

        QgsMapLayerRegistry.instance().addMapLayer(layer)
        canvas_layer = QgsMapCanvasLayer(layer)
        self.map_canvas.setLayerSet([canvas_layer])
        self.map_canvas.zoomToFullExtent()

        self.shapes = load_shapes(fileName)
        self.graph = build_graph(self.shapes)

        self.please('click on the starting point')


app = QApplication([])
QgsApplication.setPrefixPath(QGIS_PATH, True)
QgsApplication.initQgis()

main_win = zlyShow()
f = main_win.windowFlags()
f |= QtCore.Qt.WindowMinMaxButtonsHint
main_win.setWindowFlags(f)

main_win.show()
sys.exit(app.exec_())
