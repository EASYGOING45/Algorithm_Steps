#include "LinkedList.h"

LinkedList::LinkedList()
{
    cout<<"---初始化链表---"<<endl;
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
    //添加到尾节点后面
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
    //插入元素到指定位置
    Node* workNode=head;    //工作指针 用于游历链表
    int count=0;            //计数器
    while(workNode!=nullptr && count<index-1)
    {
        //定位到传入索引的前一个结点
        workNode=workNode->next;
        count++;
    }
    if(workNode==nullptr)
    {
        throw "传入索引位置错误";
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
    //遍历链表
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
    //获得指定位置的数据
    Node* workNode=head;
    int count=0;  //累加器初始化
    while(workNode!=nullptr && count<index)
    {
        workNode=workNode->next;
        count++;
    }
    if(workNode==nullptr)
    {
        throw "索引错误";
    }
    else
    {
        return workNode->val;
    }
}

void LinkedList::deleteByIndex(int index)
{
    //删除指定位置的元素
    Node* workNode=head;
    Node* temp=new Node(0);  //存储要被删除的结点
    int count=0;
    while(workNode!=nullptr && count<index-1)
    {
        //定位到前一个结点
        workNode=workNode->next;
        count++;
    }
    if(workNode==nullptr)
    {
        throw "位置错误";
    }
    else
    {
        temp=workNode->next;   //清除内存
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
    //排序算法
    //大致思路 先将所有元素存储到vector中 再使用vector的排序算法进行排序
    //遍历链表
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
