# open as read text file containing names
with open ("names.txt") as file:
    content = file.read()

# command that will take content of previous text file and write a new text file with same names as title case
with open ("names-formatted.txt", "w") as file2:
    file2.write(content.title())
