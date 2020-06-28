For this probloem, recursion will be a good choice because it can detect and handle sub-problems. As long as it reaches a directory, it goes down a level until it finds a file. 

The time complexity is O(n) because it needs to loop all the files once where n is the number of files. 
Extra space comes from the stack space for recursion, so space complexity is O(m), where m is the number of directories and sub directories in the input path.