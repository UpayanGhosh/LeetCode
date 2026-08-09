// Last updated: 10/08/2026, 02:37:19
class Solution {
public:
    int romanToInt(string s) {
       unordered_map<char,int> romanValues = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
       };
        unsigned int result = 0;
        int prevValue = 0;
        for(int i = s.length()-1;i >= 0; i--){
            int currentValue = romanValues[s[i]];
            if(currentValue<prevValue)
                result -= currentValue;
            else
                result += currentValue;
            
            prevValue = currentValue;
        }
        return result;
    }
};

/*
                                         EXPLANATION
First we will declare an unordered map to store the roman values so that we can use them to compare in future.
Next we will declare and unsigned int varialbe "result" to store the result in it.
Here the prevValue is used to store the value of the previous roman number for example if the roman number is IV the prevValue will contain I but initially we are assing 0 to it.
Then we will use a for loop which will run backwards i.e from right to left of an roman number. For example if the roman number is IV then the loop will run from V -> I.
The currentValue stores the value of the current element of the input roman number string "s" with the help of the map.
Now we will comapre if the currentValue is less than the prevValue then we will susbtract it from the currentValue. For example if the roman number is IV then the currentValue will contain "5" and it is not less than the prevValue so we will execute the else part of the code and result will be 0 + 5 = 5 and the prevValue will now be the currentValue i.e 5. In the next itteration of the loop the currentValue will be I i.e 1 and now it is less than the prevValue so we will substrtact it from the result so now the value of result will be 5 - 1 = 4 which is our answer.
*/