#文件的读取
# f = open('相对路径或者绝对路径')
# f.read()
# f.close()

#f.readline()   逐行读取数据
# f = open('相对路径或者绝对路径')
# f.readline()
# f.readline()

# all_file=[]
# for i in range(9999):
#     all_file.append(open('相对路径或者绝对路径','r'))
#     print(i)

#写入文件
f=open('相对路径或者绝对路径','w')
f.write('写入内容')
f.close()

#你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，
# 空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数
# 据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。
# 所以，还是用with语句来得保险：
with open('相对路径或者绝对路径', 'w') as f:
    f.write('Hello, world!')

#字符编码
#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
f = open('相对路径或者绝对路径', 'r', encoding='gbk')
f.read()
#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
#二进制文件
f = open('/Users/michael/test.jpg', 'rb')
f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节