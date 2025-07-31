class Solution {
    public void reverseString(char[] s) {
       
     
        for (int i = 0; i < s.length; i++) {
           
           int j = s.length - 1 - i;
            if (i >= j) { 
               return;
            }
            
           Character temp = s[i];
           s[i] =  s[j];
           s[j] =  temp;
          

        
           
        }
    }
}