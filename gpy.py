import datetime

# Data stores
guardians, institutions, messages = [], [], []

# Register a new guardian or institution
def register_user(user_list, user_type):
    email = input(f"{user_type} Email: ")
    if any(user['email'] == email for user in user_list):
        return "Email already registered"
    user_list.append({
        "id": len(user_list) + 1,
        "name": input("Name: "),
        "email": email,
        "password": input("Password: ") if user_type == "Guardian" else None,
        "phone": input("Phone: "),
        "address": input("Address: ")
    })
    return f"{user_type} registered successfully"

# View and update guardian or institution profile
def manage_user(user_list, user_type):
    email = input(f"{user_type} Email: ")
    user = next((u for u in user_list if u['email'] == email), None)
    if not user:
        return f"{user_type} not found"
    action = input("View (1) or Update (2)? ")
    if action == '1':
        return user
    if action == '2':
        user.update({
            "name": input("Name: ") or user['name'],
            "password": input("Password: ") or user.get('password'),
            "phone": input("Phone: ") or user['phone'],
            "address": input("Address: ") or user['address']
        })
        return "Profile updated successfully"

# Send a message from guardian to institution
def send_message():
    sender_email = input("Sender Email: ")
    receiver_email = input("Receiver Email: ")
    if not any(g['email'] == sender_email for g in guardians) or not any(i['email'] == receiver_email for i in institutions):
        return "Sender or receiver not found"
    messages.append({
        "sender_email": sender_email,
        "receiver_email": receiver_email,
        "message": input("Message: "),
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return "Message sent successfully"

# View messages sent/received by a user
def view_messages():
    email = input("Email to view messages: ")
    user_messages = [m for m in messages if m['sender_email'] == email or m['receiver_email'] == email]
    for msg in user_messages:
        print(f"From: {msg['sender_email']}\nTo: {msg['receiver_email']}\nMessage: {msg['message']}\nTime: {msg['time']}\n")
    return "End of messages"

# Main program loop
if __name__ == "__main__":
    while True:
        action = input("\nChoose action:\n1. Register Guardian\n2. Manage Guardian\n3. Register Institution\n4. Manage Institution\n5. Send Message\n6. View Messages\n7. Quit\nYour choice: ")
        if action == '1':
            print(register_user(guardians, "Guardian"))
        elif action == '2':
            print(manage_user(guardians, "Guardian"))
        elif action == '3':
            print(register_user(institutions, "Institution"))
        elif action == '4':
            print(manage_user(institutions, "Institution"))
        elif action == '5':
            print(send_message())
        elif action == '6':
            print(view_messages())
        elif action == '7':
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 7.")
