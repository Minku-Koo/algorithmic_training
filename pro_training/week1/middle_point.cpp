
// # F = G * m1 * m2 / (d*d)
// # 소수점 10번째까지 출력





// #1 1.5000000000
// #2 1.0306534300
// #3 462.5504629633
// #4 1.4060952085 2.5939047915
// #5 2.5328594461 3.7271944335 6.0999536409
// #6 6.3428568767 11.5477377494 15.9641592998 24.9267991615
// #7 57.8805685415 81.8651598883 91.0573691382 105.0835650491 133.2934094881
// #8 74.2211477711 190.6837563313 305.8269181686 348.3304429927 470.2694219293 555.4943093854
// #9 21.5171374463 47.9890597763 68.6536668433 82.9131954023 95.0052272762 99.1999097770 116.4978330953
// #10 11.5573600056 24.0238341337 38.4847676134 44.6137453708 64.7500445424 126.9908128982 184.3221650927 197.9760596291 266.0574653677



#include<iostream>
#include<cmath>
using namespace std;
// double getPoser[2];
double* power(int x_coords[], int weight[], int count, double pos){
	double left=0.0, right=0.0;
	for(int i=0; i<count; i++){
		double x = x_coords[i] *1.0;
		if(x==pos ) continue;
		
		if (x<pos) {
			if(x-pos<0)
				left += (double)weight[i] / pow(( (x - pos)*-1 ) , 2);
			else left += (double)weight[i] / pow(( x - pos ) , 2);
		}
		else  right += (double)weight[i] / pow(( x - pos ) ,2);
	}
	static double getPoser[2] = {left, right};
	return  getPoser;
}

double* solution(int count, int info[]){
	// x_coords, weight = info[:count], info[count:]
	
	double result[10]={0.0,};
	int cnt=0;
	// static double side[2];
	double start, end, org_start, org_end, moc;
	int x_coords[count], weight[count];
	
	for(int j=0; j<count*2; j++){
		if(j<count) x_coords[j] = info[j];
		else  weight[j-count] = info[j];
	}
	
	// for(int k=0; k<count; k++) printf(">%d ", x_coords[k]);
	
	printf("%d ", 1);
	for(int i=0; i<count-1 ; i++){
		int change, status;
		
		start = (x_coords[i]+x_coords[i+1])/2.0;
		end = x_coords[i+1];
		org_start = x_coords[i];
		org_end = end;
		moc= 0.1;
		
		// printf("start, end %f %f ", start, end);
		double* side = power(x_coords, weight, count, start);
		if(side[0]>side[1]) status = 0;
		else status =1;
		
		double temp;
		printf("r and l %d %d ", side[0], side[1]);
		while(side[0]!=side[1]){
			printf("%d ", 2);
			temp = start;
			double* side = power(x_coords, weight, count, start);
			
			if(side[0]>side[1]) change = 0;
			else change =1;
			
			if (change==0)
				start += moc;
			else
				start -= moc;
			
			if (start < org_start){
				start += moc;
				moc *= 0.1;
			}
			if (start > org_end){
				start -= moc;
				moc *= 0.1;
			}
			if (change!=status){
				moc *= 0.1;
				status = change;
			}
			
			double check = side[0]-side[1];
			if(check < 0) check *= -1;
			
			if (check < pow(0.1, 8) && start == temp)
                break;
			
		}
		
		result[cnt++] = start;
		
	}
	
	
	return result;
}


int main(int argc, char** argv)
{
	int test_case;
	int T;
	
	cin>>T;
	/*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
	for(test_case = 1; test_case <= T; ++test_case)
	{

		/////////////////////////////////////////////////////////////////////////////////////////////
		/*
			 이 부분에 여러분의 알고리즘 구현이 들어갑니다.
		 */
		/////////////////////////////////////////////////////////////////////////////////////////////
		int count;
		scanf("%d", &count);
		int info[count];
		for(int j=0; j<count*2; j++)
			scanf("%d", &info[j]);

		// 표준출력(화면)으로 답안을 출력합니다.
		cout << "#" << test_case << endl;
		
		// int* r;
		double* r =  solution(count, info);
		for(int j=0; j<count*2; j++)
			printf("%f ", r[j]);
		
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}

