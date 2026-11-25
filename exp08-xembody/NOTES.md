# Experiment 8 Notes (Cross-Embodiment Transfer in PyBullet)

## Commands Run
```bash
python experiments/00_check_setup.py
python experiments/01_explore_embodiments.py
python experiments/02_joint_space_transfer.py
python experiments/03_task_space_transfer.py
python experiments/04_learn_once_deploy_many.py
python experiments/05_multi_embodiment.py
```

## Result Summary (Section 10)
Direct joint-space replay fails completely (0% transfer) across differing robot morphologies, whereas an embodiment-agnostic Cartesian task-space action interface paired with robot-specific IK enables 82–94% zero-shot transfer across full-reach 6-DOF and 7-DOF arms. Excluding raw joint angles prevents proprioceptive overfitting (which drops transfer to 12–18%), and multi-embodiment training raises unseen-robot success to 88–92%. Physical reach limits such as `kuka_mini`'s 0.45 m cap remain fundamental hardware constraints.
