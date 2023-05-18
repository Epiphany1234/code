import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up! Stay focused!")

if __name__ == "__main__":
    focus_time = int(input("请输入专注时长（以分钟为单位）："))
    focus_timer(focus_time)
