# Hack Computer Capstone — Nand2Tetris

A beginner-friendly implementation split into the three assignment parts. Python is used for the assembler, personalised assembly generator, test scripts and optional demonstration emulator. The hardware chips in Part A remain HDL because that is the language accepted by the official Hardware Simulator.

## Before you start
1. Install Python 3.10 or newer. Check with `python --version` in PowerShell.
2. Download the official Nand2Tetris Software Suite and extract it somewhere easy to find.
3. Find the last two digits of your roll number. This is your personal `K`.
4. Open `Part-B-Assembler/config.json` and replace `"K": 0` with your K.

## Run the project
Open PowerShell in this folder (`Hack-Computer-Capstone`) and follow these steps:

### Part A — Hardware
Open the official HardwareSimulator, open each chip in `Part-A-Computer`, and run the course-provided test scripts. Save the five screenshots in `Part-A-Computer/tests/` or `Documentation/`.

### Part B — Assembler
```powershell
cd Part-B-Assembler
python -m unittest discover -s tests -v
python assembler.py programs/Add.asm
python assembler.py programs/Max.asm
python assembler.py programs/Rect.asm
python assembler.py programs/Pong.asm
```
The `.hack` files are created next to their `.asm` files. `symbols.txt` is created/updated in this folder.

### Part C — Personal box
```powershell
cd ..\Part-C-Box-Program
python generate_box.py
cd ..\Part-B-Assembler
python assembler.py ..\Part-C-Box-Program\Box.asm -o ..\Part-C-Box-Program\Box.hack
cd ..\Part-C-Box-Program
python emulator.py Box.hack
```
Click the emulator window, hold any key to show the box, and release it to erase the box. Save a screenshot while the box is visible to `Part-C-Box-Program/screenshots/`.

## What to submit
- Push the entire `Hack-Computer-Capstone/` folder into your existing lab GitHub repository.
- Complete `Documentation/REPORT_TEMPLATE.md` and add your real test screenshots.
- Read `Documentation/VIVA_QUESTIONS.md` and practise changing K / moving the box.

## Important accuracy notes
- The assignment's five official `.tst` test scripts and reference `.cmp` outputs are not reproduced here. Use the official course files from your Nand2Tetris download and save genuine screenshots of their results.
- The sample `Pong.asm` in this folder is a small assembler smoke test, not the full Pong game. For the required official comparison, use the official `Pong.asm` from the course distribution.
- The included Python emulator is a small teaching/demo emulator for the box program. Part A's official HDL verification and Part C's required CPU Emulator screenshot should still be done in the official Nand2Tetris tools when available.
- Set your real K before generating `Box.asm`; K=0 is only a safe starter placeholder, not your personalised submission.
# SUBMITTED BY :
Vikash Singh
2501730395
BTECH CSE AI&ML [Sec-F]
