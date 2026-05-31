#include "../src/utils.h"
#include <cassert>

void test_get_pollen() {
    int pollen = get_pollen();
    assert(pollen >= 0 && pollen < 5000);
}

int main() {
    test_get_pollen();
    return 0;
}