import sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from assembler import assemble, AssemblerError
class AssemblerTests(unittest.TestCase):
 def assemble_text(self,text,k=0):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'test.asm'; p.write_text(text)
   return assemble(p,k,Path(d)/'symbols.txt')
 def test_add_output(self):
  words,_,_=self.assemble_text('@2\nD=A\n@3\nD=D+A\n@0\nM=D\n')
  self.assertEqual(words,['0000000000000010','1110110000010000','0000000000000011','1110000010010000','0000000000000000','1110001100001000'])
 def test_labels_and_variables(self):
  words,_,symbols=self.assemble_text('(LOOP)\n@value\nM=1\n@LOOP\n0;JMP\n')
  self.assertEqual(symbols['LOOP'],0); self.assertEqual(symbols['value'],16)
 def test_duplicate_label_warning_for_k2(self):
  _,warnings,_=self.assemble_text('(X)\n@0\n(X)\n@1\n',2)
  self.assertTrue(any('duplicate label' in w for w in warnings))
 def test_line_number_error_for_k1(self):
  with self.assertRaisesRegex(AssemblerError,'Line 2'):
   self.assemble_text('@0\nD=BAD\n',1)
if __name__=='__main__': unittest.main()
