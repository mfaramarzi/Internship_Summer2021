#include <iostream>
#include <map>
#include <string>
#include <set>


int main()
{
    unsigned int n;
    std::cin >> n;

    std::map<std::string, std::set<std::string>> courses;

    std::string fname, lname, course;

    for (auto i = 0; i < n; i++)
    {
        std::cin >> fname >> lname >> course;

        courses[course].insert(fname.append(lname));
    }

    for (const auto& c : courses)
    {
        std::cout << c.first << ' ' << c.second.size() << std::endl;
    }

}