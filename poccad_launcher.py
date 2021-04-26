import sys

from qtpy import QtWidgets

from poccad_Method import Application

if __name__ == "__main__":
    App = QtWidgets.QApplication.instance()
    
    if App is None: # sinon on crée une instance de QApplication
        App =QtWidgets. QApplication(sys.argv)
        App.setStyle(QtWidgets.QStyleFactory.create("Cleanlooks"))
        App.lastWindowClosed.connect(App.quit)
    else:
        pass
    MyApp = Application(App)
    MyApp.show()
    
    
    
    try:
        sys.exit(App.exec_())
    except:
        pass

