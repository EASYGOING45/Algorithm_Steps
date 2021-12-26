#include "LinkedList.h"

LinkedList::LinkedList()
{
    cout<<"---��ʼ������---"<<endl;
    this->head=new Node(1e9);
    this->size++;
}

LinkedList::~LinkedList()
{
    Node* workNode=head;
    while(head!=nullptr)
    {
        head=head->next;
        delete workNode;
        workNode=head;
    }
    this->size=0;
}

void LinkedList::addAtTail(int newVal)
{
    //��ӵ�β�ڵ����
    Node* workNode=new Node(0);
    Node* newNode=new Node(newVal);
    workNode=head;
    for(int i=0;i<size;i++)
    {
        if(workNode->next!=nullptr)
        {
            workNode=workNode->next;
        }
    }
    workNode->next=newNode;
    this->size++;
}

void LinkedList::addAtSomeWhere(int index,int newVal)
{
    //����Ԫ�ص�ָ��λ��
    Node* workNode=head;    //����ָ�� ������������
    int count=0;            //������
    while(workNode!=nullptr && count<index-1)
    {
        //��λ������������ǰһ�����
        workNode=workNode->next;
        count++;
    }
    if(workNode==nullptr)
    {
        throw "��������λ�ô���";
    }
    else
    {
        Node* newNode=new Node(newVal);
        newNode->next=workNode->next;
        workNode->next=newNode;
    }
}

void LinkedList::printList()
{
    //��������
    Node* workNode=new Node(0);
    workNode=head->next;
    while(workNode!=nullptr)
    {
        cout<<workNode->val<<" ";
        workNode=workNode->next;
    }
    cout<<endl;
}

int LinkedList::get(int index)
{
    //���ָ��λ�õ�����
    Node* workNode=head;
    int count=0;  //�ۼ�����ʼ��
    while(workNode!=nullptr && count<index)
    {
        workNode=workNode->next;
        count++;
    }
    if(workNode==nullptr)
    {
        throw "��������";
    }
    else
    {
        return workNode->val;
    }
}

void LinkedList::deleteByIndex(int index)
{
    //ɾ��ָ��λ�õ�Ԫ��
    Node* workNode=head;
    Node* temp=new Node(0);  //�洢Ҫ��ɾ���Ľ��
    int count=0;
    while(workNode!=nullptr && count<index-1)
    {
        //��λ��ǰһ�����
        workNode=workNode->next;
        count++;
    }
    if(workNode==nullptr)
    {
        throw "λ�ô���";
    }
    else
    {
        temp=workNode->next;   //����ڴ�
        workNode->next=workNode->next->next;
    }
    delete temp;
}

int LinkedList::length()
{
    Node* workNode=head;
    int length=0;
    while(workNode->next!=nullptr)
    {
        workNode=workNode->next;
        length++;
    }
    return length;
}

void LinkedList::mySort()
{
    //�����㷨
    //����˼· �Ƚ�����Ԫ�ش洢��vector�� ��ʹ��vector�������㷨��������
    //��������
    Node* workNode=new Node(0);
    vector<int> v1;
    workNode=head->next;
    while(workNode!=nullptr)
    {
        v1.push_back(workNode->val);
        workNode=workNode->next;
    }
    sort(v1.begin(),v1.end());
    workNode=head->next;
    int count=0;
    while(workNode!=nullptr)
    {
        workNode->val=v1[count];
        workNode=workNode->next;
        count++;
    }
    cout<<v1.size()<<endl;
}
