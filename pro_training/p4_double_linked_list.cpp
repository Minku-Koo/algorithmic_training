//double linked list

#define MAX_NODE 10000

struct Node {
	int data;
	Node* prev;
	Node* next;
};

Node node[MAX_NODE];
int nodeCnt;
Node* head;

Node* getNode(int data) {
	node[nodeCnt].data = data;
	node[nodeCnt].prev = nullptr;
	node[nodeCnt].next = nullptr;
	return &node[nodeCnt++];
}

void init()
{
    head = nullptr;
    nodeCnt = 0;
}
 
void addNode2Head(int data)
{
    Node* node_ = getNode(data);
    if (head == nullptr){ 
		head = node_; 
		return; 
	}
 
    node_->next = head;
    head->prev = node_;
    head = node_;
}
 
void addNode2Tail(int data)
{
    Node* node_ = getNode(data);
    if (head == nullptr){
		head = node_;
		return;
	}
 
    Node* target = head;
    while (target->next != nullptr){
        target = target->next;
    }
    target->next = node_;
    node_->prev = target;
}
 
void addNode2Num(int data, int num)
{
    Node* node_ = getNode(data);
    if (head == nullptr || num == 1) {
		addNode2Head(data); 
		return;
	}
 
    Node* target = head;
    for (int i = 2; i < num; i++) {
        target = target->next;
    }
 
    node_->prev = target;
    node_->next = target->next;
    if(target->next != nullptr)
        target->next->prev = node_;
    target->next = node_;
}
 
int findNode(int data)
{
    Node* target = head;
    int num = 1;
    while (target != nullptr) {
        if (target->data == data) {
            break;
        }
        target = target->next;
        num++;
    }
    return num;
}
 
void removeNode(int data)
{
    Node* target = head;
    while (target != nullptr) {
        if (target->data == data) {
            break;
        }
        target = target->next;
    }
	
    if (target == nullptr) 
		return;
	
    if (target->prev != nullptr) 
        target->prev->next = target->next;
    else{ // if head
        target->next->prev = nullptr;
        head = target->next;
    }
	
    if (target->next != nullptr) // if tail
        target->next->prev = target->prev;
    else 
        target->prev = nullptr;
 
 
}
 
// count node 
int getList(int output[MAX_NODE])
{
    int count = 0;
    Node* target = head;
    while (target != nullptr) {
        output[count++] = target->data;
        target = target->next;
    }
    return count;
}
 
int getReversedList(int output[MAX_NODE])
{
    int count = 0;
    Node* target = head;
    while (target->next != nullptr) {
        target = target->next;
    }
 
    while (target != nullptr) {
        output[count++] = target->data;
        target = target->prev;
    }
    return count;
}


