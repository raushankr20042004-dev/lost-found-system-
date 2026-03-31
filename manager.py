import json

FILE = "data.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {"lost": [], "found": []}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_lost_item(name, desc):
    data = load_data()

    data["lost"].append({
        "name": name.lower(),
        "desc": desc.lower()
    })

    save_data(data)
    print("Lost item recorded!")

def add_found_item(name, desc):
    data = load_data()

    data["found"].append({
        "name": name.lower(),
        "desc": desc.lower()
    })

    save_data(data)
    print("Found item recorded!")

def find_matches():
    data = load_data()

    print("\nPossible Matches:")

    for lost in data["lost"]:
        for found in data["found"]:
            if lost["name"] in found["name"] or found["name"] in lost["name"]:
                print(f"\nLost: {lost['name']} | Found: {found['name']}")
