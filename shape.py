def sphere_volume(radius):
    pi = 3.14159 
    return (4.0 / 3) * pi * (radius ** 3)
R = float(input()) 

volume = sphere_volume(R)

print(f"VOLUME = {volume:.3f}")
