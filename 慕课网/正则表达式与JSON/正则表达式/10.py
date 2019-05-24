# 组
import re
a = 'PythonPythonPython'
r = re.findall('(Python){3}(JS)', a)  # ()成为为一个组,为且关系,[]为或关系

print(r)
