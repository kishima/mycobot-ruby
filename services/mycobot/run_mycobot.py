import time
from pymycobot.mycobot280 import MyCobot280

mc = MyCobot280('/dev/ttyUSB0',1000000)
time.sleep(0.5)
mc.set_fresh_mode(0)
time.sleep(0.5)

mc.send_angles([0, 0, 0, 0, 0, 50], 50)
time.sleep(1)

mc.set_gripper_value(0,50)
time.sleep(1)

mc.set_gripper_value(100,50)
