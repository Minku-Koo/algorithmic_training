// https://www.acmicpc.net/problem/1158
// clear

#include <iostream>
#include <stdio.h>

using namespace std;

struct Node{
	int data;
	Node *next = NULL;
	Node *prev = NULL;
};

int nSize, k;
Node *now = new Node;
Node *tail = new Node;

void init(){
	
	for(int i = 1; i <= nSize; ++i){
		Node *t = new Node;
		t->data = i;
		if(i == 1){
			// first input
			now = t;
			tail = t;
		}else if(i == nSize){
			// final input
			t->prev = tail;
			tail->next = t;
			
			now->prev = t;
			t->next = now;
			
			now = now->prev; // start from like zero
		}else{
			t->prev = tail;
			tail->next = t;
			
			tail = t;
		}
	}
	
	
}

int remNode(){
	if(nSize == 1){
		return now->data;
	}
	// remove node
	for(int j = 0; j < k; ++j){
		// move k 
		now = now->next;
	}
	
	// remove node
	Node *pNode = new Node;
	Node *nNode = new Node;
	pNode = now->prev;
	nNode = now->next;
	
	pNode->next = nNode;
	nNode->prev = pNode;
	
	return now->data;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	cin >> nSize >> k;
	
	init();
	
	printf("<");
	for(int j = 0; j < nSize; ++j){
		int ans = remNode();
		if(j == nSize - 1){
			printf("%d>\n", ans);
		}else{
			printf("%d, ", ans);
		}
	}
	
	return 0;
}

