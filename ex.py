parent_directory = 'path_to_parent_directory'
folder_name = 'folder_name'

for item in os.listdir(parent_directory):
    if os.path.isdir(os.path.join(parent_directory, item)) and item == folder_name:
        print("Folder shares a name with another folder")
        break
else:
    print("Folder does not share a name with another folder")
