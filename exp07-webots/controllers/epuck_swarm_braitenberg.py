# Modified e-puck Braitenberg reactive obstacle avoidance controller (Exp 7, Part A + Exercise 1)
import numpy as np

W_LEFT = np.array([-0.8, -0.5, -0.2, 0.0, 0.0, 0.2, 0.5, 0.8])
W_RIGHT = np.array([0.8, 0.5, 0.2, 0.0, 0.0, -0.2, -0.5, -0.8])

def compute_wheel_speeds(ir_norm, cruise=0.5, gain_asym=1.0, max_speed=6.28):
    vl = np.clip(cruise + np.dot(W_LEFT * gain_asym, ir_norm), -1.0, 1.0) * max_speed
    vr = np.clip(cruise + np.dot(W_RIGHT, ir_norm), -1.0, 1.0) * max_speed
    return float(vl), float(vr)
