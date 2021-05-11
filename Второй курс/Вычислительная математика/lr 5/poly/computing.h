//
// Created by poly on 04.05.2021.
//

#include <vector>

#ifndef POLY_COMPUTING_H
#define POLY_COMPUTING_H

#ifndef POLY_MOST_COMMON_TYPE_OF_BOTH
#define POLY_MOST_COMMON_TYPE_OF_BOTH typename std::common_type<T1, T2>::type

#endif // POLY_MOST_COMMON_TYPE_OF_BOTH

// todo: подумать на тем, чтобы производить вычисления только на меньшем векторе и использовать конструкцию ()?():()

template<typename T1, typename T2>
std::vector<POLY_MOST_COMMON_TYPE_OF_BOTH> operator+(const std::vector<T1> &v1, const std::vector<T2> &v2) {

    if (v1.size() != v2.size()) {
        throw std::runtime_error("Sizes of vectors are not equal");
    }

    size_t size = v1.size();

    std::vector<POLY_MOST_COMMON_TYPE_OF_BOTH> res;
    res.reserve(size);
    for (int i = 0; i < size; ++i) {
        res.push_back(v1[i] + v2[i]);
    }
    return res;
}

template<typename T1, typename T2>
std::vector<POLY_MOST_COMMON_TYPE_OF_BOTH> operator-(const std::vector<T1> &v1, const std::vector<T2> &v2) {

    if (v1.size() != v2.size()) {
        throw std::runtime_error("Sizes of vectors are not equal");
    }

    size_t size = v1.size();

    std::vector<POLY_MOST_COMMON_TYPE_OF_BOTH> res;
    res.reserve(size);
    for (int i = 0; i < size; ++i) {
        res.push_back(v1[i] - v2[i]);
    }
    return res;
}

template<typename T1, typename T2>
std::vector<POLY_MOST_COMMON_TYPE_OF_BOTH> operator*(const std::vector<T1> &v1, const std::vector<T2> &v2) {

    if (v1.size() != v2.size()) {
        throw std::runtime_error("Sizes of vectors are not equal");
    }

    size_t size = v1.size();

    std::vector<POLY_MOST_COMMON_TYPE_OF_BOTH> res;
    res.reserve(size);
    for (int i = 0; i < size; ++i) {
        res.push_back(v1[i] * v2[i]);
    }
    return res;
}

template<typename T1, typename T2>
std::vector<POLY_MOST_COMMON_TYPE_OF_BOTH> operator/(const std::vector<T1> &v1, const std::vector<T2> &v2) {

    if (v1.size() != v2.size()) {
        throw std::runtime_error("Sizes of vectors are not equal");
    }

    size_t size = v1.size();

    std::vector<POLY_MOST_COMMON_TYPE_OF_BOTH> res;
    res.reserve(size);
    for (int i = 0; i < size; ++i) {
        res.push_back(v1[i] / v2[i]);
    }
    return res;
}

#endif //POLY_COMPUTING_H
