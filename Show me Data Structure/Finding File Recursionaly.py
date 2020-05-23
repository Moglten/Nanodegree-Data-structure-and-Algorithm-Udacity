import  os

def flattenlist(arr):
    flat = []
    for elem in arr :
        if type(elem) is list :
            flat.extend(flattenlist(elem))
        elif elem is not None :
            flat.append(elem)
    return flat

def find_files(suffix, path):
    """
       Find all files beneath path with file name suffix.

       Note that a path may contain further subdirectories
       and those subdirectories may also contain further subdirectories.

       There are no limit to the depth of the subdirectories can be.

       Args:
         suffix(str): suffix if the file name to be found
         path(str): path of the file system

       Returns:
          a list of paths
       """
    if len(suffix) == 0 or len(path) == 0:
        return None
    if os.path.isdir(path):
        path = flattenlist(finder_file(suffix,path))
    else:
        return None
    return path

def finder_file(suff,path):
    path_of_suffix = []

    if os.path.isfile(path) and path.endswith(suff):
            return path

    elif os.path.isdir(path):
        extend = os.listdir(path)
        if len(extend) != 0:
            for elem in extend:
                paths = finder_file(suff,path+"/{}".format(elem))
                path_of_suffix.append(paths)
            return path_of_suffix

print(find_files(".c" , "testdir"))     #right test case
print(find_files(".h" , "testdir"))     #other right test case
print(find_files("" , "testdir"))       #empty suffix return None
print(find_files(".c" , ""))            #empty path return None
print(find_files(".c" , "i ma"))        #dir not exist return None
print(find_files(".8","testdir"))       #suffix not exist return empty list
