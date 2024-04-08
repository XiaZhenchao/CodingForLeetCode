class LeetCode75_MergeStringAlternately{
    public static void main(String[] args)
    {
        String word1 = "abcd";
        String word2 = "pq";
        System.out.println(mergeAlternately(word1,word2));
    }

    public static String mergeAlternately(String word1, String word2)
    {
        String Result = "";
        if(word1.length() == word2.length())
        {
            for(int i = 0; i< word1.length(); i++)
            {
                Result+= word1.charAt(i);
                Result+= word2.charAt(i);
            }
        }

        if(word1.length() > word2.length())
        {
            for(int i = 0; i< word2.length(); i++)
            {
                Result+= word1.charAt(i);
                Result+= word2.charAt(i);
            }
            for(int j = word2.length(); j< word1.length(); j++)
            {
                Result+= word1.charAt(j);
            }
        }

        if(word1.length() < word2.length())
        {
            for(int i = 0; i< word1.length(); i++)
            {
                Result+= word1.charAt(i);
                Result+= word2.charAt(i);
            }
            for(int j = word1.length(); j< word2.length(); j++)
            {
                Result+= word2.charAt(j);
            }
        }


        return Result;
    }
}