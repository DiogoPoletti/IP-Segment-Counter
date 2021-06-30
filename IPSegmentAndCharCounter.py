ipAddress = input("Enter your IP address: ")

segmentCount = 1
segmentCharacters = 0
character = ''

for character in ipAddress:
    if character == '.':
        print("Segment {} has {} characters.".format(segmentCount, segmentCharacters))
        segmentCount += 1
        segmentCharacters = 0

    else:
        segmentCharacters += 1

if character != '.':
    print("Segment {} has {} characters.".format(segmentCount, segmentCharacters))

exit = input("Press ENTER to exit...")
