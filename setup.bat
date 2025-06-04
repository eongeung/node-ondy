@echo off
echo [가상환경 생성: ondy-env]
python -m venv ondy-env

echo [가상환경 활성화]
call ondy-env\Scripts\activate

echo [필요 패키지 설치]
pip install --upgrade pip
pip install pyqt5 pyserial
pip install pyserial

pip install opencv-python

echo [설치 완료. ondy_env 활성화된 상태입니다.]
pause
