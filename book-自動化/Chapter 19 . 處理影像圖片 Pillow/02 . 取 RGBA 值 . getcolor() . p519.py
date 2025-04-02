
from PIL import ImageColor

>>> ImageColor.getcolor('red', 'RGBA')

>>> from PIL import ImageColor
>>> ImageColor.getcolor('red', 'RGBA')
(255, 0, 0, 255)
>>>
>>> ImageColor.getcolor('RED', 'RGBA')
(255, 0, 0, 255)
>>>
>>> ImageColor.getcolor('Black', 'RGBA')
(0, 0, 0, 255)
>>>
>>> ImageColor.getcolor('chocolate', 'RGBA')
(210, 105, 30, 255)
>>>
>>> ImageColor.getcolor('CornflowerBlue', 'RGBA')
(100, 149, 237, 255)
>>>
>>>
