class maobeibei:
    def __init__(self):
        self.face='cute'
        self.brain='clever'

    def __repr__(self):
        return '<maobeibei is a %s neko and is %s !>' %(self.face,self.brain)

    def kaoshi(self,test,bitch):
        return 'maobeiebi beats %s and %s gua le'%(test,bitch)

    @property
    def face(self):
        return self.face

    @face.setter
    def face(self,face):
        raise EnvironmentError("You can not change maobeiebi's face!")


neko=maobeibei()
print neko
test=raw_input("Please input your test's name")
name=raw_input("please input  bitch's name")
print neko.kaoshi(test,name)

