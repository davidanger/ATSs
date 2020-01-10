# ATSs
Auto Test Script, by using Python through VISA.

Develop Tools(optional):
[Anaconda](https://www.anaconda.com/)
[Visual Studio Code](https://code.visualstudio.com/)

Need Plugins:
[PyVISA](https://github.com/pyvisa/pyvisa)
[NI-VISA](http://www.ni.com/zh-cn/support/downloads/drivers/download.ni-visa.html#329456) or [Keysight IO Suite](https://www.keysight.com/zh-CN/pd-1985909/io-libraries-suite?nid=-33330.977662.00&cc=CN&lc=chi)
others(optional)

Pyvisa simple
```
>>> import pyvisa
>>> rm = pyvisa.ResourceManager()
>>> rm.list_resources()
('ASRL1::INSTR', 'ASRL2::INSTR', 'GPIB0::12::INSTR')
>>> inst = rm.open_resource('GPIB0::12::INSTR')
>>> print(inst.query("*IDN?"))
```