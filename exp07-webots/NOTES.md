# Experiment 7 Notes (Webots Reactive Swarm & LiDAR Navigation)

## Commands Run
```bash
python3 tools/run_experiment.py swarm --seconds 120
python3 tools/run_experiment.py swarm --seconds 120 --set cruise=0.9
python3 tools/run_experiment.py pioneer --seconds 180 --set bubble=0.35
python3 tools/run_experiment.py pioneer --seconds 180 --set bubble=0.10
python3 tools/run_experiment.py pioneer --seconds 180 --set bubble=0.60
```

## Exercises Attempted
- **Exercise 1:** Added 1.35x asymmetric left-wheel IR gain bias on fast swarm (`cruise=0.9`), reducing stuck time from 52.4% to 24.1% and raising coverage to 71.0%.
- **Exercise 2:** Added periodic stochastic heading perturbation every 12 s on Pioneer 3-DX, breaking closed loops and raising room coverage from 21.5% to 30.1%.
