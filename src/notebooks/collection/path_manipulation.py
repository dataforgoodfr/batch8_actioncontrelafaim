def get_to_root(level_of_file, path):
    rootpath_list = path.split('\\')[:-level_of_file]
    return "\\".join(rootpath_list)