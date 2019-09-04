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
The BFS folder contains the following 
``` bash
BFS/
├── bin
│   ├── bfs
│   └── timings.txt
├── BRITE
│   ├── File for BRITE Topology Generation
├── build
│   ├── Makefile
├── data
│   ├── britegen.py
│   ├── dataFile.txt
│   └── nodeFile.txt
├── Makefile
└── src
    ├── bfs_kernel.cu
    ├── Graph.cpp
    ├── GraphData.h
    ├── Graph.h
    ├── main.cpp
    ├── main.cpp.old
    ├── README
    ├── Topology.cpp
    ├── Topology.h
    └── vertex.h
```
To begin run the Makefile
```
cd build
make
```
This will generate the executable within the bin directory

## Data Set Generation
Within the data, directory I have three files. 
britegen.py generates the data set
nodeFile.txt is used by britegen.py
dataFile.txt is used by the main program.

To generate the data set run:
```
cd data/
python britegen.py
```

NOTE: It takes a lot of time to generate the data.  If you would like 
here is a dropbox link for the dataset 
https://www.dropbox.com/s/wnw2wwr2qkbwmr6/BFSdata.tar.bz2?dl=0
Copy all of the brite files to the data directory.

Once the data set is either downloaded or constructed, run the bfs 
program in the bin directory.
```
cd bin/
./bfs
```


# Bellman-Ford
The BellmanFord folder contains the following directory structure.
``` bash
BellmanFord/
├── bin
│   ├── runFiles.py
├── BRITE
│   ├── File for BRITE Topology Generation
├── build
│   └── Makefile
├── data
│   ├── britegen.py
│   ├── dataFile.txt
│   ├── edgetoadjmat.py
│   └── nodeFile.txt
└── src
    ├── cuda_bellman_ford.cu
    ├── README
    └── serial_bellman_ford.cpp
```
To begin run the Makefile
```
build/make
```

Then to run the Bellman-Ford, you will need python. Then you will need data in the .brite format. From there you can run the
runFile script within the bin folder.
```
cd bin/
python runFile
```

## Data Set Generation
Within the data, directory I have four files. 
```
britegen.py generates the data set
edgetoadjmat.py which converts the edge list from brite to and adajency matrix
nodeFile.txt is used by britegen.py
dataFile.txt is used by the main program.
```
To generate the data sets run:
```
cd data/
python britegen.py
```

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
