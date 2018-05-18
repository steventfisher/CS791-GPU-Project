# a simple makefile for building the sample program.
# I use multiple versions of gcc, but cuda only supports
# gcc 4.4 or lower. The ccbin command tells nvcc to use
# gcc 4.4 as its regular (non-gpu) compiler.
#
# the uncommented line should do the trick for you.
CXXFLAGS="-D_MWAITXINTRIN_H_INCLUDE -D__STRICT_ANSI__"
#all: ../bin/topology
all: ../bin/cuda_bellman_ford ../bin/serial_bellman_ford

../bin/cuda_bellman_ford: ../src/cuda_bellman_ford.cu
	/usr/local/cuda-9.0/bin/nvcc -std=c++11 $(CXXFLAGS)  $^ -o $@

../bin/serial_bellman_ford: ../src/serial_bellman_ford.cpp
	g++ -std=c++11 $^ -o $@
clean:
	rm -f *.o
	rm -f *~
	rm -f serial_bellman_ford
	rm -f cuda_bellman_ford
