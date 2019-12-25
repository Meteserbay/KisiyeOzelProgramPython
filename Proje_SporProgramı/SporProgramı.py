import datetime
import random
import webbrowser
from tkinter import *

easyChest=["Physio ball pushup","Bench press","Dips","Chest press","Dumbell fly","Machine fly","Butterfly chest machine"]
mediumChest=["Pushup","Incline bench press","Dumbell bench press","Dumbell Incline Press"]
hardChest=["Smith machine incline press","Incline dumbbell fly","Cable crossover"]

easyShoulder=["Dumbell front raises","Side lateral raises","Front deltoid raise"]
mediumShoulder=["Rear deltoid raise","Dumbell overhead press","Cable side lateral raise"]
hardShoulder=["Face pull","Wide-Grip pull ups","Standing barbell overhead press"]

easyBack=["Hyperextension","Single arm dumbell row","Rowing machine"]
mediumBack=["Lat pulldown","Barfiks","Bent over row","Straight arm pulldown"]
hardBack=["Deadlift","Close grip lat pulldown","T bar row","Power shrug","Pull up","Chin up"]

easyAbdominal=["Crunches","Leg raise","Abdominal machine","Negative crunch"]
mediumAbdominal=["Flutter kicks","Mountain climbers","Ab-Cross crawl","Hanging leg raise"]
hardAbdominal=["Plank","Bicycle crunch","Reverse crunch"]

easyBiceps=["Dumbell curl","Preacher curl","Z barbell curl"]
mediumBiceps=["Barbell curl","Ez-Bar reverse curl","Incline dumbell curl","Hammer curl","Low pulley curls"]
hardBiceps=["21 barbell curl","Concentration curl","Close grip Chins curl"]

easyTriceps=["Pushdown","Weighted bench dip","Seated overhead dumbel extension"]
mediumTriceps=["Close grip bench press","Dips","Dumbell kickback","SkullCrusher","Cable pushdown"]
hardTriceps=["Rope pushdown","Lying barbell triceps extensions","Cable overhead extension"]

easyLeg=["Front squat","Dumbell stepup","Leg extension machine"]
mediumLeg=["Squat","Leq press","Seated calf raise","Walking Lunge","Leg curl"]
hardLeg=["Bulgarian split squat","Deadlift"]

antrenman=[]
yapilacakSet=[]
yapilacakTekrar=[]

def kitleindexHesapla(kilo,boy):
    kitleindex=kilo/(boy**2)
    return kitleindex

def easyotomatikProgram():
    antrenman.append(isinma[0])
    antrenman.append(easyChest[random.randint(0, 6)])
    antrenman.append(easyChest[random.randint(0, 6)])
    while (antrenman[1] == antrenman[2]):
        antrenman[2] = easyChest[random.randint(0, 6)]
    antrenman.append(easyBiceps[random.randint(0, 2)])
    antrenman.append(easyBiceps[random.randint(0, 2)])
    while (antrenman[3] == antrenman[4]):
        antrenman[4] = easyChest[random.randint(0, 2)]
    antrenman.append(easyTriceps[random.randint(0, 2)])
    antrenman.append(easyShoulder[random.randint(0, 2)])
    antrenman.append(easyBack[random.randint(0, 2)])
    antrenman.append(easyLeg[random.randint(0, 2)])
    antrenman.append(easyAbdominal[random.randint(0, 3)])

def mediumotomatikProgram():
    antrenman.append(isinma[1])
    antrenman.append(mediumChest[random.randint(0, 3)])
    antrenman.append(mediumChest[random.randint(0, 3)])
    while (antrenman[1] == antrenman[2]):
        antrenman[2] = mediumChest[random.randint(0, 3)]
    antrenman.append(mediumBiceps[random.randint(0, 4)])
    antrenman.append(mediumBiceps[random.randint(0, 4)])
    while (antrenman[3] == antrenman[4]):
        antrenman[4] = mediumBiceps[random.randint(0, 4)]
    antrenman.append(mediumTriceps[random.randint(0, 4)])
    antrenman.append(mediumShoulder[random.randint(0, 2)])
    antrenman.append(mediumBack[random.randint(0, 3)])
    antrenman.append(mediumLeg[random.randint(0, 4)])
    antrenman.append(mediumAbdominal[random.randint(0, 3)])

def hardotomatikProgram():
    antrenman.append(isinma[2])
    antrenman.append(hardChest[random.randint(0, 2)])
    antrenman.append(hardChest[random.randint(0, 2)])
    while (antrenman[1] == antrenman[2]):
        antrenman[2] = hardChest[random.randint(0, 2)]
    antrenman.append(hardBiceps[random.randint(0, 2)])
    antrenman.append(hardBiceps[random.randint(0, 2)])
    while (antrenman[3] == antrenman[4]):
        antrenman[4] = hardBiceps[random.randint(0, 2)]
    antrenman.append(hardTriceps[random.randint(0, 2)])
    antrenman.append(hardShoulder[random.randint(0, 2)])
    antrenman.append(hardBack[random.randint(0, 5)])
    antrenman.append(hardLeg[random.randint(0, 1)])
    antrenman.append(hardAbdominal[random.randint(0, 2)])
def LISSKardiyoProgramOlustur():
    if (baslamaSuresiAy <= 2):
        if (cinsiyet == "Erkek" or cinsiyet == "e" or cinsiyet == "E"):
            easyotomatikProgram()
            antrenman.append(isinma[1])
            antrenman.append(isinma[2])
            for i in range(1, len(antrenman)):
                yapilacakSet.append(4)
                yapilacakTekrar.append(12)
            for i in range(3,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
        elif (cinsiyet == "Kadın" or cinsiyet == "K" or cinsiyet == "k"):
            easyotomatikProgram()
            antrenman.append(isinma[1])
            antrenman.append(isinma[2])
            for i in range(1, len(antrenman)):
                yapilacakSet.append(3)
                yapilacakTekrar.append(10)
            for i in range(3,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
    elif (baslamaSuresiAy > 2 and baslamaSuresiAy <= 6):
        if (cinsiyet == "Erkek" or cinsiyet == "e" or cinsiyet == "E"):
            mediumotomatikProgram()
            antrenman.append(isinma[0])
            antrenman.append(isinma[2])
            for i in range(1, len(antrenman)):
                yapilacakSet.append(4)
                yapilacakTekrar.append(12)
            for i in range(3,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
        elif (cinsiyet == "Kadın" or cinsiyet == "k" or cinsiyet == "K"):
            mediumotomatikProgram()
            antrenman.append(isinma[0])
            antrenman.append(isinma[2])
            for i in range(1, len(antrenman)):
                yapilacakSet.append(3)
                yapilacakTekrar.append(10)
            for i in range(3,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
    if (baslamaSuresiAy > 6):
        if (cinsiyet == "Erkek" or cinsiyet == "e" or cinsiyet == "E"):
            hardotomatikProgram()
            antrenman.append(isinma[0])
            antrenman.append(isinma[1])
            for i in range(1, len(antrenman)):
                yapilacakSet.append(4)
                yapilacakTekrar.append(12)
            for i in range(3,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
        elif (cinsiyet == "Kadın" or cinsiyet == "K" or cinsiyet == "k"):
            hardotomatikProgram()
            antrenman.append(isinma[0])
            antrenman.append(isinma[1])
            for i in range(1, len(antrenman)):
                yapilacakSet.append(3)
                yapilacakTekrar.append(10)
            for i in range(3,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
def idealIndexProgramOlustur():
    if (baslamaSuresiAy <= 2):
        if (cinsiyet == "Erkek" or cinsiyet == "e" or cinsiyet == "E"):
            easyotomatikProgram()
            for i in range(1, len(antrenman)):
                yapilacakSet.append(4)
                yapilacakTekrar.append(12)
            for i in range(1,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
        elif (cinsiyet == "Kadın" or cinsiyet == "K" or cinsiyet == "k"):
            easyotomatikProgram()
            for i in range(1, len(antrenman)):
                yapilacakSet.append(3)
                yapilacakTekrar.append(10)
            for i in range(1,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
    elif (baslamaSuresiAy > 2 and baslamaSuresiAy <= 6):
        if (cinsiyet == "Erkek" or cinsiyet == "e" or cinsiyet == "E"):
            mediumotomatikProgram()
            for i in range(1, len(antrenman)):
                yapilacakSet.append(4)
                yapilacakTekrar.append(12)
            for i in range(1,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
        elif (cinsiyet == "Kadın" or cinsiyet == "k" or cinsiyet == "K"):
            mediumotomatikProgram()
            for i in range(1, len(antrenman)):
                yapilacakSet.append(3)
                yapilacakTekrar.append(10)
            for i in range(1,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
    if (baslamaSuresiAy > 6):
        if (cinsiyet == "Erkek" or cinsiyet == "e" or cinsiyet == "E"):
            hardotomatikProgram()
            for i in range(1, len(antrenman)):
                yapilacakSet.append(4)
                yapilacakTekrar.append(12)
            for i in range(1,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
        elif (cinsiyet == "Kadın" or cinsiyet == "K" or cinsiyet == "k"):
            hardotomatikProgram()
            for i in range(1, len(antrenman)):
                yapilacakSet.append(3)
                yapilacakTekrar.append(10)
            for i in range(1,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
def HITKardiyoProgramOlustur():
    for i in range (0,3):
        antrenman.append(isinma[i])
        yapilacakSure.append(20)
    for i in range(0,3):
        print(antrenman[i],"------ Yapılacak süre:",yapilacakSure[i])
def dusukIndexProgramOlustur():
    if(baslamaSuresiAy<=2):
        if(cinsiyet=="Erkek" or cinsiyet=="e" or cinsiyet=="E"):
            easyotomatikProgram()
            del antrenman[2]
            del antrenman[4]
            for i in range(1,len(antrenman)):
                yapilacakSet.append(4)
                yapilacakTekrar.append(12)
            for i in range(1,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
        elif(cinsiyet=="Kadın" or cinsiyet=="K" or cinsiyet=="k"):
            easyotomatikProgram()
            del antrenman[2]
            del antrenman[4]
            for i in range(1, len(antrenman)):
                yapilacakSet.append(3)
                yapilacakTekrar.append(10)
            for i in range(1,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
    elif(baslamaSuresiAy>2 and baslamaSuresiAy<=6):
        if (cinsiyet == "Erkek" or cinsiyet == "e" or cinsiyet == "E"):
            mediumotomatikProgram()
            del antrenman[2]
            del antrenman[4]
            for i in range(1, len(antrenman)):
                yapilacakSet.append(4)
                yapilacakTekrar.append(12)
            for i in range(1,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
        elif(cinsiyet=="Kadın" or cinsiyet=="k" or cinsiyet=="K"):
            mediumotomatikProgram()
            del antrenman[2]
            del antrenman[4]
            for i in range(1, len(antrenman)):
                yapilacakSet.append(3)
                yapilacakTekrar.append(10)
            for i in range(1,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
    if (baslamaSuresiAy>6):
        if (cinsiyet == "Erkek" or cinsiyet == "e" or cinsiyet == "E"):
            hardotomatikProgram()
            del antrenman[2]
            del antrenman[4]
            for i in range(1, len(antrenman)):
                yapilacakSet.append(4)
                yapilacakTekrar.append(12)
            for i in range(1,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
        elif (cinsiyet == "Kadın" or cinsiyet == "K" or cinsiyet == "k"):
            hardotomatikProgram()
            del antrenman[2]
            del antrenman[4]
            for i in range(1, len(antrenman)):
                yapilacakSet.append(3)
                yapilacakTekrar.append(10)
            for i in range(1,len(antrenman)):
                print(antrenman[i],"------ Set sayısı:",yapilacakSet[i-1],"------ Tekrar sayısı: ",yapilacakTekrar[i-1])
isinma=["Running","Cycling","Spacewalk"]
simdikiTarih=datetime.datetime.now()
yas=0
kilo=0
boy=0,1
yapilacakSure=[]
baslamaTarihi=""
cinsiyet=""
vücutKitleindex=0
yas=int(input("Yaşınız:"))
kilo=int(input("Kilonuz:"))
boy=int(input("Boyunuz(örn:183):"))
mcinsiboy=boy/100
vücutKitleindex=kitleindexHesapla(kilo,mcinsiboy)
baslamaTarihi=input("Spora başlama tarihiniz(GG:AA:YYYY):")
deger=baslamaTarihi.split(":")
Ay=int(deger[1])
Yil=int(deger[2])
baslamaSuresiAy=((simdikiTarih.year-Yil)*12+(simdikiTarih.month-Ay))
cinsiyet=input("Cinsiyetiniz(E/K):")
if(cinsiyet=="E" and cinsiyet=="e"):
    cinsiyet="Erkek"
elif(cinsiyet=="K" and cinsiyet=="k"):
    cinsiyet="Kadın"
print("Vücut kitle index puanınız:",vücutKitleindex)
if(vücutKitleindex<=18.49):
    print("Programınız kilo alma ve kas kütlenizi artırma amacıyla yapıldı...")
    dusukIndexProgramOlustur()
elif(vücutKitleindex>=18.5 and vücutKitleindex<=24.99):
    print("Kilonuz ideal... Programınız kas kütlenizi artırma amacıyla yapıldı...")
    idealIndexProgramOlustur()
elif(vücutKitleindex>=25 and vücutKitleindex<=29.99):
    print("Programınız kilonuzu azaltma ve kas kütlenizi artırma amacıyla yapıldı... LISS kardiyo antrenmanınız:")
    LISSKardiyoProgramOlustur()
elif(vücutKitleindex>30):
    print("Programınız kilonuzu azaltma amacıyla yapıldı... HIT kardiyo antrenmanınız")
    HITKardiyoProgramOlustur()

pencere=Tk()
pencere.geometry("500x300")
pencere.title("Antreman Programı")
etiket0=Label(pencere,text="Programınız")
etiket0.pack()
i=1

yas=(antrenman[i]+"------ Set sayısı:"+str(yapilacakSet[i-1])+"------ Tekrar sayısı: "+str(yapilacakTekrar[i-1]))
etiket=Label(pencere,text=yas)
etiket.pack()
i=i+1
yas=(antrenman[i]+"------ Set sayısı:"+str(yapilacakSet[i-1])+"------ Tekrar sayısı: "+str(yapilacakTekrar[i-1]))
etiket2=Label(pencere,text=yas)
etiket2.pack()
i=i+1
yas=(antrenman[i]+"------ Set sayısı:"+str(yapilacakSet[i-1])+"------ Tekrar sayısı: "+str(yapilacakTekrar[i-1]))
etiket3=Label(pencere,text=yas)
etiket3.pack()
i = i + 1
if(len(antrenman)>i):

    yas = (antrenman[i] + "------ Set sayısı:" + str(yapilacakSet[i - 1]) + "------ Tekrar sayısı: " + str(yapilacakTekrar[i - 1]))
    etiket4 = Label(pencere, text=yas)
    etiket4.pack()
    i = i + 1

if (len(antrenman) >i):
    yas = (antrenman[i] + "------ Set sayısı:" + str(yapilacakSet[i - 1]) + "------ Tekrar sayısı: " + str(yapilacakTekrar[i - 1]))
    etiket5 = Label(pencere, text=yas)
    etiket5.pack()
    i = i + 1

if (len(antrenman) > i):
    yas = (antrenman[i] + "------ Set sayısı:" + str(yapilacakSet[i - 1]) + "------ Tekrar sayısı: " + str(yapilacakTekrar[i - 1]))
    etiket6 = Label(pencere, text=yas)
    etiket6.pack()
    i = i + 1
if (len(antrenman) > i):
    yas = (antrenman[i] + "------ Set sayısı:" + str(yapilacakSet[i - 1]) + "------ Tekrar sayısı: " + str(yapilacakTekrar[i - 1]))
    etiket7 = Label(pencere, text=yas)
    etiket7.pack()
    i = i + 1
if (len(antrenman) >i):
    yas = (antrenman[i] + "------ Set sayısı:" + str(yapilacakSet[i - 1]) + "------ Tekrar sayısı: " + str(yapilacakTekrar[i - 1]))
    etiket8= Label(pencere, text=yas)
    etiket8.pack()
    i = i + 1
if (len(antrenman) >i):
    yas = (antrenman[i] + "------ Set sayısı:" + str(yapilacakSet[i - 1]) + "------ Tekrar sayısı: " + str(yapilacakTekrar[i - 1]))
    etiket9 = Label(pencere, text=yas)
    etiket9.pack()
    i = i + 1
def siteAc():
    webbrowser.open_new("file:///C:/Users/dell/Desktop/Fitness%20Programı/index.html")

btnSiteAc=Button(pencere,text="Hareketleri Görmek İçin Tıklayınız",command=siteAc)
btnSiteAc.pack()
pencere.mainloop()

