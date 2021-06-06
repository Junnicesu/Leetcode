#include <iostream>
#include <memory>

using namespace std;

// unique_ptr-based linked list demo
struct List {
    struct Node {
        int data;
        std::unique_ptr<Node> next;
        Node(int data) : data{ data }, next{ nullptr } {}
    };
    List() : head{ nullptr }, end{ nullptr } {};  //sj!!!!
    // N.B. iterative destructor to avoid stack overflow on long lists
    ~List() { cout << "in ~List()\n";  while (head) head = std::move(head->next); }
    // copy/move and other APIs skipped for simplicity
    void push(int data) {
        auto temp = std::make_unique<Node>(data);
        if (head) temp->next = std::move(head);
        head = std::move(temp);
        if (head->next == nullptr) {
            end = head.get();
        }        
        // cout << end->data << endl;  //sjdb

    }

    void push_back(int data) {
        auto temp = std::make_unique<Node>(data);
        if (end == nullptr) {
            push(data);
        }
        else {
            end->next = std::move(temp); // end should always point to last Node.
            end = end->next.get();
        }
    }

    friend ostream& operator<<(ostream& os, const List& list) { //sj!!!!! don't forget to return ostream&
        auto node = list.head.get(); //sj!!!! for unique_ptr, never use auto node or auto& node = list.head; to iterate
        while (node != nullptr) {
            os << node->data << ' ';
            node = node->next.get();
        } //sj !!!!!! compile error: use of 'node' before deduction of 'auto', if no "auto& node = list.head", error: use of deleted function
        os << endl;
        return os;
    }

private:
    std::unique_ptr<Node> head;
    Node* end;  //sj!!!!, very odd.
};

int main() {
    List list;
    for (int i = 0; i < 10; i++) {
        list.push(i);
    }
    cout << list;

    List list2;
    for (int j = 0; j < 20; j++) {
        list2.push_back(j);
    }
    cout << list2;

    for (int k = 0; k < 10; k++) {
        list.push_back(k);
    }
    cout << list;

    List list3;
    list3.push(3);
    list3.push_back(4);
    list3.push(2);
    list3.push_back(5);
    list3.push(1);
    cout << list3;    
}

/*
$ ./linkedList.exe
9 8 7 6 5 4 3 2 1 0
in ~List()

sj conclustion:
1) push is push to the head by default.
2) why using unique_ptr instead of shared_ptr?
3) is it efficient, if the Node's data has large memory?
4) what's the default move assignment operator for Node???
5) when iterating, using get(), otherwise the point destructed.
6)
*/