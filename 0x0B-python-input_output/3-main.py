#!/usr/bin/python3
write_file = __import__('3-write_file').write_file

nb_characters = write_file("my_first_file.txt", "I love Johanna!\n")
print(nb_characters)