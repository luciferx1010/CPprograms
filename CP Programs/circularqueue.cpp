#include <iostream>
using namespace std;

class CircularQueue {
private:
    int *arr;
    int front;
    int rear;
    int capacity;
    int size;

public:
    CircularQueue(int cap) {
        capacity = cap;
        arr = new int[capacity];
        front = -1;
        rear = -1;
        size = 0;
    }

    bool isEmpty() {
        return size == 0;
    }

    bool isFull() {
        return size == capacity;
    }

    void enqueue(int value) {
        if (isFull()) {
            cout << "Queue is full. Cannot enqueue element." << endl;
            return;
        }

        rear = (rear + 1) % capacity;
        arr[rear] = value;
        if (front == -1) {
            front = rear;
        }
        size++;
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty. Cannot dequeue element." << endl;
            return;
        }

        front = (front + 1) % capacity;
        size--;
        if (size == 0) {
            front = -1;
            rear = -1;
        }
    }

    int getFront() {
        if (isEmpty()) {
            cout << "Queue is empty. No front element." << endl;
            return -1;
        }

        return arr[front];
    }

    int getRear() {
        if (isEmpty()) {
            cout << "Queue is empty. No rear element." << endl;
            return -1;
        }

        return arr[rear];
    }

    void display() {
        if (isEmpty()) {
            cout << "Queue is empty." << endl;
            return;
        }

        int i = front;
        while (i != rear) {
            cout << arr[i] << " ";
            i = (i + 1) % capacity;
        }
        cout << arr[rear] << endl;
    }
};

int main() {
    CircularQueue queue(5);

    queue.enqueue(10);
    queue.enqueue(20);
    queue.enqueue(30);
    queue.enqueue(40);

    queue.display(); // Output: 10 20 30 40

    cout << "Front: " << queue.getFront() << endl; // Output: 10
    cout << "Rear: " << queue.getRear() << endl; // Output: 40

    queue.dequeue();
    queue.enqueue(50);

    queue.display(); // Output: 20 30 40 50

    return 0;
}
