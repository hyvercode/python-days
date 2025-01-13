# Definisi konstanta
from Color import Color


PI = 3.14159
GRAVITY = 9.8
SPEED_OF_LIGHT = 299792458

print("Nilai PI:", PI)
print("Gravitasi:", GRAVITY, "m/s^2")
print("Kecepatan Cahaya:", SPEED_OF_LIGHT, "m/s")

#Call from diferent class
print(Color.RED)          # Output: Color.RED
print(Color.RED.name)     # Output: RED
print(Color.RED.value)    # Output: 1