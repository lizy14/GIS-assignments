# created by 201411172039 Zheng Liangyu
# Shirley Zheng all right reserved


from config import QGIS_PATH

from qgis.core import *
from qgis.gui import *
from PyQt4.QtGui import *
from PyQt4 import QtCore
import gui_ui as createGUI
import sys
import os

guiPath = os.getcwd()
sys.path.append(guiPath)


class zlyShow(QDialog, createGUI.Ui_dlgShape):

    def __init__(self):
        QDialog.__init__(self)
        super(zlyShow, self).__init__()

        self.setupUi(self)
        self.map_canvas = QgsMapCanvas()
        self.map_canvas.setCanvasColor(QColor(233, 233, 233))

        self.grid.addWidget(self.map_canvas, 0, 0, 1, 1)

    def openFile(self):
        fileName = QFileDialog.getOpenFileName(
            self, 'Open File', '/', 'shapefile(*.shp)')

        if not fileName:
            return

        self.label.setText(fileName)
        (name, ext) = os.path.splitext(os.path.basename(fileName))

        try:
            layer = QgsVectorLayer(fileName, name, 'ogr')
            assert(layer.isValid())
        except:
            msg = "Failed to open file {}.".format(filename)
            QMessageBox.warning(self, 'PyQt', msg, QMessageBox.Ok)
            return

        QgsMapLayerRegistry.instance().addMapLayer(layer)
        canvas_layer = QgsMapCanvasLayer(layer)
        self.map_canvas.setLayerSet([canvas_layer])
        self.map_canvas.zoomToFullExtent()


app = QApplication([])
QgsApplication.setPrefixPath(QGIS_PATH, True)
QgsApplication.initQgis()

main_win = zlyShow()
f = main_win.windowFlags()
f |= QtCore.Qt.WindowMinMaxButtonsHint
main_win.setWindowFlags(f)

main_win.show()
sys.exit(app.exec_())
