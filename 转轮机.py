import re

table=[2,3,7,5,13,12,9,1,8,10,4,11,6]   #密钥
Ciphertext='NFQKSEVOQOFNP'  #密文
with open(r'F:\github\CTF\aa.txt','r') as f:    #转轮机
    data=f.read()

#转轮机根据table重新排列
def wheel_decode(data,table):
    resultList=[]
    pattern = re.compile('[A-Z]{26}')
    result = pattern.findall(data)

    for i in table:
        resultList.append(result[i-1])
    return resultList

resultList = wheel_decode(data,table)



#根据密文重新排列
def rearrange(List,Ciphertext):
    resultList=[]
    for i in range(0,13):
        resultList.append(List[i][List[i].find(Ciphertext[i]):]+List[i][:List[i].find(Ciphertext[i])])
    return resultList
resultList= rearrange(resultList,Ciphertext)


def rearrange2(List):
    resultList=[]
    s=''
    for i in range(0,26):
        for j in List:
            s += j[i]

        resultList.append(s)
        s=''
    return resultList

resultList = rearrange2(resultList)
for i in resultList:
    print(i)