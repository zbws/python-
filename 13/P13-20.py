class Time60s(object):



    def __init__(self,hr=None,mi=None):

        self.hour=hr

        self.minute=mi



        if isinstance(hr,dict):

            s=[]

            for ti in hr.keys():

                s.append(ti)

            self.hour=hr[s[0]]

            self.minute=hr[s[1]]



        if isinstance(hr,str):

            self.hour=int(hr.split(':')[0])

            self.minute=int(hr.split(':')[1])



    def __add__(self,other):

        if (self.hour+other.hour)<60 and (self.minute+other.minute)>60:

            return '%d:%d'%((self.hour+other.hour+1),(self.minute+other.minute-60))

        else:

            return '%d:%d'%((self.hour+other.hour),(self.minute+other.minute))



    def __str__(self):

        if self.hour and self.minute:

            if self.hour<10 and self.minute>=10:

                return '%02d:%d' %(self.hour,self.minute)

            elif self.hour>=10 and self.minute<10:

                return '%d:%02d' %(self.hour,self.minute)

            else :

                return '%d:%d'% (self.hour,self.minute)

        else:

            return '00:00'



    __repr__=__str__

if __name__=='__main__':

    #wed=Time60s({'hr':10,'min':30})

    #wed=Time60s(10,30)

    wed=Time60s("10:30")

    wed2=Time60s(8,45)

    print(wed+wed2)
