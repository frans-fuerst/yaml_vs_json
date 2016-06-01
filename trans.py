#!/usr/bin/env python2

import sys
import os
import json
import yaml

from PyQt4 import QtGui, QtCore, Qt, uic

class trans(QtGui.QMainWindow):

    def __init__(self):

        QtGui.QMainWindow.__init__(self)

        self.setMouseTracking(True)
        self._directory = os.path.dirname(os.path.realpath(__file__))
        uic.loadUi(os.path.join(self._directory, 'trans.ui'), self)

        self.txt_yaml.textChanged.connect(self.on_txt_yaml_textChanged)
        self.txt_json.textChanged.connect(self.on_txt_json_textChanged)

        self.show()

    def on_txt_yaml_textChanged(self):
        x = self.txt_json.blockSignals(True)
        _text = str(self.txt_yaml.toPlainText())
        try:
            _text = json.dumps(yaml.load(_text))
        except:
            _text = 'could not parse yaml'
        self.txt_json.setPlainText(_text)
        self.txt_json.blockSignals(x)

    def on_txt_json_textChanged(self):
        x = self.txt_yaml.blockSignals(True)
        _text = str(self.txt_json.toPlainText())
        try:
            _text = yaml.dump(json.loads(_text))
        except:
            _text = 'could not parse json'
        self.txt_yaml.setPlainText(_text)
        self.txt_yaml.blockSignals(x)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = trans()

#    for s in (signal.SIGABRT, signal.SIGINT, signal.SIGSEGV, signal.SIGTERM):
#        signal.signal(s, lambda signal, frame: sigint_handler(signal, ex))

    # catch the interpreter every now and then to be able to catch signals
    timer = QtCore.QTimer()
    timer.start(200)
    timer.timeout.connect(lambda: None)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
