// Last updated: 10/08/2026, 02:37:27
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int maxArea = 0;
        while(left<right){
            int left_height = height[left];
            int right_height = height[right];
            int min_height = min(left_height,right_height);
            maxArea = max(maxArea,min_height*(right-left));
            if (left_height < right_height)
                left++;
            else
                right--;
        }
        
        return maxArea;
    }
};
// https://youtu.be/ZHQg07n_tbg