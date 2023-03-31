#include<stdio.h>
int main(){
    int size,i;
    int user_input;
    printf("\n");
    printf("\n");
    printf("***************Welcome to Operations on Array Programme***************** ");
    printf("\n");
    printf("\n");
    printf("****Make an Array and then select the function you want to perform in array****");
    printf("\n");
    printf("\n"); 
    
    
    printf("Enter size of the array: ");
    scanf("%d", &size);
    printf("\nEnter %d elements in the array: \n",size);
    int array[size];
    for(i=0; i<size; i++)
    {
        printf("\nEnter %d element in the array: ",i+1);
        scanf("%d", &array[i]);
    }
    printf("\n");
    printf("Your Array is : ");
    for( i=0;i<size;i++){
        printf("%d ",array[i]);
    }
    printf("\n");
    printf("\n");
    printf("Select The Operation You want to do with this Array: "
    "1) Reverse the Array :"
    "2) Find Maximum and Minimum in array :"
    "3) Arranging Array in acesnding order: "
    "4)Addition of all elemnent in array:"
    "5)Searching an element in array ");
    printf("\n");
    printf("Enter a number : ");
    int x;

    scanf("%d", &user_input);
    
    if(user_input == 1){
        printf("You selected to reverse the array \n");
        printf("\n");
        printf("Your Array is : ");
        for(i=0; i<size; i++){
            printf(" %d " , array[i] );
        }
        int reverse[100];
        int j=0;
        for(i=size; i>=0; i--)
        {
            reverse[j] = array[i];
            j++;
        }
        printf("\n");

        printf("\nReversed array : ");
        for(i=0; i<size; i++)
        {
            printf(" %d ", reverse[i]);
        }
        printf("\n");
        printf("\n");
        printf("\n");
        printf("Source Code :"  );
        printf("\n");
        printf("\n");

        printf("#include <stdio.h> \n"
            "int main()\n"
            "{\n"
            "int arr[100], reverse[100];\n"
            "int size, i, j;\n");
        printf("\n");
        printf("printf(Enter size of the array:);\n"
            "scanf(%d, &size);\n"
            "printf(Enter elements in array :: );\n");
        printf("\n");
        printf("for(i=0; i<size; i++)\n"
            "{\n"
            "printf(Enter %d element in array :: ,i+1);\n"
            "scanf(%d, &arr[i]);\n"
            "}\n");
        printf("\n");
        printf("j=0;\n"

            "for(i=size-1; i>=0; i--)\n"
            "{\n"
            "reverse[j] = arr[i];\n"
            "j++;\n"
            "}\n");
        printf("\n");

        printf("printf(Reversed array : );\n"
            "for(i=0; i<size; i++)\n"
            "{\n"
               "printf(%d , reverse[i]);\n"
            "}\n" 
                );
        }
    if(user_input == 2){
        printf("You selected to find Maximum and Minimum in the array \n");
        printf("\n");
        printf("Your Array is : ");
        
    
        for(i=0; i<size; i++){
            printf(" %d " , array[i]);
        }
        int max = array[0];
        int min = array[0];
        for(i=1;i<size;i++){
            if(array[i]>max){
                max = array[i];
            }
            if(array[i]<min){
                min = array[i];
            }
        }
        printf("\n");
        printf("\nMax value = %d\n",max);
        printf("Min value = %d\n",min);
        printf("\nSource Code:");
        printf(" \n/*  C program to find maximum and minimum element in array  "

            "\n#include <stdio.h>"

            "\nint main()"
            "\n{"
                "\nint arr[100];"
                "\nint i, max, min, size;"

                "\n/*"
                "\n* Reads size array and elements in the array"
                "\n*/"
                "\nprintf(Enter size of the array: );"
                "\nscanf(%d, &size);"
                "\nprintf(\nEnter %d elements in the array: \n,size);"
                "\nfor(i=0; i<size; i++)"
                "\n{"
                 "  \n printf(\nEnter %d element in the array: ,i+1);"
                    "\nscanf(%d, &arr[i]);"
                "\n}"

                "\n/* Supposes the first element as maximum and minimum */"
                "\nmax = arr[0];"
                "\nmin = arr[0];"
                "\n/*"
                "\n* Finds maximum and minimum in all array elements."
                "\n*/"
                "\nfor(i=1; i<size; i++)"
                "\n{"
                 "\n   /* If current element of array is greater than max */"
                  "\n  if(arr[i]>max)"
                   "\n {"
                    " \n   max = arr[i];"
                    "\n}"

                    "\n/* If current element of array is smaller than min */"
                    "\nif(arr[i]<min)"
                    "\n{"
                      "\n  min = arr[i];"
                    "\n}"
                "\n}"

                "\n/* Prints the maximum and minimum element*/"
                "\nprintf(\nMaximum element = %d\n, max);"
                "\nprintf(\nMinimum element = %d\n, min);"

                "\nreturn 0;"
                
                );
    }
    
    if(user_input == 3){
        printf("\nSorting Array in Ascending order");
        /*  C Program to sort array in ascending order using bubble sort  */
        int temp;
        for (i = 0 ; i < ( size - 1 ); i++){
                for (int j= 0 ; j < size - i - 1; j++){
                        if(array[j] > array[j+1]){
                                temp=array[j];
                                array[j]   = array[j+1];
                                array[j+1] = temp;
                        }
                }
        }
        printf("\nSorted list in ascending order :: ");
        for ( i = 0 ; i < size ; i++ )
                printf(" %d ", array[i]);
        printf("\n");
        printf("\n");
        printf("\nSource Code: ");
        printf("\n/*C Program to sort array in ascending order using bubble sort  */"

                "\n#include<stdio.h>"
                "\nint main(){"
        "\nint array[50], n, i, j, temp;"
        "\nprintf(Enter number of elements :: );"
        "\nscanf(%d, &n);"
        "\nprintf(\nEnter %d integers :: \n, n);"
        "\nfor(i = 0; i < n; i++)"
    "\n{"
        "\nprintf(\nEnter %d integer :: , i+1);"
        "\nscanf(%d, &array[i]);"

    "\n}"

        "\nfor (i = 0 ; i < ( n - 1 ); i++){"
                "\nfor (j= 0 ; j < n - i - 1; j++){"
                        "\nif(array[j] > array[j+1]){"
                                "\ntemp=array[j];"
                                "\narray[j]   = array[j+1];"
                                "\narray[j+1] = temp;"
                        "\n}"
                "\n}"
        "\n}"
        "\nprintf(\nSorted list in ascending order :: );"
        "\nfor ( i = 0 ; i < n ; i++ )"
                "\nprintf( %d , array[i]);"
        "\nreturn 0;"
        "\n}"
);
}
    if(user_input == 4){

        printf("\nAddition of all element in an Array");
        printf("\n");
        printf("\n");
        /* C Program to Calculate Addition of All Elements in Array */
   int sum, num;
  
   sum = 0;
   for (i = 0; i < size; i++)
      sum = sum + array[i];

   printf("\nPrinting of all elements of array :: \n");
   for (i = 0; i < size; i++)
      printf("\na[%d]=%d", i+1, array[i]);

   printf("\n\nSum of all elements = %d", sum);
    printf("\n");
    printf("\n");
    printf("Source code:");
    printf("\n/* C Program to Calculate Addition of All Elements in Array */"

            "\n#include<stdio.h>"

            "\nint main() {"
            "\nint i, arr[50], sum, num;"

            "\nprintf(Enter no of elements :);"
            "\nscanf(%d, &num);"

            "\nReading values into Array"
           " \nprintf(\nEnter the values :\n);"
            "\nfor (i = 0; i < num; i++)"
            "\n{"
                   " \nprintf(\nEnter %d value :: ,i+1);"
                    "\nscanf(%d, &arr[i]);"
            "\n}"

            "\nComputation of total"
            "\nsum = 0;"
            "\nfor (i = 0; i < num; i++)"
                "\nsum = sum + arr[i];"

            "\nprintf(\nPrinting of all elements of array :: \n);"
            "\nfor (i = 0; i < num; i++)"
                "\nprintf(\na[%d]=%d, i+1, arr[i]);"

            "\nPrinting of total"
            "\nprintf(\nSum of all elements = %d, sum);"

            "\nreturn 0;"
            "\n}"
            );



    }

    if(user_input == 5){
        printf("Searching An Element: ");
        /*  C Program to search an element in the array  */
                int num, flag;
                printf("\nEnter the element to search within the array: ");
                scanf("%d", &num);

                /* Supposes that element is not in the array */
                flag = 0;
                for(i=0; i<size; i++)
                {
                    /*
                    * If element is found in the array
                    */
                    if(array[i]==num)
                    {
                        flag = 1;
                        printf("\n%d is found at position %d", num, i+1);
                        break;
                    }
                }

                /*
                * If element is not found in array
                */
                if(flag==0)
                {
                    printf("\n%d is not found in the array", num);
                }
            
    
        printf("\n");
        printf("\n");
        printf("\n");
        printf("Source code: ");
        printf("\n/*  C Program to Search an element in the array  */"

            "\n#include <stdio.h>"

            "\nint main()"
            "\n{"
                "\nint arr[100];"
                "\nint size, i, num, flag;"

                "\n/*Read size of array and elements in array*/"
                "\nprintf(Enter size of array :: );"
                "\nscanf(%d, &size);"

                "\nprintf(\nEnter elements in array: \n);"
                "\nfor(i=0; i<size; i++)"
                "\n{"
                    "\nprintf(\nEnter %d element in array :: ,i+1);"
                    "\nscanf(%d, &arr[i]);"
                "\n}"
                "\nprintf(\nEnter the element to search within the array: );"
                "\nscanf(%d, &num);"

                "\n/* Supposes that element is not in the array */"
                "\nflag = 0;"
                "\nfor(i=0; i<size; i++)"
                "\n{"
                    "\n/* If element is found in the array*/"
                    "\nif(arr[i]==num)"
                    "\n{"
                        "\nflag = 1;"
                        "\nprintf(\n%d is found at position %d, num, i+1);"
                        "\nbreak;"
                    "\n}"
                "\n}"

               "\n/* If element is not found in array*/"
                "\nif(flag==0)"
                "\n{"
                    "\nprintf(\n%d is not found in the array, num);"
                "\n}"

                "\nreturn 0;"
            "\n}"
            "\n)");

}

                
       
    return 0;
}



