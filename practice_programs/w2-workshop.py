requests = [
    ["Aisha", "Vegetarian hamper", "prefers rice and lentils"],
    ["Ben", "Needs Gluten Free items and baby formula"],
    ["Mira", "Halal food prefered pickup after 4 pm."],
    ["Noah", "Forgot what he wanted."]
]

print(f"{requests[-2][0]}'s request says: {requests[-2][1]}")

requests[1] = ["Ravi", "Needs dairy-free hamper and baby formula"]


# print(f"{requests[1][0]}'s request says: {requests[1][1]}")

# #for request in requests:
#     #print(f"Pickup ready for {request[0]}")

# for i in range(0,len(requests)):
#     print(f"Pickup ready for {requests[i][0]}")

# input_needs = ""
# userinputs = []

# while input_needs.upper() != 'X' :
#     input_needs = input("Please enter any dietary requirements for a client (or 'X' to stop): ")
#     userinputs.append(input_needs)



while True:
    found = False
    name_request = input("Please enter a name: ")
    if name_request.upper() == 'X':
        print('Exiting code')
        break

    for name in requests:
        if name_request == name[0]:
            print(f"{requests[1][0]}'s request says: {requests[1][1]}")
            found = True
            break

    if not found:
        print('Client not found')