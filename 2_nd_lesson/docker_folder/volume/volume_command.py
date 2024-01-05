# File: env_command.py

data = "This is some data to be saved."

with open("/data/data.txt", "w") as file:
    file.write(data)
    print("Data saved to /data/data.txt")