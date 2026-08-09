// Last updated: 10/08/2026, 02:34:34
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temp) {
        int n = temp.size();
        vector<int> res(temp.size(), 0);
        stack<pair<int,int>> st; //pair: [temp,index]
        for(int i = 0; i<n; ++i){
            int t = temp[i];
            while(!st.empty() && t > st.top().first){
                int stackT = st.top().first;
                int stackInd = st.top().second;
                st.pop();
                res[stackInd] = i - stackInd;
            }
            st.push({t,i});
        }
        return res;
    }
};

