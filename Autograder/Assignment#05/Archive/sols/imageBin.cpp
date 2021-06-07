#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>

#include "bitmap_image.hpp"

int main(int argc, char *argv[]) {
    std::string fname(argv[1]);
    bitmap_image image(fname);

    image.convert_to_grayscale();

    unsigned long long mean = 0;
    unsigned int w = image.width();
    unsigned int h = image.height();
    rgb_t color;

    for(unsigned int i = 0 ; i < w ; i++) {
        for(unsigned int j = 0 ; j < h ; j++) {
            image.get_pixel(i, j, color);
            mean += color.red;
        }
    }

    mean = mean / (w * h);

    for(unsigned int i = 0 ; i < w ; i++) {
        for(unsigned int j = 0 ; j < h ; j++) {
            image.get_pixel(i, j, color);
            if(color.red < mean) {
                image.set_pixel(i, j, 0, 0, 0);
            }
            else {
                image.set_pixel(i, j, 255, 255, 255);
            }
        }
    }

    std::string outname(argv[2]);
    image.save_image(outname + ".bw");

    return 0;
}