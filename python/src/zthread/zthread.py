from threading import Thread
import time

def mytimer(name, delay, repeat):
    print('Timer: ' + name + ' started')
    while repeat > 0:
        time.sleep(delay)
        print(name + ': ' + time.ctime(time.time()))
        repeat -= 1
    print('Timer: ' + name + ' completed')

def main():
    t1 = Thread(target = mytimer, args = ('Timer1', 1, 10))
    t2 = Thread(target = mytimer, args = ('Timer2', 2, 5))
    t1.start()
    t2.start()
    print('main completed')

if __name__ == '__main__':
    main()
