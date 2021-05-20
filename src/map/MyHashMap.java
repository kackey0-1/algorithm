package map;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class MyHashMap {

    public static void main(String[] args) {
        MyHashMap myHashMap = new MyHashMap();
        myHashMap.put(1, 1); // The map is now [[1,1]]
        myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
        System.out.println(myHashMap.get(1));    // return 1, The map is now [[1,1], [2,2]]
        System.out.println(myHashMap.get(3));    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
        myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
        System.out.println(myHashMap.get(2));    // return 1, The map is now [[1,1], [2,1]]
        myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
        System.out.println(myHashMap.get(2));    // return -1 (i.e., not found), The map is now [[1,1]]
    }

    /**
     * put / get / remove
     */
    private int key_space;
    private List<Bucket> hash_table;

    public MyHashMap() {
        this.key_space = 2069;
        this.hash_table = new ArrayList<>();
        for (int i = 0; i < key_space; i++) {
            this.hash_table.add(new Bucket());
        }
    }

    protected Integer _hash(Integer key) {
        return key % this.key_space;
    }

    public void put(Integer key, Integer value) {
        Integer index = this._hash(key);
        this.hash_table.get(index).update(key, value);
    }

    public Integer get(Integer key) {
        Integer index = this._hash(key);
        return this.hash_table.get(index).get(key);
    }

    public void remove(Integer key) {
        Integer index = this._hash(key);
        this.hash_table.get(index).delete(key);
    }


    class Pair<U, K> {
        private U first;
        private K second;

        public Pair(U first, K second) {
            this.first = first;
            this.second = second;
        }
    }

    class Bucket {
        /**
         * get
         * update
         * remove
         */
        private List<Pair<Integer, Integer>> bucket;

        public Bucket() {
            this.bucket = new LinkedList<MyHashMap.Pair<Integer, Integer>>();
        }

        public Integer get(Integer key) {
            for (Pair<Integer, Integer> pair : this.bucket) {
                if (pair.first.equals(key)) {
                    return pair.second;
                }
            }
            return -1;
        }

        public void update(Integer key, Integer value) {
            boolean found = false;
            for (Pair<Integer, Integer> pair : this.bucket) {
                if (pair.first.equals(key)) {
                    pair.second = value;
                    found = true;
                    return;
                }
            }
            if (!found) {
                this.bucket.add(new Pair<>(key, value));
            }
        }

        public void delete(Integer key) {
            int index = 0;
            while (index < this.bucket.size()) {
                if (this.bucket.get(index).first.equals(key)) {
                    this.bucket.remove(index);
                    break;
                }
                index++;
            }
        }
    }
}

