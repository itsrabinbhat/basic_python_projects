import time

# Countdown function
def countdown(t):
    while t:
        mins,secs = divmod(t,60)
        hrs,mins = divmod(mins,60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hrs,mins,secs)
        print(timer,end='\r')
        time.sleep(1)
        t -= 1
    print("Countdown completed!")

t = int(input("Enter time is seconds: "))
countdown(t)