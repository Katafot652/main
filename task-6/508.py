users = {
    232: "Alice",
    550: "Bob",
    190: "Jack"
}

while True:
    try:
        user_id = int(input())
        if user_id in users:
            print(f"Hi, {users[user_id]}!")
        else:
            print("Hi, to all!")
    except EOFError:
        break
