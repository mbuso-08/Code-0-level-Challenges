time=133

hours = int(time) // 60
minutes = (time % 60 ) % 60 

print("%d:%02d" % (hours, minutes))

