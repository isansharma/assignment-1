import json
import matplotlib.pyplot as plt

json_file=open('week1.json')
data=json.load(json_file)

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

for k,v in view.items():
    x=sorted(v.keys())
    y=sorted(v.values())
    # print(y)
    print(k)
    print("========")
    print("TIme  "," Rooms ")
    lx = []
    ly = []
    for i in x:
        lx.append(i)
        ly.append(v[i])
        print("{} \t {}".format(i,v[i]))
    plt.bar(lx,ly,label=k)
    plt.legend()
    plt.xlabel('time')
    plt.ylabel('Available room')
    plt.title('My Graph')
    plt.show()
    print()


