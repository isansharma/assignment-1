import json
import matplotlib.pyplot as plt


def read(file_name):
    json_file = open(file_name)
    data = json.load(json_file)
    view={'Monday':{},'Tuesday':{},'Wednesday':{},'Thursday':{},'Friday':{}}

    for p in data:
        temp=0
        for k,v in p[2]['conference-categories-count'].items():
            temp=temp+v
        if p[0]['dow']=='Monday':
            view['Monday'][p[1]['time']]=temp
        elif p[0]['dow']=='Tuesday':
            view['Tuesday'][p[1]['time']] = temp
        elif p[0]['dow']=='Wednesday':
            view['Wednesday'][p[1]['time']] = temp
        elif p[0]['dow']=='Thursday':
            view['Thursday'][p[1]['time']] = temp
        elif p[0]['dow']=='Friday':
            view['Friday'][p[1]['time']] = temp
    return view


def extract(key,view):
    lx = []
    ly = []
    for k,v in view.items() :
        x=sorted(v.keys())
        y=sorted(v.values())

        for i in x:
            if k==key:
                lx.append(i)
                ly.append(v[i])
    return [lx,ly]


def plot(week1,week2,key):
    x1,y1=week1
    x2,y2=week2
    plt.plot(x1,y1,label='week1')
    plt.plot(x2,y2,label='week2')
    plt.xlabel('Time')
    plt.ylabel('Rooms')
    plt.title(key)
    plt.legend()
    plt.show()

dow=['Monday','Tuesday','Wednesday','Thursday','Friday']
day1=input("Please choose a Day of the Week to compare \n Monday,Tuesday,Wednesday,Thursday,Friday \n")
day=day1.title()
if day in dow:
    view1=read('week1.json')
    week1=extract(day,view1)
    view2=read('week2.json')
    week2=extract(day,view2)
    plot(week1,week2,day)
else:
    print("You Choose a wrong Day")


