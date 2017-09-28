from life import Life
import time

cgl = Life(45, 80, '#', '.')

print(cgl, "\n")
i = 0
while i < 22:
    i += 1
    cgl.update()
    time.sleep(1)
    print(cgl)
print('done')
