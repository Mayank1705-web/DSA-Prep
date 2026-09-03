class Solution {
public:
    void Sum(vector<int>& candidates, int target, vector<vector<int>>& res, vector<int>& r, int i){
        if (target == 0){
            res.push_back(r);
            return;
        }

        while(i < candidates.size() && target - candidates[i] >= 0){
            r.push_back(candidates[i]);

            Sum(candidates, target - candidates[i], res, r, i);
            ++i;
            r.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> r1;
        vector<vector<int>> fresult;
        Sum(candidates, target, fresult, r1, 0);
        
        return fresult;
    }
};