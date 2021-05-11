//
// Created by Poly on 26.12.2020.
//

#include <iostream>
#include <utility>
#include <vector>
#include <map>
#include <sstream>

#ifndef POLY_SOLUTIONS_H
#define POLY_SOLUTIONS_H


namespace poly::output {

    /* args:
     *      a - what to input
     *      msg - message for user (will send before input)
     */
    template<typename T>
    void secure_input(T &a, std::string &&msg = "") {
        std::cout << msg;
        while (!(std::cin >> a) || (std::cin.peek() != '\n') || (a < 0)) {
            std::cin.clear();
            while (std::cin.get() != '\n');
            std::cout << "\x1B[31mError\x1B[0m, try again: " << msg << std::endl;
        }
    }
}


// Allow range-based for
template<typename Collection>
static std::string Join(const Collection &c, char d) {
    std::stringstream ss;
    bool first = true;

    for (const auto &i : c) {
        if (!first) {
            ss << d;
        }
        first = false;
        ss << i;
    }
    return ss.str();
}

// Console output for std::pair
template<typename First, typename Second>
std::ostream &operator<<(std::ostream &out, const std::pair<First, Second> pair) {
    return out << '(' << pair.first << "," << pair.second << ')';
}

// Console output for std::vector
template<typename T>
std::ostream &operator<<(std::ostream &out, const std::vector<T> &v) {
    return out << '[' << Join(v, ',') << ']';
}

// Console output for std::map
template<typename T1, typename T2>
std::ostream &operator<<(std::ostream &out, const std::map<T1, T2> &m) {
    return out << '{' << Join(m, ',') << '}';
}


#endif //POLY_SOLUTIONS_H
