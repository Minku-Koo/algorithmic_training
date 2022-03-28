
int box[10][10];
int check[10][10];
int leng;
int dy[4] = {1,-1,0,0};
int dx[4] = {0,0,1,-1};

void bfs_init(int N, int map[10][10])
{
    
	for(int i=0; i<10; i++){
		for(int j=0; j<10; j++){
			box[i][j] = map[i][j];
		}
		
	}
	leng = N;
}



int bfs(int x1, int y1, int x2, int y2)
{
	x1--, y1--, x2--, y2--;
	
	int q[1001][3];
	int check[10][10]={0};
	int front = 0, rear = 0;
	int yy, xx, dist, y_, x_;
	
	q[rear][0] = y1;
	q[rear][1] = x1;
	q[rear++][2] = 0;
	check[y1][x1] = 1;
	
	while(front != rear){
		yy = q[front][0];
		xx = q[front][1];
		dist = q[front++][2];
		
		for(int j=0; j<4; j++){
			y_ = yy + dy[j], x_ = xx + dx[j];
			if(y_==y2 && x_==x2) return dist+1;
			if(y_<0 || y_>leng-1 || x_<0 || x_>leng-1 ) continue;
			if(box[y_][x_]==1||check[y_][x_]==1) continue;
			
			q[rear][0] = y_;
			q[rear][1] = x_;
			q[rear++][2] = dist + 1;
			check[y_][x_] = 1;
			
		}
	}
	
    return -1;
}







