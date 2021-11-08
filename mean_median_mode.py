import csv
from typing import Counter

with open('data.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

new_data=[]

for i in range(len(file_data)):
    n_num=file_data[i][2]
    new_data.append(float(n_num))

n=len(new_data)


def mean():
    total=0
    for x in new_data:
        total+=x

    mean=total/n

    print("Mean/Average is: "+str(mean))

def median():
    new_data.sort()

    if(n%2==0):
        median1=float(new_data[n//2])
        median2=float(new_data[n//2-1])

        median=(median1+median2)/2

    else:
        median=float(new_data[n//2])

    print("Median is: "+str(median))    


#Mode Function not completed
def mode():
    data=Counter(new_data)
    mode_data_for_range={
        "70-80":0,
        "80-90":0,
        "90-100":0,
        "100-110":0,
        "110-120":0,
        "120-130":0,
        "130-140":0,
        "140-150":0,
        "150-160":0,
        "160-170":0,
        "170-180":0
    }
    for weight,occurence in data.items():
        if 70<float(weight)<80:
            mode_data_for_range["70-80"]+=occurence
        elif 80<float(weight)<90:
            mode_data_for_range["80-90"]+=occurence
        elif 90<float(weight)<100:
            mode_data_for_range["90-100"]+=occurence
        elif 100<float(weight)<110:
            mode_data_for_range["100-110"]+=occurence
        elif 110<float(weight)<120:
            mode_data_for_range["110-120"]+=occurence
        elif 120<float(weight)<130:
            mode_data_for_range["120-130"]+=occurence
        elif 130<float(weight)<140:
            mode_data_for_range["130-140"]+=occurence
        elif 140<float(weight)<150:
            mode_data_for_range["140-150"]+=occurence
        elif 150<float(weight)<160:
            mode_data_for_range["150-160"]+=occurence
        elif 160<float(weight)<170:
            mode_data_for_range["160-170"]+=occurence
        elif 170<float(weight)<180:
            mode_data_for_range["170-180"]+=occurence

mean()
median()
mode()