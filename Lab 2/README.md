#  Artificial Intelligence Lab 2

## Included files

- `Lab2_Report.docx` - written answers for Tasks 1-3, assumptions, trace analysis, limitations, reflection, and responsible-practice notes.
- `lab2_percepts.py` - original reflex-agent baseline matching the lab manual.
- `lab2_model.py` - stateful classroom agent; `act()` returns `(target_mode, should_send_command)`.
- `lab2_check.py` - automated tests for thresholds, occupancy priority, repeated commands, transitions, input validation, and noisy-threshold behavior.
- `lab2_percepts_output.txt` - captured output from the reflex baseline.
- `lab2_stateful_output.txt` - captured required stateful trace and threshold-noise edge case.
- `lab2_test_output.txt` - captured test-run output.
- `lab2_trace.csv` - required trace in CSV format.
- `threshold_noise_trace.csv` - edge-case trace around 26 C.

## Requirements

- Python 3.9 or newer
- No third-party Python packages are required.

## Run the files

Open a terminal in this folder and run:

```bash
python lab2_percepts.py
python lab2_model.py
python lab2_check.py
```



