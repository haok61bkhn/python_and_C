/** 
 * Compute the sum an array
 * @param n number of elements
 * @param array input array
 * @return sum
 */
#include<iostream>
#include <string.h>
using namespace std;

extern "C" // required when using C++ compiler
{
    long long mysum(int n, int* array) {
    
        long long res = 0;
        for (int i = 0; i < n; ++i) {
            res += array[i];
        }
        return res;
    }

    int * create_array(int n){
        int * a = new int[n];
        for(int i = 0 ; i < n ; i++)
            a[i]=i;
        return a;

    }

// string
// void add_one_to_string(char *input) {
//     int ii = 0;
//     for (; ii < strlen(input); ii++) {
//         input[ii]++;
//     }
// }
}