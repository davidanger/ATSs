import visa
import Driver
import serial
import time
import pandas as pd

DM0 = Driver.K34461A()
DM0._ser = visa.ResourceManager().open_resource('USB0::0x2A8D::0x1301::MY53227907::0::INSTR')

DM1 = Driver.K34461A()
DM1._ser = visa.ResourceManager().open_resource('USB0::0x2A8D::0x1301::MY53227890::0::INSTR')

PS2 = Driver.IT6861A()
PS2._ser = visa.ResourceManager().open_resource('USB0::0xFFFF::0x6800::600012010727330035::0::INSTR')

LD1 = Driver.C6312A()
LD1._ser = visa.ResourceManager().open_resource('ASRL5::INSTR')

U2I = serial.Serial('COM16', 19200, timeout=1)

file = open('test57_custom.txt', 'w')

DM0.begin()
DM1.begin()
PS2.begin()
LD1.begin()

# rd00 \h(54 ea 01 00 54 eb 02)
# passwd \h(54 ea 02 2f 56)
# rd26 \h(54 ea 01 26 54 eb 01)
# st00 \h(54 ea 02 26 96)
# st01 \h(54 ea 02 26 b6)
# st10 \h(54 ea 02 26 d6)
# st11 \h(54 ea 02 26 f6)
# wta1 \h(54 ea 02 a1 a8)
# wta2 \h(54 ea 02 a2 fd)


def pb57_r00():
    U2I.write(bytes([0x54, 0xea, 0x01, 0x00, 0x54, 0xeb, 0x01]))
    return hex(int.from_bytes(U2I.readline(), 'big'))


def pb57_r26():
    U2I.write(bytes([0x54, 0xea, 0x01, 0x26, 0x54, 0xeb, 0x01]))
    return hex(int.from_bytes(U2I.readline(), 'big'))


def pb57_pw():
    U2I.write(bytes([0x54, 0xea, 0x02, 0x2f, 0x56]))
    return hex(int.from_bytes(U2I.readline(), 'big'))


def pb57_s00():
    U2I.write(bytes([0x54, 0xea, 0x02, 0x26, 0x69]))
    return hex(int.from_bytes(U2I.readline(), 'big'))


def pb57_s01():
    U2I.write(bytes([0x54, 0xea, 0x02, 0x26, 0xb6]))
    return hex(int.from_bytes(U2I.readline(), 'big'))


def pb57_s10():
    U2I.write(bytes([0x54, 0xea, 0x02, 0x26, 0xd6]))
    return hex(int.from_bytes(U2I.readline(), 'big'))


def pb57_s11():
    U2I.write(bytes([0x54, 0xea, 0x02, 0x26, 0xf9]))
    return hex(int.from_bytes(U2I.readline(), 'big'))


def pb57_sa1():
    U2I.write(bytes([0x54, 0xea, 0x02, 0xa1, 0xa8]))
    return hex(int.from_bytes(U2I.readline(), 'big'))


def pb57_sa2():
    U2I.write(bytes([0x54, 0xea, 0x02, 0xa2, 0xfd]))
    return hex(int.from_bytes(U2I.readline(), 'big'))


def test_loop():
    PS2.set_vi(5.4, 0.7)
    time.sleep(0.1)
    pb57_pw()
    pb57_sa1()
    pb57_sa2()
    pb57_s00()
    LD1.set_cc(0, 0.5)
    time.sleep(0.2)
    vset = DM0.measure_v_dc()
    rset = DM1.measure_v_dc()
    ccbst = vset/rset * 2.7
    file.write('VSET:'+str(vset)+' RSET:'+str(rset)+' CCBST:'+str(ccbst)+'\n')

    LD1.load_off()
    PS2.stop()


for i in range(0, 4):
    test_loop()
    time.sleep(20)

file.close()

LD1.close()
PS2.close()
DM0.close()
DM1.close()

U2I.close()