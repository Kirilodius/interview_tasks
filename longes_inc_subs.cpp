#include <vector>
#include <algorithm>

using namespace std;

size_t lis(const vector<int> &iSeq) {
	vector<int> incSeq;
	size_t longestSubs{ 1 };

	incSeq.push_back(iSeq[0]);

	for (size_t i = 1; i < iSeq.size(); ++i) {
		if (incSeq.back() < iSeq[i]) {
			incSeq.back() = iSeq[i];
			++longestSubs;
		}
		else {
			auto pos = lower_bound(begin(incSeq), end(incSeq), iSeq[i]);
			*pos = iSeq[i];
		}
	}

	return longestSubs;
}

int main() {
	auto i = lis({1, 2, 3, 5, 4, 7 ,6});
	return 0;
}
