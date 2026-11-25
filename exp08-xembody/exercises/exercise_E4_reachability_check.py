# Exercise E4: Pre-deployment workspace capability-gap detector
import numpy as np

def check_capability_gap(max_reach_m, task_x=(0.35, 0.65), task_y=(-0.25, 0.25), threshold=0.80):
    xs = np.linspace(task_x[0], task_x[1], 25)
    ys = np.linspace(task_y[0], task_y[1], 25)
    gx, gy = np.meshgrid(xs, ys)
    cov = float(np.mean(np.hypot(gx, gy) <= max_reach_m))
    return cov, cov < threshold

if __name__ == "__main__":
    for name, r in [("kuka_iiwa", 0.82), ("franka_panda", 0.855), ("xarm6", 0.70), ("kuka_mini", 0.45)]:
        cov, gap = check_capability_gap(r)
        print(f"{name:14s}: coverage={cov*100:5.1f}%  capability_gap={gap}")
