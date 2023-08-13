#include <iostream>
#include <vector>

using namespace std;

class Solution {

public:
    int missingNumber(vector<int>& nums) {

        int si = nums.size();
        int res = si;

        for(int i=0; i<si; i++) {
            res ^= i;
            res ^=nums[i];
        }

        return res;
    }
};


int main() {

    Solution obj;

    vector<int> nums = {0,1,3};
    cout << "missing number: " << obj.missingNumber(nums) << endl;

    return 0;
}
