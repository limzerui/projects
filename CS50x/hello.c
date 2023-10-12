#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // prompt for name
    string name = get_string("What's your name? ");
    // display name and greet the user
    printf("hello %s, nice to meet you...\n", name);
}
