from collections import namedtuple

Time = namedtuple('Time', ['hour', 'minute', 'second'])

t = Time(13, 30, 45)
print(t.hour, t.minute, t.second) 