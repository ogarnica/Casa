import winsound
dur = 1000
for x in range(500, 10000, 10):
    freq = x
    winsound.Beep(freq, dur)