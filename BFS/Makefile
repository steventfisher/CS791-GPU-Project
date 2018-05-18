# a simple makefile for building the sample program.
# I use multiple versions of gcc, but cuda only supports
# gcc 4.4 or lower. The ccbin command tells nvcc to use
# gcc 4.4 as its regular (non-gpu) compiler.
#
# the uncommented line should do the trick for you.
CXXFLAGS="-D_MWAITXINTRIN_H_INCLUDE -D__STRICT_ANSI__"
all: ../bin/topology

#../bin/topology: ../build/bfs_kernel.o ../build/Graph.o ../build/TopologyGenerator.o ../src/main.cpp
#	nvcc -std=c++11 -arch=sm_20 $^ -o $@

../bin/topology: ../build/bfs_kernel.o ../build/Graph.o ../build/Topology.o ../src/main.cpp
	/usr/local/cuda-9.0/bin/nvcc -std=c++11 $(CXXFLAGS) $^ -o $@

#../build/Graph.o: ../src/Graph.cpp
#	g++ -std=c++11 -c $^


../build/Topology.o: ../src/Topology.cpp
	g++ -std=c++0x -c $^
#../build/TopologyGenerator.o: ../src/TopologyGenerator.cpp
#	g++ -std=c++11 -c $^


../build/Graph.o: ../src/Graph.cpp
	g++ -std=c++0x -c $^

#../build/bfs_kernel.o: ../src/bfs_kernel.cu
#	nvcc -std=c++11 -arch=sm_20 -c $^ -o $@
../build/bfs_kernel.o: ../src/bfs_kernel.cu
	/usr/local/cuda-9.0/bin/nvcc -std=c++11 $(CXXFLAGS)  -c $^ -o $@

clean:
	rm -f *.o
	rm -f *~
	rm -f ../bin/topology
