# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainframe.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(321, 325)
        Form.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Form.setAutoFillBackground(False)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 294, 248))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.Parameters = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.Parameters.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.Parameters.setContentsMargins(0, 0, 0, 0)
        self.Parameters.setObjectName("Parameters")
        self.pic_dia = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pic_dia.setObjectName("pic_dia")
        self.Parameters.addWidget(self.pic_dia, 0, 0, 1, 1)
        self.param_dia = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.param_dia.setFont(font)
        self.param_dia.setMaxLength(5)
        self.param_dia.setFrame(True)
        self.param_dia.setClearButtonEnabled(False)
        self.param_dia.setObjectName("param_dia")
        self.Parameters.addWidget(self.param_dia, 0, 2, 1, 1)
        self.param_feed = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.param_feed.setMaxLength(5)
        self.param_feed.setCursorPosition(0)
        self.param_feed.setObjectName("param_feed")
        self.Parameters.addWidget(self.param_feed, 1, 2, 1, 1)
        self.param_feedz = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.param_feedz.setMaxLength(5)
        self.param_feedz.setCursorPosition(0)
        self.param_feedz.setObjectName("param_feedz")
        self.Parameters.addWidget(self.param_feedz, 2, 2, 1, 1)
        self.param_speed = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.param_speed.setMaxLength(5)
        self.param_speed.setCursorPosition(0)
        self.param_speed.setObjectName("param_speed")
        self.Parameters.addWidget(self.param_speed, 3, 2, 1, 1)
        self.param_spindle = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.param_spindle.setMaxLength(5)
        self.param_spindle.setCursorPosition(0)
        self.param_spindle.setObjectName("param_spindle")
        self.Parameters.addWidget(self.param_spindle, 4, 2, 1, 1)
        self.param_z = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.param_z.setMaxLength(5)
        self.param_z.setCursorPosition(0)
        self.param_z.setObjectName("param_z")
        self.Parameters.addWidget(self.param_z, 5, 2, 1, 1)
        self.label_feed = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_feed.sizePolicy().hasHeightForWidth())
        self.label_feed.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_feed.setFont(font)
        self.label_feed.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_feed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_feed.setIndent(5)
        self.label_feed.setObjectName("label_feed")
        self.Parameters.addWidget(self.label_feed, 0, 1, 1, 1)
        self.label_feedz = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_feedz.sizePolicy().hasHeightForWidth())
        self.label_feedz.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_feedz.setFont(font)
        self.label_feedz.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_feedz.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_feedz.setIndent(5)
        self.label_feedz.setObjectName("label_feedz")
        self.Parameters.addWidget(self.label_feedz, 1, 1, 1, 1)
        self.label_speed = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_speed.sizePolicy().hasHeightForWidth())
        self.label_speed.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_speed.setFont(font)
        self.label_speed.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_speed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_speed.setIndent(5)
        self.label_speed.setObjectName("label_speed")
        self.Parameters.addWidget(self.label_speed, 2, 1, 1, 1)
        self.label_speed_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_speed_2.sizePolicy().hasHeightForWidth())
        self.label_speed_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_speed_2.setFont(font)
        self.label_speed_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_speed_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_speed_2.setIndent(5)
        self.label_speed_2.setObjectName("label_speed_2")
        self.Parameters.addWidget(self.label_speed_2, 3, 1, 1, 1)
        self.label_spindle = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_spindle.sizePolicy().hasHeightForWidth())
        self.label_spindle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_spindle.setFont(font)
        self.label_spindle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_spindle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_spindle.setIndent(5)
        self.label_spindle.setObjectName("label_spindle")
        self.Parameters.addWidget(self.label_spindle, 4, 1, 1, 1)
        self.label_z = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_z.sizePolicy().hasHeightForWidth())
        self.label_z.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_z.setFont(font)
        self.label_z.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_z.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_z.setIndent(5)
        self.label_z.setObjectName("label_z")
        self.Parameters.addWidget(self.label_z, 5, 1, 1, 1)
        self.pic_feed = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pic_feed.setObjectName("pic_feed")
        self.Parameters.addWidget(self.pic_feed, 1, 0, 1, 1)
        self.pic_feedz = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pic_feedz.setObjectName("pic_feedz")
        self.Parameters.addWidget(self.pic_feedz, 2, 0, 1, 1)
        self.pic_speed = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pic_speed.setObjectName("pic_speed")
        self.Parameters.addWidget(self.pic_speed, 3, 0, 1, 1)
        self.pic_spindle = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pic_spindle.setObjectName("pic_spindle")
        self.Parameters.addWidget(self.pic_spindle, 4, 0, 1, 1)
        self.pic_z = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pic_z.setObjectName("pic_z")
        self.Parameters.addWidget(self.pic_z, 5, 0, 1, 1)
        self.Parameters.setColumnMinimumWidth(1, 180)
        self.material_p = QtWidgets.QLabel(Form)
        self.material_p.setGeometry(QtCore.QRect(20, 280, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.material_p.setFont(font)
        self.material_p.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.material_p.setAcceptDrops(True)
        self.material_p.setAutoFillBackground(True)
        self.material_p.setAlignment(QtCore.Qt.AlignCenter)
        self.material_p.setObjectName("material_p")
        self.material_m = QtWidgets.QLabel(Form)
        self.material_m.setGeometry(QtCore.QRect(73, 280, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.material_m.setFont(font)
        self.material_m.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.material_m.setAcceptDrops(True)
        self.material_m.setAutoFillBackground(True)
        self.material_m.setAlignment(QtCore.Qt.AlignCenter)
        self.material_m.setObjectName("material_m")
        self.material_k = QtWidgets.QLabel(Form)
        self.material_k.setGeometry(QtCore.QRect(130, 280, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.material_k.setFont(font)
        self.material_k.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.material_k.setAcceptDrops(True)
        self.material_k.setAutoFillBackground(True)
        self.material_k.setAlignment(QtCore.Qt.AlignCenter)
        self.material_k.setObjectName("material_k")
        self.material_n = QtWidgets.QLabel(Form)
        self.material_n.setGeometry(QtCore.QRect(180, 280, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.material_n.setFont(font)
        self.material_n.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.material_n.setAcceptDrops(True)
        self.material_n.setAutoFillBackground(True)
        self.material_n.setAlignment(QtCore.Qt.AlignCenter)
        self.material_n.setObjectName("material_n")
        self.material_s = QtWidgets.QLabel(Form)
        self.material_s.setGeometry(QtCore.QRect(230, 280, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.material_s.setFont(font)
        self.material_s.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.material_s.setAcceptDrops(True)
        self.material_s.setAutoFillBackground(True)
        self.material_s.setAlignment(QtCore.Qt.AlignCenter)
        self.material_s.setObjectName("material_s")
        self.material_h = QtWidgets.QLabel(Form)
        self.material_h.setGeometry(QtCore.QRect(280, 280, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.material_h.setFont(font)
        self.material_h.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.material_h.setAcceptDrops(True)
        self.material_h.setAutoFillBackground(True)
        self.material_h.setAlignment(QtCore.Qt.AlignCenter)
        self.material_h.setObjectName("material_h")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Estilite - CNC Helper"))
        self.pic_dia.setText(_translate("Form", "<html><head/><body><p><img src=\":/pictures/param_pic.png\"/></p></body></html>"))
        self.label_feed.setText(_translate("Form", "N of Teeth"))
        self.label_feedz.setText(_translate("Form", "Feed per Tooth"))
        self.label_speed.setText(_translate("Form", "Cutting Speed"))
        self.label_speed_2.setText(_translate("Form", "Diameter"))
        self.label_spindle.setText(_translate("Form", "Spindle Speed"))
        self.label_z.setToolTip(_translate("Form", "<html><head/><body><p>Feed rate</p></body></html>"))
        self.label_z.setText(_translate("Form", "Feed Rate"))
        self.pic_feed.setText(_translate("Form", "<html><head/><body><p><img src=\":/pictures/param_pic.png\"/></p></body></html>"))
        self.pic_feedz.setText(_translate("Form", "<html><head/><body><p><img src=\":/pictures/param_pic.png\"/></p></body></html>"))
        self.pic_speed.setText(_translate("Form", "<html><head/><body><p><img src=\":/pictures/param_pic.png\"/></p></body></html>"))
        self.pic_spindle.setText(_translate("Form", "<html><head/><body><p><img src=\":/pictures/param_pic.png\"/></p></body></html>"))
        self.pic_z.setText(_translate("Form", "<html><head/><body><p><img src=\":/pictures/param_pic.png\"/></p></body></html>"))
        self.material_p.setToolTip(_translate("Form", "<html><head/><body><p>Steel</p></body></html>"))
        self.material_p.setStatusTip(_translate("Form", "Steel"))
        self.material_p.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#1c71d8;\">P</span></p></body></html>"))
        self.material_m.setToolTip(_translate("Form", "<html><head/><body><p>Stainless steel</p></body></html>"))
        self.material_m.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#f5c211;\">M</span></p></body></html>"))
        self.material_k.setToolTip(_translate("Form", "<html><head/><body><p>Cast iron</p></body></html>"))
        self.material_k.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#c01c28;\">K</span></p></body></html>"))
        self.material_n.setToolTip(_translate("Form", "<html><head/><body><p>Non-ferrous</p></body></html>"))
        self.material_n.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#2ec27e;\">N</span></p></body></html>"))
        self.material_s.setToolTip(_translate("Form", "<html><head/><body><p>High-temp alloys</p></body></html>"))
        self.material_s.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#865e3c;\">S</span></p></body></html>"))
        self.material_h.setToolTip(_translate("Form", "<html><head/><body><p>Hardened steels</p></body></html>"))
        self.material_h.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#5e5c64;\">H</span></p></body></html>"))

import resources_rc
