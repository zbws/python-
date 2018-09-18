import os
import re
'打开windows目录下的文件'
#f=open('D:/python_work/whodata.txt','r')
f=os.popen('dir','r')
h=open('D:/python_work/rewrite.txt','w')
for eachLine in f.readlines():
    h.write(str(re.split('\s\s+|\n',eachLine.strip())))
    h.write('\n')
h.close()
f.close()
