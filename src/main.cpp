#include <iostream>
#include "autofarm.h"
#include "utils.h"

int main() {
    std::cout << "Bee Swarm Simulator Helper\n";
    std::cout << "Current pollen: " << get_pollen() << "\n";

    if (should_autofarm()) {
        std::cout << "Starting autofarm...\n";
        autofarm();
    }

    return 0;
}