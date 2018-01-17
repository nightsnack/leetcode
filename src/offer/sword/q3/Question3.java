package offer.sword.q3;

/**
 * 查找数组里的重复数字，若有则输出并返回true
 * {2，3，1，0，2，5，3}
 */
public class Question3 {
    public static void main(String[] args) {
        int[] nums = {2,3,1,0,6,5,3};
        Question3 q3 = new Question3();
        q3.findDumplicate(nums);
    }

    public boolean findDumplicate(int nums[]) {

        for (int i = 0; i < nums.length ; i++) {
            while (nums[i] != i) {
                int x = nums[nums[i]];
                if (nums[i] == x) {
                    System.out.println(x);
                    return true;
                }
                nums[nums[i]] = nums[i];
                nums[i] = x;
            }
        }
        return false;
    }


}
