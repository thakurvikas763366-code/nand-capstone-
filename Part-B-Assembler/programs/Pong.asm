// Small valid assembler smoke-test program (not the full Pong game).
@KBD
D=M
@PRESSED
D;JGT
@0
D=A
@SCREEN
M=D
@LOOP
0;JMP
(PRESSED)
@SCREEN
M=-1
(LOOP)
@LOOP
0;JMP
