pip install --user pyinputplus

安裝 Log
(c) Microsoft Corporation. 著作權所有，並保留一切權利。

C:\Users\Rlulu>pip install --user pyinputplus
Collecting pyinputplus
  Downloading PyInputPlus-0.2.12.tar.gz (20 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting pysimplevalidate>=0.2.7 (from pyinputplus)
  Downloading PySimpleValidate-0.2.12.tar.gz (22 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting stdiomask>=0.0.3 (from pyinputplus)
  Downloading stdiomask-0.0.6.tar.gz (3.6 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: pyinputplus, pysimplevalidate, stdiomask
  Building wheel for pyinputplus (pyproject.toml) ... done
  Created wheel for pyinputplus: filename=pyinputplus-0.2.12-py3-none-any.whl size=11374 sha256=0c137b2c83eb9951c244038572cdf6ed3a68a9365a173a7c143652cef49697af
  Stored in directory: c:\users\rlulu\appdata\local\pip\cache\wheels\a3\6b\89\3bec14288af8e0729d088fb41a785e583d49e772f2529c7676
  Building wheel for pysimplevalidate (pyproject.toml) ... done
  Created wheel for pysimplevalidate: filename=pysimplevalidate-0.2.12-py3-none-any.whl size=16251 sha256=41a2666fde0dd096a7922cf7e2aee86e1838b5fcf5df32b87ff47880ccf1276e
  Stored in directory: c:\users\rlulu\appdata\local\pip\cache\wheels\fc\40\7a\4d3b2dc2e80b4b3bbda89eec94fcefd6c8bd1101cc7bb89554
  Building wheel for stdiomask (pyproject.toml) ... done
  Created wheel for stdiomask: filename=stdiomask-0.0.6-py3-none-any.whl size=3375 sha256=aa00a75eb2240820619b50d5fe91759acadc38731ec0f3e365b66d0fd656a345
  Stored in directory: c:\users\rlulu\appdata\local\pip\cache\wheels\19\0c\90\5ee0da7cf06ff7e233f273063797785d5eabf0ab9f04220866
Successfully built pyinputplus pysimplevalidate stdiomask
Installing collected packages: stdiomask, pysimplevalidate, pyinputplus
Successfully installed pyinputplus-0.2.12 pysimplevalidate-0.2.12 stdiomask-0.0.6

[notice] A new release of pip is available: 25.0.1 -> 25.1.1
[notice] To update, run: C:\Users\Rlulu\AppData\Local\Programs\Python\Python311\python.exe -m pip install --upgrade pip

C:\Users\Rlulu>

# 預設沒安裝
# ==========
>>> import pyinputplus
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pyinputplus'
>>>

# 正確安裝後
# ==========
>>> import pyinputplus
>>>

  
