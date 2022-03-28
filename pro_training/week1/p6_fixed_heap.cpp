//heap
#include <iostream>
#include <unordered_map>
#include <string>
#include <set>
#include <cstring>
using namespace std;
 
 
struct DATA {
    int id;
    string name;
    bool operator < (const DATA &b) const
    {
        if (name != b.name) 
			return name > b.name;
        return id < b.id;
    }
 
};
 
set <DATA > pr_q;
unordered_map<int, string> lst;

void init() {
    pr_q = {};
	lst.clear();
}
 
void clear() {
    pr_q = {};
	lst.clear();
}
 

void push(int idx, char name[]) {
    lst[idx] = name;
    pr_q.insert({idx, name});
	
}
 
int pop() {
    auto result = pr_q.begin();
    pr_q.erase(result);
	lst.erase(result->id);
    return result->id;
}
 
 
 
void mod(int idx , char name[]){
    string getName = lst[idx];
    lst[idx] = name;
     
    auto b = pr_q.find(DATA{ idx, getName });
    pr_q.erase(b);
    pr_q.insert({ idx, name });
}