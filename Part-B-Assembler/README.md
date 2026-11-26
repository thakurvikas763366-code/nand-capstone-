# Part B — Python Hack Assembler

`assembler.py` translates Hack assembly instructions into 16-bit machine code.

## Run it (Windows PowerShell)
From the project root:

```powershell
cd Part-B-Assembler
python assembler.py programs/Add.asm
python assembler.py programs/Max.asm
python assembler.py programs/Rect.asm
python assembler.py programs/Pong.asm
```

Each command creates a matching `.hack` file and updates `symbols.txt`.

## Personal K
Edit `config.json` and replace `0` with the last two digits of your roll number. You can also pass `--k 41` to the assembler. The selected extra feature is `K mod 3`:

- `0`: always writes labels and variables with their RAM/ROM addresses to `symbols.txt`.
- `1`: reports invalid instructions with their source line number instead of an unhandled crash.
- `2`: prints a warning when a label is defined more than once.

The symbol table is saved for every K, which is useful for debugging and viva.

## Two-pass method
1. Pass 1 removes comments/blank lines and records label addresses (labels do not consume ROM addresses).
2. Pass 2 converts A-instructions and C-instructions to 16-bit binary. New variables begin at RAM address 16.

## Compare with the official assembler
Open the Nand2Tetris **Assembler** tool, assemble the same `.asm` file, and compare the resulting `.hack` text line by line. Use the official `Add.asm`, `Max.asm`, `Rect.asm` and `Pong.asm` supplied with your course if available; the small programs in this folder are learning/test examples.
