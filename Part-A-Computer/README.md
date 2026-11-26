# Part A — Build the Hack Computer

This folder contains the three top-level HDL chips required by the assignment:

- `CPU.hdl` — registers, ALU control, memory write and jump control.
- `Memory.hdl` — RAM, screen and keyboard memory map.
- `Computer.hdl` — joins ROM32K, CPU and Memory.

## Important
HDL is required here: the official Nand2Tetris Hardware Simulator reads `.hdl` files. The Python programs in Parts B and C do not replace the hardware description.

## Run the official tests
1. Install/download the official Nand2Tetris Software Suite.
2. Open **HardwareSimulator**.
3. Set the working directory to this folder.
4. Load each official test script: `CPU.tst`, `Memory.tst`, and `ComputerAdd.tst`, `ComputerMax.tst`, `ComputerRect.tst`.
5. Press **Run**. Save a screenshot showing the test name and `End of script` / passed status.
6. If a test fails, read the first failing comparison. Check chip pin names, bus slices and the selected built-in chips.

The official test `.tst` files and test `.cmp` files are distributed with the Nand2Tetris course/software suite; put your copies in `tests/`. They are not fabricated here.

## Built-in chips
This implementation uses standard built-in chips such as `ALU`, `ARegister`, `DRegister`, `PC`, `RAM16K`, `Screen`, `Keyboard`, `ROM32K`, and mux/demux chips. In your report, identify any lab chip you replaced with a built-in chip, as required by the assignment.
