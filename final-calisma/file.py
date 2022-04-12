import os
import shutil
'''
ad=input("hoşgeldiniz öncelikle adınızı giriniz: " )
numara=input("numaranızı da giriniz: ")
sifre=input("sifrenizi giriniz: ")

os.getcwd()
os.chdir('..')
os.listdir()
os.mkdir("yeniklasör")
os.rename("yeniklasör","dahayeniklasör")
shutil.rmtree("dahayeniklasör")#dolu klasörleri silmek için kullanılıyor


f=open("test.txt",'w')
f.write(ad+"\n")
f.write(numara+"\n")
f.write(sifre+"\n")
f.close()


f=open("test.txt",'r')
f.readline()
f.readline()
pw=f.readline()
print("sifreniz"+pw)


numara={}
numara["ahmet"]=501
numara["mehmet"]=205
for i,j in numara.items():
    print(i)
    print(j)

try:
    num=int(input("Bir tamsayı giriniz: "))
except ValueError:
    print("Hatalı bir değer girdiniz!")
else:
    a=5/num
    print(a)
finally:
    print("Program bitti!")
'''
'''
class Rectangle:
    def __init__(self,filled,width,height,color):
        self.__filled=filled
        self.__width=width
        self.__height=height
        self.__color=color
    def isFilled(self):
        return self.__filled
    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color=color
        return self.__color
    def getArea(self):
        return self.__width*self.__height
    def setFilled(self,filled):
        self.__filled=filled
        return self.__filled

r1=Rectangle(false,2.5,34,"blue")


class A:
    def Explore(self):
        print("Explore açıldı A")
class B:
    def Discover(self):
        print("Discover açıldı B")
class C:
    def Search(self):
        print("Search açıldı C")
class D(A,B,C):
    def test(self):
        print("test açıldı D")
    def Search(self):
        print("Search açıldı D")

r2=D()
r2.Explore()
r2.Search()
r2.Discover()
r2.test()


class Dosya:
    
    def __init__(self,pathi):
        self.__pathi=pathi
        
    def Oku(self,birim):
        file=open(self.__pathi,"r")
        print(file.read(birim))
        file.close()
    def Yaz(self,yazi):
        file=open(self.__pathi,"a")
        file.write(yazi)
        file.close()
    def FullOku(self):
        file=open(self.__pathi,"r")
        print(file.read())
        file.close()
    def GetWorkingDirectory(self):
        print(os.getcwd())
    

test=Dosya("test.txt")
test.Oku(15)
test.Yaz("Seni Seviyorum")
test.FullOku()
test.GetWorkingDirectory()
'''
counter=0
sayilar=[0,5,4,3,5,2,3,5,0,9,0]
for i in sayilar:
    sayilar[counter]=i%2
    counter+=1
print(sayilar)