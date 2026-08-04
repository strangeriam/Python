# 只使用 1 個 Function --> 讀入 位在 include/apc.py 的 _f_apc_info.
# 要使用 _f_apc_info 的功能.

import include.apc as _f_apc_info

# 使用 多 個 Functions --> 讀入 位在 include/apc.py 的 _f_apc_info & _f_apc_power.
from include.apc import _f_apc_info, _f_apc_power
