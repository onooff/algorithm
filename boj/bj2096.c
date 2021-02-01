#include <stdio.h>

int main()
{
    int n;
    int arr[3];
    int mindp[2][3] = {
        0,
    };
    int maxdp[2][3] = {
        0,
    };
    int min = 0, max = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            scanf("%d", &arr[j]);
        }
        mindp[1][0] = mindp[0][0] < mindp[0][1] ? mindp[0][0] + arr[0] : mindp[0][1] + arr[0];
        mindp[1][2] = mindp[0][1] < mindp[0][2] ? mindp[0][1] + arr[2] : mindp[0][2] + arr[2];
        mindp[1][1] = min + arr[1];

        maxdp[1][0] = maxdp[0][0] > maxdp[0][1] ? maxdp[0][0] + arr[0] : maxdp[0][1] + arr[0];
        maxdp[1][2] = maxdp[0][1] > maxdp[0][2] ? maxdp[0][1] + arr[2] : maxdp[0][2] + arr[2];
        maxdp[1][1] = max + arr[1];

        min = mindp[1][0];
        max = maxdp[1][0];
        for (int k = 0; k < 3; k++)
        {
            mindp[0][k] = mindp[1][k];
            maxdp[0][k] = maxdp[1][k];
            if (min > mindp[0][k])
            {
                min = mindp[0][k];
            }
            if (max < maxdp[0][k])
            {
                max = maxdp[0][k];
            }
        }
    }
    printf("%d %d", max, min);
    return 0;
}
