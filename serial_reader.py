import serial
from PyQt5.QtCore import QTimer
print("serial 모듈 위치:", serial.__file__)

def setup_serial_reader(overlay):
    try:
        ser = serial.Serial('COM3', 9600, timeout=1)  # COM 포트는 환경에 따라 변경
    except serial.SerialException:
        print("시리얼 포트 열기 실패")
        return

    def check_serial():
        if ser.in_waiting > 0:
            line = ser.readline().decode().strip()
            if line == "BAD":
                if not overlay.is_bad_state:
                    overlay.is_bad_state = True
                    overlay.bad_timer.start()
            elif line == "GOOD":
                overlay.clear_ondys()
                overlay.bad_timer.stop()
                overlay.is_bad_state = False

    timer = QTimer()
    timer.timeout.connect(check_serial)
    timer.start(200)

    return timer
