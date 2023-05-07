"""
Author: Yousuf Fauzan

Convert Load and Store Instruction from machine code. It uses Operand2 (operand2.py)
"""
from .operand2 import Operand2

class LSInstruction(object):
    def __init__(self, instr):
        self.opcode = None
        self.rt = None
        self.rn = None
        self.operand2 = None
        self.immediate = None
        self._convert(instr)

    def _convert(self, instr):
        # Drop Cond Code
        instr = instr[4:]

        # Optype
        self.is_imm = instr[:3] == '010'
        instr = instr[3:]

        is_neg = instr[:3] == '1000'
        instr = instr[4:]

        self.opcode = 'LDR' if instr[0] == '1' else 'STR'
        instr = instr[1:]

        self.rn = f'R{int(instr[:4], 2)}'
        instr = instr[4:]

        self.rt = f'R{int(instr[:4], 2)}'
        instr = instr[4:]

        if self.is_imm:
            self.immediate = f'#{int(instr, 2)}'
        else:
            self.operand2 = Operand2(instr, is_scaled=True)

    @property
    def value(self):
        if self.is_imm:
            if self.immediate == '#0':
                return f'{self.opcode} {self.rt}, [{self.rn}]'
            return f'{self.opcode} {self.rt}, [{self.rn}, {self.immediate}]'
        return f'{self.opcode} {self.rt}, [{self.rn}, {self.operand2.value}]'
        

    
