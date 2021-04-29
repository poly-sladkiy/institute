//
// Created by Poly on 26.04.2021.
//

#include <string>

#ifndef POLY_COLORS_H
#define POLY_COLORS_H

namespace poly::color {

    // Reset all settings
    const std::string RESET = "\x1B[0m";

    const std::string BOLD = "\x1B[1m";

    const std::string BRIGHT = "\x1B[2m";

    const std::string UNDERLINE     = "\x1B[4m";
    const std::string UNDERLINE_OFF = "\x1B[24m";

    const std::string BLINK     = "\x1B[5m";
    const std::string BLINK_OFF = "\x1B[25m";

    const std::string INVERTED_VIDEO      = "\x1B[7m";
    const std::string INVERTED_VIDEO_OFF  = "\x1B[27m";

    const std::string NORMAL_INTENSITY     = "\x1B[21m";
    const std::string NORMAL_INTENSITY_OFF = "\x1B[22m";

    // Text colors
    const std::string BLACK   = "\x1B[30m";
    const std::string RED     = "\x1B[31m";
    const std::string GREEN   = "\x1B[32m";
    const std::string BROWN   = "\x1B[33m";
    const std::string BLUE    = "\x1B[34m";
    const std::string PURPLE  = "\x1B[35m";
    const std::string CYAN    = "\x1B[36m";
    const std::string WHITE   = "\x1B[37m";

    const std::string BLINK_RESET     = "\x1B[38m";
    const std::string BLINK_OFF_RESET = "\x1B[39m";

    // Background colors
    const std::string BACK_BLACK   = "\x1B[30m";
    const std::string BACK_RED     = "\x1B[31m";
    const std::string BACK_GREEN   = "\x1B[32m";
    const std::string BACK_BROWN   = "\x1B[33m";
    const std::string BACK_BLUE    = "\x1B[34m";
    const std::string BACK_PURPLE  = "\x1B[35m";
    const std::string BACK_CYAN    = "\x1B[36m";
    const std::string BACK_WHITE   = "\x1B[37m";

    const std::string BACK_RESET   = "\x1B[37m";

}

#endif //POLY_COLORS_H
