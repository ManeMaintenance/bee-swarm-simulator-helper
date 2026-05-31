#include "utils.h"
#include <cstdlib>
#include <ctime>

int get_pollen() {
    srand(time(0));
    return rand() % 5000;
}

void collect_flowers() {
    // Simulate flower collection
}