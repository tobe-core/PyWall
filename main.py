import os, sys, json, random

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'config.json')

with open(json_path, 'r') as f:
    configs = json.load(f)
    f.close()

def help_text():
    print("PyWall Help\n")
    print("help    - Shows this text.")
    print("save    - Save a new wallpaper to the list of wallpapers.")
    print("remove  - Removes a wallpaper from the list of wallpapers.")
    print("random  - Changes the wallpaper randomly from the list of wallpapers.")
    print("list    - Shows all the wallpapers saved.")
    print("type    - Changes the transition type. (\"grow\" by default)")
    print("step    - Changes how many steps has the transition. (\"30\" by default)")

if (len(sys.argv) < 2):
    help_text()
    exit()
else:
    if (sys.argv[1] == "help"):
        help_text()
        exit()
    elif (sys.argv[1] == "save"):
        with open(json_path, 'w') as f:
            configs["wallpapers"].append(sys.argv[2])
            json.dump(configs, f)
            f.close()
        exit()
    elif (sys.argv[1] == "remove"):
        configs["wallpapers"].remove(str(sys.argv[2]))
        with open(json_path, 'w') as f:
            json.dump(configs, f)
            f.close()
        exit()
    elif (sys.argv[1] == "random"):
        os.system("swww img --transition-type " + configs["type"] + " --transition-step " + configs["step"] + " " + configs["path"] + random.choice(configs["wallpapers"]))
        exit()
    elif (sys.argv[1] == "list"):
        for walls in configs["wallpapers"]:
            print(f"- {walls}")
        exit()
    elif (sys.argv[1] == "type"):
        with open(json_path, 'w') as f:
            configs["type"] = str(sys.argv[2])
            json.dump(configs, f)
            f.close()
        exit()
    elif (sys.argv[1] == "step"):
        with open(json_path, 'w') as f:
            configs["step"] = str(sys.argv[2])
            json.dump(configs, f)
            f.close()
        exit()
    else:
        help_text()
        exit()
