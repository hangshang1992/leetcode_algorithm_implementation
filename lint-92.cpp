class Solution {
public:
    
    int backPack(int m, vector<int> &a) {
        int n = a.size();
        if(n==0||m==0)
        	return 0;
        
        vector<vector<bool> > f(n+1,vector<bool>(m+1));		
		
		for(int i=0;i<=m;i++)
			f[0][i]=0;
		
		f[0][0]=1; 
			
		for(int i=1;i<=n;i++)
			for(int j=0;j<m+1;j++)
			{
				f[i][j]=f[i-1][j];
				if(j>=a[i-1])			//当前承重比当前物品的重量重时 
				{
					f[i][j]=f[i][j]||f[i-1][j-a[i-1]];	
				}
			}
			
		for(int i=m;i>=0;--i)
		{
			if(f[n][i])
				return i;
		}				 
        
    }
};
