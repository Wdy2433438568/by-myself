#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<Windows.h>


int hang, lie;
//define 0=无,1=墙，2=箱子，3=目的地，4=人，5=箱子进入目的地
//画地图：
int level_1[10][12]{
    0,0,0,0,1,1,1,0,0,0,0,0,
	0,0,0,0,1,3,1,0,0,0,0,0,
	0,0,0,0,1,0,1,1,1,1,1,1,
	1,1,1,1,1,2,0,2,0,0,3,1,
	1,3,0,0,0,2,4,1,1,1,1,1,
	1,1,1,1,1,1,2,1,0,0,0,0,
	0,0,0,0,0,1,0,1,0,0,0,0,
	0,0,0,0,0,1,0,1,0,0,0,0,
	0,0,0,0,0,1,3,1,0,0,0,0,
	0,0,0,0,0,1,1,1,0,0,0,0
};




//显示地图
void showgame()
{
	int i;
	int n;
	for (i = 0; i <10; i++)
	{
		for (n = 0; n < 12; n++)
		{
			switch (level_1[i][n])
			{
			case 0:
				printf("  ");
				break;
			case 1:
				printf("■");
				break;
			case 2:
				printf("□");
				break;
			case 3:
				printf("☆");
				break;
			case 4:
				printf("♂");
				hang = i;
				lie = n;
				break;
			case 5:
				printf("⊙");
				break;
			case 9:
				printf("◆");

			}
		
		}

			
		printf("\n");
		
	}

}


//控制游戏
void cg()
{
	int input;
	input = _getch();
	switch (input)
	{
	case 'w':
		if (level_1[hang - 1][lie] == 0)//空地
		{
			level_1[hang - 1][lie] = 4;
			level_1[hang][lie] = 0;
		}
		if (level_1[hang - 1][lie] == 1)//墙
		{
			level_1[hang - 1][lie] = 1;
			level_1[hang][lie] = 4;
		}
		if (level_1[hang - 1][lie] == 2)//箱子
		{

			if (level_1[hang - 2][lie] == 0)
			{

				level_1[hang - 2][lie] = 2;
				level_1[hang - 1][lie] = 4;
				level_1[hang][lie] = 0;
			}

			if (level_1[hang - 2][lie] == 1)
			{
				level_1[hang][lie] = 4;
				level_1[hang -1][lie] = 2;
				level_1[hang - 2][lie] = 1;
			}
			if (level_1[hang - 2][lie] == 3)
			{
				level_1[hang][lie] = 0;
				level_1[hang - 1][lie] = 4;
				level_1[hang - 2][lie] = 9;
			}
		}
		break;

	case 's':
		if (level_1[hang + 1][lie] == 0)//空地
		{
			level_1[hang + 1][lie] = 4;
			level_1[hang][lie] = 0;
		}
		if (level_1[hang + 1][lie] == 1)//墙
		{
			level_1[hang + 1][lie] = 1;
			level_1[hang][lie] = 4;
		}
		if (level_1[hang + 1][lie] == 2)//箱子
		{

			if (level_1[hang+2][lie] == 0)
			{

				level_1[hang+2][lie] = 2;
				level_1[hang+1][lie] = 4;
				level_1[hang][lie] = 0;
			}

			if (level_1[hang+2][lie] == 1)
			{
				level_1[hang][lie] = 4;
				level_1[hang+1][lie] = 2;
				level_1[hang+2][lie] = 1;
			}
			if (level_1[hang+2][lie] == 3)
			{
				level_1[hang][lie] = 0;
				level_1[hang+1][lie] = 4;
				level_1[hang+2][lie] = 9;
			}
		}
		break;
	case'a':
		if (level_1[hang][lie - 1] == 0)//空地
		{
			level_1[hang][lie - 1] = 4;
			level_1[hang][lie] = 0;
		}
		if (level_1[hang][lie - 1] == 1)//墙
		{
			level_1[hang][lie - 1] = 1;
			level_1[hang][lie] = 4;
		}
		if (level_1[hang][lie - 1] == 2)//箱子
		{

			if (level_1[hang][lie - 2] == 0)
			{
				
				level_1[hang][lie - 2] = 2;
				level_1[hang][lie - 1] = 4;
				level_1[hang][lie] = 0;
			}
			
			if (level_1[hang][lie - 2 ]== 1)
			{
				level_1[hang][lie] = 4;
				level_1[hang][lie - 1] = 2;
				level_1[hang][lie - 2] = 1;
			}
			if (level_1[hang][lie - 2] == 3)
			{
				level_1[hang][lie] = 0;
				level_1[hang][lie - 1] = 4;
				level_1[hang][lie - 2] = 9;
			}
		
		}
		break;
	
		 
		//define 0=无,1=墙，2=箱子，3=目的地，4=人，5=箱子进入目的地

		 
		 
	case'd':
		if (level_1[hang][lie + 1] == 0)//空地
		{
			level_1[hang][lie + 1] = 4;
			level_1[hang][lie] = 0;
		}
		if (level_1[hang][lie + 1] == 1)//墙
		{
			level_1[hang][lie + 1] = 1;
			level_1[hang][lie] = 4;
		}
		if (level_1[hang][lie + 1] == 2)//箱子
		{

			if (level_1[hang][lie + 2] == 0)
			{

				level_1[hang][lie + 2] = 2;
				level_1[hang][lie + 1] = 4;
				level_1[hang][lie] = 0;
			}

			if (level_1[hang][lie + 2] == 1)
			{
				level_1[hang][lie] = 4;
				level_1[hang][lie + 1] = 2;
				level_1[hang][lie + 2] = 1;
			}
			if (level_1[hang][lie + 2] == 3)
			{
				level_1[hang][lie] = 0;
				level_1[hang][lie + 1] = 4;
				level_1[hang][lie + 2] = 9;
			}

		}
		break;
	}
}

//得分
int score()
{
	int i, j, num;
	num = 0;
	for (i = 0; i <= 10; i++)
	{
		for (j = 0; j <= 10; j++)
		{
			if (level_1[i][j] == 9)
			{
				num++;
			}
		}
	}
	printf("\n\n\n你的得分为:%d\n", num);
	return 0;
}
//胜负判断
void sfpd()
{
	int num=0;
	int k = 4; 
	int i, j;
	for (i = 0; i <= 10; i++)
	{
		for (j = 0; j <= 12; j++)
		{
       
		}
		
	}
	
	

}


int main()//主函数
{
	SetConsoleTitle("推箱子");
	



	while (1)
	{
	
		
		system("color EC");
		showgame();
		score();
		cg();
	
		system("cls");

	}
	
	
	return  0;
}

