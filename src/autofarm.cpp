#include "autofarm.h"
#include "utils.h"
#include <thread>
#include <chrono>

void autofarm() {
    while (true) {
        collect_flowers();
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
}

bool should_autofarm() {
    return get_pollen() < 1000;
}