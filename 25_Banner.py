def banner(text):
    print((len(text)+4) * "*")
    print("* " + text + " *")
    print((len(text) + 4) * "*")

def banner2(text):
    reeksSterren = "****"
    aantalSterren = len(text)
    for i in range(aantalSterren):
        reeksSterren = reeksSterren + "*"

    print(reeksSterren)
    print("* " + text + " *")
    print(reeksSterren)

def banner3(text, icon):
    print((len(text)+4) * icon)
    print(f"{icon} " + text + f" {icon}")
    print((len(text) + 4) * icon)

name = input("Give a name for the banner: ")

banner(name)

banner2(name)

banner3(name, '\u2605')