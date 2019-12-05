
To build the project use:
```bash
mkdir build && cd build && cmake ../ && make
```

To generate various graph inputs run the python script. 
From project root:
```bash
cd sample_inputs && ./gen_inputs.py
```

Flags for input:
- -o [write performance time results to file]
- -n VALUE [prepend name to filename]
- -i [this flag bypasses the sat solver if trying inputs of large v]
- -l [enables write results to std::clog]

To run project with generated inputs:
```bash
cd build && cat ../sample_inputs/input.txt | ./ece650-prj -n 0 -o
```

To send errors and logs to file, use:
```bash
cd build && cat ../sample_inputs/input.txt | ./ece650-prj 2> file.txt
```

