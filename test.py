from sys import argv
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from urllib.parse import urlsplit, urlparse
from PyQt5 import QtGui


class TabDialog (QDialog):
    def __init__(self, fileName, parent = None):
        QDialog.__init__(self, parent)
        fileInfo = QFileInfo(fileName)

        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(GeneralTab(fileInfo), "General")
        self.tabWidget.addTab(PermissionsTab(fileInfo), "Permissions")
        self.tabWidget.addTab(ApplicationsTab(fileInfo), "Applications")