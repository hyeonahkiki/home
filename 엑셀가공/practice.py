import csv
file = open('rowdata.csv', 'r')
reader = csv.reader(file)
# 가 업체의 물량
cnt1 = 0
# 나 업체의 물량
cnt2 = 0
# 다 업체의 물량
cnt3 = 0
for line in reader:
