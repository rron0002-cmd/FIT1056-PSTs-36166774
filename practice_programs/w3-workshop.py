#global lists request

global_requests = []


global_requests.append( ["Aisha", "Vegetarian hamper, prefers rice and lentils."])
global_requests.append( ["Ravi", "Needs dairy-free hamper and baby formula."])
global_requests.append( ["Mira", "Halal food preferred, pickup after 4 pm."])
global_requests.append(["Noah", "Low-sugar items requested; nut allergy."])


def register_request(name, request):
    global_requests.append([name, request])
    pass


def print_request(idx):
    client = global_requests[idx]
    print(f"{client[0]}, request says {client[1]}")
    pass

def evaluate_request(idx, keyword="allergy"):
    client = global_requests[idx]
    if keyword in client[1].lower():
        print(f"Allergy note for {client[0]}")
        if "baby formula" in client[1].lower():
            return keyword + " baby formula"
        else:
            return keyword
    elif "baby formula" in client[1].lower():
        print(f"Infant supply priorty for {client[0]}")
        return "baby formula"
    else:
        print(f"{client[0]}'s request is ready to pack")
        return None

def assess_priority(idx):
    standard_client = global_requests[idx]
    priority_product = evaluate_request(idx)
    if priority_product == None and "delivery" not in standard_client[1] or priority_product == None and "pick up"  in standard_client[1]:
        print("Standard Priority - ready for normal packing")
    elif "allergy" in priority_product and "baby formula" in priority_product:
        print("High Priority")
    elif "allergy" in priority_product or "baby formula" in priority_product:
        print("Medium Priority")
    elif "delivery" in standard_client[1] or "pick up" in standard_client[1]:
        print("Medium Priority")
    


