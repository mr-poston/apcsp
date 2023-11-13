void linear_check(int current);
void binary_check(int values[], int start, int end);
void print_found(bool found);

int linear_count = 0;
int binary_call = 0;

void print_found(bool found)
{
    if (found)
    {
        printf("Found it!\n");
    }
    else
    {
        printf("Not there.\n");
    }
}

void linear_check(int current)
{
    linear_count++;
    printf("Step %i: Checking... %i\n", linear_count, current);
}

void binary_check(int values[], int start, int end)
{
    binary_call++;
    printf("Step %i: Searching... ", binary_call);
    for (int i = start; i <= end; i++)
    {
        printf("%i ", values[i]);
    }
    printf("\n");
}
