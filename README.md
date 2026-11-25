# CSAI4014 AISR Laboratory Repository (`aisr-lab-500123667`)

- **Student Name:** Somansh Goel
- **SAP ID:** 500123667
- **Roll No.:** R2142230744
- **Batch / Cohort:** A (B.Tech CSE AI & ML B1)
- **Partner(s):** None (Solo)
- **Course Teacher:** Dr. Resham Raj Shivwanshi
- **Semester:** VII (Autumn Semester 2026–27), School of Computer Science, UPES Dehradun
- **Environment:** Windows 11 (64-bit), Intel Core i7, Python 3.11.2, NumPy 2.1.3, SciPy 1.15.2, Matplotlib 3.10.1

## Repository Layout

```text
aisr-lab-500123667/
  README.md
  exp01-signals/        exp01.ipynb   figs/
  exp02-queens/         exp02.ipynb   figs/
  exp03-search/         exp03.ipynb   figs/
  exp04-hillclimb/      exp04.ipynb   figs/
  exp05-rl/             exp05.ipynb   figs/
  exp06-neural/         exp06.ipynb   figs/
  exp07-webots/         controllers/  runs/*.csv   figs/   NOTES.md
  exp08-xembody/        results/*.csv figs/        exercises/ NOTES.md
```

## Setup & Execution

```bash
python3 -m venv ~/aisr-venv
source ~/aisr-venv/bin/activate   # Windows: ~\aisr-venv\Scripts\activate
pip install numpy scipy matplotlib jupyterlab
```

Every notebook (`exp01.ipynb`–`exp06.ipynb`) runs cleanly top to bottom on a fresh kernel and saves its figures into its local `figs/` directory.

## References & AI Assistants Used

1. A. V. Oppenheim and R. W. Schafer, *Discrete-Time Signal Processing*, 3rd ed., Pearson, 2010 (Exp. 1).
2. K. J. Åström and R. M. Murray, *Feedback Systems*, Princeton Univ. Press, 2008 (Exp. 1).
3. S. Russell and P. Norvig, *Artificial Intelligence: A Modern Approach*, 4th ed., Pearson, 2020 (Exp. 2–4).
4. R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed., MIT Press, 2018 (Exp. 5).
5. I. Goodfellow, Y. Bengio, and A. Courville, *Deep Learning*, MIT Press, 2016 (Exp. 6).
6. O. Michel, "Webots: Professional mobile robot simulation," *Int. J. Adv. Robotic Systems*, 2004; V. Braitenberg, *Vehicles*, MIT Press, 1984 (Exp. 7).
7. Open X-Embodiment Collaboration, ICRA 2024; E. Coumans and Y. Bai, PyBullet, 2016–2024 (Exp. 8).
8. **AI Assistant Disclosure:** Google Gemini was used to assist with LaTeX formatting, Matplotlib plotting templates, and verifying derivations. All code and results have been reviewed and are understood for viva defence.
