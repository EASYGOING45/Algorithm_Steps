#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
/*
*Author:YiXing Liu
*Date:2021
*Des:Singly Linked List
*/

//��˺��������
class LinkedList
{
private:
    struct Node
    {
        int val;      //������
        Node* next;   //��̽ڵ�
        Node(int newVal):val(newVal),next(nullptr) {}
    };
    Node* head;  //ͷָ��Ӧ���ÿ�
    int size;
public:
    LinkedList();
    ~LinkedList();
    void addAtTail(int newVal);  //��ӵ�β�ڵ�֮��
    void addAtSomeWhere(int index,int newVal);  //��ӵ�ָ��λ��
    void printList();   //����������������ֵ
    int get(int index);  //���ָ��λ�õ�����ֵ
    void deleteByIndex(int index); //ɾ��ָ��λ�õ�Ԫ��
    int length(); //���ص�������ĳ���  ������ͷ���ڵ�
    void mySort();   //������������
};
