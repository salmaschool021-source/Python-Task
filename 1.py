import random
posture = random.choice(["sitting", "standing"])
3
direction = random.choice(["left", "right", "facing"])
distance = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Start State -> Posture: {posture}, Direction: {direction}, Distance: {distance}")
if posture=="sitting":
    print("Nexus stands up")
    print("Nexus is now standing up")

elif posture=="standing":
    print("Nexus is standing up")
if direction=="facing":
    print("Nexus is facing the door")
elif direction=="left" or direction=="right":
    print("Nexus turns to the door")
    print("Nesus is now facing the door")
while(distance != 0):
    print(f"Moving... {distance} steps left")
    distance=distance-1
print("Nexus arrived!!")