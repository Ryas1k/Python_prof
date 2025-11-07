import sys

l = list()
dates = [line.strip() for line in sys.stdin]
topic = dates[-1]
for line in dates[:-1]:
    news,category,reliability = line.split('/')
    if category.strip() == topic:        
        l.append((news.strip(),reliability.strip()))  
        
l1 = sorted(list(map(lambda x: [x[0],float(x[1])],l)),key=lambda x: x[1]) 
for i in range(len(l1)-1):
    if l1[i][1] == l1[i+1][1]:        # сравниваем в лексикографическом порядке
        if l1[i][0] > l1[i+1][0]:
            l1[i][0], l1[i+1][0] = l1[i+1][0], l1[i][0]    
for x in l1:
    print(x[0],sep='\n')