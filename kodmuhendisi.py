import time
start = time.time()
katlar = []
for i in range(1000):
    if i%3==0 or i%5==0:
        katlar.append(i)
print(sum(katlar))
finish = time.time()
print(f"Toplam Süre: {str(finish-start)}")