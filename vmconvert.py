#oto转vsdxmf
#本脚本将UTAU CVVC oto.ini转换为vocalsharp vsdxmf。目的是减少重复劳动，提高自动化程度
import os
import sys
import json
import itertools
#载入vmconvert.json
externaldict=json.load(open(sys.argv[0].replace(".py",".json"),encoding="utf8"))
Calias=externaldict["Calias"]
Valias=externaldict["Valias"]
#载入oto.ini
if(len(sys.argv)==1):
    otopath=os.path.join(os.path.split(sys.argv[0])[0],"oto.ini")
elif(os.path.isfile(sys.argv[1])):
    otopath=sys.argv[1]
else:
    otopath=os.path.join(sys.argv[1],"oto.ini")
otodict={}#条目名称->对应的oto条目
for line in open(otopath,encoding="shift-jis").readlines():
    linecontent=line.replace("=",",").split(",")
    for i in [2,3,4,5,6]:
        linecontent[i]=float(linecontent[i])
    otodict[linecontent[1]]=linecontent
#载入lsd字典
incomment=False
lsddict={}
currentword=""
for line in open(otopath.replace("oto.ini","main.lsd"),encoding="utf8").readlines():
    line=line.strip(" \n\t")
    if(line.startswith("###")):#注释
        incomment=not(incomment)
    else:
        if("#" in line):#拆音形式
            lsddict[currentword]=line.split("#")
        else:#拼音
            currentword=line
Cs={value[0] for value in lsddict.values()}#辅音列表
Vs={value[1] for value in lsddict.values()}#元音列表

#oto转vsdxmf
vsdxmfdict={}#{vsdxmf记号:oto记号}


#VC、VV
print("====VC====")
#print("i" in Vs)
#print("bi" in Vs)
#input()
for (V,C) in itertools.product(Vs|{""},Cs|Vs|{""}):
    VCotokey=Valias.get(V,V)+" "+Calias.get(C,C)
    if(VCotokey in otodict):
        vsdxmfdict[V+" "+C]=VCotokey
        #lineconvert(otodict[VCotokey],V+" "+C)
    else:
        print(VCotokey+" 缺失")
        #print('"'+Calias.get(C,C)+'":"",')
    #if(V=="i" and C=="bi"):
        #input()

#字典反转去重
vsdxmfdict_r={}#{oto记号:[vsdxmf记号]}
for (vskey,otokey) in vsdxmfdict.items():
    vsdxmfdict_r[otokey]=vsdxmfdict_r.get(otokey,[])+[vskey]
#转换
def lineconvert(otoline,name=[]):
    #print(otoline)
    global vsdxmfdict
    if(name==[]):
        name=[otoline[1]]
    return [
        name,
        otoline[0],
        otoline[2],
        otoline[2]+otoline[5],
        otoline[2]+otoline[3],
        otoline[2]-otoline[4],
        otoline[2]+otoline[6],
    ]
vsdxmf=[lineconvert(otodict[otokey],vskeys) for (otokey,vskeys) in vsdxmfdict_r.items()]
#缺失的开头音用空白音频
begins=[]
print("====开头音====")
for C in (Cs|Vs)-{""," "}:
    if(not(" "+C in vsdxmfdict)):
        print("开头音"+" "+C)
        begins.append(" "+C)
if(begins!=[]):
    vsdxmf.append([begins,"empty.wav",1100,1300,1400,1500,1200])

#输出vsdxmf文件
with open(otopath.replace("oto.ini","main.vsdxmf"),"w",encoding="utf8") as vsdxmffile:
    for value in vsdxmf:
        names=value[0]
        value[0]=names[0]
        value=[str(i) for i in value]
        vsdxmffile.write(",".join(value)+"\n")
        for name in names[1:]:
            vsdxmffile.write("{},#{},0,0,0,0,0\n".format(name,names[0]))

#for i in lsddict.items():
#    print(i)
#    input()
