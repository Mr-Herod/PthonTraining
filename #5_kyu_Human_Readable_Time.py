Description:

"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)
You can find some examples in the test fixtures.

"""

My codes:

def make_readable(seconds):
    s = ""
    sc = seconds%60
    sm = int((seconds%3600)/60)
    sh = int((seconds-(sm*60+sc))/3600)
    if sh<10:
        s +="0" + str(sh)+":"
    else:
        s += str(sh)+":"
    if sm < 10:
        s +="0" + str(sm)+":"
    else:
        s +=str(sm)+":"
    if sc < 10:
        s +="0" + str(sc)
    else:
        s += str(sc)
    return s

Others codes:

def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

def make_readable(seconds):
    return "{0:02d}:{1:02d}:{2:02d}".format(seconds / 3600, seconds / 60 % 60, seconds % 60)
