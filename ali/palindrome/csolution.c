#include <string.h>

bool isPalindrome(char * s){
        size_t size_s = strlen(s);
        //char nums[10] = ['0','1','2','3','4','5','6','7','8','9']
        char new_s[200000] = "";
        int k = 0;
        for(int i = 0; i<size_s; i++){
            if(isalnum(s[i])){
                printf("%c\n",s[i]);
                new_s[k++] = tolower(s[i]); 
            }
        }
        new_s[k] = '\0';
        printf("%s\n", new_s);       
        for(int i = 0; i<k; i++){
            if(new_s[i] != new_s[--k]){
                return false;
            }
        }
        return true;
    

}