//
// Created by ignak on 26.04.2021.
//

#include <string>

#ifndef POLY_CURSOR_H
#define POLY_CURSOR_H

namespace poly {

    // Scrolling
    std::string scroll_up(const int&& n = 1) {
        return "\x1B[" + std::to_string(n) + "S";
    }

    std::string scroll_down(const int&& n = 1) {
        return "\x1B[" + std::to_string(n) + "T";
    }

}

#endif //POLY_CURSOR_H
