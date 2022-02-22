OBJECTS=    main.o
CLEANOBJS=  main.o
CC = g++

LFLAGS=
CFLAGS=
EXE=prog

$(EXE):     $(OBJECTS)
			$(CC) $(CFLAGS) -o $(EXE) $(OBJECTS) $(LFLAGS)
main.o:     main.cpp deque.h dequeNode.h
			$(CC) $(CFLAGS) -c main.cpp
test:		prog xpected_output.txt
			./prog < testfile.txt > output.txt
			diff output.txt xpected_output.txt
clean:
			rm -rf  $(CLEANOBJS) $(EXE) output.txt *~
