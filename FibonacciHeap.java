/**
 * FibonacciHeap
 * user1 - tomshmueli
 * id1 - 315363473
 * user2 - einatgelbort
 * id2 - 208275651
 * An implementation of a Fibonacci Heap over integers.
 */
public class FibonacciHeap
{
    public HeapNode first;
    public HeapNode last;
    public HeapNode min_node;
    public int size;
    public int trees_amount;
    public int marked_amount;
    public static int total_links = 0;
    public static int total_cuts = 0;

    public FibonacciHeap(){
        this.first = null;
        this.last = null;
        this.size = 0;
        this.marked_amount = 0;
        this.min_node = null;
        this.trees_amount = 0;
    }

    /**
     * reset the FibonacciHeap from all information
     *
     * $ret == new empty FibonacciHeap
     *
     */
    public void reset(boolean include_size){
        this.first = null;
        this.last = null;
        this.min_node = null;
        this.trees_amount = 0 ;
        if (include_size == true){
            this.size = 0;
        }
    }

    public String toString(){
        String str = "F: " + first.toString() +"..." + "L: " + last.toString();
        return str;
    }

    /**
     * get the First HeapNode in the FibonacciHeap - most left.
     *
     * @post $ret == was inserted last
     *
     */
    public HeapNode getFirst(){
        return this.first;
     }

    /**
     * set the first node of the FibonacciHeap to be node
     *
     * @pre $ret == node != null
     *
     */
    public void setFirst(HeapNode node) {
        this.first = node;
        this.last.next = first;
        this.first.prev = last;
    }

    /**
     * get the Last HeapNode in the FibonacciHeap - most right.
     *
     * @post $ret == was inserted first
     *
     */
    public HeapNode getLast(){
        return this.last;
    }

    /**
     * set the last node of the FibonacciHeap to be node
     *
     * @pre $ret == node != null
     *
     */
    public void setLast(HeapNode node) {
        this.last = node;
        this.last.next = first;
        this.first.prev = last;
    }

    /**
     * get the pointer to the minimum node in the FibonacciHeap
     *
     * @Post $ret == for all HeapNode in this FibonacciHeap $ret.key < HeapNode.key
     *
     */
   public HeapNode getMin(){
        return this.min_node;
    }

    /**
     * set the pointer of the minimum node in the FibonacciHeap to be node
     *
     * @Post $ret == for all HeapNode in this FibonacciHeap $ret.key < HeapNode.key
     *
     */
    public void setMin(HeapNode node) {this.min_node = node;}

    /**
     * set the pointer of the minimum node in the FibonacciHeap to be node
     *
     * @Pre node != null
     * @Post --> for all HeapNode in this FibonacciHeap min_node.key < HeapNode.key
     */
    public void UpdateMinOfHeap(HeapNode node)         // compare new node to this.min_node
    {
        if (node.getKey() < min_node.getKey())
            min_node = node;
    }

    /**
     * Returns an array of length 2 s.t : lst[0] = minimum root , lst[1] = other root
     *
     * @pre (node1 != node2 ) && != null
     *
     */
    public static HeapNode[] MinMaxArray(HeapNode node1,HeapNode node2)         // compare new node to this.min_node
    {
        HeapNode[] min_lst = new HeapNode[2];
        if (node1.getKey() <= node2.getKey()){
            min_lst[0] = node1;
            min_lst[1] = node2;
        }
        else{
            min_lst[0] = node2;
            min_lst[1] = node1;
        }
            return min_lst;
    }

    /**
     *
     * Bypass the current node --> connect its prev to its next.
     *
     *
     */
    public static void Bypass(HeapNode node){

        if (node.getNext() != node) {

            HeapNode tmp_prev = node.getPrev();
            HeapNode tmp_next = node.getNext();
            tmp_prev.setNext(tmp_next);
            node.setNext(node);
        }
    }

    /**
     * public static boolean CheckViolation(HeapNode node)
     *
     * check if the key in the given node is bigger than the parent key
     *
     * Returns boolean is the node is violation or no
     */
    public static boolean CheckViolation(HeapNode node) {
        if (node.getParent() == null) {
            return false;
        }
        return node.getParent().getKey() > node.getKey();
    }

   /**
    * public boolean isEmpty()
    *
    * true if and only if the heap is empty.
    * @post = isEmpty <--> this FibonacciHeap is a new FibonacciHeap
    *
    */
    public boolean isEmpty()
    {
    	if(first == null)
            return true;
        return false;
    }


   /**
    * public HeapNode insert(int key)
    *
    * Creates a node (of type HeapNode) which contains the given key, and inserts it into the heap.
    * The added key is assumed not to already belong to the heap.
    * @pre key != HeapNode.key for all HeapNodes in FibonacciHeap
    * @post $ret = this.first
    * $ret == HeapNode(key)
    * Returns the newly created node.
    */
    public HeapNode insert(int key)
    {
        HeapNode new_node = new HeapNode(key);
        if (this.isEmpty()){
            min_node = new_node;
            first = new_node;
            last = new_node;
            last.setNext(first);
            }
        else{
            new_node.setNext(first);
            last.setNext(new_node);
            first = new_node;
        }
        //Update fields
        this.UpdateMinOfHeap(new_node);
        this.trees_amount ++;
        this.size++;

    	return new_node;
    }

    /**
     * append HeapNode to the FibonacciHeap
     *
     * @pre new_node.key != HeapNode.key for all HeapNodes in FibonacciHeap
     * @post new_node = this.first
     * @pre new_node != null
     *
     */
    public void append(HeapNode new_node){

            if (this.isEmpty()){
                min_node = new_node;
                first = new_node;
                last = new_node;
                last.setNext(first);
                trees_amount = 1;
            }
            else{
                last.setNext(new_node);
                last = new_node;
                UpdateMinOfHeap(new_node);
                this.trees_amount ++;
            }
        }


   /**
    * Deletes the node containing the minimum key.
    * @pre: child.getParent() = null //child is a root
    * @post legal FibonacciHeap
    * @post if this.size <= 1 --> isEmpty() == true
    */
    public void deleteMin()
    {
        if (this.size <= 1)
            reset(true);

        else{
            HeapNode tmp_next = min_node.getNext();
            HeapNode tmp_prev = min_node.getPrev();
            HeapNode child = min_node.getChild();

            if (child != null) {  // update cuts/parent for all children of min_node
                HeapNode next_child = null;
                do {
                    if (next_child == null)
                        next_child = child;
                    else
                        next_child = next_child.getNext();
                    next_child.setParent();
                    if (next_child.getMarked()) {
                        next_child.setMark(false);
                        marked_amount--;
                    }
                }
                while (next_child.getNext() != child);
            }
            else
                Bypass(min_node);

            // update fields
            this.trees_amount += min_node.getRank() - 1;    // added all children minus root to heap
            this.size --;
            if(min_node.equals(last)) { // update last
                if (child == null)
                    last = tmp_prev;
                else
                    last = child.getPrev();
            }
            if(min_node.equals(first)) { // update first
                if (child == null)
                    first = tmp_next;
                else
                    first = child;
            }
            if ((child != null)&&(this.trees_amount > 1)){
                child.getPrev().setNext(tmp_next);
                tmp_prev.setNext(child);
            }
            this.Consolidate();
            findMin();
        }
    }


    /**
     * public int Link (HeapNode
     * @pre: this.rank = heap2.rank
     * @pre: both nodes are roots.
     * Melds heap2 with the current heap.
     *
     */
    public static HeapNode Link(HeapNode root1 ,HeapNode root2)
    {
        Bypass(root1);
        Bypass(root2);
        HeapNode[] min_max = MinMaxArray(root1,root2);  // min_max[0] = min, min_max[1] = max
        HeapNode min_root = min_max[0];
        HeapNode max_root = min_max[1];

        HeapNode min_child = min_root.getChild();    //curr min = child of min_root
        if (min_child != null){
            min_child.getPrev().setNext(max_root);
            max_root.setNext(min_child);
        }
        else
            max_root.setNext(max_root);

        min_root.setRank(min_root.getRank() + 1);
        min_root.setChild(max_root);


        total_links ++;
        return min_root;
    }

    /**
     * perform consolidation/successive linking on the FibonacciHeap
     *
     * @post trees_amount <= log(maximum heap.rank +1)
     * @post legal FibonacciHeap
     */
    public void Consolidate()
    {
        if (this.size>1 && this.trees_amount>1){
            int num_of_buckets = (int)(Math.ceil(Math.log(this.size())/Math.log(2)))+1; // <= log(n+1) + 1
            HeapNode[] buckets = new HeapNode[num_of_buckets];
            HeapNode curr_root = this.first;
            while (curr_root != last){
                first = first.getNext();
                int index = curr_root.getRank(); //degree of current root = index of bucket
                buckets = LinkBucketSequence(buckets,curr_root,index);
                curr_root = first;
            }
            int index = curr_root.getRank(); //degree of current root = index of bucket
            buckets = LinkBucketSequence(buckets,curr_root,index);


            this.reset(false);
            for(int i=0;i<num_of_buckets;i++) {
                if (buckets[i] != null)
                    this.append(buckets[i]);

            }
            this.last.setNext(this.first);
        }
    }
    /**
     * Helper Function of Consolidate:
     * get a current root and links it with current tree with the same rank in the buckets array
     * stop when the next bucket is empty and puts the linked new root there
     *
     * @pre index = curr_root.rank
     * @pre index < buckets.length
     * @post buckets != empty
     * @post buckets[index+1] == null or index+1 == buckets.length
     *
     */
    public HeapNode[] LinkBucketSequence(HeapNode[] buckets, HeapNode curr_root,int index)
    {
        if (buckets[index]==null)
            buckets[index] = curr_root;
        else{
            while ((index<buckets.length)&&(buckets[index]!=null))
            {
                HeapNode next_root = buckets[index];
                HeapNode linked_root = Link(curr_root,next_root);
                curr_root = linked_root;
                buckets[index] = null;
                index++;
                if (buckets[index] == null){
                    buckets[index] = linked_root;
                    break;
                }

            }
        }
        return buckets;
    }

   /**
    * go over all roots in the FibonacciHeap and find the minimum root
    *
    * $ret --> is a root in the FibonacciHeap
    * @post $ret.key < HeapNode.key for all HeapNodes in FibonacciHeap
    *
    */
    public HeapNode findMin()
    {
        if (this.isEmpty())
            return null;
        min_node = first;
    	HeapNode curr = first.getNext();
        UpdateMinOfHeap(curr);
        while(curr!=first){
            UpdateMinOfHeap(curr);
            curr = curr.getNext();
        }
        return min_node;
    }

   /**
    * public void meld (FibonacciHeap heap2)
    *
    * Melds heap2 with the current heap.
    *
    */
    public void meld (FibonacciHeap heap2)
    {  if (this.getFirst() == null && heap2.getFirst() != null) {
        this.first = heap2.getFirst();
        this.last = heap2.getLast();
        this.min_node = heap2.getMin();
    }
    else if (this.getFirst() != null && heap2.getFirst() != null) {
        HeapNode l_mid = this.first.getPrev();
        HeapNode r_end = heap2.getFirst().getPrev();
        l_mid.setNext(heap2.getFirst());
        r_end.setNext(this.first);
        UpdateMinOfHeap(heap2.getMin());
        this.setLast(heap2.getLast());
    }

        this.size += heap2.size();
        trees_amount += heap2.trees_amount;
        marked_amount += heap2.marked_amount;
        total_cuts += heap2.totalCuts();
        total_links += heap2.totalLinks();
    }

   /**
    * public int size()
    *
    * Returns the number of elements in the heap.
    *
    */
    public int size() {
    	return this.size;
    }

    /**
     * public int findMaxRank()
     *
     * Returns the max tree rank in the heap
     *
     */
    public int findMaxRank() {
        HeapNode node = this.first;
        int max_rank = node.getRank();
        while (node != this.last) {
            if (node.getRank() > max_rank) {
                max_rank = node.getRank();
            }
            node = node.getNext();
        }
        if (node.getRank() > max_rank) {    // for when node = last
            max_rank = node.getRank();
        }
        return max_rank;
    }

    /**
    * public int[] countersRep()
    *
    * Return an array of counters. The i-th entry contains the number of trees of order i in the heap.
    * (Note: The size of the array depends on the maximum order of a tree.)
    *
    */
    public int[] countersRep() {
        if (this.isEmpty()) {
        return new int[0];
        }
        int max_rank = this.findMaxRank();
        int[] arr = new int[max_rank+1];
        arr[first.getRank()] = 1;
        HeapNode node = first.getNext();
        while (node != first) {
            arr[node.getRank()] += 1;
            node = node.getNext();
        }
        return arr;
    }

   /**
    * public void delete(HeapNode x)
    *
    * Deletes the node x from the heap.
	* It is assumed that x indeed belongs to the heap.
    *
    */

   public void delete(HeapNode x)
   {
       int current_key = x.getKey();
       int delta = current_key - min_node.getKey() + 1;
       decreaseKey(x, delta);
       this.setMin(x);
       deleteMin();
   }

    /**
     * public void cascadingCut(HeapNode node)
     *
     * cut the edge in case that the parent lose more than one chile.
     * create new tree for the parent that we cut.
     *
     */
    public void cascadingCut(HeapNode node){
        while (node != null && node.getMarked()) {
            HeapNode parent = node.getParent();
            createNewTree(node);
            node = parent;
        }
        if (node!= null && node.getParent()!=null) {
            node.setMark(true);
            marked_amount++;
        }
    }

    /**
     * public void updateParentField(HeapNode parent, HeapNode prev_child)
     *
     * update the parent rank field and the child pointer.
     *
     */
    public void updateParentField(HeapNode parent, HeapNode prev_child, HeapNode next_before_changes){
        if (parent != null) {
            if (parent.getRank() == 1){
                parent.setChild();
            }
            else{
                //if the node was the first in this level
                if (parent.getChild() == prev_child) {
                    parent.setChild(next_before_changes);
                }
            }

            parent.setRank(parent.getRank() - 1);
        }
    }

    /**
     * public void createNewTree(HeapNode node)
     *
     * create new tree from specific node. cut the node from the parent and from the prev and next nodes.
     * every new tree his root contain the field : mark = false
     *
     */
    public void createNewTree(HeapNode node) {
        HeapNode parent = node.getParent();
        node.setParent();
        HeapNode tmp_next = node.getNext();
        Bypass(node);
        if (node.getMarked()) {
            node.setMark(false);
            marked_amount--;
        }
        HeapNode curr_first = this.getFirst();
        node.setNext(curr_first);
        this.setFirst(node);
        updateParentField(parent, node, tmp_next);

        trees_amount++;
        total_cuts++;
    }
   /**
    * public void decreaseKey(HeapNode x, int delta)
    *
    * Decreases the key of the node x by a non-negative value delta. The structure of the heap should be updated
    * to reflect this change (for example, the cascading cuts procedure should be applied if needed).
    */
    public void decreaseKey(HeapNode x, int delta)
    {
        int current_key = x.getKey();
        if (x.getRank() == 0 && this.size() ==1 )
            this.reset(true);
        else {
            int new_key = current_key - delta;
            x.setKey(new_key);
            if (CheckViolation(x)) {
                HeapNode parent = x.getParent();
                createNewTree(x);
                cascadingCut(parent);
            }
        }
    }

    /**
     * public int getMarked()
     *
     * This function returns the current number of marked items in the heap
     */
    public int getMarked()
    {
        return this.marked_amount;
    }

   /**
    * public int potential()
    *
    * This function returns the current potential of the heap, which is:
    * Potential = #trees + 2*#marked
    *
    * In words: The potential equals to the number of trees in the heap
    * plus twice the number of marked nodes in the heap.
    */
    public int potential(){
        int marked_nodes = this.getMarked();
        int potential = this.trees_amount + 2 * marked_nodes;
        return potential;
    }

   /**
    * public static int totalLinks()
    *
    * This static function returns the total number of link operations made during the
    * run-time of the program. A link operation is the operation which gets as input two
    * trees of the same rank, and generates a tree of rank bigger by one, by hanging the
    * tree which has larger value in its root under the other tree.
    */
    public static int totalLinks()
    {
    	return total_links;
    }

   /**
    * public static int totalCuts()
    *
    * This static function returns the total number of cut operations made during the
    * run-time of the program. A cut operation is the operation which disconnects a subtree
    * from its parent (during decreaseKey/delete methods).
    */
    public static int totalCuts()
    {
    	return total_cuts; // should be replaced by student code
    }

     /**
    * public static int[] kMin(FibonacciHeap H, int k)
    *
    * This static function returns the k smallest elements in a Fibonacci heap that contains a single tree.
    * The function should run in O(k*deg(H)). (deg(H) is the degree of the only tree in H.)
    * @post: sorted array of the k minimal items in the given heap
    */
    public static int[] kMin(FibonacciHeap H, int k)
    {
        if (H.size == 0){
            return new int[0];
        }
        int[] smallest_k_arr = new int[k];
        int rank_min_node = H.getMin().getRank();
        int size_arr;
        if (rank_min_node == 0 ){
            size_arr = 2 *1;
        }
        else {
            size_arr = 2 * rank_min_node;
        }
        HeapNode[] kMin_arr = new HeapNode[size_arr];
        HeapNode min_node = H.getMin();
        kMin_arr[0] = min_node;
        int index = 1;
        for (int i=0; i<k; i++) {
            int min_index = 0;
            int min_value = kMin_arr[0].getKey();
            for (int j=1; j<index; j++) {
                if (kMin_arr[j].getKey() < min_value) {
                    min_value = kMin_arr[j].getKey();
                    min_index = j;
                }
            }
            HeapNode curr_min_node =  kMin_arr[min_index];
            smallest_k_arr[i] = curr_min_node.getKey();

            if (curr_min_node.getRank()>0) {
                HeapNode[] childes = getLevelDownNodes(curr_min_node);
                kMin_arr[min_index] = childes[0];
                for (int j = 1; j < childes.length; j++) {
                    kMin_arr[index] = childes[j];
                    index++;
                }
            }
            else {
                for (int j = min_index; j < index -1 ; j++) {
                    kMin_arr[j] = kMin_arr[j+1];
                }
                if (kMin_arr[(index-1)] != null){
                    kMin_arr[index-1] = null;
                    index --;
                }
            }
        }
        return smallest_k_arr;
    }


    /**
     * public static HeapNode[] getLevelDownNodes(HeapNode node)
     *
     * This static function returns an array of the childes of given nodes.
     * @post: a nodes array of the childes
     */

    public static HeapNode[] getLevelDownNodes(HeapNode node){
        HeapNode[] childes =new HeapNode[node.getRank()];
        int index = 0;
        HeapNode first_child = node.getChild();
        HeapNode child= null;
        do {
            if (child == null) {
                child = first_child;
            }
            else
                child =child.getNext();
            childes[index] = child;
            index ++;
        }
        while (child.getNext() != first_child);
        return childes;
    }
   /**
    * public class HeapNode
    *
    */
    public static class HeapNode {

       public int key;
       public int rank;
       public boolean mark;
       public HeapNode child;
       public HeapNode parent;
       public HeapNode next;
       public HeapNode prev;

       public HeapNode(int key) {
           this.key = key;
           this.rank = 0;
           this.mark = false;
           this.prev = this;
           this.next = this;
           this.child = null;
           this.parent = null;
       }

       public String toString(){
           String repr = "|" +  this.key + "|" ;
           if (this.next != this)
               repr = repr + "<-->" + this.next.getKey();
           if (this.prev != this)
               repr = this.prev.getKey() + "<-->" + repr;
           return repr;
       }
       public int getKey() {
           return this.key;
       }

       public void setRank(int new_rank) {
           this.rank = new_rank;
       }
       public int getRank() {
           return this.rank;
       }

       public void setNext(HeapNode node) {
           this.next = node;
           if (node != null)
               node.prev = this;
       }

       public void setKey(int key){
           this.key = key;
       }

       public void setParent() {
           this.parent = null;
       }

       public void setParent(HeapNode parent) {
           this.parent = parent;
       }

       public void setChild(HeapNode child) {
           this.child = child;
           child.setParent(this);
       }

       public void setChild() {
           this.child = null;
       }

       public void setMark(boolean mark)  {
           this.mark = mark;
       }

       public HeapNode getNext() {
           return this.next;
       }

       public HeapNode getPrev() {
           return this.prev;
       }

       public HeapNode getParent() {
           return this.parent;
       }

       public HeapNode getChild() {
           return this.child;
       }
       public boolean getMarked(){
           return this.mark;
       }
   }

}
