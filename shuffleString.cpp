// Shuffle String Solution

#include <bits/stdc++.h>
using namespace std;

class Solution {

	public:
		string restoreString(string s, vector<int>& indices) {
			map<int, char> tmp;
			int length = s.length();
			string retVal;
			for(int i = 0; i < length; i++)
				tmp.insert(pair<int, char>(indices[i], s[i]));			
			for (int i = 0; i < length; i++)
				retVal += tmp[i];

			return retVal;
		}
};

int main(void) {
	Solution S1;
	string s = "codeleet";
	vector<int> vect;
	vect.push_back(4);
	vect.push_back(5);
	vect.push_back(6);
	vect.push_back(7);
	vect.push_back(0);
	vect.push_back(2);
	vect.push_back(1);
	vect.push_back(3);

	cout << "Return: " << S1.restoreString(s, vect) << endl;



}
