import os
import re
'��windowsϵͳ�µ�Ŀ¼'
#f=open('D:/python_work/whodata.txt','r')
f=os.popen('dir','r')
h=open('D:/python_work/rewrite.txt','w')
for eachLine in f.readlines():
    h.write(str(re.split('\s\s+|\n',eachLine.strip())))
    h.write('\n')
h.close()
f.close()