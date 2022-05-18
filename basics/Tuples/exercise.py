# Exercise
emojis = {
    ":)": '😊',
    ":(": '😒'
}

message = input("> ")
sp_message = message.split(" ")
new_message = ""
if ":)" in message or ":(" in message:
    for msg in sp_message:
        if msg == ":)" or msg == ":(":
            new_message += " "+emojis.get(msg, "none")
        else:
            new_message += " "+msg
else:
    new_message = message

print(new_message)
