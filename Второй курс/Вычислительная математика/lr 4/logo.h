//
// Created by ignak on 29.04.2021.
//

#include <string>
#include "../lr 3/colors.h"

using namespace poly::color;

#ifndef POLY_LOGOTYPE_LIB
#define POLY_LOGOTYPE_LIB

[[maybe_unused]] const std::string logotype =
        PURPLE +
        "       _                        \n"
        "       \\`*-.                    \n"
        "        )  _`-.                 \n"
        "       .  : `. .                \n"
        "       : _   '  \\               \n"
        "       ; " + CYAN + "*" + PURPLE + "  `_.   `*-._          \n"
        "       `-.-'          `-.                  " + RED + "@PolySladkiy developer\n" + PURPLE +
        "         ;       `       `.                " + RED + "github: https://github.com/polySladkiy\n" + PURPLE +
        "         :.       .        \\    \n"
        "         . \\  .   :   .-'   .   \n"
        "         '  `+.;  ;  '      :   \n"
        "         :  '  |    ;       ;-. \n"
        "         ; '   : :`-:     _.`* ;\n"
        "      .*' /  .*' ; .*`- +'  `*' \n"
        "      `*-*   `*-*  `*-*'" + RESET;

#endif