#!/usr/bin/env python3
import time
import pyrealsense2 as rs
from gpiozero import Motor, Servo, Button

# --- Pin setup ---
motor = Motor(forward=17, backward=27, pwm=True, enable=22)
servo = Servo(18)
button = Button(25, bounce_time=0.3)

# --- Global flag ---
started = False

# --- Movement settings ---
TURN_DIRECTION = "right"   # can be "left" or "right"
FORWARD_SPEED = 0.4        # motor power (0–1)
TURN_SPEED = 0.4
TURN_TIME = 1.0            # how long to keep the motor running during a turn
DISTANCE_LIMIT = 0.9       # 0.9 m ≈ 90 cm
LAPS = 4                   # number of laps

# --- RealSense setup ---
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
pipeline.start(config)

def reset_all():
    motor.stop()
    servo.mid()

def get_distance():
    """Get distance at the center of the frame"""
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    if not depth_frame:
        return None
    w, h = depth_frame.get_width(), depth_frame.get_height()
    return depth_frame.get_distance(w // 2, h // 2)

def go_forward_until_obstacle():
    """Drive forward until the distance <= DISTANCE_LIMIT"""
    motor.forward(FORWARD_SPEED)
    while True:
        dist = get_distance()
        if dist and dist < DISTANCE_LIMIT:
            break
    motor.stop()

def turn():
    """Turn left or right"""
    if TURN_DIRECTION == "right":
        servo.max()
    else:
        servo.min()
    motor.forward(TURN_SPEED)
    time.sleep(TURN_TIME)
    motor.stop()
    servo.mid()

def race():
    global started
    if started:
        print("Button pressed again — ignoring")
        return
    started = True

    print("  Race started!")
    for lap in range(1, LAPS + 1):
        print(f"  Lap {lap}/{LAPS}")
        go_forward_until_obstacle()
        turn()

    print("  Race finished!")
    reset_all()

def main():
    reset_all()
    print("System ready. Waiting for button press...")

    button.when_pressed = race

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping script")
        reset_all()
        pipeline.stop()

if __name__ == "__main__":
    main()
