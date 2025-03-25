# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard_lihatJadwalKereta.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dashboard_lihatJadwalKereta(object):
    def setupUi(self, dashboard_lihatJadwalKereta):
        dashboard_lihatJadwalKereta.setObjectName("dashboard_lihatJadwalKereta")
        dashboard_lihatJadwalKereta.resize(1078, 879)
        dashboard_lihatJadwalKereta.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #6a11cb, stop:1 #2575fc);\n"
"")
        self.centralwidget = QtWidgets.QWidget(dashboard_lihatJadwalKereta)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_utama = QtWidgets.QFrame(self.centralwidget)
        self.frame_utama.setGeometry(QtCore.QRect(30, 30, 1051, 781))
        self.frame_utama.setStyleSheet("background-color: rgba(255, 255, 255, 180); /* Transparansi */\n"
"border-radius: 15px; /* Membuat sudut melengkung */")
        self.frame_utama.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_utama.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_utama.setObjectName("frame_utama")
        self.user = QtWidgets.QStackedWidget(self.frame_utama)
        self.user.setGeometry(QtCore.QRect(240, 0, 811, 781))
        self.user.setStyleSheet("background : white;")
        self.user.setFrameShape(QtWidgets.QFrame.Box)
        self.user.setFrameShadow(QtWidgets.QFrame.Plain)
        self.user.setObjectName("user")
        self.user_dashboard = QtWidgets.QWidget()
        self.user_dashboard.setObjectName("user_dashboard")
        self.home_user = QtWidgets.QTextEdit(self.user_dashboard)
        self.home_user.setGeometry(QtCore.QRect(10, 120, 791, 651))
        self.home_user.setObjectName("home_user")
        self.home_title_user = QtWidgets.QTextBrowser(self.user_dashboard)
        self.home_title_user.setGeometry(QtCore.QRect(0, 0, 811, 111))
        self.home_title_user.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #6a11cb, stop:1 #2575fc);\n"
"border-radius: 0px; \n"
"")
        self.home_title_user.setObjectName("home_title_user")
        self.user.addWidget(self.user_dashboard)
        self.pembelian_tiket = QtWidgets.QWidget()
        self.pembelian_tiket.setObjectName("pembelian_tiket")
        self.pembelian_tiket_title_user = QtWidgets.QTextBrowser(self.pembelian_tiket)
        self.pembelian_tiket_title_user.setGeometry(QtCore.QRect(0, 0, 811, 111))
        self.pembelian_tiket_title_user.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #6a11cb, stop:1 #2575fc);\n"
"border-radius: 0px; \n"
"")
        self.pembelian_tiket_title_user.setObjectName("pembelian_tiket_title_user")
        self.pembelian_tiket_user = QtWidgets.QTextEdit(self.pembelian_tiket)
        self.pembelian_tiket_user.setGeometry(QtCore.QRect(10, 120, 791, 651))
        self.pembelian_tiket_user.setObjectName("pembelian_tiket_user")
        self.user.addWidget(self.pembelian_tiket)
        self.lihat_jadwal_kereta = QtWidgets.QWidget()
        self.lihat_jadwal_kereta.setObjectName("lihat_jadwal_kereta")
        self.lihat_jadwal_kereta_title_user = QtWidgets.QTextBrowser(self.lihat_jadwal_kereta)
        self.lihat_jadwal_kereta_title_user.setGeometry(QtCore.QRect(0, 0, 811, 111))
        self.lihat_jadwal_kereta_title_user.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #6a11cb, stop:1 #2575fc);\n"
"border-radius: 0px; ")
        self.lihat_jadwal_kereta_title_user.setObjectName("lihat_jadwal_kereta_title_user")
        self.lihat_jadwal_kereta_user = QtWidgets.QTextEdit(self.lihat_jadwal_kereta)
        self.lihat_jadwal_kereta_user.setGeometry(QtCore.QRect(10, 120, 791, 651))
        self.lihat_jadwal_kereta_user.setObjectName("lihat_jadwal_kereta_user")
        self.verticalFrame_2 = QtWidgets.QFrame(self.lihat_jadwal_kereta)
        self.verticalFrame_2.setGeometry(QtCore.QRect(170, 130, 491, 211))
        self.verticalFrame_2.setStyleSheet("QFrame {\n"
"    background-color: #E3F2FD; /* Warna latar belakang */\n"
"    border: 2px solid #5C6BC0; /* Warna border */\n"
"    border-radius: 10px; /* Membuat sudut melengkung */\n"
"    padding: 10px; /* Memberikan jarak dalam frame */\n"
"}\n"
"\n"
"QFrame#mainFrame {\n"
"    background-color: #FFFFFF; /* Warna latar belakang utama */\n"
"    border: 3px solid #3F51B5; /* Warna border lebih tebal */\n"
"    border-radius: 12px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QFrame#sidePanel {\n"
"    background-color: #E1E1E1; /* Warna untuk panel samping */\n"
"    border-right: 4px solid #3F51B5; /* Border hanya di sebelah kanan */\n"
"}\n"
"")
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_nama_kereta_2 = QtWidgets.QLineEdit(self.verticalFrame_2)
        self.input_nama_kereta_2.setStyleSheet("QLineEdit {\n"
"    font-size: 14px;\n"
"    padding: 8px;\n"
"    border: 2px solid #5C6BC0; /* Warna border */\n"
"    border-radius: 5px;\n"
"    background-color: #F3F4F6; /* Warna latar */\n"
"    selection-background-color: #7986CB; /* Warna saat teks dipilih */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3F51B5; /* Warna border saat fokus */\n"
"    background-color: #FFFFFF; /* Warna latar saat fokus */\n"
"}\n"
"")
        self.input_nama_kereta_2.setText("")
        self.input_nama_kereta_2.setObjectName("input_nama_kereta_2")
        self.verticalLayout_2.addWidget(self.input_nama_kereta_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.input_stasiun_awal_2 = QtWidgets.QLineEdit(self.verticalFrame_2)
        self.input_stasiun_awal_2.setStyleSheet("QLineEdit {\n"
"    min-width: 180px; /* Lebar minimum */\n"
"    max-width: 200px; /* Lebar maksimum */\n"
"    width: 50%; /* Lebar mengikuti parent */\n"
"    padding: 8px; /* Jarak teks dari border */\n"
"    border: 2px solid #3F51B5;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    background-color: #F3F4F6; /* Warna latar */\n"
"    selection-background-color: #7986CB;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3F51B5; /* Warna border saat fokus */\n"
"    background-color: #FFFFFF; /* Warna latar saat fokus */\n"
"}\n"
"")
        self.input_stasiun_awal_2.setText("")
        self.input_stasiun_awal_2.setObjectName("input_stasiun_awal_2")
        self.horizontalLayout_3.addWidget(self.input_stasiun_awal_2)
        self.label_3 = QtWidgets.QLabel(self.verticalFrame_2)
        self.label_3.setMinimumSize(QtCore.QSize(20, 20))
        self.label_3.setMaximumSize(QtCore.QSize(150, 150))
        self.label_3.setStyleSheet("QLabel#label_2 {\n"
"    background-image: url(E:/newPrefix/PYTHONN/ujiCoba1/icon/right-arrow.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-size:10px 10px; /* Ubah ukuran sesuai kebutuhan */\n"
"}\n"
"")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/E:/PYTHONN/ujiCoba1/icon/right-arrow.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.input_stasiun_tujuan_2 = QtWidgets.QLineEdit(self.verticalFrame_2)
        self.input_stasiun_tujuan_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.input_stasiun_tujuan_2.setStyleSheet("QLineEdit {\n"
"    min-width: 180px; /* Lebar minimum */\n"
"    max-width: 200px; /* Lebar maksimum */\n"
"    width: 50%; /* Lebar mengikuti parent */\n"
"    padding: 8px; /* Jarak teks dari border */\n"
"    border: 2px solid #3F51B5;\n"
"    border-radius: 5px;\n"
"    font-size: 14px;\n"
"    background-color: #F3F4F6; /* Warna latar */\n"
"    selection-background-color: #7986CB;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3F51B5; /* Warna border saat fokus */\n"
"    background-color: #FFFFFF; /* Warna latar saat fokus */\n"
"}\n"
"\n"
"")
        self.input_stasiun_tujuan_2.setText("")
        self.input_stasiun_tujuan_2.setObjectName("input_stasiun_tujuan_2")
        self.horizontalLayout_3.addWidget(self.input_stasiun_tujuan_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tombo_search_2 = QtWidgets.QPushButton(self.verticalFrame_2)
        self.tombo_search_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tombo_search_2.setStyleSheet("QPushButton {\n"
"    background-color: #3F51B5; /* Warna biru */\n"
"    color: white; /* Warna teks putih */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #303F9F; /* Border biru tua */\n"
"    border-radius: 8px; /* Membuat sudut tombol membulat */\n"
"    padding: 8px 15px; /* Jarak dalam tombol */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #303F9F; /* Warna lebih gelap saat hover */\n"
"    border: 2px solid #1A237E;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1A237E; /* Warna lebih gelap saat ditekan */\n"
"    border: 2px solid #000051;\n"
"}\n"
"")
        self.tombo_search_2.setObjectName("tombo_search_2")
        self.verticalLayout_2.addWidget(self.tombo_search_2)
        self.tombo_search_3 = QtWidgets.QPushButton(self.verticalFrame_2)
        self.tombo_search_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tombo_search_3.setStyleSheet("QPushButton {\n"
"    background-color: #3F51B5; /* Warna biru */\n"
"    color: white; /* Warna teks putih */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #303F9F; /* Border biru tua */\n"
"    border-radius: 8px; /* Membuat sudut tombol membulat */\n"
"    padding: 8px 15px; /* Jarak dalam tombol */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #303F9F; /* Warna lebih gelap saat hover */\n"
"    border: 2px solid #1A237E;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1A237E; /* Warna lebih gelap saat ditekan */\n"
"    border: 2px solid #000051;\n"
"}\n"
"")
        self.tombo_search_3.setObjectName("tombo_search_3")
        self.verticalLayout_2.addWidget(self.tombo_search_3)
        self.tableWidget = QtWidgets.QTableWidget(self.lihat_jadwal_kereta)
        self.tableWidget.setGeometry(QtCore.QRect(40, 350, 731, 371))
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    border: 1px solid #ccc;\n"
"    gridline-color: #aaa;\n"
"    font-size: 12pt;\n"
"    background-color: white;\n"
"    alternate-background-color: #f9f9f9;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #e0e0e0;\n"
"    padding: 6px;\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"    border: 1px solid #bbb;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tombol_kembali = QtWidgets.QPushButton(self.lihat_jadwal_kereta)
        self.tombol_kembali.setGeometry(QtCore.QRect(190, 730, 449, 37))
        self.tombol_kembali.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tombol_kembali.setStyleSheet("QPushButton {\n"
"    background-color: #E52020 ; /* Warna biru */\n"
"    color: black; /* Warna teks putih */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #303F9F; /* Border biru tua */\n"
"    border-radius: 8px; /* Membuat sudut tombol membulat */\n"
"    padding: 8px 15px; /* Jarak dalam tombol */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #982B1C; /* Warna lebih gelap saat hover */\n"
"    border: 2px solid #1A237E;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1D1616; /* Warna lebih gelap saat ditekan */\n"
"    border: 2px solid #000051;\n"
"}")
        self.tombol_kembali.setObjectName("tombol_kembali")
        self.user.addWidget(self.lihat_jadwal_kereta)
        self.tiket_saya = QtWidgets.QWidget()
        self.tiket_saya.setObjectName("tiket_saya")
        self.tiket_saya_tittle_user = QtWidgets.QTextBrowser(self.tiket_saya)
        self.tiket_saya_tittle_user.setGeometry(QtCore.QRect(0, 0, 811, 111))
        self.tiket_saya_tittle_user.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #6a11cb, stop:1 #2575fc);\n"
"border-radius: 0px; ")
        self.tiket_saya_tittle_user.setObjectName("tiket_saya_tittle_user")
        self.tiket_saya_user = QtWidgets.QTextEdit(self.tiket_saya)
        self.tiket_saya_user.setGeometry(QtCore.QRect(10, 120, 791, 651))
        self.tiket_saya_user.setObjectName("tiket_saya_user")
        self.user.addWidget(self.tiket_saya)
        self.home_button = QtWidgets.QPushButton(self.frame_utama)
        self.home_button.setGeometry(QtCore.QRect(10, 130, 221, 81))
        self.home_button.setMouseTracking(True)
        self.home_button.setTabletTracking(True)
        self.home_button.setObjectName("home_button")
        self.sakapeung = QtWidgets.QTextBrowser(self.frame_utama)
        self.sakapeung.setGeometry(QtCore.QRect(10, 30, 251, 71))
        self.sakapeung.setStyleSheet("  background: transparent;")
        self.sakapeung.setObjectName("sakapeung")
        self.pembelian_tiket_button = QtWidgets.QPushButton(self.frame_utama)
        self.pembelian_tiket_button.setGeometry(QtCore.QRect(10, 220, 221, 81))
        self.pembelian_tiket_button.setMouseTracking(True)
        self.pembelian_tiket_button.setTabletTracking(True)
        self.pembelian_tiket_button.setObjectName("pembelian_tiket_button")
        self.lihat_jadwal_kereta_button = QtWidgets.QPushButton(self.frame_utama)
        self.lihat_jadwal_kereta_button.setGeometry(QtCore.QRect(10, 310, 221, 81))
        self.lihat_jadwal_kereta_button.setMouseTracking(True)
        self.lihat_jadwal_kereta_button.setTabletTracking(True)
        self.lihat_jadwal_kereta_button.setObjectName("lihat_jadwal_kereta_button")
        self.tiket_saya_button = QtWidgets.QPushButton(self.frame_utama)
        self.tiket_saya_button.setGeometry(QtCore.QRect(10, 400, 221, 81))
        self.tiket_saya_button.setMouseTracking(True)
        self.tiket_saya_button.setTabletTracking(True)
        self.tiket_saya_button.setObjectName("tiket_saya_button")
        self.dashboard_akun_button = QtWidgets.QPushButton(self.frame_utama)
        self.dashboard_akun_button.setGeometry(QtCore.QRect(10, 490, 221, 81))
        self.dashboard_akun_button.setMouseTracking(True)
        self.dashboard_akun_button.setTabletTracking(True)
        self.dashboard_akun_button.setObjectName("dashboard_akun_button")
        self.dashboard_rekening_button = QtWidgets.QPushButton(self.frame_utama)
        self.dashboard_rekening_button.setGeometry(QtCore.QRect(10, 580, 221, 81))
        self.dashboard_rekening_button.setMouseTracking(True)
        self.dashboard_rekening_button.setTabletTracking(True)
        self.dashboard_rekening_button.setObjectName("dashboard_rekening_button")
        self.keluar_button = QtWidgets.QPushButton(self.frame_utama)
        self.keluar_button.setGeometry(QtCore.QRect(10, 670, 221, 81))
        self.keluar_button.setMouseTracking(True)
        self.keluar_button.setTabletTracking(True)
        self.keluar_button.setObjectName("keluar_button")
        self.sakapeung.raise_()
        self.user.raise_()
        self.home_button.raise_()
        self.pembelian_tiket_button.raise_()
        self.lihat_jadwal_kereta_button.raise_()
        self.tiket_saya_button.raise_()
        self.dashboard_akun_button.raise_()
        self.dashboard_rekening_button.raise_()
        self.keluar_button.raise_()
        dashboard_lihatJadwalKereta.setCentralWidget(self.centralwidget)

        self.retranslateUi(dashboard_lihatJadwalKereta)
        self.user.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(dashboard_lihatJadwalKereta)

    def retranslateUi(self, dashboard_lihatJadwalKereta):
        _translate = QtCore.QCoreApplication.translate
        dashboard_lihatJadwalKereta.setWindowTitle(_translate("dashboard_lihatJadwalKereta", "Dashboard SAKAPEUNG"))
        self.home_user.setHtml(_translate("dashboard_lihatJadwalKereta", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">Ini adalah dashboard user</span></p></body></html>"))
        self.home_title_user.setHtml(_translate("dashboard_lihatJadwalKereta", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Dashboard User</span></p></body></html>"))
        self.pembelian_tiket_title_user.setHtml(_translate("dashboard_lihatJadwalKereta", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Pembelian Tiket Kereta Api</span></p></body></html>"))
        self.pembelian_tiket_user.setHtml(_translate("dashboard_lihatJadwalKereta", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ini adalah halaman pembelian tiket</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lihat_jadwal_kereta_title_user.setHtml(_translate("dashboard_lihatJadwalKereta", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Lihat Jadwal Kereta Api</span></p></body></html>"))
        self.lihat_jadwal_kereta_user.setHtml(_translate("dashboard_lihatJadwalKereta", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.input_nama_kereta_2.setPlaceholderText(_translate("dashboard_lihatJadwalKereta", "Masukkan nama kereta"))
        self.input_stasiun_awal_2.setPlaceholderText(_translate("dashboard_lihatJadwalKereta", "Staisun Awal"))
        self.input_stasiun_tujuan_2.setPlaceholderText(_translate("dashboard_lihatJadwalKereta", "Stasiun Tujuan"))
        self.tombo_search_2.setText(_translate("dashboard_lihatJadwalKereta", "Cari Kereta"))
        self.tombo_search_3.setText(_translate("dashboard_lihatJadwalKereta", "Reset "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dashboard_lihatJadwalKereta", "Id_kereta"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dashboard_lihatJadwalKereta", "Nama_kereta"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("dashboard_lihatJadwalKereta", "Tanggal"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("dashboard_lihatJadwalKereta", "Staisun_Transit"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("dashboard_lihatJadwalKereta", "Waktu_Transit"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("dashboard_lihatJadwalKereta", "Jenis Layanan"))
        self.tombol_kembali.setText(_translate("dashboard_lihatJadwalKereta", "Kembali"))
        self.tiket_saya_tittle_user.setHtml(_translate("dashboard_lihatJadwalKereta", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Tiket Saya</span></p></body></html>"))
        self.tiket_saya_user.setHtml(_translate("dashboard_lihatJadwalKereta", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">Ini adalah menu tiket saya</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.home_button.setText(_translate("dashboard_lihatJadwalKereta", "Home"))
        self.sakapeung.setHtml(_translate("dashboard_lihatJadwalKereta", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\">SAKAPEUNG</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt;\"><br /></p></body></html>"))
        self.pembelian_tiket_button.setText(_translate("dashboard_lihatJadwalKereta", "Pembelian Tiket"))
        self.lihat_jadwal_kereta_button.setText(_translate("dashboard_lihatJadwalKereta", "Lihat Jadwal Kereta"))
        self.tiket_saya_button.setText(_translate("dashboard_lihatJadwalKereta", "Tiket Saya"))
        self.dashboard_akun_button.setText(_translate("dashboard_lihatJadwalKereta", "Dashboard Akun"))
        self.dashboard_rekening_button.setText(_translate("dashboard_lihatJadwalKereta", "Dashboard Rekening"))
        self.keluar_button.setText(_translate("dashboard_lihatJadwalKereta", "Keluar Dari Aplikasi"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dashboard_lihatJadwalKereta = QtWidgets.QMainWindow()
    ui = Ui_dashboard_lihatJadwalKereta()
    ui.setupUi(dashboard_lihatJadwalKereta)
    dashboard_lihatJadwalKereta.show()
    sys.exit(app.exec_())
