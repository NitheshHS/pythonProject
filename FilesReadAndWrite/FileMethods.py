# with open("Jabberwocky.txt") as jabber:
#     text = jabber.read()
#
# print(text)

# readlines
# with open("Jabberwocky.txt") as jabber:
#     lines = jabber.readlines()
#     print(lines)

#readline
with open("Jabberwocky.txt") as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if "Lewis Carroll" in line:
            break

