class PriorityQueueSorted:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        """Cek apakah queue kosong."""
        return len(self.queue) == 0
    def __len__(self):
        """Return panjang queue."""
        return len(self.queue)
    def remove(self):
        """Menghapus data paling depan (prioritas tertinggi)."""
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty, cannot remove item.")
    def peek(self):
        """Mengambil data paling depan (prioritas tertinggi)."""
        if not self.is_empty():
            print(f"Peek: {self.queue[0]}")
            return self.queue[0]
        else:
            print("Queue is empty, nothing to peek.")
    def add(self, item, priority):
        """Menambah item ke dalam queue dengan pengurutan berdasarkan prioritas."""
        self.queue.append((item, priority))
        # Urutkan queue menggunakan Quick Sort berdasarkan prioritas (dari besar ke kecil)
        self.queue = sorted(self.queue, key=lambda x: x[1], reverse=True)
    def print_all(self):
        """Return isi dari queue urut dari yang terbesar."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue contents (sorted by priority):")
            for item in self.queue:
                print(f"{item[0]} (Priority: {item[1]})")
# TEST CASE
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


#Cara 2
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

#Cara 3
class PriorityQueueSorted:
    def __init__(self):
        self.listbaru = list()
    def is_empty(self):
        return len(self.listbaru) == 0
    def __len__(self):
        return len(self.listbaru)
    def add(self, data, priority):
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
        if not self.is_empty():
            self.listbaru.pop(0)
        else:
            print("Queue is empty, cannot remove item.")
    def peek(self):
        if not self.is_empty():
            a = self.listbaru[0]
            print(f"Tertinggi adalah {a[0]} dengan priority {a[1]}")
        else:
            print("Queue is empty, nothing to peek.")
    def print_all(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            for i in self.listbaru:
                print((i[0], i[1]))
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
myQueue.print_all()


#Cara 4
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
        """Menambah item ke dalam queue dan menyortirnya dengan metode quicksort."""
        baru = (data, priority)
        self.listbaru.append(baru)
        self.quicksort(0, len(self.listbaru) - 1)
    def partition(self, start, end):
        """Metode partisi untuk quicksort."""
        pivot = self.listbaru[end][1]
        left = start
        right = end - 1
        while left <= right:
            while left <= right and self.listbaru[left][1] > pivot:
                left += 1
            while left <= right and self.listbaru[right][1] < pivot:
                right -= 1
            if left <= right:
                self.listbaru[left], self.listbaru[right] = self.listbaru[right], self.listbaru[left]
                left += 1
                right -= 1
        self.listbaru[left], self.listbaru[end] = self.listbaru[end], self.listbaru[left]
        return left
    def quicksort(self, start, end):
        """Metode quicksort untuk mengurutkan queue berdasarkan prioritas."""
        if start < end:
            pivot_index = self.partition(start, end)
            self.quicksort(start, pivot_index - 1)
            self.quicksort(pivot_index + 1, end)
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
            print("Queue contents (sorted by priority):")
            for item in self.listbaru:
                print(f"{item[0]} (Priority: {item[1]})")
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
