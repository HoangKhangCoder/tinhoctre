cam = int(input())
dino = int(input())
days = int(input())
if days > cam:
    cam, dino = 0, dino + cam
else:
    cam, dino = cam - days, dino + days
print(abs(cam - dino))