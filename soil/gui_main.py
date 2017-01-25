# created by 201411172039 Zheng Liangyu
# Shirley Zheng all right reserved


from config import *


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


class PointTool(QgsMapTool):

    last_start_marker = None

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

        main_win.start = point
        if self.last_start_marker is not None:
            self.canvas.scene().removeItem(self.last_start_marker)
        self.last_start_marker = add_new_marker(point)

        main_win.update()


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
        self.map_canvas.setSelectionColor(QColor("red"))

        self.grid.addWidget(self.map_canvas, 0, 0, 1, 1)

        tool = PointTool(self.map_canvas)
        self.map_canvas.setMapTool(tool)

        self.please('click the button to choose a shapefile')


    def please(self, verb):
        self.prompt.setText("" if not verb else "Please {}.".format(verb))
        QApplication.processEvents()

    def get_selected_feature(self):
        point = self.start
        fids = self.index.intersects(QgsRectangle(point, point))

        request = QgsFeatureRequest()
        request.setFilterFids(fids)
        features = self.layer.getFeatures(request)

        for feature in features:
            if feature.geometry().contains(point):
                return feature
        raise Exception()

    def update(self):

        feature = self.get_selected_feature()
        self.layer.setSelectedFeatures([feature.id()])
        box = feature.geometry().boundingBox()

        if self.last_rubber is not None:
            self.map_canvas.scene().removeItem(self.last_rubber)
        r = QgsRubberBand(self.map_canvas, False)  # False = not a polygon
        r.setColor(QColor(0, 255, 0, 80))
        r.setToGeometry(QgsGeometry.fromRect(box), None)
        self.last_rubber = r

        text = "Shape #{}'s MBR: xmin={}, xmax={}, ymin={}, ymax={}".format(
            feature.id(),
            box.xMinimum(), box.xMaximum(), box.yMinimum(), box.yMaximum()
        )
        self.prompt.setText(text)

    def openFile(self):
        try:
            assert(DEBUG <= 1)
            fileName = QFileDialog.getOpenFileName(
                self, 'Open File', '/', 'shapefile(*.shp)')
        except:
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
            msg = "Failed to open file {}.".format(fileName)
            QMessageBox.warning(self, 'PyQt', msg, QMessageBox.Ok)
            return

        QgsMapLayerRegistry.instance().addMapLayer(layer)
        canvas_layer = QgsMapCanvasLayer(layer)
        self.map_canvas.setLayerSet([canvas_layer])
        self.map_canvas.zoomToFullExtent()

        main_win.please('wait while spacial index being built ...')
        self.features = layer.getFeatures()
        self.index = QgsSpatialIndex(layer.getFeatures())

        self.please('click on a shape')


app = QApplication([])
QgsApplication.setPrefixPath(QGIS_PATH, True)
QgsApplication.initQgis()

main_win = zlyShow()
f = main_win.windowFlags()
f |= QtCore.Qt.WindowMinMaxButtonsHint
main_win.setWindowFlags(f)

main_win.show()
sys.exit(app.exec_())
