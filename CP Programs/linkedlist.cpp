#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int value) {
        data = value;
        next = nullptr;
    }
};

class LinkedList {
private:
    Node* head;

public:
    LinkedList() {
        head = nullptr;
    }

    bool isEmpty() {
        return head == nullptr;
    }

    void insertAtBeginning(int value) {
        Node* newNode = new Node(value);
        newNode->next = head;
        head = newNode;
        cout << "Element " << value << " inserted at the beginning." << endl;
    }

    void insertAtEnd(int value) {
        Node* newNode = new Node(value);
        if (isEmpty()) {
            head = newNode;
        } else {
            Node* temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newNode;
        }
        cout << "Element " << value << " inserted at the end." << endl;
    }

    void insertAfter(int key, int value) {
        Node* newNode = new Node(value);
        Node* temp = head;
        while (temp != nullptr) {
            if (temp->data == key) {
                newNode->next = temp->next;
                temp->next = newNode;
                cout << "Element " << value << " inserted after " << key << "." << endl;
                return;
            }
            temp = temp->next;
        }
        cout << "Key " << key << " not found. Element " << value << " not inserted." << endl;
    }

    void deleteNode(int value) {
        if (isEmpty()) {
            cout << "List is empty. Cannot delete element." << endl;
            return;
        }

        if (head->data == value) {
            Node* temp = head;
            head = head->next;
            delete temp;
            cout << "Element " << value << " deleted." << endl;
            return;
        }

        Node* prev = nullptr;
        Node* curr = head;
        while (curr != nullptr) {
            if (curr->data == value) {
                prev->next = curr->next;
                delete curr;
                cout << "Element " << value << " deleted." << endl;
                return;
            }
            prev = curr;
            curr = curr->next;
        }

        cout << "Element " << value << " not found. Cannot delete." << endl;
    }

    void display() {
        if (isEmpty()) {
            cout << "List is empty." << endl;
            return;
        }

        Node* temp = head;
        cout << "Linked List: ";
        while (temp != nullptr) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
};

int main() {
    LinkedList linkedList;

    linkedList.insertAtEnd(10);
    linkedList.insertAtBeginning(5);
    linkedList.insertAfter(10, 15);
    linkedList.display(); // Output: Linked List: 5 10 15

    linkedList.deleteNode(10);
    linkedList.display(); // Output: Linked List: 5 15

    return 0;
}
