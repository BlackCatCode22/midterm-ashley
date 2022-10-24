# ashleyMidterm.py
# 10/18/2022

nameOfFile = "listOfEmailsSent.txt"
# Open up our file being used
handle = open(nameOfFile)

# set accumulator to 0
# An accumulator "accumulates" the desired amount to the variables initial value. Here, the initial value is 0, and
# later we will be adding, subtracting, multiplying, dividing, totaling, etc. some amount to adjust this value based
# on our function's directions.
count = 0

# The handle came from the variable we used above to access our external file called mbox-short.txt
# (which is the relative file path). It is easier to type that variable name than to re-type the file name every time we
# need to access it for information. You can technically make the variable whatever you want it to be, but it should be
# recognizable in case you have to share your code or work with others on it. The handle is the file handler
# telling this program that we want to open the file indicated inside the nameOfFile variable. The textInEachLine is
# part of the for-loop which is in place to test the file for certain conditions and increase the counter if conditions
# meet the criteria set within the loop.
for textInEachLine in handle:
    # The [0:5] refers to the index we are searching for within the info represented by the textInEachLine variable. In
    # this case, we are mapping the first index (0) through the fourth (5). This says that if those indexes of the line
    # are equal to the string "From " then the condition of the loop is true and the program should print the info
    # directed below that if statement.
    # In this situation the decision control structure is checking to see if the specified indexes match the string
    # "From "
    if textInEachLine[0:5] == "From ":
        # The elements of a list refer to each object in a list. They could be individual letters, numbers, words, or
        # sentences. Whatever it is you are listing. They get separated by commas, whatever they are. You can sort
        # through them using their index within the list, which is called index-based traversal.
        # The split() method splits the strings for a list. You pick the separator, in this case it is the "@" symbol.
        wordsInList = textInEachLine.split()
        print()
        print("dir(list):")
        # Here, x[1] refers to the full email address in the list which will be printed due to the usage of the print
        # command.
        print(wordsInList[1])
        # Next we are re-printing the email address again, but instead of printing it like before, we are splitting the
        # email address in two at the "@" symbol. The result shows with the first half and second half separated by a
        # comma.
        separateEachEmailAddress = wordsInList[1].split('@')
        print(separateEachEmailAddress)
        prefix = separateEachEmailAddress[0]
        domain = separateEachEmailAddress[1]
        print(prefix)
        print(domain)
        # We don't use count++ because we want the value of count +1 stored back into the count variable instead of the
        # count variable remaining 0 as it was originally initialized. We want to return the increment itself vs
        # simply returning the result of the increment.
        count = count + 1

print()
print("Using our code, we find ", count, " entries/lines in our file that start with the word 'From'")

# We have to close the file up so that we are able to use it in the next section
handle.close()

print()
print("====================== Python Dictionary ======================")
print()

nameOfFile = "listOfEmailsSent.txt"
# Open up our file being used
handle = open(nameOfFile)

# Dictionary tabulates the number of messages from each sender
countMessagesFromEachSender = dict()

# Use the loop you created for prefix/domain parsing.
for textInEachLine in handle:
    if textInEachLine[0:5] == "From ":
        wordsInList = textInEachLine.split()
        separateEachEmailAddress = wordsInList[1].split('@')
        prefix = separateEachEmailAddress[0]
        domain = separateEachEmailAddress[1]
        print(prefix)
        print(domain)

        if prefix in countMessagesFromEachSender:
            print("*************")
            print()
            print(countMessagesFromEachSender[prefix], " ", prefix, " is a key in our dictionary")
            countMessagesFromEachSender[prefix] = countMessagesFromEachSender[prefix] + 1
            print()
        else:
            countMessagesFromEachSender[prefix] = 1

valueCount = None
keyCount = None
# C++ can also use two variables as loop control variables.
for key, value in countMessagesFromEachSender.items():
    if valueCount is None or value > valueCount:
        keyCount = key
        valueCount = value

print()
print("*************************")
print(keyCount, "shows with the most messages with a total of: ", valueCount)
print()
print("*************************")
print("Here we use the 'countMessagesFromEachSender' to see the following: ", countMessagesFromEachSender)
print()
print("*************************")
print("We sort the 'countMessagesFromEachSender' by keys to show: ", countMessagesFromEachSender.keys())
print()
print("*************************")
print("We sort the 'countMessagesFromEachSender' by values and we get: ",
      sorted(countMessagesFromEachSender.values()))
print()
print("*************************")
print()
print("===================Tuples in a dictionary====================")
print()
print("Key-value pairs are:")
for (myKey, myVal) in countMessagesFromEachSender.items():
    print(myKey, myVal)

print()
print("Now here is the same info, but printed in tuples form: ")
tuples = countMessagesFromEachSender.items()
print(tuples)

# Close it up again for easier re-use
handle.close()

print("====================== Advanced ========================")

nameOfFile = "listOfEmailsSent.txt"
# Open up our file being used
handle = open(nameOfFile)

countMessagesFromEachSender = dict()

for textInEachLine in handle:
    if textInEachLine[0:5] == "From ":
        wordsInList = textInEachLine.split()
        whoSent = wordsInList[1]
        # This line of code is trying to count the occurrences of each sender using the 'get' function instead.
        # It uses a variable that is initialized with the value that is created by 'getting' the sender name and adding
        # it to the list.
        countMessagesFromEachSender[whoSent] = countMessagesFromEachSender.get(whoSent, 0) + 1

# For-loop that looks through our dictionary and finds the sender and if they sent the most messages
valueCount = None
keyCount = None
# C++ can also use two variables as loop control variables.
for (key, value) in countMessagesFromEachSender.items():
    if valueCount is None or value > valueCount:
        keyCount = key
        valueCount = value

print("Most messages are by: ", keyCount, valueCount)
print()
# Here we print the output from the dictionary.
print("The countMessagesFromEachSender shows like this : ", countMessagesFromEachSender)
print()
# Here we print the dictionary output showing the keys, sorted by key
print("The keys, sorted by key, from countMessagesFromEachSender shows like this: ",
      sorted(countMessagesFromEachSender.keys()))
print()
# Here we print the output from the the dictionary that shows our values, sorted by value
print("The values, sorted by value, from countMessagesFromEachSender shows like this: ",
      sorted(countMessagesFromEachSender.values()))
print()
# Key-value pairs sorted by key
# For-loop looking through dictionary, in order, sorted by key
# We use parentheses around k1,k2 for added clarity
print("Sorted by key: ")
for (k1, k2) in sorted(countMessagesFromEachSender.items()):
    print(k1, k2)

# Print/sort dictionary's key-value pairs by descending value
print()
print("********************")
print("Sorted by value: ")
temporaryList = list()
for (k1, k2) in countMessagesFromEachSender.items():
    # Reversal of the value/key order.
    temporaryList.append((k2, k1))
temporaryList = sorted(temporaryList, reverse=True)
print(temporaryList)
print()
# Listing of tuples
print("Sorted by value, but in tuple form: ")
for tuple2 in temporaryList:
    print(tuple2)

# Close the file so it can be re-used
handle.close()
