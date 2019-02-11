/** You can use std::generate algorithm to fill a vector
    of n elements with random numbers.

    In modern C++ it’s recommended not to use any time-based
    seeds and std::rand, but instead to use random_device to
    generate a seed. For software-based engine, you always
    need to specify the engine and distribution. Read More..

	If you want to rearrange the elements of a range in a random order:

	std::shuffle(begin(vec), end(vec), mersenne_engine);
 */

#include <random>
#include <algorithm>
#include <iterator>
#include <iostream>
#include <functional>

using namespace std;

int main()
{
    // First create an instance of an engine.
    random_device rnd_device;

    // Specify the engine and distribution.
    mt19937 mersenne_engine {rnd_device()};  // Generates random integers
    uniform_int_distribution<int> dist {1, 52};

    auto gen = [&dist, &mersenne_engine](){
                   return dist(mersenne_engine);
               };

    vector<int> vec(10);
    generate(begin(vec), end(vec), gen);

    copy(vec.begin(), vec.end(), ostream_iterator<int>(cout, " "));
}
