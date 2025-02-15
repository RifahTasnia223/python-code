print("Alphabets:", end=" ")

for ch in range(ord('a'), ord('z') + 1):
    if ch < ord('z'):
        print(chr(ch), end=", ") 
    else:
        print(chr(ch))
