#include <cs50.h>
#include <stdio.h>
#include "utilities.c"

bool linear_search(int value, int values[], int size);
bool binary_search(int value, int values[], int start, int end);

int main(int argv, string argc[])
{
    int numbers[] = {5, 7, 8, 24, 27, 32, 34, 36, 37, 39, 47, 50, 53, 58, 64, 66, 77, 78, 84, 92, 99};
    int length = 21;
    int value = get_int("What value do you want to search for? ");
    printf("---LINEAR SEARCH---\n");
    print_found(linear_search(value, numbers, length));
    printf("---BINARY SEARCH---\n");
    print_found(binary_search(value, numbers, 0, length - 1));
    printf("The array of numbers:\n");
    for (int i = 0; i < length; i++)
    {
        printf("%i ", numbers[i]);
    }
    printf("\n");
}

bool linear_search(int value, int values[], int size)
{
    // TODO: Implement a linear search
}

bool binary_search(int value, int values[], int start, int end)
{
    // TODO: Implement a binary search
    
    // If nnothing left to search, return false
    

    // Calculate the middle position
    

    // If value is in the middle position, return true
    

    // Else if value is less than what is in the middle position, search the left side
    

    // Else if value is greater than what is in the middle position, search the right side
    
}