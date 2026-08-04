requests = [
    ["Aisha", "Vegetarian hamper", "prefers rice and lentils"],
    ["Ben", "Something.","Something" ],
    ["Mira", "Halal food prefered", "pickup after 4 pm."],
    ["Noah"]
]

print(f"{requests[-2][0]}'s request says: {requests[-2][1]}")

requests[1] = ["Ravi", "Needs dairy-free hamper and baby formula"]


print(f"{requests[1][0]}'s request says: {requests[1][1]}")
