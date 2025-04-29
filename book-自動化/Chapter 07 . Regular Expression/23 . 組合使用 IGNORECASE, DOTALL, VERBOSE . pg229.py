IGNORECASE # 忽略大小寫
DOTALL
VERBOSE

除了 re.IGNORECASE, 加入第二個引數 re.DOTALL
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
or
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
