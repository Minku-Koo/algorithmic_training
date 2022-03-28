
#define MAX_ 101
int childnum[MAX_];
int child[MAX_][5];


void dfs_init(int N, int path[100][2])
{
    for(int i=0; i<MAX_; i++){
		childnum[i] = 0;
	}
	for(int i=0; i<N; i++){
		child[path[i][0]][childnum[path[i][0]]++] = path[i][1];
	}
}

int deep_dfs(int king, int now){
	if(king < now) return now;
	int result;
	for(int j=0; j<childnum[now]; j++){
		result = deep_dfs(king, child[now][j]);
		if(result != -1) return result;
	}
	return -1;
}

int dfs(int n)
{
	
	return deep_dfs(n, n);
}