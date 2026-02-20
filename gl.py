d = 1
m = 1
estimate = 1
prev = 1
while True: 
    d += 2
    m *= -1
    estimate += 1/(m * d)
   # print(d, m, estimate * 4)
    if (abs(estimate * 4 - prev * 4)) < 1e-6: break 
    prev = estimate # after running estimate so they're not the same
print(d) # iterations 