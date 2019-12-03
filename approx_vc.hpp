#pragma once

#include <iostream>
#include <vector>
#include "cnf-sat-vc.hpp"

// helper functions
std::vector< std::vector<int> > generategraph_adjlist(int v, std::vector< std::pair<int,int> > edges);
std::vector< std::vector<int> > generategraph_adjmatrix(int v, std::vector< std::pair<int,int> > edges);
bool checkvalidinput(int v, std::vector< std::pair<int,int> > edges);

// approximation vertex cover algorithm 1
std::string approxVC1(int v, std::vector< std::pair<int,int> > edges);

// approximation vertex cover algorithm 2
std::string approxVC2(int v, std::vector< std::pair<int,int> > edges);
