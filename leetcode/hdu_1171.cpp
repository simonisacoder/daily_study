# include <bits/stdc++.h>
using namespace std;

#define N 105
#define max 250005
int num[N],value[N];

long long ans[max];
long long tmp[max];

int main()
{
    int n;
    int sum = 0;
    while(cin >> n && n != -1)
    {
        for(int i = 0; i < n; i++)
        {
            cin >> value[i] >> num[i];
            sum += value[i] * value[i];
        }
        ans[0] = 1;
        for(int i = 0;i < n;i++)
        {

            for(int j = 1; j < num[i]; j++)
            {
                
            }
        }
    }
}
