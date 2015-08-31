#include <algorithm>

using namespace std;

double maxProfitInKBuySell(const vector<double> &prices, unsigned int k){
	vector<double> ksumms(k * 2, numeric_limits<double>::lowest());
	for (size_t i = 0; i < prices.size(); ++i){
		vector<double> pre_k_summs{ ksumms };
		for (int j = 0, sign = -1; j < ksumms.size() && j <= i; ++j, sign *= -1){
			double diff = sign * prices[i] + (j == 0 ? 0 : pre_k_summs[j - 1]);
			ksumms[j] = max(diff, pre_k_summs[j]);
		}
	}

	return ksumms.back();
}


int main(){
	vector<double> pricess{310, 315, 275, 295, 260, 270, 290, 230, 255, 250};
	maxProfitInKBuySell(pricess, 1);
	return 0;
}
