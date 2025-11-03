# load_time = 4.2
#  Page load too slow: 4.2 seconds

load_time = float(input("Enter the page load time in seconds:"))

if load_time <= 0:
    print("Page is buffering")
elif load_time <= 3:
    print("The page is loaded sucefully")
else:
    print("The page is not loaded too slow")