from PyQt5.QtWidgets import QApplication

import gui.ModWindow

if __name__ == '__main__':
    # I'm sure we'll do something eventually, but for now I'm just gonna launch the mod UI
    app = QApplication([])
    modWindow = gui.ModWindow.ModWindow()
    modWindow.show()
    app.exec_()
    # Uhh, yeah, I think that is it so far...
