#include"LinkedList.h"
using namespace std;

int main()
{
    cout<<"Hello"<<endl;
    cout<<"你好"<<endl;
    LinkedList l1;
    l1.addAtTail(3);
    l1.addAtSomeWhere(2,4);
    l1.addAtTail(8);
    l1.addAtSomeWhere(3,6);
    l1.printList();
    cout<<"长度为"<<l1.length()<<endl;
    cout<<l1.get(2)<<endl;
    l1.deleteByIndex(2);
    l1.addAtSomeWhere(2,9);
    l1.printList();
    cout<<"长度为"<<l1.length()<<endl;
    l1.mySort();
    l1.printList();
    system("pause");
    return 0;
}
