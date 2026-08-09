// Last updated: 10/08/2026, 02:34:22
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        // Declare a map to store negative positions of cars as keys and arrival times as values.
        map<int, double> map;
        // Iterate through each car's position and calculate arrival time.
        for(int i = 0; i<position.size(); i++){
            // Calculate time it takes for the car to reach the target and store the calculated arrival time in the map with negative position as key.
            map[-position[i]] = (double) (target - position[i]) / speed[i];
        }
        // Initialize variables to count fleets and track current maximum arrival time.
        int res = 0; // Number of car fleets that will reach the target.
        double currentTime = 0; // Current maximum arrival time.
        // Iterate through each entry in the map.
        for(auto element : map){
            // Check if the current car's arrival time is greater than the current max.
            if(element.second > currentTime){
                // Update the current max arrival time.
                currentTime = element.second;
                // Increment the fleet count since a new fleet will reach the target.
                res++;
            }
        }
        // Return the total number of car fleets.
        return res;
    }   
};

/*IMPORTANT!!!!
Why we are storing the negative position values here?

Sorting in a Descending Order: In this problem, you want to simulate car fleets that move towards a target point. The map data structure used in this code is sorted in ascending order by default based on its keys. However, the problem requires you to sort the cars in descending order of their initial positions (closest to the target first). By storing the negative values of positions as keys in the map, the sorting behavior of the map works in the desired way. Since negative values are "smaller" than positive values, they effectively sort the positions in descending order.
*/