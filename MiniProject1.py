#Mini Project – Countdown Timer (with 1-second gap)
#Print a countdown before something “exciting” happens (like “Launching...” or
#“Happy New Year!”).

import time
count = int(input("Enter the counter timer:"))
print("\nThe countdown starts now:")

for i in range(count, 0, -1):
    print(i)
    time.sleep(2)

print("\nHappppyyyyyy Birthdayyyyyyy")    