def print_directory_contents(path_current):
    import os                                       
    for path_sub in os.listdir(path_current):                
        path_sub_child = os.path.join(path_current, path_sub)
        if os.path.isdir(path_sub_child):
            print_directory_contents(path_sub_child)
        else:
            print(path_sub_child)
