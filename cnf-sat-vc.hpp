#pragma once

#include <iostream>
#include <vector>
#include <minisat/core/SolverTypes.h>
#include <minisat/core/Solver.h>

std::string printvect(std::vector<int> resultpaths);
class VertexCover {
private:
    int vertices;
    std::vector< std::pair<int,int> > edges;

    Minisat::Var toVar(int row, int column, int k);
    bool checkvalidinput(std::vector< std::pair<int,int> > edges);
    void addclause_atleastone(Minisat::Solver& solver, int k);
    void addclausevertexonlyonce(Minisat::Solver& solver, int k);
    void addclause_onepercoverpos(Minisat::Solver& solver, int k);
    void addclause_alledgecovered(Minisat::Solver& solver, int k);

    bool solve(Minisat::Solver& solver, int k);
    std::vector<int> getpath(Minisat::Solver& solver, int k);

public:
    VertexCover ( int v, std::vector< std::pair<int,int> > edges );
    
    // Accessors
    int getvertices() const;
    
    // Mutators
    void addedges(std::vector< std::pair<int,int> > edges);
    std::string binsearch_VC();
    std::string linsearch_VC();
};