import time

# Digital Multimeter


class K34461A:
    _ser = None

    def begin(self):
        self._ser.open()
        time.sleep(0.2)
        self._ser.write('SYSTem:VERSion?')
        __ver = self._ser.read()
        time.sleep(0.1)
        self._ser.write('SYSTem:BEEPer')
        print(f'34461A Ver:{__ver}Is Ready\n')

    def close(self):
        time.sleep(0.1)
        self._ser.write('SYSTem:LOCal')
        time.sleep(0.1)
        self._ser.close()
        print('34461A Closed\n')

    def measure_v_dc(self):
        self._ser.write('MEASure:VOLTage:DC?')
        __value = float(self._ser.read()[:-1])
        print(f'34461A DC Voltage:{__value}V\n')
        return __value

    def measure_i_dc(self):
        self._ser.write('MEASure:CURRent:DC?')
        __value = float(self._ser.read()[:-1])
        print(f'34461A DC Current:{__value}V\n')
        return __value

    def measure_i_dc_range(self, range):
        self._ser.write(f'MEASure:CURRent:DC? {range}')
        __value = float(self._ser.read()[:-1])
        print(f'DC Current:{__value}V\n')
        return __value


class K34401A:
    _ser = None

    def begin(self):
        self._ser.open()
        time.sleep(0.2)
        self._ser.write('SYSTem:VERSion?')
        __ver = self._ser.read()
        time.sleep(0.1)
        self._ser.write('SYSTem:REMote')
        time.sleep(0.1)
        self._ser.write('SYSTem:BEEPer')
        print(f'34401A Ver:{__ver}Is Ready\n')

    def close(self):
        time.sleep(0.1)
        self._ser.write('SYSTem:LOCal')
        time.sleep(0.1)
        self._ser.close()
        print('34401A Closed\n')

    def measure_v_dc(self):
        self._ser.write('MEASure:VOLTage:DC?')
        __value = float(self._ser.read()[:-1])
        print(f'DC Voltage:{__value}V\n')
        return __value

    def measure_i_dc(self):
        self._ser.write('MEASure:CURRent:DC?')
        __value = float(self._ser.read()[:-1])
        print(f'DC Current:{__value}V\n')
        return __value

    def measure_i_dc_range(self, range):
        self._ser.write(f'MEASure:CURRent:DC? {range}')
        __value = float(self._ser.read()[:-1])
        print(f'DC Current:{__value}V\n')
        return __value

# Power Supply


class E3631A:
    _ser = None

    def begin(self):
        self._ser.open()
        time.sleep(0.2)
        self._ser.write('SYSTem:VERSion?')
        __ver = self._ser.read()
        time.sleep(0.1)
        self._ser.write('SYSTem:REMote')
        time.sleep(0.1)
        self._ser.write('SYSTem:BEEPer')
        print(f'E3631A Ver:{__ver}Is Ready\n')

    def close(self):
        self.stop()
        time.sleep(0.1)
        self._ser.write('SYSTem:LOCal')
        time.sleep(0.1)
        self._ser.close()
        print('E3631A Closed\n')

    def set_vi(self, output, voltage, current):
        self._ser.write(f'APPLy {output}, {voltage:.3f}, {current:.3f}')
        time.sleep(0.1)
        print(f'E3631A {output}: {voltage:.3f}V {current:.3f}A\n')

    def stop(self):
        self._ser.write('OUTPut 0')
        time.sleep(0.1)
        print('E3631A Stop Output\n')


class DP832A:
    _ser = None

    def begin(self):
        self._ser.open()
        time.sleep(0.2)
        self._ser.write('SYSTem:VERSion?')
        __ver = self._ser.read()
        time.sleep(0.1)
        self._ser.write('SYSTem:REMote')
        time.sleep(0.1)
        # self._ser.write('SYSTem:BEEPer')
        print(f'DP832A Ver:{__ver}Is Ready\n')

    def close(self):
        self.stop()
        time.sleep(0.1)
        self._ser.write('SYSTem:LOCal')
        time.sleep(0.1)
        self._ser.close()
        print('DP832A Closed\n')

    def set_vi(self, output, voltage, current):
        """
        Apply the voltage and current.
        ouput: CH1|CH2|CH3
        CH1&CH2 30V/3A
        CH3 8V/5A
        """
        self._ser.write(f'APPLy {output}, {voltage:.3f}, {current:.3f}')
        self._ser.write(f'OUTP {output}, ON')
        time.sleep(0.1)
        print(f'DP832A {output}: {voltage:.3f}V {current:.3f}A\n')

    def measure_v(self, output):
        """
        Measure Output Voltage
        ouput: CH1|CH2|CH3
        """
        self._ser.write(f'MEAS? {output}')
        __value = float(self._ser.read()[:-1])
        print(f'DP832A {output} OUT Voltage: {__value}V')
        return __value

    def measure_i(self, output):
        """
        Measure Output Current
        ouput: CH1|CH2|CH3
        """
        self._ser.write(f'MEAS:CURR? {output}')
        __value = float(self._ser.read()[:-1])
        print(f'DP832A {output} OUT Current: {__value}A')
        return __value

    def measure_p(self, output):
        """
        Measure Output Power
        ouput: CH1|CH2|CH3
        """
        self._ser.write(f'MEAS:POWE? {output}')
        __value = float(self._ser.read()[:-1])
        print(f'DP832A {output} OUT Power: {__value}W')
        return __value

    def stop(self):
        self._ser.write('OUTPut ALL, OFF')
        time.sleep(0.1)
        print('DP832A Stop Output\n')


class DP811A:
    _ser = None

    def begin(self):
        self._ser.open()
        time.sleep(0.2)
        self._ser.write('SYSTem:VERSion?')
        __ver = self._ser.read()
        time.sleep(0.1)
        self._ser.write('SYSTem:REMote')
        time.sleep(0.1)
        # self._ser.write('SYSTem:BEEPer')
        print(f'DP811A Ver:{__ver}Is Ready\n')

    def close(self):
        self.stop()
        time.sleep(0.1)
        self._ser.write('SYSTem:LOCal')
        time.sleep(0.1)
        self._ser.close()
        print('DP811A Closed\n')

    def set_range(self, _range):
        """
        Set Output Range
        _range: P20V|P40V|LOW|HIGH
        P20V|LOW 20V/10A
        P40V|HIGH 40V/5A
        """
        self._ser.write(f'OUTP:RANG {_range}')
        print(f'DP811A Output Range is {_range}')

    def set_vi(self, voltage, current):
        """
        Apply the voltage and current.
        Range P20V|LOW: 20V/10A
        Range P40V|HIGH: 40V/5A
        """
        self._ser.write(f'APPLy {voltage:.3f}, {current:.3f}')
        self._ser.write(f'OUTP ON')
        time.sleep(0.1)
        print(f'DP811A: {voltage:.3f}V {current:.3f}A\n')

    def measure_v(self):
        """
        Measure Output Voltage
        """
        self._ser.write(f'MEAS?')
        __value = float(self._ser.read()[:-1])
        print(f'DP811A OUT Voltage: {__value}V')
        return __value

    def measure_i(self):
        """
        Measure Output Current
        """
        self._ser.write(f'MEAS:CURR?')
        __value = float(self._ser.read()[:-1])
        print(f'DP832A OUT Current: {__value}A')
        return __value

    def measure_p(self, output):
        """
        Measure Output Power
        """
        self._ser.write(f'MEAS:POWE?')
        __value = float(self._ser.read()[:-1])
        print(f'DP832A OUT Power: {__value}W')
        return __value

    def stop(self):
        self._ser.write('OUTPut OFF')
        time.sleep(0.1)
        print('DP811A Stop Output\n')


class IT6861A:
    _ser = None

    def begin(self):
        """
        Set to remote control mode.
        """
        self._ser.open()
        time.sleep(0.2)
        self._ser.write('SYSTem:VERSion?')
        __ver = self._ser.read()
        time.sleep(0.1)
        self._ser.write('SYSTem:REMote')
        time.sleep(0.2)
        self._ser.write('SYSTem:BEEPer')
        print(f'IT6861A Ver:{__ver}Is Ready\n')

    def close(self):
        """
        Set to local control mode.
        """
        self.stop()
        time.sleep(0.1)
        self._ser.write('SYSTem:LOCal')
        time.sleep(0.1)
        self._ser.close()
        print('IT6861A Closed\n')

    def set_vi(self, voltage, current):
        """
        Output ON with set voltage and current.
        """
        self._ser.write(f'VOLT {voltage:.3f}')
        time.sleep(0.1)
        self._ser.write(f'CURR {current:.3f}')
        time.sleep(0.1)
        self._ser.write('OUTP 1')
        time.sleep(0.1)
        print(f'IT6861A OUT: {voltage:.3f}V {current:.3f}A\n')

    def measure_v(self):
        """
        Measure the output voltage.
        """
        self._ser.write('MEAS?')
        __value = float(self._ser.read()[:-1])
        print(f'IT6861A OUT Voltage: {__value}V')
        return __value

    def measure_i(self):
        """
        Measure the output current.
        """
        self._ser.write('MEAS:CURR?')
        __value = float(self._ser.read()[:-1])
        print(f'IT6861A OUT Current: {__value}A')
        return __value

    def measure_p(self):
        """
        Measure the ouput power.
        """
        self._ser.write('MEAS:POW?')
        __value = float(self._ser.read()[:-1])
        print(f'IT6861A OUT Power: {__value}W')
        return __value

    def stop(self):
        """
        Output OFF.
        """
        self._ser.write('OUTPut 0')
        time.sleep(0.1)
        print('IT6861A Stop Output\n')

class HP6644A:
    _ser = None

    def begin(self):
        self._ser.open()
        time.sleep(0.2)
        self._ser.write('SYSTem:VERSion?')
        __ver = self._ser.read()
        time.sleep(0.1)
        print(f'HP6644A Ver:{__ver}Is Ready\n')

    def close(self):
        self.stop()
        time.sleep(0.1)
        self._ser.close()
        print('HP6644A Closed\n')

    def set_vi(self, voltage, current):
        self._ser.write(f'VOLTage {voltage:.3f}')
        self._ser.write(f'CURRent {current:.3f}')
        self._ser.write('OUTPut 1')
        time.sleep(0.1)
        print(f'HP6644A OUT: {voltage:.3f}V {current:.3f}A\n')

    def stop(self):
        self._ser.write('OUTPut 0')
        time.sleep(0.1)
        print('HP6644A Stop Output\n')

class C62012P:
    _ser = None

    def begin(self):
        self._ser.open()
        time.sleep(0.2)
        self._ser.write('CONF:REM ON')
        print(f'C62012P Is Ready\n')

    def close(self):
        self.stop()
        time.sleep(0.1)
        self._ser.close()
        print('C62012P Closed\n')

    def set_vi(self, voltage, current):
        self._ser.write(f'SOUR:VOLT {voltage:.3f}')
        self._ser.write(f'SOUR:CURR {current:.3f}')
        self._ser.write('CONF:OUTP ON')
        time.sleep(0.1)
        print(f'C62012P OUT: {voltage:.3f}V {current:.3f}A\n')
    def measure_v(self):
        """
        Measure the output voltage.
        """
        self._ser.write('MEAS:VOLT?')
        __value = float(self._ser.read()[:-1])
        print(f'C62012P OUT Voltage: {__value}V')
        return __value

    def measure_i(self):
        """
        Measure the output current.
        """
        self._ser.write('MEAS:CURR?')
        __value = float(self._ser.read()[:-1])
        print(f'C62012P OUT Current: {__value}A')
        return __value

    def measure_p(self):
        """
        Measure the ouput power.
        """
        self._ser.write('MEAS:POW?')
        __value = float(self._ser.read()[:-1])
        print(f'C62012P OUT Power: {__value}W')
        return __value
        
    def stop(self):
        self._ser.write('CONF:OUTP OFF')
        time.sleep(0.1)
        print('C62012P Stop Output\n')

# Electronic Load


class C6312A:
    _ser = None
    _name = 'C6312A'

    def begin(self):
        self._ser.open()
        time.sleep(0.1)
        self._ser.write('CONFigure:REMote ON')
        time.sleep(0.2)
        self._ser.write('CHAN:ID?')
        __ver = self._ser.read()
        time.sleep(0.1)
        print(f'{self._name} Ver:{__ver}Is Ready\n')

    def close(self):
        self.load_off()
        time.sleep(0.1)
        self._ser.write('CONFigure:REMote OFF')
        time.sleep(0.1)
        self._ser.close()
        print(f'{self._name} Closed\n')

    def set_cc(self, from_current, to_current):
        """
        Set CC Mode and Load ON.

        from_current: Start current.
        to_current: Target current.
        """
        self.load_off()
        time.sleep(0.1)
        self._ser.write(f'CURR:STAT:L1 {from_current:.3f}')
        self._ser.write(f'CURRent:STATic:L2 {to_current:.3f}')
        self._ser.write('LOAD ON')
        time.sleep(0.1)
        print(f'{self._name} CC LOAD: {from_current:.3f}~{to_current:.3f}A\n')

    def set_cv(self, from_voltage, to_voltage):
        """
        Set CV Mode and Load ON.

        from_voltage: Start voltage.
        to_voltage: Target voltage.
        """
        self.load_off()
        time.sleep(0.1)
        self._ser.write(f'VOLT:L1 {from_voltage:.3f}')
        self._ser.write(f'VOLTage:L2 {to_voltage:.3f}')
        self._ser.write('LOAD ON')
        time.sleep(0.1)
        print(f'{self._name} CV LOAD: {from_voltage:.3f}~{to_voltage:.3f}V\n')

    def measure_i(self):
        self._ser.write('MEAS:CURR?')
        __value = float(self._ser.read()[:-1])
        print(f'{self._name} OUT Current: {__value}A')
        return __value

    def measure_v(self):
        self._ser.write('MEAS:VOLT?')
        __value = float(self._ser.read()[:-1])
        print(f'{self._name} OUT Voltage: {__value}V')
        return __value

    def measure_p(self):
        self._ser.write('MEAS:POW?')
        __value = float(self._ser.read()[:-1])
        print(f'{self._name} OUT Power: {__value}W')
        return __value

    def load_off(self):
        self._ser.write('LOAD OFF')
        time.sleep(0.1)
        print(f'{self._name} Stop Input\n')

    def set_fast_cc(self, from_current, to_current):
        """
        Just set cc current.
        """
        self._ser.write(f'CURR:STAT:L1 {from_current:.3f}')
        self._ser.write(f'CURRent:STATic:L2 {to_current:.3f}')
        #self._ser.write('LOAD ON')


class PLZ205W:
    _ser = None
    _name = 'PLZ205W'

    def begin(self):
        self._ser.open()
        time.sleep(0.1)
        self._ser.write('SYST:COMM:RLST RWL')
        time.sleep(0.2)
        self._ser.write('SYST:VERS?')
        __ver = self._ser.read()
        time.sleep(0.1)
        print(f'{self._name} Ver:{__ver}Is Ready\n')

    def close(self):
        self.load_off()
        time.sleep(0.1)
        self._ser.write('SYST:COMM:RLST LOC')
        time.sleep(0.1)
        self._ser.close()
        print(f'{self._name} Closed\n')

    def set_cc_range(self, _range):
        """
        Set CC Mode Range
        range: LOW|MED|HIGH
        """
        self._ser.write(f'CURR:RANG {_range}')
        print(f'{self._name} CC MODE Range is {_range}')

    def set_cc(self, current):
        """
        Set CC Mode and Load ON.

        current: 
        Range H 0.000 to 42.000 Resolution 0.001
        Range M 0.0000 to 4.2000 Resolution 0.0001
        Range L 0.00000 to 0.42000 Resolution 0.00001
        """
        self.load_off()
        time.sleep(0.1)
        self._ser.write(f'CURR {current:.5f}')
        self._ser.write('OUTP ON')
        time.sleep(0.1)
        print(f'{self._name} CC LOAD: {current:.5f}A\n')

    def set_cv_range(self, _range):
        """
        Set CV Mode Range
        range: LOW|HIGH
        """
        self._ser.write(f'VOLT:RANG {_range}')
        print(f'{self._name} CV MODE Range is {_range}')

    def set_cv(self, voltage):
        """
        Set CV Mode and Load ON.

        voltage:
        Range H 0.000 to 157.500 Resolution 0.005
        Range L 0.000 to 15.7500 Resolution 0.0005
        """
        self.load_off()
        time.sleep(0.1)
        self._ser.write(f'VOLT {voltage:.4f}')
        self._ser.write('OUTP ON')
        time.sleep(0.1)
        print(f'{self._name} CV LOAD: {voltage:.4f}V\n')

    def set_cp_range(self, _range):
        """
        Set CP Mode Range
        range: LOW|MED|HIGH
        """
        self._ser.write(f'POW:RANG {_range}')
        print(f'{self._name} CP MODE Range is {_range}')

    def set_cp(self, power):
        """
        Set CP Mode and Load ON.

        power: 
        Range H 0.00 to 210.00 Resolution 0.005
        Range M 0.00 to 21.000 Resolution 0.0005
        Range L 0.00 to 2.1000 Resolution 0.00005
        """
        self.load_off()
        time.sleep(0.1)
        self._ser.write(f'POW {power:.5f}')
        self._ser.write('OUTP ON')
        time.sleep(0.1)
        print(f'{self._name} CP LOAD: {power:.5f}W\n')

    def measure_i(self):
        self._ser.write('MEAS:CURR?')
        __value = float(self._ser.read()[:-1])
        print(f'{self._name} OUT Current: {__value}A')
        return __value

    def measure_v(self):
        self._ser.write('MEAS:VOLT?')
        __value = float(self._ser.read()[:-1])
        print(f'{self._name} OUT Voltage: {__value}V')
        return __value

    def measure_p(self):
        self._ser.write('MEAS:POW?')
        __value = float(self._ser.read()[:-1])
        print(f'{self._name} OUT Power: {__value}W')
        return __value

    def load_off(self):
        self._ser.write('OUTP OFF')
        time.sleep(0.1)
        print(f'{self._name} Stop Input\n')

    def set_fast_cc(self, current):
        """
        Just set cc current.

        current: 0.000 to 42.000
        """
        self._ser.write(f'CURR: {current:.3f}')
        #self._ser.write('LOAD ON')
