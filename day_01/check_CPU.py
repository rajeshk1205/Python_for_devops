# aapko kaam krna h ki, user se CPU threshold lo
# current cpu usage check kro
# agar cpu usage threshold se jada h to, email trigger kr do


import psutil

def get_CPU_threshold_limit():
    user_cpu_threshold = int(input("Enter a CPU threshold: "))
    current_cpu = psutil.cpu_percent(interval=1)
    print( "Current CPU threshold: ", current_cpu)

    if current_cpu > user_cpu_threshold:
        print("The CPU is above the requested threshold")
    else:
        print("The CPU is below the requested threshold")

get_CPU_threshold_limit()