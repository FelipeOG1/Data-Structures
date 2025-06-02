#include <stdio.h>
#include <stdlib.h>



 typedef struct{
  
  int *arr;
  int max;

  int *stack;





  

  
  
  

  

  
  

  
}Queue;

Queue initQueue(int capa,int firstValue){
  
  Queue q;

  int s[capa];

  q.arr=s;

  q.max=firstValue;
  
  q.stack=malloc(capa *sizeof(int));
  
  *q.stack=firstValue;



   return q;

}



int main(){
  Queue queue=initQueue(10,20);
  


  
}



