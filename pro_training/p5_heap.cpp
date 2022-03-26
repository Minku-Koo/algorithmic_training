//heap


#include <set>
#include <cstring>
using namespace std;
 
 
struct DATA {
    int id;
    char name[11];
    bool operator < (const DATA &b) const
    {
        if (name != b.name) 
			return name > b.name;
        return id < b.id;
    }
 
};
 
set <DATA > pr_q;


void init() {
    pr_q = {};
}
 
void clear() {
    pr_q = {};
}
 
void push(int idx, char* name) {
    pr_q.insert({idx, name});
}
 
int pop() {
    auto result = pr_q.begin();
    pr_q.erase(result);
    return result->id;
}
 
int top() {
    auto result = pr_q.begin();
    return result->id;
}
 