// https://www.acmicpc.net/problem/2346
// clear

#include <iostream>
#include <stdio.h>
#include <string.h>

#define MM 1001

using namespace std;

int nSize; // 링크드 리스트 길이

struct Node{
	int num, idx; // 이동할 숫자, 현재 인덱스
	Node* next = NULL;
	Node* prev = NULL;
};

Node* now = new Node; // 현재 노드
Node* tail = new Node; // 마지막 노드 (처음 노드와 연결 위해)

void solve(){
	/// num 만큼 이동 + 삭제 -> nSize만큼 반복
	
	Node *t = tail; // tail == 최초 입력 노드
	for(int j = 0; j < nSize; ++j){
		int move = t->num;
		printf("%d ", t->idx);
		// 삭제
		Node *nNode = new Node;
		Node *pNode = new Node;
		nNode = t->next;
		pNode = t->prev;
		
		nNode->prev = pNode;
		pNode->next = nNode;
		
		// num만큼 이동
		if(move > 0){
			// prev
			for(int i = 0; i < move; ++i)
				t = t->prev;
		}else{
			// next
			for(int i = 0; i < move * -1; ++i)
				t = t->next;
		}
	}
	
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	cin >> nSize;
	int n;
	
	for(int i = 0; i < nSize; ++i){
		cin >> n;
		Node *t = new Node;
		t->num = n;
		t->idx = i + 1;
		
		if(i == 0){ // 최초 입력 -> tail 설정
			tail = t;
		}else if(i == nSize - 1){ // 마지막 입력 -> 처음과 현재 연결
			now->prev = t;
			tail->next = t;
			t->prev = tail;
			t->next = now;
		}else{ // 처음도 마지막도 아닌 경우 -> 앞뒤만 연결
			now->prev = t;
			t->next = now;
		}
		
		now = t;
		
	}
	
	
	solve();
	
	return 0;
}

