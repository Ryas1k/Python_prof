dates = [line.strip().split(' / ') for line in sys.stdin]
new_dates = list(filter(lambda x: dates[-1][0]==x[1],dates[:-1]))
for i in sorted(new_dates,key=lambda x: (float(x[2]),x[0])):
    print(i[0])