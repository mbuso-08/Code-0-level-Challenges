def time_func(t):
    hours = int(t) // 60
    minutes = (t % 60 ) % 60 
    print("%d:%02d" % (hours, minutes))

print(time_func(133))
