# 序列化
import json
student = [{'name': 'qiyue', 'age': 18, 'flag': False},
           {'name': 'qiyue', 'age': 18}
           ]
# NOSQL MongoDB
json_str = json.dumps(student)
print(type(json_str))
print(json_str)

# JSON对象、JSON、JSON字符串
# ECMASCRIPT Actionscript JSON Typescript
# 实现的标准  版本
