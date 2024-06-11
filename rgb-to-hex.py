#!/usr/bin/python3

# Conversions
def rgb_to_hex(rgb):
    res = []
    x=rgb.split()
    for i in x:
        print(i)
        if i.isnumeric():
            res.append(int(i))
    print(res)
    print('-')

def hex_to_rgb(hex):
    h = hex.lstrip('#')
    print('rgb', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

# Read values to convert
f = open("convert.txt", "r")
lines = f.readlines()

# Convert read values
for line in lines:
    if line[0:3] == 'rgb':
        rgb_to_hex(line.strip())
    # elif line.strip(): 
        # hex_to_rgb(line.strip())

# Display converted values