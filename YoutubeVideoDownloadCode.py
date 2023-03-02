import pytube
from pytube import YouTube
import sys
from PyQt5 import QtWidgets as qtw
from VideoDownloadDesign import Ui_MainWindow

class Uygulama(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow() 
        self.ui.setupUi(self)

        self.ui.indirbutton.clicked.connect(self.indir)
        

    def indir(self):
        link = self.ui.indirtext.text()
        youtube = pytube.YouTube(link)
        path="C:/Users/enes_/OneDrive/Masaüstü/PythonEgitimleri/YoutubeVideoIndirFormUygulaması/IndirilenVıdeolar"
        youtube_streams = youtube.streams.filter(file_extension='mp4').get_by_itag(22) #720p çözünürlükte bir videoyu indirmek için
        youtube_streams.download(path)
        print("Download Successful")
        


def app():
    app=qtw.QApplication(sys.argv)
    win=Uygulama()
    win.show()
    sys.exit(app.exec_())
app()
