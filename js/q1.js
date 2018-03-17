// Given nums = [2, 7, 11, 15], target = 9,

// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].

// [2, 3, 5, 6] = 9

function addSum (nums, target) {
    var sum1, sum2;
    nums.sort(function (a, b) {
        return a - b;
    });

    for (var i = nums.length-1; i >= 0; i--) {
        if (nums[i] > target) {
            nums.splice(i-1);
            break;
        }
    }

    for (var i=0, len=nums.length; i<len; i++) {
        for (var j=len-1; j>=0; j--) {
            if ((nums[i] + nums[j]) == target) {
                return [i, j];
            } else if ((nums[i] + nums[j]) > target) {
                nums.splice(j);
            }
        }
    }
    return [null, null];
}
