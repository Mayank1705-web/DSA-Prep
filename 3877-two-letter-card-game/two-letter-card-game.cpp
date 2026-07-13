class Solution {
public:
    int solve(vector<int> &cnt) {
        int total = 0, mx = 0;
        for (int x : cnt) {
            total += x;
            mx = max(mx, x);
        }
        return min(total / 2, total - mx);
    }

    int score(vector<string>& cards, char x) {
        vector<int> first(10, 0), second(10, 0);
        int both = 0;

        for (auto &card : cards) {
            if (card[0] == x && card[1] == x) {
                both++;
            }
            else if (card[0] == x) {
                first[card[1] - 'a']++;
            }
            else if (card[1] == x) {
                second[card[0] - 'a']++;
            }
        }

        int ans = 0;

        // Try assigning 'both' cards to either group
        for (int k = 0; k <= both; k++) {
            vector<int> A = first;
            vector<int> B = second;

            A[x - 'a'] += k;
            B[x - 'a'] += (both - k);

            ans = max(ans, solve(A) + solve(B));
        }

        return ans;
    }
};