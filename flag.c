#include <stdio.h>
#include <stdlib.h>

#define MAX 256

int main (int argc, char * argv[]) {
    
    int counter = 0;

    while (counter < MAX) {
        printf ("f%d ", counter);
        counter++;
    }
    
    return EXIT_SUCCESS;
}
