import json
import datetime
import sys
from main import meetAutomation

# todayClasses = None
finishedCount = 0

def readJson():
    try:
        json_open = open("class_data.json","r")
        json_load = json.load(json_open)
        classTimes = json_load["data"]["class_time"]
        myClasses = json_load["data"]["myClasses"]
        return classTimes, myClasses,True
    except FileNotFoundError:
        print('ファイルが見つかりません')
        return None, None, False
    

def getTodayClasses(dayOfweek, myClasses):
    todayClasses = None
    for day in myClasses:
        if day == dayOfweek:
            todayClasses = myClasses[day]
            return todayClasses
        
def makeDatetime(now, time):
    time = time.split(":")
    classObj = now.replace(hour=int(time[0]),minute=int(time[1]))
    # print(classObj)
    return classObj
    
def countFinishedClasses(day,myClasses):
    end = False
    count = 0
    for item in myClasses:
        if day == item:
            end = True
        if day != item and not end:
            count = count + len(myClasses[item])
    return count
        # if end:
        #     break
        # if day == item:
        #     end = True
        #     return
        # if day != item:
        #     print(item)
        #     count += len(myClasses[item])
        #     return count
            

def nextClass(classTimes,todayClasses,now):
    classTmp = now
    linkTmp = ""
    exist = False
    count = 0
    print(todayClasses)
    for item in todayClasses:
        print(item)
        classDatetime = makeDatetime(now, classTimes[item])
        if now < classDatetime and not exist:
            classTmp = classDatetime
            linkTmp = todayClasses[item]
            exist = True
        elif now > classDatetime and exit:
            count = count + 1
            
    if not exist:
        return classTmp,linkTmp, count,exist
    
    return classTmp,linkTmp,count,exist
    
    # for item in myClasses:
    #     global finishedCount
    #     finishedCount = finishedCount + len(myClasses[item])
    #     print(len(myClasses[item])
        
        

now_dt = datetime.datetime.now()
dayOfweek = now_dt.strftime("%A")
print(f'today:{dayOfweek}')


classTimes, myClasses,isSuccess = readJson()
if not isSuccess:
    sys.exit()

todayClasses = getTodayClasses(dayOfweek, myClasses)
# print(todayClasses)

# makeDatetime(now_dt, "13:00")

finishedCount = countFinishedClasses(dayOfweek, myClasses)
# finishedCount = countFinishedClasses("Friday", myClasses)
print(finishedCount)

# print(nextClass(classTimes, todayClasses, now_dt))
nextClass,nextLink,todaysfinishedCount,isExist = nextClass(classTimes, todayClasses, now_dt)

if isExist is False:
    print('今日の授業は終了しました')
else:
    print('次の授業')
    print(nextClass)
    print(nextLink)
    print('----------')
    print(f'今日の終了数{todaysfinishedCount}')

finishedCount = finishedCount + todaysfinishedCount
print(f'合計終了数{finishedCount}')


# 終わった授業の数で次に参加する授業を指定する
# 手順
# 今日の時間割を取得
# 次の授業を探す datetime obj 比較
# finishedCountにそれまでの授業数を足す
# finishedCountを配列になっているDOM要素にアクセスするために使う
if not nextLink == "":
    meetAutomation(nextLink)


    




