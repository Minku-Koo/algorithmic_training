#include <stdio.h>

int cnt;


int func(char* pattern, char* target)
{
	int i, j, cnt, start, end;
	i = 0; j = 0; cnt = 0;
	start = strlen(pattern);
	end = strlen(target);
	while (j < start && i < end) {
		if (target[i] != pattern[j]) {
			i = i - j;
			j = -1;
		}
		i++;
		j++;
		cnt++;
	}
	
	if (j == start) 
			return i - start;
	else return i;
}

bool same(char a, char b, int *cnt) {
	(*cnt)++;
	return a == b;
}

void boy(const char* st, const char* ch) {
	int skip[256] = {};
	int st_ = strlen(st);
	int ch_ = strlen(ch);
	int result = 0;
	for (int i = ch_ - 2; i >= 0; i--) {
		if (skip[ch[i]] == 0) 
			skip[ch[i]] = ch_ - 1 - i;
	}
	for (int i = 0; i < 256; i++) {
		if (skip[i] == 0) 
			skip[i] = ch_;
	}
	
	for (int i = ch_ - 1, j; i < st_; i += skip[st[i]]) {
		bool success = false;
		for (j = 0; j < ch_; j++) {
			if (!same(st[i - j], ch[ch_ - 1 - j], &result)) {
				success = true;
				break;
			} 
		}
		if (!success) 
			printf("%d\n", i-ch_ + 1);
	}
}

