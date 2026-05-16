
documents = {
    'name': "documents",
    'type': "folder",
    'children': [
        {
            'name': "notes.txt",
            'type': "file"
        }
    ]
}

downloads = {
    'name': "downloads",
    'type': "folder",
    'children': []
}

pictures = {
    'name': "pictures",
    'type': "folder",
    'children': []
}

home = {
    'name': "home",
    'type': "folder",
    'children': [documents, downloads, pictures]
}

def dict_traverse(node, indent=0):
    print(' ' * indent + node['name'])
    if node['type'] == 'folder':
        for child in node['children']:
            dict_traverse(child, indent + 2)

def add_file(folder, file_name):
    if folder['type'] == 'folder':
        folder['children'].append({
            'name': file_name,
            'type': "file"
        })

add_file(pictures, "screenshot.png")

dict_traverse(home)

def find_folder(node, folder_name):
     if node['type'] == 'folder' and node['name'] == folder_name:
        return node
     else:
        if node['type'] == 'folder':
            for child in node['children']:
                    result = find_folder(child, folder_name)
                    if result is not None:
                        return result 
        return None