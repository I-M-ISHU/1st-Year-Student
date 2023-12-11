/*CHECK THE FREQUENCY OF VOWEL IN THE GIVEN STRING
NITYANAND MAURYA SRMIST DELHI NCR*/

# include<stdio.h>
# include<string.h>
int main(){
   int fre=0;
   char po[]="AldksaioreiIOANBCie";
   char vo[]="aeiouAEIOU";
   for(int i=0;po[i]!='\0';i++){
      for(int j=0;vo[j]!='\0';j++){
         if (po[i]==vo[j]){
            fre+=1;
         }
      }
   }
   printf("The freq is : %d",fre);
}