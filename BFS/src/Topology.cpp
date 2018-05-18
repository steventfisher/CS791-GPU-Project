
#include "Topology.h"

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iterator>
#include <fstream>
#include <map>
#include <algorithm>


#define PERCENTAGE_OF_NEIGHBORING_NODES_ 0.015
#define RANDOM_SEED_ 5

typedef std::map<int,int> IngresPairs;
 typedef std::multimap<std::pair<int, int>,int > myMap;


using std::chrono::system_clock;
using namespace std;



//Seed random number generator
std::mt19937 generator5(system_clock::to_time_t(system_clock::now()));

Brite::Brite(){}



template <typename Container>
Container& split(Container& result,
  const typename Container::value_type& s,
  const typename Container::value_type& delimiters)
{
  result.clear();
  size_t current;
  size_t next = -1;
  do {
    current = next + 1;
    next = s.find_first_of( delimiters, current );
    result.push_back( s.substr( current, next - current ) );
  } while (next != Container::value_type::npos);
  return result;
}




Graph* Brite::Populate_Topology_Result(std::string fileName)
{
	int num_of_vertex,num_of_edges;
	std::vector <int> nodes;
	myMap edges; 

    const std::string delimiter{"\t"};
    std::vector<std::vector<std::string> > v;
    // fetch the file into v
    std::string line;
    std::vector<std::string> fields;

    for( std::ifstream in(fileName.c_str()); std::getline(in, line); ) 
    {
    	//std::cout << line << std::endl;
        v.push_back(split(fields, line, delimiter));
    }
    // now print the results
	
	const auto &first = v[0];
	const auto &second = v[1];
	num_of_vertex=stoi(first[1]);
	num_of_edges=stoi(second[1]);
	
	v.erase (v.begin());
	v.erase (v.begin());

	cout<<"Number of Vertices: " << num_of_vertex << endl;
	cout<<"Number of Edges:    " << num_of_edges << endl;
	
	// add all the vertices to the vector
	for(int i = 0; i < num_of_vertex; i++)
	{
		nodes.push_back(i);
	}

	// add all the edges to the vector
    for (const auto &i : v) 
    	{		
	  edges.insert(std::make_pair(std::make_pair(stoi(i[1]),stoi(i[2])),stoi(i[3])));
		}

	v.clear();

	Graph * n1= new Graph(num_of_vertex,num_of_edges, nodes,edges);
	return n1 ;
}
