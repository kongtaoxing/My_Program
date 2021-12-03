#include<graphics.h>
#include<conio.h>
 
#define M 14
#define G 30
 
struct Grid
{
    int left;
    int right;
    int up;
    int down;
    int arr[M][M];
    int num;
}grid;
 
void Welcome();
void PaintGrid(int mx, int my, int num, int color);
void OnLButtonDown(MOUSEMSG m, int num);
void OnRButtonDown(int num);
int JudheFull(int num, int arr[M][M]);
void NextLevel(int num);
int Dispatch();
 
int main()
{
    int end = 0;
    grid.num = 4;
    Welcome();
    PaintGrid(320, 240, grid.num, RGB(0, 255, 0));
    while (end != 1)
    {
        end = Dispatch();
    }
    closegraph();
    return 0;
}
//欢迎界面
void Welcome()
{
    initgraph(640, 480);
    cleardevice();//刷新
    settextcolor(RGB(0, 255, 0));
    settextstyle(64, 0, "方正情不知所起");  //字体可以根据自己的电脑做相应的调整
    outtextxy(200, 50, "点灯游戏");
 
    settextcolor(WHITE);
    settextstyle(20, 0, "微软雅黑");
    outtextxy(100, 200, "每点击一个格子，上下左右的格子也会做出与现状相反的动作");
    outtextxy(100, 240, "总共11关，左键填色，右键重来");
 
    int c = 255;
    while (!_kbhit())     //_kbhit()->键盘录入  !是取反
    {
        settextcolor(RGB(0, c, 0));
        outtextxy(280, 400, "请按任意键继续");
        c -= 8;
        if (c < 0)
            c = 255;
        Sleep(20);
    }
    _getch();
    cleardevice();
}
 
/*游戏主界面*/
 
void PaintGrid(int mx, int my, int num, int color)
{
    int x, y, nx, ny;//游戏左右上下边界
    grid.left = mx - num * G / 2;
    grid.right = mx + num * G / 2;
    grid.up = my - num * G / 2;
    grid.down = my + num * G / 2;
 
    //绘制格子的方法
    setlinecolor(color);
    for (x = grid.left; x <= grid.right; x += G)
        line(x, grid.up, x, grid.down);
    for (y = grid.up; y <= grid.down; y += G)
        line(grid.left, y, grid.right, y);
 
    //外边框
    for (x = 20; x > 10; x--)
    {
        rectangle(grid.left - x, grid.up - x, grid.right + x, grid.down + x);
        Sleep(10);
    }
    //清空单元格
    for (x = 0; x < num; x++)
        for (y = 0; y < num; y++)
            grid.arr[x][y] = -1;
    for (nx = 0; nx < num; nx++)
        for (ny = 0; ny < num; ny++)
        {
            setfillcolor(BLACK);
            x = nx * G + grid.left;
            y = ny * G + grid.up;
            solidrectangle(x + 1, y + 1, x + G - 1, y + G - 1);
        }
 
}
 
//鼠标左键点击
void OnLButtonDown(MOUSEMSG m, int num)
{
    int nx, ny, x, y;
    if (m.x > grid.left && m.x<grid.right && m.y>grid.up && m.y < grid.down)
    {
        //坐标转换成下标
        nx = (int)(m.x - grid.left) / G;
        ny = (int)(m.y - grid.up) / G;
        grid.arr[nx][ny] = -grid.arr[nx][ny];
        if (nx >= 0 && nx < num - 1)
            grid.arr[nx + 1][ny] = -grid.arr[nx + 1][ny];
        if (nx > 0 && nx < num)
            grid.arr[nx - 1][ny] = -grid.arr[nx - 1][ny];
        if (ny >= 0 && ny < num - 1)
            grid.arr[nx][ny + 1] = -grid.arr[nx][ny + 1];
        if (ny > 0 && ny < num)
            grid.arr[nx][ny - 1] = -grid.arr[nx][ny - 1];
 
        for (nx = 0; nx < num; nx++)
            for (ny = 0; ny < num; ny++)
            {
                if (grid.arr[nx][ny] == 1)
                    setfillcolor(GREEN);
                else
                    setfillcolor(BLACK);
                x = nx * G + grid.left;
                y = ny * G + grid.up;
                solidrectangle(x + 1, y + 1, x + G - 1, y + G - 1);
            }
    }
}
//右键清空单元格
void OnRButtonDown(int num)
{
    int x, y, nx, ny;
    for (x = 0; x < num; x++)
        for (y = 0; y < num; y++)
            grid.arr[x][y] = -1;
    for (nx = 0; nx < num; nx++)
        for (ny = 0; ny < num; ny++)
        {
            setfillcolor(BLACK);
            x = nx * G + grid.left;
            y = ny * G + grid.up;
            solidrectangle(x + 1, y + 1, x + G - 1, y + G - 1);
        }
}
 
int JudheFull(int num, int arr[M][M])
{
    int c = -1;//格子状态
    int nx = 0, ny = 0;
    while (nx < num && ny < num)
    {
        for (nx = 0; nx < num; nx++)
            for (ny = 0; ny < num; ny++)
                if (arr[nx][ny] == 1)
                    continue;
                else
                    return c;
    }
    c = 1;
    return c;
}
 
 
void NextLevel(int num)
{
    BeginBatchDraw();
    for (int y = 0; y <= 480; y += 5)
    {
        setlinecolor(RGB(255, 0, 0));
        line(0, y, 640, y);
        line(0, 480 - y, 640, 480 - y);
        settextstyle(20, 0, "黑体");
        outtextxy(300, y - 8, "下一关");
        FlushBatchDraw();
        Sleep(16);
        setfillcolor(BLACK);
        solidrectangle(0, y, 640, y - 10);
        solidrectangle(0, 480 - y, 640, 480 - y + 1);
    }
    EndBatchDraw();
    PaintGrid(320, 240, num, RGB(0, 255, 0));
}
 
int Dispatch()
{
    MOUSEMSG m;
    while (1)
    {
        m = GetMouseMsg();
        switch (m.uMsg)
        {
        case WM_LBUTTONDOWN:
            OnLButtonDown(m, grid.num);
            if (JudheFull(grid.num, grid.arr) == 1)
            {
                grid.num++;
                if (grid.num > M)
                {
                    return 1;
                    break;
                }
                else
                    NextLevel(grid.num);
            }
            break;
        case WM_RBUTTONDOWN:
            OnRButtonDown(grid.num);
            break;
        default:
            break;
        }
 
    }
}
