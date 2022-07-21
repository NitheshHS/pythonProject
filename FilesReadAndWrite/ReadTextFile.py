# jabber = open("Jabberwocky.txt", 'r')
#
# for line in jabber:
#     print(line.strip())
#
# jabber.close()

#Reading file with operator
with open("Jabberwocky.txt", 'r') as jabber:
    for line in jabber:
        print(line.rstrip())