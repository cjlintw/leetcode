// Given a string, find the length of the longest substring without repeating characters.

// Examples:

// Given "abcabcbb", the answer is "abc", which the length is 3.

// Given "bbbbb", the answer is "b", with the length of 1.

// Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

function longestSubstr (str) {
    var rec, max = 0;
    for (var i = 1; i < str.length; i++) {
        if (str[i] !== str[i-1]) {
            rec++;
        } else {
            if (rec > max) {
                max = rec;
            }
            rec = 0;
        }
    }   
}