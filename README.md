# BFS and Bellman-Ford GPU Implementations

```
NOTE: These were all compiled using nvcc 9.0 and g++ 6.4
NOTE: The python version used was 2.7.14
```

The following is include in this folder:
```
BFS <- this contains the code for the Breadth-First Search algorithm
BellmanFord <- this contains the code for the Breadth-First Search algorithm
```

# BFS
The BFS folder contains the build directory, data directory and src directory
I have also include the bin directory.  If you would like to recompile, there
is a MakeFile in the build directory.
Within the data, directory I have three files. 
britegen.py generates the data set
nodeFile.txt is used by britegen.py
dataFile.txt is used by the main program.

NOTE: It takes a lot of time to generate the data.  If you would like 
here is a dropbox link for the dataset 
https://www.dropbox.com/s/wnw2wwr2qkbwmr6/BFSdata.tar.bz2?dl=0
Copy all of the brite files to the data directory.

Once the data set is either downloaded or constructed, run the bfs 
program in the bin directory.
```
bin/bfs
```


# Bellman-Ford
The BellmanFord folder contains the build directory, data directory and src directory
I have also include the bin directory.  If you would like to recompile, there
is a MakeFile in the build directory.

To run the Bellman-Ford, you will need python. From there you can run the
runFile script within the bin folder.
```
runFile
```

Within the data, directory I have three files. 
britegen.py generates the data set
edgetoadjmat.py which converts the edge list from brite to and adajency matrix
nodeFile.txt is used by britegen.py
dataFile.txt is used by the main program.

NOTE: It takes a lot of time to generate the data.  If you would like 
here is a dropbox link for the dataset
https://www.dropbox.com/s/h4361ebvqr9psbo/bfdata-small.tar.bz2?dl=0
Copy all of the brite files to the data directory.
This data is a smaller set. I am creating, let me know if you need it.

Once the data set is either downloaded or constructed, run the runFile 
script in the bin directory.

The results directory contains the collected data for the graphs in the
report.

Final Note: In the future, I would like to run this with more weighted edges
the current.  In addition, the max edge weight is only 5, I would like to
increase this.
