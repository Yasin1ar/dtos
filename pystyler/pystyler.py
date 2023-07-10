import os

# accessing all files in a directory as a list
files = os.listdir(os.getcwd())

def restyle(file):
    '''Changes the style of a file to our preference'''
    file_name, file_suffix = file[:-4], file[-4:]
    file_name = file_name.translate(str.maketrans("._", "  "))
    return file_name + file_suffix

for file in files:
    # loops through the list and applies our preference
    if ".mkv" in file or ".mp4" in file:
        new_style = restyle(file)
        try:
            os.rename(file, new_style)
        # we don't need the old file if we already have the new one
        except FileExistsError:
            os.remove(file)
            print(file," was removed")


input("Done! press anything to quit : ")