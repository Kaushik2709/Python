# file = open('youtube.ext', "w")
# try:
#     file.write("This is a YouTube manager file.")
# finally:
#     file.close()

# But we have better syntax for file handeling

with open('youtube.ext', "w") as file:
    file.write("This is a YouTube manager file.")
    # print(file.read())  