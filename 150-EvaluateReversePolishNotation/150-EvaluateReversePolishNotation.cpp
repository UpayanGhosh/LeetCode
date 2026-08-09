// Last updated: 10/08/2026, 02:36:02
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for(auto ele : tokens){
            if(ele == "+"){
                int a = st.top(); st.pop();
                int b = st.top(); st.pop();
                st.push(b+a);
            }
            else if(ele == "-"){
                 int a = st.top(); st.pop();
                int b = st.top(); st.pop();
                st.push(b-a);
            }
            else if(ele == "*"){
                 int a = st.top(); st.pop();
                int b = st.top(); st.pop();
                st.push(b*a);
            }
            else if(ele == "/"){
                 int a = st.top(); st.pop();
                int b = st.top(); st.pop();
                st.push(b/a);
            }
            else {
                st.push(stoi(ele));
            }
        }
        return st.top();
    }
};