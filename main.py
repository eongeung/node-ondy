import sys
from PyQt5.QtWidgets import QApplication
from transparent_overlay import TransparentOverlay
from serial_reader import setup_serial_reader

if __name__ == '__main__':
    print("Ondy 시작")
    app = QApplication(sys.argv)
    overlay = TransparentOverlay()
    setup_serial_reader(overlay)
    sys.exit(app.exec_())
