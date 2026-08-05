import time
minutes = int(input("Enter test minutes: "))
seconds = int(input("Enter test seconds: "))
t = (minutes * 60) + seconds
while 1:
  if t<=0 or seconds>59:
   print("Invalid test duration.")
   break
  if t > 300:
    print("Safety limit exceeded! Test duration capped to 05:00")
    t=300
  while(t>0):
      m=t//60
      s=t%60
      if(t>30):
        print(f"POWER ON | Remaining: {m}:{s}",end="\r",flush=True)
        time.sleep(1)
      elif(t<=30 and t>10):
        print(f"STABILIZING SYSTEM | Remaining: {m}:{s}",end="\r",flush=True)
        time.sleep(1)
      elif(t<=10):
        print(f"COOLDOWN PHASE | Do not touch | {m}:{s}  ",end="\r",flush=True)
        time.sleep(1)
      t=t-1
  if(t==0):
    print("\r",end="",flush=True)
    print("Power test completed successfully.  ")
    break

      
