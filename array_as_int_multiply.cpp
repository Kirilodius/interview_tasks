#include <vector>

template<class T>
using vector = std::vector < T > ;


auto multiply(vector<int> &a, vector<int> &b) -> vector<typename std::remove_reference<decltype(a[0])>::type>{
	vector<int> result(a.size() + b.size() + 1, 0);

	for (int ai = a.size(); ai > 0; --ai){
		for (int bi = b.size(); bi > 0; --bi){
			result[ai + bi] += a[ai - 1] * b[bi - 1];
			result[ai + bi - 1] = result[ai + bi] / 10;
			result[ai + bi] %= 10;
		}
	}
	return result;
}

int main(const char** argc, int argv){
	vector < int > a{ 1, 2, 3 };
	vector<int> b{ 1, 7 }; 

	auto c = multiply(a, b);
}
