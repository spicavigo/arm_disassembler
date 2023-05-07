"""
Author: Yousuf Fauzan

Convert MUL and MLA Instruction from machine code.
"""
class MulInstruction(object):
    def __init__(self, instr):
        self.rd = None
        self.rm = None
        self.rs = None
        self._convert(instr)

    def _convert(self, instr):
        # Drop Cond Code
        instr = instr[4:]
        # Drop Optype
        instr = instr[3:]
        # Drop Opcode
        instr = instr[3:]
        # Drop A
        instr = instr[1:]
        # Drop S
        instr = instr[1:]
        # Rd
        self.rd = f'R{int(instr[:4], 2)}'
        instr = instr[4:]
        # Drop Rn
        instr = instr[4:]
        # Rs
        self.rs = f'R{int(instr[:4], 2)}'
        instr = instr[4:]
        # Drop Multicd
        instr = instr[4:]
        # Rm
        self.rm = f'R{int(instr[:4], 2)}'
        instr = instr[4:]

    @property
    def value(self):
        return f'MUL {self.rd}, {self.rm}, {self.rs}'
    

class MlaInstruction(object):
    def __init__(self, instr):
        self.rd = None
        self.rm = None
        self.rs = None
        self.rn = None
        self._convert(instr)

    def _convert(self, instr):
        # Drop Cond Code
        instr = instr[4:]
        # Drop Optype
        instr = instr[3:]
        # Drop Opcode
        instr = instr[3:]
        # Drop A
        instr = instr[1:]
        # Drop S
        instr = instr[1:]
        # Rd
        self.rd = f'R{int(instr[:4], 2)}'
        instr = instr[4:]
        # Rn
        self.rn = f'R{int(instr[:4], 2)}'
        instr = instr[4:]
        # Rs
        self.rs = f'R{int(instr[:4], 2)}'
        instr = instr[4:]
        # Drop Multicd
        instr = instr[4:]
        # Rm
        self.rm = f'R{int(instr[:4], 2)}'
        instr = instr[4:]

    @property
    def value(self):
        return f'MLA {self.rd}, {self.rm}, {self.rs}, {self.rn}'
    