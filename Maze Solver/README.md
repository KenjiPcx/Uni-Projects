# Where do I put my files?

You should store all of your Java source files in the `src` directory, or subdirectories within the `src` directory.

You should store any graphics files (e.g. `.jpg`) or other non source-code resources in the `resources` directory, or subdirectories within the `src` directory.

# How to compile/run the code

```
$ cd comp16412-coursework-1_username
$ ./javac.sh src/MazeApplication.java  
$ ./java.sh MazeApplication
```

Note that in the above example, on line 3, the name of the class file to run (`MazeApplication`) is **NOT** prefixed with the source path.

