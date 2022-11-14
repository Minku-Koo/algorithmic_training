// https://www.acmicpc.net/problem/5397
// clear


#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

int tc;
string command;
char cmd;

struct Node {
	char c;
	Node* prev = NULL;
	Node* next = NULL;
};

Node* head;
Node* now;
Node* fin;

void init() {
	head = new Node;
	now = new Node;
	fin = new Node;
	
	head->next = fin;
	fin->prev = head;

	now = head;
}

void insertCmd(char data) {
	Node* t = new Node;
	
	t->c = data;
	t->prev = now;
	t->next = now->next;
	
	now->next->prev = t;
	now->next = t;
	now = t;
}

void moveCmd(int d) {
	if (d == 1) {
		// right
		if (now->next == fin) {
			return;
		}
		now = now->next;
	}
	else {
		// left
		if (now == head) {
			return;
		}
		now = now->prev;
	}
}

void remCmd() {
	// remove left
	if (now == head) {
		return;
	}
	now->prev->next = now->next;
	now->next->prev = now->prev;
	now = now->prev;
}

void pp() {
	for(Node* temp = head->next; temp != fin; temp = temp->next)
            cout << temp->c;
        cout << '\n';
}

int main() {
	cin >> tc;
	for (int t = 0; t < tc; t++) {
		cin >> command;
		init();
		for (int i = 0; i < command.size(); i++) {
			cmd = command[i];
			if (cmd == '<') {
				moveCmd(0);
			}
			else if (cmd == '>') {
				moveCmd(1);
			}
			else if (cmd == '-') {
				remCmd();
			}
			else {
				insertCmd(cmd);
			}
		}
		pp();
	}
	
	return 0;
}