from datetime import datetime

final_diary =''
diary_dict = {}
with open("diary.txt", "r", encoding="utf-8") as diarys:
    contents = diarys.read()
    text = contents.split("\n\n")
    
    for t in text:
        data_diary = datetime.strptime(t[: t.index("\n")], "%d.%m.%Y; %H:%M")
        diary_dict[data_diary] = t
        
last = len(diary_dict)  
for key in sorted(diary_dict):
  if len(diary_dict[key]) != last:
    print(diary_dict[key])
    print()
  else:
    print(diary_dict[key].rstrip('\n'),end='')

