#!/usr/bin/python3

# Note
print('Enter numbers like this:')
print('rgb X Y Z')
print('#XYZABC' + '\n')

# Conversions
def rgb_to_hex(rgb):
    res = [int(i) for i in rgb.split() if i.isdigit()]
    if len(res) == 3: 
        h = '#%02x%02x%02x' % (res[0], res[1], res[2])
        print(rgb + ' == ' + h)

def hex_to_rgb(hex):
    h = hex.lstrip('#')
    print(hex + ' == rgb', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

# Read values to convert
f = open("convert.txt", "r")
lines = f.readlines()

# Convert & display read values
for line in lines:
    if line[0:3] == 'rgb':
        rgb_to_hex(line.strip())
    elif line[0:1] == '#': 
        hex_to_rgb(line.strip())