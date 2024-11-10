
class PriorityQueueSorted:
    def __init__(self):
        self.listbaru = list()
    
    def is_empty(self):
        return len(self.listbaru) == 0
    
    def __len__(self):
        return len(self._listbaru)
    
    def add(self, data, priority):
        baru = (data, priority)
        self.listbaru.append(baru)

        def quicksort(data, start, end):
            if start < end:
                pivot_index = partition(data, start, end)
                quicksort(data, start, pivot_index-1)
                quicksort(data, pivot_index+1, end)

        def partition(data, start, end):
            pivot = data[end][1]
            left = start
            right = end - 1
            while left <= right:
                while data[left][1] > pivot:
                    left = left + 1
                while data[right][1] < pivot:
                    right = right - 1
                if left <= right:
                    data[left], data[right] = data[right], data[left]
                    left = left + 1
                    right = right - 1
            data[left], data[end] = data[end], data[left]
            return left

        quicksort(self.listbaru, 0, len(self.listbaru)-1)

    def remove(self):
        if self.is_empty() == False:
            self.listbaru.pop(0)
        
    def peek(self):
        a = self.listbaru[0]
        print (f"Tertinggi adalah {a[0]} dengan priority {a[1]}")
    
    def print_all(self):
        a = self.listbaru
        for i in a:
            print ((i[0], i[1]))
        print ()
        

myQueue = PriorityQueueSorted()
myQueue.add('Gian', 2)
myQueue.add('Kezia', 4)
myQueue.print_all()
myQueue.peek()
print()
myQueue.add('Glen', 8)
myQueue.add('Christo', 1)
myQueue.print_all()
myQueue.peek()
print()
print("========REMOVE========")
myQueue.remove()
myQueue.print_all()
print()
myQueue.remove()
myQueue.print_all()
print()
myQueue.remove()
myQueue.print_all()
print()
myQueue.add('Saya', 7)
myQueue.print_all()

#Cara Akhir
class PriorityQueueSorted:
    def __init__(self):
        self.listbaru = []

    def is_empty(self):
        """Cek apakah queue kosong."""
        return len(self.listbaru) == 0

    def __len__(self):
        """Return panjang queue."""
        return len(self.listbaru)

    def add(self, data, priority):
        """Menambah item ke dalam queue dan mengurutkannya dengan metode quicksort."""
        baru = (data, priority)
        self.listbaru.append(baru)

        def quicksort(data, start, end):
            if start < end:
                pivot_index = partition(data, start, end)
                quicksort(data, start, pivot_index - 1)
                quicksort(data, pivot_index + 1, end)

        def partition(data, start, end):
            pivot = data[end][1]
            left = start
            right = end - 1
            while left <= right:
                while left <= right and data[left][1] > pivot:
                    left += 1
                while left <= right and data[right][1] < pivot:
                    right -= 1
                if left <= right:
                    data[left], data[right] = data[right], data[left]
                    left += 1
                    right -= 1
            data[left], data[end] = data[end], data[left]
            return left

        quicksort(self.listbaru, 0, len(self.listbaru) - 1)

    def remove(self):
        """Menghapus data paling depan (prioritas tertinggi)."""
        if not self.is_empty():
            return self.listbaru.pop(0)
        else:
            print("Queue is empty, cannot remove item.")

    def peek(self):
        """Mengambil data paling depan (prioritas tertinggi)."""
        if not self.is_empty():
            a = self.listbaru[0]
            print(f"Tertinggi adalah {a[0]} dengan priority {a[1]}")
            return a
        else:
            print("Queue is empty, nothing to peek.")

    def print_all(self):
        """Return isi dari queue urut dari yang terbesar."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            for item in self.listbaru:
                print((item[0], item[1]))
            print()

# Test case
myQueue = PriorityQueueSorted()
myQueue.add('Gian', 2)
myQueue.add('Kezia', 4)
myQueue.print_all()
myQueue.peek()
print()
myQueue.add('Glen', 8)
myQueue.add('Christo', 1)
myQueue.print_all()
myQueue.peek()
print()
print("========REMOVE========")
myQueue.remove()
myQueue.print_all()
print()
myQueue.remove()
myQueue.print_all()
print()
myQueue.remove()
myQueue.print_all()
print()
myQueue.add('Saya', 7)
