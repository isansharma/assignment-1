import json

json_file=open('week1.json')
data=json.load(json_file)
print(type(data))
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
    print("{}===>{}".format(k,v))



