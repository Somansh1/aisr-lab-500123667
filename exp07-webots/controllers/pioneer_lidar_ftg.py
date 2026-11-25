# Modified Pioneer 3-DX Follow-the-Gap controller (Exp 7, Part B + Exercise 2)
import math
import numpy as np

def follow_the_gap(ranges, fov_angles, bubble_radius=0.35, min_gap_range=0.45):
    proc = np.array(ranges, dtype=float, copy=True)
    n = len(proc)
    closest_i = int(np.argmin(proc))
    closest_d = float(proc[closest_i])
    if closest_d < 1.8:
        half_ang = math.atan2(bubble_radius, max(0.1, closest_d))
        span = int(half_ang / ((fov_angles[-1] - fov_angles[0]) / (n - 1)))
        proc[max(0, closest_i - span):min(n, closest_i + span + 1)] = 0.0
    best_s, best_e, cur_s = 0, 0, None
    for i, val in enumerate(proc):
        if val > min_gap_range:
            if cur_s is None: cur_s = i
        elif cur_s is not None:
            if i - cur_s > best_e - best_s: best_s, best_e = cur_s, i
            cur_s = None
    if cur_s is not None and n - cur_s > best_e - best_s:
        best_s, best_e = cur_s, n
    if best_e > best_s:
        target_i = best_s + int(np.argmax(proc[best_s:best_e]))
        return float(fov_angles[target_i])
    return 0.9
