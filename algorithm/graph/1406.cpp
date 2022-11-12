// https://www.acmicpc.net/problem/1406
// clear

#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

struct Node{
	char c;
	Node *prev;
	Node *next;
};

int ln;
string s;
Node *nowNode;
Node *head, *tailNode;

// 초기 입력값 -> 링크드리스트 생성
void init(){
	nowNode = new Node;
	tailNode = new Node;
	head = new Node;
	
	tailNode->c = '.';
	tailNode->next = NULL;
	// s -> Node double linked list로 구현
	char cr = s[s.size() - 1];
	head->c = cr;
	head->prev = NULL;
	head->next = NULL;
	
	tailNode->prev = head;
	head->next = tailNode;
	nowNode = tailNode;
	
	for(int i = s.size() - 2; i >= 0; i--){
		// head에 추가
		cr = s[i];
		Node *t = new Node;
		t->c = cr;
		t->next = head;
		t->prev = NULL;
		
		head->prev = t;
		head = t;
	}
	
	
}

// true -> right
// 노드 이동
void moveCursur(bool dir){
	if(dir == true){
		// right
		if(nowNode->next != NULL){
			nowNode = nowNode->next;
		}
	}else{
		// left
		if(nowNode->prev != NULL){
			nowNode = nowNode->prev;
		}
	}
	return;
}

// 왼쪽 노드 삭제
void delCursur(void){
	if(nowNode->prev == NULL){
		return ;
	}
	Node * prevNode = new Node;
	prevNode = nowNode->prev; // have to removed
	
	if(prevNode->prev == NULL){
		nowNode->prev = NULL;
		head = nowNode;
	}else{
		Node *ppNode = prevNode->prev;
		ppNode->next = nowNode;
		nowNode->prev = ppNode;
	}
}

// 왼쪽에 노드 추가
void addChar(char newChar){
	Node *t = new Node;
	t->c = newChar;
	t->prev = NULL;
	t->next = nowNode;
		
	if(nowNode->prev == NULL){
		// first char
		nowNode->prev = t;
		head = t;
	}else{
		Node *pNode = nowNode->prev;
		
		t->prev = pNode;
		nowNode->prev = t;
		pNode->next = t;
	}
}

// 모든 링크드리스트 노드 출력
void result(){
	Node *t = head;
	while(t->c != '.'){
		printf("%c", t->c);
		t = t->next;
	}
}

int main(){
	int n;
	char cmd, inputChar;
	
	cin >> s >> n;
	
	init();
	
	for(int i = 0; i < n; i++){
		cin >> cmd;
		if(cmd == 'P'){
			cin >> inputChar;
			addChar(inputChar);
		}
		else{
			if(cmd == 'L') moveCursur(false);
			if(cmd == 'D') moveCursur(true);
			if(cmd == 'B') delCursur();
		}
	}
	
	result();
	
	return 0;
}

