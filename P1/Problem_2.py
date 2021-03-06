import os 

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
    if not os.path.isdir(path):
        if os.path.isfile(path) and path.endswith(suffix):
            return [path]
        return []
    
    files = os.listdir(path)
    
    res = []
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            res += find_files(suffix, file_path)
        if os.path.isfile(file_path) and file_path.endswith(suffix):
            res.append(file_path)
        
    return res



# Test 1
print(find_files('.c', 'testdir'))


# Test 2
print(find_files('.h', 'testdir'))


# Test 3
print(find_files('.c', 'dir'))