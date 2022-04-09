import sys, time


# 进度条
def progress_bar():
    for i in range(1, 101):
        print("\r", end="")
        print("Download progress: {}%: ".format(i), "▋" * (i//2), end="")
        sys.stdout.flush()
        time.sleep(0.05)
        
progress_bar()