"""
Author: Yousuf Fauzan

Convert Move Instruction from machine code. It uses Operand2 (operand2.py)
"""
from .operand2 import Operand2

class MoveInstruction(object):
    def __init__(self, instr):
        self.mapping = {
            13: 'MOV',
            15: 'MVN',
        }
        self.opcode = None
        self.rd = None
        self.operand2 = None
        self._convert(instr)

    def _convert(self, instr):
        # Drop Cond Code
        instr = instr[4:]
        # Optype
        is_imm = instr[:3] == '001'
        instr = instr[3:]
        # Opcode
        self.opcode = self.mapping[int(instr[:4], 2)]
        instr = instr[4:]
        # Drop S
        instr = instr[1:]
        # Dop Rn
        instr = instr[4:]
        # Rd
        self.rd = f'R{int(instr[:4], 2)}'
        instr = instr[4:]
        # Operand2
        self.operand2 = Operand2(instr, is_imm)

    @property
    def value(self):
        return f'{self.opcode} {self.rd}, {self.operand2.value}'