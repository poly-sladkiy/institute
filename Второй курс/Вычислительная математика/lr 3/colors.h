//
// Created by Poly on 26.04.2021.
//

#ifndef POLY_COLORS_H
#define POLY_COLORS_H

namespace poly::color {

    // Reset all settings
    #define RESET "\x1B[0m"

    #define BOLD "\x1B[1m"

    #define BRIGHT "\x1B[2m"

    #define UNDERLINE     "\x1B[4m"
    #define UNDERLINE_OFF "\x1B[24m"

    #define BLINK     "\x1B[5m"
    #define BLINK_OFF "\x1B[25m"

    #define INVERTED_VIDEO      "\x1B[7m"
    #define INVERTED_VIDEO_OFF  "\x1B[27m"

    #define NORMAL_INTENSITY     "\x1B[21m"
    #define NORMAL_INTENSITY_OFF "\x1B[22m"

    // Text colors
    #define BLACK   "\x1B[30m"
    #define RED     "\x1B[31m"
    #define GREEN   "\x1B[32m"
    #define BROWN   "\x1B[33m"
    #define BLUE    "\x1B[34m"
    #define PURPLE  "\x1B[35m"
    #define CYAN    "\x1B[36m"
    #define WHITE   "\x1B[37m"

    #define BLINK_RESET     "\x1B[38m"
    #define BLINK_OFF_RESET "\x1B[39m"

    // Background colors
    #define BACK_BLACK   "\x1B[30m"
    #define BACK_RED     "\x1B[31m"
    #define BACK_GREEN   "\x1B[32m"
    #define BACK_BROWN   "\x1B[33m"
    #define BACK_BLUE    "\x1B[34m"
    #define BACK_PURPLE  "\x1B[35m"
    #define BACK_CYAN    "\x1B[36m"
    #define BACK_WHITE   "\x1B[37m"

    #define BACK_RESET   "\x1B[37m"

}

#endif //POLY_COLORS_H
