class Solution {
public:
    int score(vector<string>& cards, char x) {
        int a = 0;
        vector<int> cntB(10, 0);
        vector<int> cntC(10, 0); 

        for (const string& card : cards) {
            bool has0 = (card[0] == x);
            bool has1 = (card[1] == x);
            if (has0 && has1) {
                a++;
            } else if (has0) {
                cntB[card[1] - 'a']++;
            } else if (has1) {
                cntC[card[0] - 'a']++;
            }
        }

        auto solveGroup = [](vector<int>& cnt, int& leftover) -> int {
        int N = 0, mx = 0;
        for (int c : cnt) {
            N += c;
            mx = max(mx, c);
        }
        int M = min(N / 2, N - mx);
        leftover = N - 2 * M;
        return M;
    };
    int leftoverB = 0, leftoverC = 0;
    int matchB = solveGroup(cntB, leftoverB);
    int matchC = solveGroup(cntC, leftoverC);

    int extra = min(a, leftoverB + leftoverC);    
    int remainingA = a - extra;
    int bonus = min(remainingA / 2, matchB + matchC); 

    return matchB + matchC + extra + bonus;
    }
};