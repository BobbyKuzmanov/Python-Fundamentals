text = input().split(", ")
text_to_filter = input()
for word in text:
    text_to_filter = text_to_filter.replace(word, "*" * len(word))
print(text_to_filter)

# Write a program that receives a text and a string of banned words, separated by a comma and space ", ".
# All banned words in the text should be replaced with the number of asterisks "*", equal to the word's length.
# The ban list will be entered on the first input line and the text - on the second input line.
#
# Input:
# Linux, Windows
# It is not Linux, it is GNU/Linux. Linux is merely the kernel,
# while GNU adds the functionality.
# Therefore we owe it to them by calling the OS GNU/Linux!
# Sincerely, a Windows client
#
# Output:
# It is not *****, it is GNU/*****. ***** is merely the kernel,
# while GNU adds the functionality.
# Therefore we owe it to them by calling the OS GNU/*****!
# Sincerely, a ******* client
