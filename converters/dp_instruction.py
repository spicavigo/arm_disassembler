"""
Author: Yousuf Fauzan

Convert Data Processing Instruction from machine code. It uses Operand2 (operand2.py)
"""

from .operand2 import Operand2

class DPInstruction(object):
    def __init__(self, instr):
        self.mapping = {
            'AND': 0,
            'ADD': 4,
            'SUB': 2,
            'EOR': 1,
            'ORR': 12
        }
        self.mapping = {v: k for k, v in self.mapping.items()}
        self.opcode = None
        self.rd = None
        self.rn = None
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
        # Rn
        self.rn = f'R{int(instr[:4], 2)}'
        instr = instr[4:]
        # Rd
        self.rd = f'R{int(instr[:4], 2)}'
        instr = instr[4:]
        # Operand2
        self.operand2 = Operand2(instr, is_imm)

    @property
    def value(self):
        return f'{self.opcode} {self.rd}, {self.rn}, {self.operand2.value}'
    