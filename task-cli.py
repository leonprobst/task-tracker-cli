import sys
import json
import datetime

date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    with open("tasks.json", "r") as json_file:
        loaded = json.load(json_file)
except IOError:
    pass

def add(task):
    global date
    data = {"id": 0, "description": task, "status": "todo", "createdAt": date, "updatedAt": date}
    try:
        data["id"] = loaded.get("todos")[-1].get("id") + 1
        loaded.get("todos").append(data)
        with open("tasks.json", "w") as json_file:
            json.dump(loaded, json_file, indent=4)
        return
    except:
        pass
    
    #Creates new json if it doesn't exist
    with open("tasks.json", "w") as json_file:
        json.dump({"todos": [data]}, json_file, indent=4)

def update(id, task):
    global date
    found = False

    for i in loaded.get("todos"):
        if i.get("id") == int(id):
            found = True
            i.update({"description": task, "updatedAt": date})
            break

    if not found:
        print("ID not found!")
        return

    with open("tasks.json", "w") as json_file:
        json.dump(loaded, json_file, indent=4)
        return

def delete(id):
    found = False
    for i in loaded.get("todos"):
        if i.get("id") == int(id):
            found = True
            loaded.get("todos").remove(i)

    if not found:
        print("ID not found!")
        return

    with open("tasks.json", "w") as json_file:
        json.dump(loaded, json_file, indent=4)
        return

def mark(id, marktask):
    global date
    found = False
    for i in loaded.get("todos"):
        if i.get("id") == int(id):
            found = True
            i.update({"status": marktask, "updatedAt": date})
            break

    if not found:
        print("ID not found!")
        return

    with open("tasks.json", "w") as json_file:
        json.dump(loaded, json_file, indent=4)
        return

def list(status=None):
    for i in loaded.get("todos"):
        if status is None:
            print(i)
        elif status == "todo" or status == "in progress" or status == "done":
            if i.get("status") == status:
                print(i)
    return


if __name__ == "__main__":
    operation = sys.argv[1]
    if operation == "add":
        add(sys.argv[2])
    elif operation == "update":
        update(sys.argv[2], sys.argv[3])
    elif operation == "delete":
        delete(sys.argv[2])
    elif operation == "mark-in-progress":
        mark(sys.argv[2], "in progress")
    elif operation == "mark-done":
        mark(sys.argv[2], "done")
    elif operation == "list":
        list(sys.argv[2])
    else: print("Unknown Operation!")