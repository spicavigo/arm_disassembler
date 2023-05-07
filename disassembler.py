
"""
Author: Yousuf Fauzan

Program to test disassembling
"""
from converters.instruction import Instruction

assert Instruction('0xe1a01002').value == 'MOV R1, R2'
assert Instruction('0xe3a01203').value == 'MOV R1, #805306368'
assert Instruction('0xe1a01182').value == 'MOV R1, R2, LSL #3'
assert Instruction('0xe1a01352').value == 'MOV R1, R2, ASR R3'
assert Instruction('0xe2837005').value == 'ADD R7, R3, #5'
assert Instruction('0xe0468003').value == 'SUB R8, R6, R3'
assert Instruction('0xe0030594').value == 'MUL R3, R4, R5'
assert Instruction('0xe0214392').value == 'MLA R1, R2, R3, R4'
assert Instruction('0xe5921000').value == 'LDR R1, [R2]'
assert Instruction('0xe592100c').value == 'LDR R1, [R2, #12]'
assert Instruction('0xe5902004').value == 'LDR R2, [R0, #4]'
assert Instruction('0xe7821003').value == 'STR R1, [R2, R3]'
assert Instruction('0xe7821103').value == 'STR R1, [R2, R3, LSL #2]'
assert Instruction('0xe3a01e82').value == 'MOV R1, #2080'
assert Instruction('0xe3a01c01').value == 'MOV R1, #256'
