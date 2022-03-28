
#define MAX_LEN (20)
#define MAX_ 300001

unsigned long hashtable[MAX_] ;

char search(char word[MAX_LEN + 1])
{
	unsigned long hash = 2311;
    int  key;
	int c;
	while(c = *word++){
		
		hash = ((hash << 5) + hash) + c;
	}
	
	key = hash % MAX_ ;
	
	while(hashtable[key]!=0){
		if(hashtable[key]==hash){
			return '1';
		}else{
			key = (key + 1) % MAX_ ;
		}
	}
	hashtable[key] = hash;
	
	return '0';
	
}




