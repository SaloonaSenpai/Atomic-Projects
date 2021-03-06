from sys import argv
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from urllib.parse import urlsplit, urlparse
from PyQt5 import QtGui

""" ///////// MAIN WINDOW CLASS /////    """

#inherits from the qmain window 
class Mainwindow(QMainWindow):
    def __init__(self):
        #connecting with the main class
        super(Mainwindow,self).__init__()
        #opens as max / full screen mode
        self.showMaximized()
        #creating the brower // Widget that is used to view and edit web documents
        self.browser = QWebEngineView()
        #setting the url for the browser 
        self.browser.setUrl(QUrl("https://duckduckgo.com"))
        #centering shit to view
        self.setCentralWidget(self.browser)
        #adding an icon for the browser
        self.setWindowIcon(QtGui.QIcon('icons\logo.jpg')) 

        title = QLabel("Disconnect")
        title_font = QtGui.QFont("Times", 18)
        title.setFont(title_font)


        # //// adding tool bars  //// 
        
        #navbars 
        navbar = QToolBar()
        navbar.setFixedHeight(35)   #resizing the height of the navbar
        #adding a navbar
        self.addToolBar(navbar)
        
        #adding some tool bars
        
        #back button 
        back_btn = QAction('back',self)    #declaring the back btn using action 
        back_btn.setIcon(QtGui.QIcon('icons/back_buttonx2.png')) #putting an icon 
        back_btn.triggered.connect(self.browser.back)   #when its triggered connect to the browser and go back [type of connect is back]
        navbar.addAction(back_btn)  #adding it to the navbar 
        
        
        #forward 
        forward_btn = QAction('forward',self) #declaring the foward btn using action 
        forward_btn.setIcon(QtGui.QIcon('icons/foward_buttonx2.png')) #putting an icon 
        forward_btn.triggered.connect(self.browser.forward) #when its triggered connect to the browser and go forward [type of connect is forward]
        navbar.addAction(forward_btn)
        
        #reload 
        reload_btn = QAction("reload",self) #declaring the reload btn using action 
        reload_btn.setIcon(QtGui.QIcon('icons/reload.png')) #putting an icon 
        reload_btn.triggered.connect(self.browser.reload)   #connect reload when tiggered
        navbar.addAction(reload_btn)    #add it to the navbar
        
        #stop 
        stop_btn = QAction("Stop",self) #declaring the stop btn
        stop_btn.setIcon(QtGui.QIcon('icons/stop.png'))   #setting an icon for the 
        stop_btn.triggered.connect(self.browser.stop)   #connect stop when triggered
        navbar.addAction(stop_btn)  #add it to the navbar 
        
        

        #nav url_bar 
        self.url_bar = QLineEdit()   #text line to write in
        self.url_bar.setFixedSize(500,30)   #resizing the bar
        font = QtGui.QFont("Times", 10)
        self.url_bar.setFont(font)
        self.url_bar.setStyleSheet("QLineEdit { border-radius: 5px; }")    #adding radius to the bar
        self.url_bar.returnPressed.connect(self.navi_to_url)    #when return is pressed, connect to specific thing that would be a method
        navbar.addWidget(self.url_bar)  #adding the url bar to the navbar
        self.history_list = []
        
        
        #if url has changed you need to update the URL BAR
        self.browser.urlChanged.connect(self.update_url_bar)

        #Home 
        home_btn = QAction("Home",self)
        home_btn.setIcon(QtGui.QIcon('icons/home.png'))
        home_btn.triggered.connect(self.navi_home)  #when clicking on this home button, a method would be running
        navbar.addAction(home_btn)
        
        #history 
        #history = QWebEngineHistory()
        #home_btn.triggered.connect(self.browser.history)
        #navbar.addWidget(self.history_btn) 
        
        

        
        
    def navi_home(self):
        self.browser.setUrl(QUrl("https://duckduckgo.com")) #set the url back to the original
    
    def navi_to_url(self):
        url = self.url_bar.text() #getting the text written 
        split_url = urlsplit(url)
        if split_url.scheme == 'https':
            pass
        elif split_url.scheme == 'http':
            pass
        else:
            url = 'https://' + str(url)
            
        self.browser.setUrl(QUrl(url))  #set the url to the url text from the line edit written 
        self.history_list.append(url)
        
    #takes a paramter
    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())  #to string to make sure its a string
        #takes the parameter and sets it as the text in the url bar
        
    

    
    
    
        
#creating an app taking an arugment from the system 
app = QApplication(argv)
#Naming the browser 
QApplication.setApplicationName(window.title)
#creating the object 
window = Mainwindow()
#execute 
app.exec_()

print(window.history_list)