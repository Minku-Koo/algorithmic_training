
#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <chrono>
#include <stdio.h>

using namespace std;
using namespace chrono;

#define CMD_INIT 1
#define CMD_ADD 2
#define CMD_DEL 3
#define CMD_UPDATE_STUDENT 4
#define CMD_UPDATE_CLASS 5
#define CMD_WORST_STUDENT 6

extern void init();
extern void add(int mID, int mClass, int mScore);
extern void del(int mID);
extern void updateStudent(int mID, int mScore);
extern void updateClass(int mClass, int mChangeScore);
extern int worstStudent(int mClass);

/////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////

static bool run()
{
	int numQuery;

	int mID, mClass, mScore, mChangeScore;

	int userAns, ans;

	bool isCorrect = false;

	scanf("%d", &numQuery);

	for (int i = 0; i < numQuery; ++i)
	{
		int cmd;
		scanf("%d", &cmd);
		switch (cmd)
		{
		case CMD_INIT:
			init();
			isCorrect = true;
			break;
		case CMD_ADD:
			scanf("%d %d %d", &mID, &mClass, &mScore);
			add(mID, mClass, mScore);
			break;
		case CMD_DEL:
			scanf("%d", &mID);
			del(mID);
			break;
		case CMD_UPDATE_STUDENT:
			scanf("%d %d", &mID, &mScore);
			updateStudent(mID, mScore);
			break;
		case CMD_UPDATE_CLASS:
			scanf("%d %d", &mClass, &mChangeScore);
			updateClass(mClass, mChangeScore);
			break;
		case CMD_WORST_STUDENT:
			scanf("%d", &mClass);
			// printf("class %d\n", mClass);
			userAns = worstStudent(mClass);
			scanf("%d", &ans);
			if (userAns != ans)
			{
				isCorrect = false;
				printf("wrong %d %d\n",userAns, isCorrect);
			}
			// printf("%d\n",99);
			break;
		default:
			isCorrect = false;
			break;
		}
	}

	return isCorrect;
}

int main()
{
	setbuf(stdout, NULL);
	//freopen("sample_input.txt", "r", stdin);

	int T, MARK, total_time_cost = 0;
	system_clock::time_point tmp;
	scanf("%d %d", &T, &MARK);

	for (int tc = 1; tc <= T; tc++)
	{
		tmp = system_clock::now();
		int score = run() ? MARK : 0;
		total_time_cost += duration_cast<microseconds>(system_clock::now() - tmp).count();
		printf("#%d %d\n", tc, score);
	}
	printf("#TIME %d\n", total_time_cost);

	return 0;
}

/////////////////

#define MAX_CALL 100001

struct Node {
	int id;
	int cl;
	int score;
	Node* next;
};

int nodeCnt[5];
Node node[5][MAX_CALL];


Node *head[5];
Node* getNode(int mID, int mClass, int mScore, Node* ptr) {
	node[mClass-1][nodeCnt[mClass-1]].id = mID;
	node[mClass-1][nodeCnt[mClass-1]].cl = mClass;
	node[mClass-1][nodeCnt[mClass-1]].score = mScore;
	node[mClass-1][nodeCnt[mClass-1]].next = ptr;
	return &node[mClass-1][nodeCnt[mClass-1]++];
}

void init()
{
	
	for(int p=0; p<5; p++){
		head[p] = nullptr;
		nodeCnt[p]= 0;
	}
}

void add(int mID, int mClass, int mScore)
{
	Node* node_ = getNode(mID, mClass, mScore, nullptr);
	if(head[mClass-1]==nullptr){
		head[mClass-1] = node_;
		return;
	}
	node_->next = head[mClass-1];
	head[mClass-1] = node_;
	
}

void del(int mID)
{
	for(int a=1; a<6; a++){
		// printf("a %d\n", a);
		Node* preptr = head[a-1];
		Node* nextptr = head[a-1]->next;
		Node* tempptr;
		do{
			if(preptr->id == mID){
				
				if(head[a-1]->id == mID){
					// for(int j=0; j<5; j++) printf("%d class %d id\n", a, head[a-1]->id);
					head[a-1] = getNode(nextptr->id, nextptr->cl, nextptr->score, nextptr->next);
					// printf("dodo\n");
				}else if(preptr->next == nullptr){
					tempptr->next = nullptr;
				}else{
					preptr->next = nextptr->next;
				}
				return ;
			}
			tempptr = preptr;
			preptr = nextptr;
			if(nextptr==nullptr){
				break;
			}
			nextptr = nextptr->next;
			
		}while(true);
		
	}
	
}

void updateStudent(int mID, int mScore)
{
	for(int a=1; a<6; a++){
		Node* now = head[a-1];
		while(now!=nullptr){
			if( now->id == mID){
				now->score = mScore;
				return ;
			}
			now = now->next;
		}
	}
}

void updateClass(int mClass, int mChangeScore)
{
	Node* now = head[mClass-1];
	int prescore;
	while(now!=nullptr){
		if(now->cl == mClass){
			prescore = now->score + 0;
			if(prescore + mChangeScore > 5)
				now->score = 5;
			else if(prescore + mChangeScore < 1)
				now->score = 1;
			else
				now->score = prescore + mChangeScore;
			
		}
		now = now->next;
	}
}

int worstStudent(int mClass)
{
	int max_score = 0, scnt=0, max_id = 0;
	Node* now = head[mClass-1];
	
	while(now!=nullptr){
		if(now->cl == mClass){
					if(max_score < now->score){
					
					max_id = now->id;
					max_score = now->score;
					// printf("max id >> %d\n", max_id);
					continue;
				}
				if(max_score == now->score){
					if(max_id < now->id){
						max_id = now->id;
						// printf("max id > %d\n", max_id);
					}
				}
			// cnt++;
		}
		now = now->next;
	}
	
    return max_id;
}



