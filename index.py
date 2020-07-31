# Imports:
import requests, json, time

# View MojangAPI related stuff here: https://wiki.vg/Mojang_API
# Please note the API has a rate limit of 600 requests in a 10 minute interval.
# Also note that names written to the output file might have a block, this can only be checked manually.

try:
    # Open unclaimed words dump file for appending:
    unclaimedFile = open("unclaimed.txt", "a")

    # Open words dump file for reading:
    wordFile = open("words.txt", "r")
    wordArray = wordFile.readlines()

    # Print some useful info:
    print("[INFO] {0} words were read from the provided file.".format(len(wordArray)))
    print("[INFO] Starting checks. You will be notified when an account is added to the unclaimed file.")

    # Loop over each line in word array:
    for x in range(len(wordArray)):

        word = wordArray[x].strip()
        response = requests.get("https://api.mojang.com/users/profiles/minecraft/{0}".format(word))
        if response.status_code == 204:
            print("[INFO] {0} is not taken.".format(word))
            unclaimedFile.write(word + ",")

        # Sleep for one second (Only lower if your list is short):
        time.sleep(1)

    # Finish up:
    print("[INFO] All names have been checked.")
    unclaimedFile.close()

except Exception as e:
    print('[INFO] An unexpected error occured. Words file might be corrupt.')

exit()