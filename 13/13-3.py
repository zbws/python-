
'''没有实现对非0数值的处理，即__nozero__()方法没有实现，习题上的其他要求已经实现'''
class MoneyFmt():
    def __init__(self,num=None):
        self.number=num

    def __nonzero__(self):
        if self.number :
            return True
        else:
            return False

    def __repr__(self):
        return self.number

    #允许数值修改
    def update(self,value=None):
        self.number=value

    # 格式化显示金额字符
    def __str__(self):

        x = str(self.number)
        m1 = x.split('.')[0]; n1 = x.split('.')[1]
        n2 = '';s2 = [];m2 = '';count = 0;i = len(m1)
        if len(n1) > 2:
            n2 = n1[0] + n1[1]

        while i > 0:
            s2.append(m1[i - 1])
            i = i - 1;
            count = count + 1
            if count % 3 == 0 and m1[i - 1] != '-' and i != 0:
                s2.append(',')
        s2.reverse()

        for i in range(len(s2)):
            m2 += s2[i]
        m3 = list(m2)

        # 在金额前加美元符
        if m3[0] == '-':
            m3.insert(1, '$')
        else:
            m3.insert(0, '$')

        # 连接小数点前后的数，形成金额总数
        if m3[-1] == ',':
            m3[-1] = '.';m4 = ''.join(m3);s = m4 + n2
        else:
            m4 = ''.join(m3);s = m4 + '.' + n2
        return s
