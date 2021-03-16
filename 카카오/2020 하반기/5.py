play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

logss = []
for i in logs:
    temp = i.split('-')
    logss.append(temp)
logss.sort()

slogs = ['00:00:00']
elogs = []
for s, e in logss:
    slogs.append(s)
    elogs.append(e)
elogs.sort()
elogs.append(play_time)

index = len(logs)
sindex=0
eindex=0
count=0
logsc = []
while sindex < index or eindex < index:
    if slogs[sindex] < elogs[eindex]:
        count+=1
        sindex+=1
    else:
        count-=1
        eindex+=1
    logsc.append(count)
print(logsc)

##run_time = 
##answer = 
