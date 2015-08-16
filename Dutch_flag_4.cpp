#include <utility>

template<size_t N>
void DutchFlagProblem(int(&arr)[N]){
	size_t lo = 0;
	size_t mid = 0;
	size_t hi = N - 1;

	using namespace std;
	while (mid <= hi){
		switch (arr[mid])
		{
		case 1:
			swap(arr[lo++], arr[mid++]);
			break;
		case 2:
			mid++;
			break;
		case 3:
		case 4:
			swap(arr[mid], arr[hi--]);
			break;
		default:
			break;
		}
	}

	size_t i4 = N - 1;
	hi += 1;
	while (hi <= i4) {
		switch (arr[hi]){
		case 3:
			hi++;
			break;
		case 4:
			swap(arr[hi], arr[i4--]);
			break;
		}
	}
}

int main(const char** argc, int argv){
	int arr[] = { 2, 1, 4, 3,  1, 2, 3, 4, 1, 2, 3, 4};
	DutchFlagProblem(arr);
}
