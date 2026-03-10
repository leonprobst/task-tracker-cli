import sys
import json
import datetime

def add(task):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {"id": 0, "description": task, "status": "todo", "createdAt": date, "updatedAt": date}

    #Checks if json exists
    try:
        with open("tasks.json", "r") as json_file:
            loaded = json.load(json_file)
            data["id"] = loaded.get("todos")[-1].get("id") + 1
            loaded.get("todos").append(data)
        with open("tasks.json", "w") as json_file:
            json.dump(loaded, json_file, indent=4)
            return
    except IOError:
        pass
    #Creates new json if it doesn't exist
    with open("tasks.json", "w") as json_file:
        json.dump({"todos": [data]}, json_file, indent=4)
        print("test3")

if __name__ == "__main__":
    operation = sys.argv[1]
    if operation == "add":
        add(sys.argv[2])
    elif operation == "update":
        print("update")
    elif operation == "delete":
        print("delete")
    elif operation == "mark-in-progress":
        print("mark in progress")
    elif operation == "mark-done":
        print("mark-done")
    elif operation == "list":
        print("list")
    else: print("Unknown Operation!")