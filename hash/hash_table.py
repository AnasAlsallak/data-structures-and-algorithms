from .chain import LinkedList

class HashTable ():
    def __init__(self,size=3):
        self.size=size
        self.map=[None]*size

    def custom_hash (self,key):
        sum_of_ascii = 0
        for ch in key:
            ascii_co = ord(ch)
            sum_of_ascii += ascii_co
        m_res = sum_of_ascii*599
        index = m_res%self.size
        return index
    
    def set (self, key, value):
        hashed_key = self.custom_hash (key)
        if not self.map[hashed_key]:
            self.map[hashed_key]= [key,value]
        else: 
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].add([key,value])
            else: 
                chain = LinkedList()
                exsiting_pair = self.map[hashed_key]
                new_pair = [key, value]
                self.map[hashed_key] = chain
                chain.add(exsiting_pair)
                chain.add(new_pair)

    def get(self, key):
        hashed_key = self.custom_hash(key)

        if isinstance(self.map[hashed_key], LinkedList):
            current_node = self.map[hashed_key].head

            while current_node:
                if current_node.data[0] == key:
                    return current_node.data[1]
                current_node = current_node.next

        elif isinstance(self.map[hashed_key], list) and self.map[hashed_key][0] == key:
            return self.map[hashed_key][1]

        return None


    def has (self, key):
        hashed_key = self.custom_hash(key)
        if self.map[hashed_key] is None:
            return False
        elif isinstance(self.map[hashed_key], LinkedList):
            current_node = self.map[hashed_key].head

            while current_node:
                if current_node.data[0] == key:
                    return True
                current_node = current_node.next

        elif self.map[hashed_key][0]==key :
            return True
        
        return False
    
    def keys(self):
        arr = []
        for item in self.map:
            if isinstance(item, LinkedList):
                current_node = item.head
                while current_node:
                    arr.append(current_node.data[0])
                    current_node = current_node.next
            elif item is not None:
                arr.append(item[0])
        return arr
    
    def __str__(self) -> str:
        st_rep = ""
        for index, item in enumerate(self.map):
            if isinstance(item, LinkedList):
                current_node = item.head
                while current_node:
                    st_rep = f"Hashed Key: {index}, Key: {current_node.data[0]}, Value: {current_node.data[1]}\n"
                    print(st_rep)
                    current_node = current_node.next
            elif item is not None:
                st_rep = f"Hashed Key: {index}, Key: {item[0]}, Value: {item[1]}\n"
                print(st_rep)

if __name__ == "__main__":
    hashtable = HashTable()

    print("set A,70 - B,90 - C,80 - E,60\n")
    hashtable.set("A", 70)
    hashtable.set("B", 90)
    hashtable.set("C", 80)
    hashtable.set("E", 60)
    print("get A: \n", hashtable.get("A"))
    print("has A: \n", hashtable.has("A"))
    print("hash A,70: \n", hashtable.custom_hash("A"))
    print("keys: \n", hashtable.keys())









