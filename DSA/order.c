#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <string.h>
int main()
{
    int i, num, count;
    char lastmode, curmode;
    char str[100];
    printf("Input string : ");
    scanf("%s", str);
    lastmode = 'n';
    num = 1; // #1
    for (i = 0; i < strlen(str); i++)
    {
        if (str[i] >= 'a' and str[i] <= 'z')
        {
            curmode = 'c';
        }
        else if (str[i] >= '0' and str[i] <= '9')
        {
            curmode = 'n';
        }
        if (lastmode == 'n' and curmode == 'n')
        {
            num = num * 10 + (str[i] - '0');
        } // #2
        else if (lastmode == 'n' and curmode == 'c')
        {
            for (count = 0; count < num; count++)
            {
                printf("%c", str[i]);
            }
            num = 1;
        } // #3
        else if (lastmode == 'c' and curmode == 'n')
        {
            num = str[i] - '0';
        }
        else if (lastmode == 'c' and curmode == 'c')
        {
            printf("%c", str[i]);
            num = 1;
        }
        lastmode = curmode;
    }
    return 0;
}