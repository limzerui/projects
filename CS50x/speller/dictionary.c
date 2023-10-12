// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <strings.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>


#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

//declare variable
unsigned int word_count;


// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    //use hash function to get value
    //acces link list and traverse to look for name
    //strcasecmp to compare two strings, case insensitively(regardless if its small case or wtv)
    //set up variable called cursor which points to first element in linked list.
    //cursor moves along linked list
    //cursor=cursor->next until NULL
    int hash_value=hash(word);
    //point cursor to first word
    node *cursor = table [hash_value];
    while(cursor != 0)
    {
        if(strcasecmp(word, cursor->word)==0)
        {
            return true;
        }
        cursor=cursor->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    return toupper(word[0]) - 'A'; //convert to uppercase and convert letter to number
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *file=fopen(dictionary, "r");
    if(file == NULL)
        {
            printf("unable open %s\n", dictionary);
            return false;
        }
    //read string until eof
    char word[LENGTH + 1];
    while (fscanf(file, "%s", word) != EOF)
    {
        //allocate memory
        node *n=malloc(sizeof(node));
        if (n==NULL)
        {
            return false;
        }

    strcpy(n -> word, word);
    int hash_value = hash(word);
    //now insert node in and do lnkage coorectly
    //set pointer of new node to current head of table
    n->next = table[hash_value];
    //get new node to head of list
    table[hash_value]=n;
    //track no. of word in dictionery to declare word count
    word_count++;
    }
    fclose(file);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if(word_count>0)
    {
        return word_count;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i=0;i<N;i++)
    {
        //set cursor start @linked list
        node *cursor = table[i];
        //if cursor not null,free mem
        while(cursor)
        {
            node *tmp=cursor;
            cursor=cursor->next;
            free(tmp);


        }
        if(cursor==NULL)
            {
                return true;
            }
    }
    return false;
}
