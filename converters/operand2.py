"""
Author: Yousuf Fauzan

Convert Operand2 from machine code.
"""
class ShiftOp(object):
    def __init__(self, instr):
        self.shift_type = None
        self.immediate_format = None
        self.rs = None
        self._convert(instr)

    def _convert(self, instr):
        if instr[-1] == '0':
            # Immediate format
            self.immediate_format = ImmediateFormat(instr[:5])
        else:
            self.rs = f'R{int(instr[:4], 2)}'

        self.shift_type = ['LSL', 'LSR', 'ASR', 'ROR', 'RRX'][int(instr[5:7], 2)]

    @property
    def value(self):
        if self.immediate_format and self.immediate_format.number:
            return f'{self.shift_type} {self.immediate_format.value}'
        if self.rs is not None:
            return f'{self.shift_type} {self.rs}'
        return ''


class ImmediateFormat(object):
    def __init__(self, instr):
        self.rotamt = 0
        self.number = 0
        if len(instr) == 5:
            self._convert_shiftamt(instr)
        else:
            self._convert(instr)

    def _convert(self, instr):
        # RotAmt
        self.rotamt = int(instr[:4], 2)
        instr = instr[4:]
        self.number = int(instr, 2)
        if self.rotamt:
            self.number = self.rotate_right(self.number, self.rotamt*2)
            self.rotamt = 0

    def _convert_shiftamt(self, instr):
        self.number = int(instr, 2)

    def rotate_left(self, x, n):
        return int(f"{x:032b}"[n:] + f"{x:032b}"[:n], 2)

    def rotate_right(self, x, n):
        return int(f"{x:032b}"[-n:] + f"{x:032b}"[:-n], 2)

    def rotate(self, n):
        rot = 0
        for rot in range(2, 32, 2):
            if self.rotate_left(n, rot) < 255:
                return self.rotate_left(n, rot), rot
        raise Exception("Unable to encode number %d", n)

    @property
    def value(self):
        return f'#{self.number}'

class RegisterFormat(object):
    def __init__(self, instr):
        self.shiftop = None
        self.rm = 0
        self._convert(instr)

    def _convert(self, instr):
        self.shiftop = ShiftOp(instr[:8])
        self.rm = f'R{int(instr[8:], 2)}' 

    @property
    def value(self):
        if self.shiftop.value:
            return f'{self.rm}, {self.shiftop.value}'
        return f'{self.rm}'

class Operand2(object):
    def __init__(self, instr, is_imm=False, is_scaled=False):
        self.immediate_format = None
        self.register_format = None
        if not is_scaled:
            self._convert(instr, is_imm)
        else:
            self._convert_scaled_register(instr)

    def _convert(self, instr, is_imm):
        if is_imm:
            self.immediate_format = ImmediateFormat(instr)
        else:
            self.register_format = RegisterFormat(instr)

    def _convert_scaled_register(self, instr):
        self.register_format = RegisterFormat(instr)

    @property
    def value(self):
        if self.immediate_format:
            return self.immediate_format.value
        return self.register_format.value
