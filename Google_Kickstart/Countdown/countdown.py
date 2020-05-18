#include <stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    for(int x = 1; x<=t;x++)
    {
        int n, k;
        scanf("%d %d",&n,&k);
        int a[n];
        for (int i = 0; i < n; i++)
        {
            scanf("%d",&a[i]);
        }
        int y=0;
        for (int i = 0; i < n; i++)
        {
            if (a[i] == k)
            {
                i++;
                int c = 1;
                for (int j = k-1; j > 0; j--, i++)
                {
                    if(a[i]!=j)
                    {
                        c = 0;
                        break;
                    }
                }
                if(c)
                {
                    y++;
                }
                i--;
            }
        }
        printf("Case #%d: %d\n",x,y);
    }
    return 0;
}