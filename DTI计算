#include<Windows.h>
#include<stdio.h>
#include<conio.h>
void daifa()
{
	int a, f,c;
	float b,dti, w,d;
	printf("请输入6个月的平均工资（自然数）\n");
	scanf_s("%d", &a);
	w = a * 1.5;
	printf("请输入客户当前卡类负债(自然数)\n");
	scanf_s("%d", &f);
	b = f * 0.1;
	printf("请输入客户信用贷款月供\n");
	scanf_s("%d", &c);
	d = b + c;
	dti = d / w;
	if (dti <= 1.5)
	{
		printf("恭喜开单,dti为:%f\n\n", dti);
	}
	else
	{
		printf("非常抱歉,dti为:%f\n\n", dti);
	}

}

void anjie()
{
	int a, w, f,b;
	float c,d,dti;
	printf("请输入按揭房贷月供（自然数）\n");
	scanf_s("%d", &a);
	w = a * 8;
	printf("请输入客户当前卡类负债\n");
	scanf_s("%d", &f);
	d = f * 0.1;
	printf("请输入客户信用贷款月供\n");
	scanf_s("%d", &b);
	c = b + d;
	dti = c / w;
	if (dti <= 1.5)
	{
		printf("恭喜开单,dti为:%f\n\n", dti);
	}
	else
	{
		printf("非常抱歉,dti为:%f\n\n", dti);
	}
}

void quankuan()
{
	int a, f,b;
	float y, w, dti,c,d;
	printf("请输入全款房金额（自然数）\n");
	scanf_s("%d", &a);
	y = a * 0.7 * 0.05 / 12 + a * 0.7 / 30 / 12;
	w = y * 8;
	printf("请输入客户当前卡类负债\n");
	scanf_s("%d", &f);
	d = f * 0.1;
	printf("请输入客户信用贷款月供\n");
	scanf_s("%d", &b);
		c = d + b;
	dti = c / w;
	if (dti <= 1.5)
	{
		printf("恭喜开单,dti为:%f\n\n", dti);
	}
	else
	{
		printf("非常抱歉,dti为:%f\n\n", dti);
	}
}

void diya()
{
	int n, w, f,a;
	float i, dti,b,c,d;
	printf("请输入抵押年限(按月份计算)（自然数）\n");
	scanf_s("%d", &n);
	printf("请输入抵押金额(自然数)\n");
	scanf_s("%d", &w);
	i = w * 0.05 / 12 + w / n ;
	d = i * 8;
	printf("请输入客户当前卡类负债\n");
	scanf_s("%d", &f);
	c = f * 0.1;
	printf("请输入客户信用贷款月供\n");
	scanf_s("%d", &a);
	b = c + a;
	dti = b / d;
	if (dti <= 1.5)
	{
		printf("恭喜开单,dti为:%f\n\n", dti);
	}
	else
	{
		printf("非常抱歉,dti为:%f\n\n", dti);
	}

}

void gongjijin()
{
	int a, f,c;
	float dti, w,b,d;
	printf("请输入公积金月缴存额（单位＋个人)（自然数）\n");
	scanf_s("%d", &a);
	w = a / 0.12;
	printf("请输入客户当前卡类负债\n");
	scanf_s("%d", &f);
	b = f * 0.1;
	printf("请输入客户信用贷款月供\n");
	scanf_s("%d", &c);
	d = c + f;
	dti = f/a;
	if (dti <=1.5)
	{
		printf("恭喜开单,dti为:%f\n\n", dti);
	}
	else
	{
		printf("非常抱歉,dti为:%f\n\n", dti);
	}


}

void gongzi()
{
	//printf("[file :%s line :%d]\n", __FILE__, __LINE__);

	printf("请输入工资类型\n");
	printf("1.自雇/标薪\n");
	printf("2.自由职业\n");

	int a, b, d, e, g,i,k,l,m;
	float c, dti, dtti, f,h,j;
	a = getchar();
	scanf_s("%d", &a);
	switch (a)
	{
	case 1:
		printf("请输入结息:\n");
		scanf_s("%d", &b);
		c = b *1100/ 3;
		printf("请输入客户当前卡类负债\n");
		scanf_s("%d", &d);
		h = d * 0.1;
		printf("请输入客户信用贷款月供\n");
		scanf_s("%d", &i);
		j = h + i;
		dti = j / c;
		if (dti <= 5)
		{
			printf("恭喜开单dti为:%f\n\n", dti);
		}
		else
		{
			printf("非常抱歉，dti为:%f\n\n", dti);
		}
		break;
	case 2:
		printf("请输入结息:\n");
		scanf_s("%d", &e);
		f = e *1100/ 6;
		printf("请输入客户当前卡类负债\n");
		scanf_s("%d", &g);
		m = g * 0.1;
		printf("请输入客户信用贷款月供\n");
		scanf_s("%d", &k);
		l = k + m;
		dtti = l / f;
		if (dtti <= 5)
		{
			printf("恭喜开单dti为:%f\n\n", dtti);
		}
		else
		{
			printf("非常抱歉，dti为:%f\n\n", dtti);
		}
		break;
	}


}
int main()
{
	int input = 0;
	bool flag = true;

	do
	{
		printf("           请选择认收条件      \n");
		printf("-------------------------------\n");
		printf("   1.流水          2.代发工资  \n");
		printf("   3.按揭房贷      4.全款房    \n");
		printf("   5.抵押房        6.公积金    \n");
		printf("-------------------------------\n");

		scanf_s("%d", &input);
		//printf("input:%d\n", input);

		switch (input)
		{
		case 1:
			//printf("[file :%s line :%d]\n", __FILE__, __LINE__);
			gongzi();
			break;
		case 2:
			daifa();
			break;
		case 3:
			anjie();
			break;
		case 4:
			quankuan();
			break;
		case 5:
			diya();
			break;
		case 6:
			gongjijin();
			break;
		case 7:
			flag = false;
			printf("退出\n");
			break;
		default:
			printf("没有匹配的输入值:%c\n", input);
		}

		//printf("[file :%s line :%d]\n", __FILE__, __LINE__);
		//system("cls");
	} while (flag);

	return 0;

}
