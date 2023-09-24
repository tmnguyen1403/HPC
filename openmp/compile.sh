#!/bin/bash
source_file=$1
export LDFLAGS="-L/usr/local/opt/libomp/lib"
export CPPFLAGS="-I/usr/local/opt/libomp/include"
echo "Source file $source_file"
clang++ -std=c++2a -Xpreprocessor -fopenmp -lomp "$source_file" "$LDFLAGS" "$CPPFLAGS"

#Requirement
#brew install llvm
#brew install libomp
