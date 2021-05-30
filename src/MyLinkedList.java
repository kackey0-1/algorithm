public class MyLinkedList {
    int size;
    Node head;
    MyLinkedList() {
        this.size = 0;
        this.head = new Node(0);
    }

    public int get(int index) {
        if (this.size <= index || index < 0) return -1;

        Node curr = this.head;
        for (int i = 0; i < index+1; i++) curr = curr.next;
        return curr.value;
    }

    public void addAtIndex(int index, int value) {
        if (index < 0 || index > this.size) return;

        Node curr = this.head;
        for (int i = 0; i < index; i++) curr = curr.next;
        Node newNode = new Node(value);
        newNode.next = curr.next;
        curr.next = newNode;
        this.size++;
    }

    public void addAtHead(int value) {
        this.addAtIndex(0, value);
    }

    public void addAtTail(int value) {
        this.addAtIndex(this.size, value);
    }

    public void deleteAtIndex(int index) {
        if (index < 0 || index >= this.size) return;
        Node curr = this.head;
        for (int i = 0; i < index; i++) curr = curr.next;
        curr.next = curr.next.next;
        this.size--;
    }

    public static void main(String[] args) {
        /**
            # Your MyLinkedList object will be instantiated and called as such:
            # ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
            # [[],[1],[3],[1,2],[1],[1],[1]]
            # -------------------------------------------------------
            # ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
            # [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
            # -------------------------------------------------------
            # ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
            # [[],[1],[3],[1,2],[1],[1],[1]]
        */
        MyLinkedList obj = new MyLinkedList();
        obj.addAtHead(1);
        obj.addAtTail(3);
        obj.addAtIndex(1, 2);
        System.out.println(obj.get(1));
        obj.deleteAtIndex(1);
        System.out.println(obj.get(1));

    }


    class Node {
        int value;
        Node next;

        Node(int value) {
            this.value = value;
        }
    }
}

