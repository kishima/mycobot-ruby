FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    git \
    lsb-release \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install crc pyserial opencv-python

RUN git clone --branch v3.9.7 https://github.com/elephantrobotics/pymycobot.git && \
    sed -i "/from pymycobot.mycobotpro630 import Phoenix/d" pymycobot/pymycobot/__init__.py && \
    sed -i "/import linuxcnc/d" pymycobot/pymycobot/mycobotpro630.py && \
    sed -i "/from can import Message/d" pymycobot/pymycobot/mycobotpro630.py && \
    sed -i "/from pymycobot.mybuddyemoticon import MyBuddyEmoticon/d" pymycobot/pymycobot/__init__.py && \
    cd pymycobot && pip install .

CMD ["python3"]
