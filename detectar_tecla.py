# import sys
# from msvcrt import getch
import msvcrt, time

# c = ''
# while c != 'a':
#    c = sys.stdin.read(1)

#while True:
#    key = msvcrt.getch()
#    print(key)

print('antes sleep')
time.sleep(3)
print('despues sleep')

while msvcrt.kbhit():
    # do something else while we're waiting
    print ('.'),
    time.sleep(0.1)

print ('Fin')
