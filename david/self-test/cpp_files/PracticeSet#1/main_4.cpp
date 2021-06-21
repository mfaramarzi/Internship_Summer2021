#include <iostream>
#include <cmath>
#include <iomanip>

// Need to use doubles

struct Vector2D
{
  Vector2D()
  : x(0),y(0){}

  Vector2D(double x, double y)
  : x(x),y(y){}

  double x, y;

  double length()
  {
      return sqrt(x*x + y * y);
  }

  double dotProduct(const Vector2D& other)
  {
    double dot = x*other.x + y* other.y;
    return dot;
  }

  Vector2D normalize()
  {
    Vector2D norm_vec = Vector2D(x/length(),y/length());
    return norm_vec;
  }

};

int main()
{
  Vector2D v1, v2;
  std::string angle;

  std::cin >> v1.x >> v1.y >> v2.x >> v2.y;
  std::cout.precision(4);
  std::cout << std::fixed;
  double dot = v1.dotProduct(v2);

  dot < 0 ? angle = "Obtuse" : dot > 0 ? angle = "Acute" : angle = "Perpendicular";  

  std::cout<< "Length of v1: "<< v1.length() <<std::endl;
  std::cout<< "Length of v2: " << v2.length()<<std::endl;
  
  std::cout<< "Their normalized dot product is "<< v1.normalize().dotProduct(v2.normalize()) << " and they are " << angle << std::endl;

 // "Length of v1: 1.000 \n Length of v2: 1.000 \n Their normalized dot product is 0.000 and they are Perpendicular"
}