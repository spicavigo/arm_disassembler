"""
Author: Yousuf Fauzan

Convert MUL and MLA Instruction from machine code.
"""
from converters.dp_instruction import DPInstruction
from converters.ls_instruction import LSInstruction
from converters.mov_instruction import MoveInstruction
from converters.multiply_instruction import MulInstruction, MlaInstruction

class Instruction(object):
	def __init__(self, instr):
		if instr.startswith('0x'):
			instr = format(int(instr, 16), '032b')
		optype = instr[4:7]
		opcode = instr[7:11]
		if optype == '010' or optype == '011':
			self.instr = LSInstruction(instr)
		elif optype == '000' and instr[24:28] == '1001' and opcode in ('0000', '0001'):
			if opcode == '0000':
				self.instr = MulInstruction(instr)
			else:
				self.instr = MlaInstruction(instr)
		elif opcode == '1101':
			self.instr = MoveInstruction(instr)
		else:
			self.instr = DPInstruction(instr)

		print(f'{hex(int(instr, 2))}: {self.instr.value}')


	@property
	def value(self):
		return self.instr.value
	

