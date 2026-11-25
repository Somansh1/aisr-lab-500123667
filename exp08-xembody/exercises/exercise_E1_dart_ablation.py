# Exercise E1: DART noise injection ablation summary
results_e1 = {
    "kuka_iiwa_with_dart": 0.92,
    "kuka_iiwa_no_dart": 0.68,
}
if __name__ == "__main__":
    for k, v in results_e1.items():
        print(f"{k}: {v*100:.1f}%")
