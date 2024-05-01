emoji = {
    ":)": "😊",
    ":(": "☹️",
    ":D": "😂",
    ":3": "😺"
}

message = input("Emoticon to Emoji!\n> ")

emoji_message = [emoji.get(emoticon, emoticon) for emoticon in message.split()]

print(" ".join(emoji_message))