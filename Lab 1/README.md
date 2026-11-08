# AI Lab 1 — Complete Solution Package

This folder contains the editable Word report, PDF fallback, plain-text report backup, source code, and captured outputs for Lab 1.

## Start here
1. Open `Lab1_Report.docx` in Microsoft Word or Google Docs. Replace `[Enter your full name]` and `[Enter your registration number]` on the cover page.
2. Personalize the reflection in Section 7 using your own words and what you actually observed.
3. Read the PDF (`Lab1_Report.pdf`) if Word cannot open or download the DOCX. `Lab1_Report_Backup.txt` is an additional plain-text backup.
4. Run both Python programs using the commands below.

## Files
- `Lab1_Report.docx` — editable 9-page report.
- `Lab1_Report.pdf` — same report in PDF format.
- `Lab1_Report_Backup.txt` — text copy of report content and tables.
- `lab1_rules.py` — Task 2 extended rule-based checker with exactly four core test cases.
- `lab1_compare.py` — rule-vs-probability-threshold comparison using the manual's four demonstration cases.
- `outputs/lab1_rules_output.txt` — captured output for Task 2.
- `outputs/lab1_compare_output.txt` — captured output for the comparison.
- `sources.md` — sources cited in the report.
- `START_HERE.txt` — short submission and setup notes.

## Run the code
Requires Python 3.9+; no third-party packages are needed.

```bash
python lab1_rules.py
python lab1_compare.py
```

In Google Colab, upload/extract the ZIP, open the `Lab1_Solution` folder and run:

```python
!python lab1_rules.py
!python lab1_compare.py
```

## Important academic and evidence notes
- All thresholds and scholarship cases are synthetic lab assumptions, not an actual scholarship policy.
- `Review` is only a flag for human review; it is not an award decision.
- The probability values in `lab1_compare.py` are invented inputs. No machine-learning model is trained or evaluated.
- The four Task 2 core tests are: one pass, failure of the first added condition, failure of the second added condition, and the score boundary at 70.
- Run the scripts yourself in the environment you will demonstrate and take your own screenshots if the instructor requests them.
- The PDF filename includes `CS4944`, but the course code printed inside the supplied manual is `CAI601400`. Confirm the official code with your instructor before submission.
- The supplied manual asks for a GitHub repository URL and final commit ID. Those account-specific submission actions are not performed by these files.

## Before submission
Replace the two student-detail placeholders, personalize the reflection, check the course code, run the scripts, and submit the repository URL/commit identifier through the course channel as instructed by your teacher.
