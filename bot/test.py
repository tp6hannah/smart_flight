from main import Main as Main
data = Main.get_flight('我要一張2017 10月8號從台北到西雅圖的機票')
for row in data[0]:
    print(row)
    print(data[1])
    

