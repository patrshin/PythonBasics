import re
line = "Sikrosky Aircrafts 2061"
regex = re.compile("(Sikorsky Aircrafts) (\d{4})")
if regex.search(line):
    print(line)
