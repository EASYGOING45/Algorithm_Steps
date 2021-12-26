#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
/*
*Author:YiXing Liu
*Date:2021
*Des:Singly Linked List
*/

//手撕单向链表
class LinkedList
{
private:
    struct Node
    {
        int val;      //数据域
        Node* next;   //后继节点
        Node(int newVal):val(newVal),next(nullptr) {}
    };
    Node* head;  //头指针应该置空
    int size;
public:
    LinkedList();
    ~LinkedList();
    void addAtTail(int newVal);  //添加到尾节点之后
    void addAtSomeWhere(int index,int newVal);  //添加到指定位置
    void printList();   //遍历输出链表的所有值
    int get(int index);  //获得指定位置的链表值
    void deleteByIndex(int index); //删除指定位置的元素
    int length(); //返回单向链表的长度  不包含头部节点
    void mySort();   //单向链表排序
};
