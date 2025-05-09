// Student:    Vincent Dufour
// Professor:  Dr. Ranjidha Rajan
// Assignment: Homework 5, Part 3: Verbal Arithmetic
// Date:       09.05.2025
// Time Taken: A bit more than 7 hours in total

#include <vector>
#include <string>
#include <set>
#include <iostream>

// converts string to number based on mapping
long long getNum(const std::string &s, const std::vector<int> &charmp) {
    long long num = 0;
    for (auto ch : s) {
        int n = charmp[ch - 'A'];
        num = num * 10 + n;
    }
    return num;
}

// Solver - uses recursive backtracking
bool solve(int ind, std::vector<char> &unique, std::vector<int> &charmp, 
           std::vector<bool> &usednum, const std::vector<std::string>& words, 
           const std::string &result, std::set<char> &firstnum) {
    if (ind >= unique.size()) {
        long long res = getNum(result, charmp), sum = 0;
        for (auto &word : words) {
            long long num = getNum(word, charmp);
            sum += num;
            if (sum > res) return false;
        }
        return sum == res;
    }

    char ch = unique[ind];
    for (int digit = 0; digit <= 9; digit++) {
        if (!usednum[digit]) {
            if (digit == 0 && firstnum.count(ch)) continue;
            usednum[digit] = true;
            charmp[ch - 'A'] = digit;
            if (solve(ind + 1, unique, charmp, usednum, words, result, firstnum)) {
                return true;
            }
            charmp[ch - 'A'] = -1;
            usednum[digit] = false;
        }
    }
    return false;
}

// main function to figure out if the vector is solvable
bool isSolvable(std::vector<std::string> words, std::string result) {
    std::vector<int> charmp(26, -2);
    std::vector<bool> usednum(10, false);
    std::set<char> firstnum;
    std::vector<char> unique;

    for (auto &word : words) {
        if (word.size() > result.size()) return false;
        if (word.size() > 1) firstnum.insert(word[0]);
        for (auto &ch : word) {
            if (charmp[ch - 'A'] != -1) {
                unique.push_back(ch);
                charmp[ch - 'A'] = -1;
            }
        }
    }

    if (result.size() > 1) firstnum.insert(result[0]);
    for (auto ch : result) {
        if (charmp[ch - 'A'] != -1) {
            unique.push_back(ch);
            charmp[ch - 'A'] = -1;
        }
    }

    return solve(0, unique, charmp, usednum, words, result, firstnum);
}

// runs the tests
void runTests() {
    struct TestCase {
        std::vector<std::string> words;
        std::string result;
        bool expected;
    };

    std::vector<TestCase> tests = {
        {{"SEND", "MORE"}, "MONEY", true},          // SEND + MORE = MONEY;         valid
        {{"A", "B"}, "C", true},                    // A + B = C;                   valid
        {{"LEET", "CODE"}, "POINT", false},         // LEET + CODE = POINT          false 
        {{"SIX", "SEVEN", "SEVEN"}, "TWENTY", true} // SIX + SEVEN + SEVEN = TWENTY valid
    };

    // building the string
    for (const auto& test : tests) {
        std::string equation;
        for (size_t i = 0; i < test.words.size(); ++i) {
            if (i != 0) equation += " + ";
            equation += test.words[i];
        }
        equation += " = " + test.result;

        bool result = isSolvable(test.words, test.result);
        
        std::cout << "Test: " << equation << "\n"
                  << "Status: " << (result == test.expected ? "PASSED" : "FAILED")
                  << " (Expected: " << (test.expected ? "Solvable" : "Not solvable")
                  << ", Got: " << (result ? "Solvable" : "Not solvable") << ")\n\n";
    }
}

int main() {
    runTests();
    return 0;
}
