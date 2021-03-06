# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainframe.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(500, 600))
        Form.setMaximumSize(QtCore.QSize(500, 600))
        Form.setBaseSize(QtCore.QSize(500, 600))
        Form.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pictures/Main_icon_32x32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 40, 454, 521))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pic_dia = QtWidgets.QLabel(self.layoutWidget)
        self.pic_dia.setMinimumSize(QtCore.QSize(64, 64))
        self.pic_dia.setMaximumSize(QtCore.QSize(64, 64))
        self.pic_dia.setText("")
        self.pic_dia.setPixmap(QtGui.QPixmap(":/pictures/D_icon.png"))
        self.pic_dia.setObjectName("pic_dia")
        self.horizontalLayout.addWidget(self.pic_dia)
        self.label_dia = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dia.sizePolicy().hasHeightForWidth())
        self.label_dia.setSizePolicy(sizePolicy)
        self.label_dia.setMinimumSize(QtCore.QSize(160, 0))
        self.label_dia.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_dia.setFont(font)
        self.label_dia.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_dia.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_dia.setLineWidth(5)
        self.label_dia.setMidLineWidth(0)
        self.label_dia.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_dia.setIndent(5)
        self.label_dia.setObjectName("label_dia")
        self.horizontalLayout.addWidget(self.label_dia)
        self.ui_dia = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_dia.sizePolicy().hasHeightForWidth())
        self.ui_dia.setSizePolicy(sizePolicy)
        self.ui_dia.setMinimumSize(QtCore.QSize(130, 64))
        self.ui_dia.setMaximumSize(QtCore.QSize(130, 64))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ui_dia.setFont(font)
        self.ui_dia.setMouseTracking(True)
        self.ui_dia.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ui_dia.setMaxLength(7)
        self.ui_dia.setFrame(True)
        self.ui_dia.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ui_dia.setClearButtonEnabled(False)
        self.ui_dia.setObjectName("ui_dia")
        self.horizontalLayout.addWidget(self.ui_dia)
        self.d_units = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.d_units.setFont(font)
        self.d_units.setObjectName("d_units")
        self.horizontalLayout.addWidget(self.d_units)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pic_speed = QtWidgets.QLabel(self.layoutWidget)
        self.pic_speed.setMinimumSize(QtCore.QSize(64, 64))
        self.pic_speed.setMaximumSize(QtCore.QSize(64, 64))
        self.pic_speed.setText("")
        self.pic_speed.setPixmap(QtGui.QPixmap(":/pictures/V_icon.png"))
        self.pic_speed.setObjectName("pic_speed")
        self.horizontalLayout_2.addWidget(self.pic_speed)
        self.label_speed = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_speed.sizePolicy().hasHeightForWidth())
        self.label_speed.setSizePolicy(sizePolicy)
        self.label_speed.setMinimumSize(QtCore.QSize(160, 0))
        self.label_speed.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_speed.setFont(font)
        self.label_speed.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_speed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_speed.setIndent(5)
        self.label_speed.setObjectName("label_speed")
        self.horizontalLayout_2.addWidget(self.label_speed)
        self.ui_speed = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_speed.sizePolicy().hasHeightForWidth())
        self.ui_speed.setSizePolicy(sizePolicy)
        self.ui_speed.setMinimumSize(QtCore.QSize(130, 64))
        self.ui_speed.setMaximumSize(QtCore.QSize(130, 64))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ui_speed.setFont(font)
        self.ui_speed.setMouseTracking(True)
        self.ui_speed.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ui_speed.setMaxLength(7)
        self.ui_speed.setFrame(True)
        self.ui_speed.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ui_speed.setClearButtonEnabled(False)
        self.ui_speed.setObjectName("ui_speed")
        self.horizontalLayout_2.addWidget(self.ui_speed)
        self.v_units = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.v_units.setFont(font)
        self.v_units.setObjectName("v_units")
        self.horizontalLayout_2.addWidget(self.v_units)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pic_rev = QtWidgets.QLabel(self.layoutWidget)
        self.pic_rev.setMinimumSize(QtCore.QSize(64, 64))
        self.pic_rev.setMaximumSize(QtCore.QSize(64, 64))
        self.pic_rev.setText("")
        self.pic_rev.setPixmap(QtGui.QPixmap(":/pictures/RPM_icon.png"))
        self.pic_rev.setObjectName("pic_rev")
        self.horizontalLayout_3.addWidget(self.pic_rev)
        self.label_rev = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rev.sizePolicy().hasHeightForWidth())
        self.label_rev.setSizePolicy(sizePolicy)
        self.label_rev.setMinimumSize(QtCore.QSize(160, 0))
        self.label_rev.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_rev.setFont(font)
        self.label_rev.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_rev.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_rev.setIndent(5)
        self.label_rev.setObjectName("label_rev")
        self.horizontalLayout_3.addWidget(self.label_rev)
        self.ui_rev = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_rev.sizePolicy().hasHeightForWidth())
        self.ui_rev.setSizePolicy(sizePolicy)
        self.ui_rev.setMinimumSize(QtCore.QSize(130, 64))
        self.ui_rev.setMaximumSize(QtCore.QSize(130, 64))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ui_rev.setFont(font)
        self.ui_rev.setMouseTracking(True)
        self.ui_rev.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ui_rev.setMaxLength(7)
        self.ui_rev.setFrame(True)
        self.ui_rev.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ui_rev.setClearButtonEnabled(False)
        self.ui_rev.setObjectName("ui_rev")
        self.horizontalLayout_3.addWidget(self.ui_rev)
        self.s_units = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.s_units.setFont(font)
        self.s_units.setObjectName("s_units")
        self.horizontalLayout_3.addWidget(self.s_units)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pic_z = QtWidgets.QLabel(self.layoutWidget)
        self.pic_z.setMinimumSize(QtCore.QSize(64, 64))
        self.pic_z.setMaximumSize(QtCore.QSize(64, 64))
        self.pic_z.setText("")
        self.pic_z.setPixmap(QtGui.QPixmap(":/pictures/Z_icon.png"))
        self.pic_z.setObjectName("pic_z")
        self.horizontalLayout_4.addWidget(self.pic_z)
        self.label_z = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_z.sizePolicy().hasHeightForWidth())
        self.label_z.setSizePolicy(sizePolicy)
        self.label_z.setMinimumSize(QtCore.QSize(160, 0))
        self.label_z.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_z.setFont(font)
        self.label_z.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_z.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_z.setIndent(5)
        self.label_z.setObjectName("label_z")
        self.horizontalLayout_4.addWidget(self.label_z)
        self.ui_z = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_z.sizePolicy().hasHeightForWidth())
        self.ui_z.setSizePolicy(sizePolicy)
        self.ui_z.setMinimumSize(QtCore.QSize(130, 64))
        self.ui_z.setMaximumSize(QtCore.QSize(130, 64))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ui_z.setFont(font)
        self.ui_z.setMouseTracking(True)
        self.ui_z.setMaxLength(7)
        self.ui_z.setFrame(True)
        self.ui_z.setClearButtonEnabled(False)
        self.ui_z.setObjectName("ui_z")
        self.horizontalLayout_4.addWidget(self.ui_z)
        self.z_untis = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.z_untis.setFont(font)
        self.z_untis.setObjectName("z_untis")
        self.horizontalLayout_4.addWidget(self.z_untis)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pic_feedrate = QtWidgets.QLabel(self.layoutWidget)
        self.pic_feedrate.setMinimumSize(QtCore.QSize(64, 64))
        self.pic_feedrate.setMaximumSize(QtCore.QSize(64, 64))
        self.pic_feedrate.setText("")
        self.pic_feedrate.setPixmap(QtGui.QPixmap(":/pictures/F_icon.png"))
        self.pic_feedrate.setObjectName("pic_feedrate")
        self.horizontalLayout_5.addWidget(self.pic_feedrate)
        self.label_feedrate = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_feedrate.sizePolicy().hasHeightForWidth())
        self.label_feedrate.setSizePolicy(sizePolicy)
        self.label_feedrate.setMinimumSize(QtCore.QSize(160, 0))
        self.label_feedrate.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_feedrate.setFont(font)
        self.label_feedrate.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_feedrate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_feedrate.setIndent(5)
        self.label_feedrate.setObjectName("label_feedrate")
        self.horizontalLayout_5.addWidget(self.label_feedrate)
        self.ui_feedrate = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_feedrate.sizePolicy().hasHeightForWidth())
        self.ui_feedrate.setSizePolicy(sizePolicy)
        self.ui_feedrate.setMinimumSize(QtCore.QSize(130, 64))
        self.ui_feedrate.setMaximumSize(QtCore.QSize(130, 64))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ui_feedrate.setFont(font)
        self.ui_feedrate.setMouseTracking(True)
        self.ui_feedrate.setMaxLength(7)
        self.ui_feedrate.setFrame(True)
        self.ui_feedrate.setClearButtonEnabled(False)
        self.ui_feedrate.setObjectName("ui_feedrate")
        self.horizontalLayout_5.addWidget(self.ui_feedrate)
        self.f_units = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.f_units.setFont(font)
        self.f_units.setObjectName("f_units")
        self.horizontalLayout_5.addWidget(self.f_units)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pic_feedpertooth = QtWidgets.QLabel(self.layoutWidget)
        self.pic_feedpertooth.setMinimumSize(QtCore.QSize(64, 64))
        self.pic_feedpertooth.setMaximumSize(QtCore.QSize(64, 64))
        self.pic_feedpertooth.setText("")
        self.pic_feedpertooth.setPixmap(QtGui.QPixmap(":/pictures/Fz_icon.png"))
        self.pic_feedpertooth.setObjectName("pic_feedpertooth")
        self.horizontalLayout_6.addWidget(self.pic_feedpertooth)
        self.label_feedpertooth = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_feedpertooth.sizePolicy().hasHeightForWidth())
        self.label_feedpertooth.setSizePolicy(sizePolicy)
        self.label_feedpertooth.setMinimumSize(QtCore.QSize(160, 0))
        self.label_feedpertooth.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_feedpertooth.setFont(font)
        self.label_feedpertooth.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_feedpertooth.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_feedpertooth.setIndent(5)
        self.label_feedpertooth.setObjectName("label_feedpertooth")
        self.horizontalLayout_6.addWidget(self.label_feedpertooth)
        self.ui_feedpertooth = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_feedpertooth.sizePolicy().hasHeightForWidth())
        self.ui_feedpertooth.setSizePolicy(sizePolicy)
        self.ui_feedpertooth.setMinimumSize(QtCore.QSize(130, 64))
        self.ui_feedpertooth.setMaximumSize(QtCore.QSize(130, 64))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ui_feedpertooth.setFont(font)
        self.ui_feedpertooth.setMouseTracking(True)
        self.ui_feedpertooth.setMaxLength(7)
        self.ui_feedpertooth.setFrame(True)
        self.ui_feedpertooth.setClearButtonEnabled(False)
        self.ui_feedpertooth.setObjectName("ui_feedpertooth")
        self.horizontalLayout_6.addWidget(self.ui_feedpertooth)
        self.fz_units = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.fz_units.setFont(font)
        self.fz_units.setObjectName("fz_units")
        self.horizontalLayout_6.addWidget(self.fz_units)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ui_mat_p = QtWidgets.QPushButton(self.layoutWidget)
        self.ui_mat_p.setMinimumSize(QtCore.QSize(50, 60))
        self.ui_mat_p.setMaximumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ui_mat_p.setFont(font)
        self.ui_mat_p.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.ui_mat_p.setObjectName("ui_mat_p")
        self.horizontalLayout_8.addWidget(self.ui_mat_p)
        self.ui_mat_m = QtWidgets.QPushButton(self.layoutWidget)
        self.ui_mat_m.setMinimumSize(QtCore.QSize(50, 60))
        self.ui_mat_m.setMaximumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ui_mat_m.setFont(font)
        self.ui_mat_m.setStyleSheet("background-color: rgb(229, 165, 10);")
        self.ui_mat_m.setObjectName("ui_mat_m")
        self.horizontalLayout_8.addWidget(self.ui_mat_m)
        self.ui_mat_k = QtWidgets.QPushButton(self.layoutWidget)
        self.ui_mat_k.setMinimumSize(QtCore.QSize(50, 60))
        self.ui_mat_k.setMaximumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ui_mat_k.setFont(font)
        self.ui_mat_k.setStyleSheet("background-color: rgb(192, 28, 40);")
        self.ui_mat_k.setObjectName("ui_mat_k")
        self.horizontalLayout_8.addWidget(self.ui_mat_k)
        self.ui_mat_n = QtWidgets.QPushButton(self.layoutWidget)
        self.ui_mat_n.setMinimumSize(QtCore.QSize(50, 60))
        self.ui_mat_n.setMaximumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ui_mat_n.setFont(font)
        self.ui_mat_n.setStyleSheet("background-color: rgb(46, 194, 126);")
        self.ui_mat_n.setObjectName("ui_mat_n")
        self.horizontalLayout_8.addWidget(self.ui_mat_n)
        self.ui_mat_s = QtWidgets.QPushButton(self.layoutWidget)
        self.ui_mat_s.setMinimumSize(QtCore.QSize(50, 60))
        self.ui_mat_s.setMaximumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ui_mat_s.setFont(font)
        self.ui_mat_s.setStyleSheet("background-color: rgb(230, 97, 0);")
        self.ui_mat_s.setObjectName("ui_mat_s")
        self.horizontalLayout_8.addWidget(self.ui_mat_s)
        self.ui_mat_h = QtWidgets.QPushButton(self.layoutWidget)
        self.ui_mat_h.setMinimumSize(QtCore.QSize(50, 60))
        self.ui_mat_h.setMaximumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ui_mat_h.setFont(font)
        self.ui_mat_h.setStyleSheet("background-color: rgb(61, 56, 70);")
        self.ui_mat_h.setObjectName("ui_mat_h")
        self.horizontalLayout_8.addWidget(self.ui_mat_h)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Estilite - CNC Helper"))
        self.label_dia.setText(_translate("Form", "Diameter"))
        self.d_units.setText(_translate("Form", "mm"))
        self.label_speed.setText(_translate("Form", "Cutting Speed"))
        self.v_units.setText(_translate("Form", "m/min"))
        self.label_rev.setText(_translate("Form", "Spindle Speed"))
        self.s_units.setText(_translate("Form", "RPM"))
        self.label_z.setText(_translate("Form", "N of Teeth"))
        self.z_untis.setText(_translate("Form", "#"))
        self.label_feedrate.setText(_translate("Form", "Feedrate"))
        self.f_units.setText(_translate("Form", "mm/min"))
        self.label_feedpertooth.setToolTip(_translate("Form", "<html><head/><body><p>Feed rate</p></body></html>"))
        self.label_feedpertooth.setText(_translate("Form", "Feed per Tooth"))
        self.fz_units.setText(_translate("Form", "mm"))
        self.ui_mat_p.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">P - Steels </span></p><p>Non-, high- and low-alloy steels</p><p><span style=\" font-style:italic;\">up to 400 N/mm</span><span style=\" font-style:italic; vertical-align:super;\">2</span></p></body></html>"))
        self.ui_mat_p.setText(_translate("Form", "P"))
        self.ui_mat_m.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">M - Stainless steel</span></p><p>alloys with Iron as major element and Chrome content higher than 12%</p><p><span style=\" font-style:italic;\">up to 700 N/mm</span><span style=\" font-style:italic; vertical-align:super;\">2</span></p></body></html>"))
        self.ui_mat_m.setText(_translate("Form", "M"))
        self.ui_mat_k.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">K - Cast iron</span></p><p>Cast irons are Fe-C composition with percentage of Silicon in between 1 and 3%.</p><p><span style=\" font-style:italic;\">up to 300 HB</span></p></body></html>"))
        self.ui_mat_k.setText(_translate("Form", "K"))
        self.ui_mat_n.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">N - Non-ferrous materials</span></p><p>soft metals with hardnesses under 130 HB. Aluminum is the most common.</p><p><span style=\" font-style:italic;\">up to 100 HB</span></p></body></html>"))
        self.ui_mat_n.setText(_translate("Form", "N"))
        self.ui_mat_s.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">S - High Temp alloys</span></p><p>High TempAlloys (Nickel, iron or cobalt-based) and Titanium.</p><p><span style=\" font-style:italic;\">up to 1050 N/mm</span><span style=\" font-style:italic; vertical-align:super;\">2</span></p></body></html>"))
        self.ui_mat_s.setText(_translate("Form", "S"))
        self.ui_mat_h.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">H - Hardened materials</span></p><p>Hardened and thermal treated materials with hardness higher than 45HRc.</p><p><span style=\" font-style:italic;\">up to 60 HRC</span></p></body></html>"))
        self.ui_mat_h.setText(_translate("Form", "H"))
import resources_rc
