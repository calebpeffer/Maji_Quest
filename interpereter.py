
import sys
import json
from event import Event

def verify_input(input: list, valid_input: set()):
    if len(input) == 1: 
        try:
            action = valid_input[str(input)]
            sucsess = True
        except KeyError:
            print("options: %s" % valid_input.keys())
            sucsess = False
    return sucsess
def end(current_event):
    return (current_event, False)
def look(current_event, specific_item = None):
    if specific_item != None:
        print(specific_item.full_description)
    else:
        print(current_event.description)
    return (current_event, True)
        
# def timeout_query(current_event):
#     print("are you still there?, if you wan't to quit, enter 'end', cast me.morti() or ^c in your terminal")
#     #print("actions: %s, or %s", current_event, 


def casting_interpereter():
    pass
def move(current_event, target = None):
    target = str(target)
    print(target)
    print(current_event.correspondingEvents)
    if target == None or target not in current_event.correspondingEvents:
        print("you havn't selected where you would like to move, or your selection is invalid. options %s" % (current_event.correspondingEvents))
        return (current_event, True)
    else:
        current_event = create_event(events, target)
        return (current_event, True)
        
def create_event(events, name):
    #print(events)
    event = events[name]
    return Event(correspondingEvents = event["correspondingEvents"], objects = event["objects"], characters = event["characters"], name = event["name"], description = event["description"])

def main():
    # print("Your eyes open. You stand in front of a pedastle covered with a black shrowd. Upon the pedastle there lies a straw doll with a rough canvas robe. Its robes are covered in thin black text that you cannot decipher")
    world_name = sys.argv[1]
    try:
        with open(world_name, "r") as f:
            script = f.read()
            global events
            events = json.loads(script)
    except:
        #print("the world file specified does not exist, please choose a different script file (usage, python interpereter.py <scriptfile.json>)")
        sys.exit()

    switcher = {
        "look": look, 
        "end": end,
        "move": move
    }
    event = create_event(events, "portal_room")
    cont = True
    while cont == True:
        print(event.description)
        user_input = input(">>>")
        arguments = user_input.lower().split(" ")
        if len(arguments) == 1:
            func = switcher[arguments[0]]
            (event, cont) = func(event)
        else:
            func = switcher[arguments[0]]
            (event, cont) = func(event, arguments[1])

if __name__ == "__main__":
    main()