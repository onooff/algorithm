/*
3
3
1 3 2
3
3 2 1
9
1 4 6 5 3 7 9 2 8
*/

#include <stdio.h>

int main()
{
    int t, tc;
    int n, ans, left, right;
    int i;
    int l[50000] = {
        0,
    };
    scanf("%d", &t);
    for (tc = 1; tc <= t; tc++)
    {
        ans = 0;
        scanf("%d", &n);
        for (i = 0; i < n; i++)
        {
            scanf("%d", &l[i]);
        }
        for (i = 0; i < n; i++)
        {
            if ((i != 0 && i != n - 1) && (l[i - 1] < l[i] && l[i] > l[i + 1]))
            {
                left = 0;
                right = 0;
                while (i - left > 0 && l[i - left] > l[i - (left + 1)])
                {
                    left++;
                }
                while (i + right < n - 1 && l[i + right] > l[i + (right + 1)])
                {
                    right++;
                }
                //printf(">>>>%d\n",ans);
                ans += left * right;
                //printf(">>%d %d %d = %d\n",left,right,i,ans);
            }
        }
        printf("#%d %d\n", tc, ans);
    }
}