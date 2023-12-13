from collections import deque
import heapq

"""
1.Перший унікальний символ у рядку
Дано рядок s, знайти в ньому перший неповторюваний символ і повернути його індекс. Якщо його не існує, поверніть -1.

Приклад 1:

Input: s = "leopard" Output: 0
Приклад 2:

Input: s = "loveleopard" Output: 2
Приклад 3:

Input: s = "aabb" Output: -1
Обмеження:
1 <= s.length <= 100 000
s складається лише з малих літер англійської мови.
"""


def unique_char(s):
    if len(s) < 1 or len(s) > 100000:
        raise ValueError('Length of input must be from 1 to 100 000')
    s = s.lower()

    for char in range(len(s)):
        if s.count(s[char]) == 1:
            return char
    return -1


# Тестимо:
# s1 = 'leopard'
# s2 = 'loveleopard'
# s3 = 'aabb'
# print(unique_char(s1))
# print(unique_char(s2))
# print(unique_char(s3))

# ______________________________________________________________________________________________________________________

"""
2.Реалізація стека за допомогою черг
Реалізуйте стек «останній прийшов першим вийшов» (LIFO), використовуючи лише дві черги. Реалізований стек повинен 
підтримувати всі функції звичайного стека (push, top, pop і empty).

Реалізуйте клас MyStack:

void push(int x) Розміщує елемент x на вершину стека.
int pop() Вилучає елемент у верхній частині стека та повертає його.
int top() Повертає елемент у верхній частині стека.
boolean empty() Повертає true, якщо стек порожній, і false в іншому випадку.

Примітки:
Ви повинні використовувати лише стандартні операції черги, що означає, що дійсними є лише операції push to back, 
peek/pop from front, size і is empty.
Залежно від вашої мови, черга може не підтримуватися нативно. Ви можете імітувати чергу за допомогою списку або 
двох черг (двосторонньої черги), якщо ви використовуєте лише стандартні операції черги.

Приклад 1:

Input ["MyStack", "push", "push", "top", "pop", "empty"] [[], [1], [2], [], [], []] 
Output [null, null, null, 2, 2, false] 
Пояснення: MyStack myStack = new MyStack(); myStack.push(1); myStack.push(2); myStack.top(); // 
return 2 
myStack.pop(); // 
return 2 
myStack.empty(); // 
return False
Обмеження:
1 <= x <= 9
Щонайбільше 100 викликів буде зроблено для push, pop, top і empty.
Усі дзвінки на pop і top дійсні.
"""


class MyStack:

    def __init__(self):
        # Ініціалізація двох черг для реалізації стеку.
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        # Додає елемент x на вершину стека.
        if 0 <= x <= 9:
            self.queue2.append(x)
            # Переносить елементи з queue1 в queue2 так, щоб новий елемент x став на початок.
            while self.queue1:
                self.queue2.append(self.queue1.popleft())
            # Змінює роль черг, щоб queue2 став основним стеком.
            self.queue1, self.queue2 = self.queue2, self.queue1
        else:
            raise ValueError('x must be from 0 to 9')

    def pop(self):
        # Видаляє і повертає елемент з вершини стека.
        return self.queue1.popleft()

    def top(self):
        # Повертає елемент з вершини стека без видалення.
        return self.queue1[0]

    def empty(self):
        # Повертає True, якщо стек порожній, і False в іншому випадку.
        return not bool(self.queue1)


def my_stack(queue_operations, queue_operands):
    stack = MyStack()
    output = []

    # Цикл для виконання операцій зі стеком.
    for key, value in zip(queue_operations, queue_operands):
        if key == "MyStack":
            # Якщо операція "MyStack", то створити новий стек.
            stack = MyStack()
            output.append(None)
        elif key == "push":
            # Якщо операція "push", то викликати функцію push і додати результат в output.
            stack.push(value[0])
            output.append(None)
        elif key == "pop":
            # Якщо операція "pop", то викликати функцію pop і додати результат в output.
            output.append(stack.pop())
        elif key == "top":
            # Якщо операція "top", то викликати функцію top і додати результат в output.
            output.append(stack.top())
        elif key == "empty":
            # Якщо операція "empty", то викликати функцію empty і додати результат в output.
            output.append(stack.empty())

    return output


# Тестимо
# queue_operations = ["MyStack", "push", "push", "top", "pop", "empty"]
# queue_operands = [[], [1], [2], [], [], []]
# print(my_stack(queue_operations, queue_operands))

# ______________________________________________________________________________________________________________________

"""
3.Кількість останніх викликів
У вас є клас RecentCounter, який підраховує кількість останніх запитів протягом певного періоду часу.

Реалізуйте клас RecentCounter:

RecentCounter() Ініціалізує лічильник нульовими останніми запитами.
int ping(int t) Додає новий запит у момент часу t, де t представляє деякий час у мілісекундах, і повертає кількість запитів, 
які відбулися за останні 3000 мілісекунд (включаючи новий запит). Зокрема, поверніть кількість запитів, які відбулися у 
включеному діапазоні [t - 3000, t].
Гарантується, що кожен виклик ping використовує строго більше значення t, ніж попередній виклик.

Приклад 1:

Input ["RecentCounter", "ping", "ping", "ping", "ping"] [[], [1], [100], [3001], [3002]] 
Output [null, 1, 2, 3, 3] 
Пояснення: RecentCounter recentCounter = new RecentCounter(); 
recentCounter.ping(1); // 
requests = [1], range is [-2999,1], return 1 
recentCounter.ping(100); // 
requests = [1, 100], range is [-2900,100], return 2 
recentCounter.ping(3001); // 
requests = [1, 100, 3001], range is [1,3001], return 3 
recentCounter.ping(3002); // 
requests = [1, 100, 3001, 3002], range is [2,3002], return 3

Обмеження:
1 <= t <= 1 000 000 000
Кожен тест буде викликати ping зі строго зростаючими значеннями t.
Щонайбільше 10 000 виклики будуть зроблені для ping
"""


class RecentCounter:

    def __init__(self):
        # Ініціалізація черги для збереження часових міток запитів.
        self.requests = deque()
        self.MAX_CALLS = 10000  # Максимальна кількість викликів для ping
        self.last_t = 0  # Останнє значення t

    def ping(self, t):
        if 1 <= t <= 1000000000 and t > self.last_t:
            # Додає новий запит у момент часу t.
            self.requests.append(t)
            self.last_t = t  # Оновлює останнє значення t

            # Видаляє всі запити, які не потрапляють в діапазон [t - 3000, t].
            while self.requests and self.requests[0] < t - 3000:
                self.requests.popleft()

            # Обмеження на кількість викликів для ping.
            while len(self.requests) > self.MAX_CALLS:
                self.requests.popleft()

            # Повертає кількість залишених запитів.
            return len(self.requests)
        else:
            raise ValueError('Invalid value for t')


def recent_counter(operations, operands):
    recent_counter = None
    output = []

    for key, value in zip(operations, operands):
        if key == "RecentCounter":
            recent_counter = RecentCounter()
            output.append(None)
        elif key == "ping":
            output.append(recent_counter.ping(value[0]))

    return output


# Тестимо:
# queue_operations = ["RecentCounter", "ping", "ping", "ping", "ping"]
# queue_operands = [[], [1], [100], [3001], [3002]]
# print(recent_counter(queue_operations, queue_operands))

# ______________________________________________________________________________________________________________________

"""
4. Дизайн замкнутої двубічної черги (Deque)
Розробіть свою реалізацію циклічної двосторонньої черги (deque).

Реалізуйте клас MyCircularDeque:

MyCircularDeque(int k) Ініціалізує deque з максимальним розміром k.
boolean insertFront() Додає елемент на початку Deque. Повертає true, якщо операція виконана успішно, або false в іншому випадку.
boolean insertLast() Додає елемент у задній частині Deque. Повертає true, якщо операція виконана успішно, або false в іншому випадку.
boolean deleteFront() Видаляє елемент із початку Deque. Повертає true, якщо операція виконана успішно, або false в іншому випадку.
boolean deleteLast() Видаляє елемент із задньої частини Deque. Повертає true, якщо операція виконана успішно, або false в іншому випадку.
int getFront() Повертає передній елемент із Deque. Повертає -1, якщо двочерга порожня.
int getRear() Повертає останній елемент із Deque. Повертає -1, якщо двочерга порожня.
boolean isEmpty() Повертає true, якщо двочерга порожня, або false в іншому випадку.
boolean isFull() Повертає true, якщо двочерга заповнена, або false в іншому випадку.
Приклад 1:

Input ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", 
"insertFront", "getFront"] [[3], [1], [2], [3], [4], [], [], [], [4], []]

Output [null, true, true, true, false, 2, true, true, true, 4]
 
Пояснення 
MyCircularDeque myCircularDeque = new MyCircularDeque(3); 
myCircularDeque.insertLast(1); // return True 
myCircularDeque.insertLast(2); // return True 
myCircularDeque.insertFront(3); // return True 
myCircularDeque.insertFront(4); // return False, the queue is full. 
myCircularDeque.getRear(); // return 2 
myCircularDeque.isFull(); // return True 
myCircularDeque.deleteLast(); // return True 
myCircularDeque.insertFront(4); // return True 
myCircularDeque.getFront(); // return 4

Обмеження:
1 <= k <= 1000
0 <= value <= 1000
Щонайбільше 2000 викликів буде зроблено для insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, 
isFull.
"""


class MyCircularDeque:
    MAX_CALLS = 2000  # Максимальна кількість викликів

    def __init__(self, k):
        if 1 <= k <= 1000:
            # Ініціалізація deque з максимальним розміром k
            self.capacity = k
            self.size = 0
            self.front = 0
            self.rear = -1
            self.deque = [0] * k
            self.call_count = 0  # Лічильник викликів
        else:
            raise ValueError('k must be in the range [1, 1000]')

    def _increment_calls(self):
        self.call_count += 1
        if self.call_count > self.MAX_CALLS:
            raise ValueError('Maximum number of calls exceeded')

    def insertFront(self, value):
        self._increment_calls()
        if 0 <= value <= 1000:
            # Додавання елементу на початку Deque
            if not self.isFull():
                self.front = (self.front - 1) % self.capacity
                self.deque[self.front] = value
                self.size += 1
                return True
            return False
        else:
            raise ValueError('value must be in the range [0, 1000]')

    def insertLast(self, value):
        self._increment_calls()
        if 0 <= value <= 1000:
            # Додавання елементу в кінці Deque
            if not self.isFull():
                self.rear = (self.rear + 1) % self.capacity
                self.deque[self.rear] = value
                self.size += 1
                return True
            return False
        else:
            raise ValueError('value must be in the range [0, 1000]')

    def deleteFront(self):
        self._increment_calls()
        # Видалення елементу з початку Deque
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return True
        return False

    def deleteLast(self):
        self._increment_calls()
        # Видалення елементу з кінця Deque
        if not self.isEmpty():
            self.rear = (self.rear - 1) % self.capacity
            self.size -= 1
            return True
        return False

    def getFront(self):
        self._increment_calls()
        # Повертає передній елемент Deque
        return self.deque[self.front] if not self.isEmpty() else -1

    def getRear(self):
        self._increment_calls()
        # Повертає останній елемент Deque
        return self.deque[self.rear] if not self.isEmpty() else -1

    def isEmpty(self):
        self._increment_calls()
        # Перевіряє, чи Deque порожній
        return self.size == 0

    def isFull(self):
        self._increment_calls()
        # Перевіряє, чи Deque заповнений
        return self.size == self.capacity


def my_circular_deque(operations, operands):
    circular_deque = None
    output = []

    for op, op_values in zip(operations, operands):
        if op == "MyCircularDeque":
            circular_deque = MyCircularDeque(op_values[0])
            output.append(None)
        elif op == "insertFront":
            output.append(circular_deque.insertFront(op_values[0]))
        elif op == "insertLast":
            output.append(circular_deque.insertLast(op_values[0]))
        elif op == "deleteFront":
            output.append(circular_deque.deleteFront())
        elif op == "deleteLast":
            output.append(circular_deque.deleteLast())
        elif op == "getFront":
            output.append(circular_deque.getFront())
        elif op == "getRear":
            output.append(circular_deque.getRear())
        elif op == "isEmpty":
            output.append(circular_deque.isEmpty())
        elif op == "isFull":
            output.append(circular_deque.isFull())

    return output


# Тестимо
# deque_operations = ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull",
#                     "deleteLast", "insertFront", "getFront"]
# deque_operands = [[3], [1], [2], [3], [4], [], [], [], [4], []]
# print(my_circular_deque(deque_operations, deque_operands))

# ______________________________________________________________________________________________________________________

"""
5. Дизайн замкнутої черги
Розробіть свою реалізацію циклічної черги. Кругова черга — це лінійна структура даних, у якій операції виконуються за 
принципом FIFO (першим прийшов, першим вийшов), а остання позиція з’єднується з першою, щоб утворити коло. Його також 
називають «кільцевим буфером».

Однією з переваг кругової черги є те, що ми можемо використовувати простір перед чергою. У звичайній черзі, коли черга 
заповнюється, ми не можемо вставити наступний елемент, навіть якщо перед чергою є пробіл. Але використовуючи циклічну 
чергу, ми можемо використовувати простір для зберігання нових значень.

Реалізуйте клас MyCircularQueue:

MyCircularQueue(k) Ініціалізує об’єкт із розміром черги k.
int Front() Отримує передній елемент із черги. Якщо черга порожня, поверніть -1.
int Rear() Отримує останній елемент із черги. Якщо черга порожня, поверніть -1.
boolean enQueue(int value) Вставляє елемент у циклічну чергу. Повертає true, якщо операція виконана успішно.
boolean deQueue() Видаляє елемент із циклічної черги. Повертає true, якщо операція виконана успішно.
boolean isEmpty() Перевіряє, чи циклічна черга порожня чи ні.
boolean isFull() Перевіряє, чи заповнена циклічна черга.
Ви повинні вирішити проблему, не використовуючи вбудовану структуру даних черги у вашій мові програмування.
Приклад 1:

Input ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"] 
[[3], [1], [2], [3], [4], [], [], [], [4], []] 
Output [null, true, true, true, false, 3, true, true, true, 4] 
Пояснення: 
MyCircularQueue myCircularQueue = new MyCircularQueue(3); 
myCircularQueue.enQueue(1); // return True 
myCircularQueue.enQueue(2); // return True 
myCircularQueue.enQueue(3); // return True 
myCircularQueue.enQueue(4); // return False 
myCircularQueue.Rear(); // return 3 
myCircularQueue.isFull(); // return True 
myCircularQueue.deQueue(); // return True 
myCircularQueue.enQueue(4); // return True 
myCircularQueue.Rear(); // return 4

Обмеження:
1 <= k <= 1000
0 <= value <= 1000
Щонайбільше 3000 викликів буде зроблено для enQueue, deQueue, Front, Rear, isEmpty та isFull.
"""


class MyCircularQueue:

    def __init__(self, k):
        if 1 <= k <= 1000:
            self.capacity = k
            self.size = 0
            self.front = 0
            self.rear = -1
            self.circular_queue = [0] * k
        else:
            raise ValueError('k must be in the range [1, 1000]')

    def Front(self):
        return self.circular_queue[self.front] if self.size > 0 else -1

    def Rear(self):
        return self.circular_queue[self.rear] if self.size > 0 else -1

    def enQueue(self, value):
        if 0 <= value <= 1000:
            if not self.isFull():
                self.rear = (self.rear + 1) % self.capacity
                self.circular_queue[self.rear] = value
                self.size += 1
                return True
            return False
        else:
            raise ValueError('value must be in the range [0, 1000]')

    def deQueue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return True
        return False

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


def test_circular_queue(operations, operands):
    circular_queue = None
    output = []

    max_calls = 3000
    total_calls = 0

    for key, value in zip(operations, operands):
        if key == "MyCircularQueue":
            circular_queue = MyCircularQueue(value[0])
            output.append(None)
        elif key == "enQueue":
            output.append(circular_queue.enQueue(value[0]))
        elif key == "deQueue":
            output.append(circular_queue.deQueue())
        elif key == "Front":
            output.append(circular_queue.Front())
        elif key == "Rear":
            output.append(circular_queue.Rear())
        elif key == "isEmpty":
            output.append(circular_queue.isEmpty())
        elif key == "isFull":
            output.append(circular_queue.isFull())

        total_calls += 1
        if total_calls > max_calls:
            raise ValueError(f"Exceeded the maximum number of calls ({max_calls}) for operation: {key}")

    return output


# Тестимо
# queue_operations = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue",
#                     "enQueue", "Rear"]
# queue_operands = [[3], [1], [2], [3], [4], [], [], [], [4], []]
# print(test_circular_queue(queue_operations, queue_operands))

# ______________________________________________________________________________________________________________________

"""
6. Штампування послідовності
Вам дають два рядки stamp і target. Спочатку є рядок s довжини target.length з усіма s[i] == '?'.

За один хід ви можете поставити stamp поверх s і замінити кожну літеру в s на відповідну літеру з stamp.

Наприклад, якщо stamp = "abc" і target = "abcba", то s означає "?????" спочатку. 
За один хід ви можете:
помістіть stamp в індексі 0 s, щоб отримати "abc??",
розмістіть stamp в індексі 1 s, щоб отримати "?abc?", або
розмістіть stamp у індексі 2 s, щоб отримати "??abc".
Зауважте, що stamp має повністю міститися в межах s, щоб штампувати (тобто ви не можете розмістити stamp у індексі 3 s).
Ми хочемо перетворити s у target, використовуючи щонайбільше 10 * target.length обертів.

Повертає масив індексу крайньої лівої літери, що штампується на кожному повороті. Якщо ми не можемо отримати target від 
s протягом 10 * target.length ходів, повертаємо порожній масив.

Приклад 1:
Input: stamp = "abc", target = "ababc" 
Output: [0,2] 
Пояснення: Initially s = "?????". - Place stamp at index 0 to get "abc??". - Place stamp at index 2 to get "ababc". 
[1,0,2] would also be accepted as an answer, as well as some other answers.

Приклад 2:
Input: stamp = "abca", target = "aabcaca" 
Output: [3,0,1] 
Пояснення: Initially s = "???????". 
- Place stamp at index 3 to get "???abca". 
- Place stamp at index 0 to get "abcabca". 
- Place stamp at index 1 to get "aabcaca". 
return True 
myCircularQueue.enQueue(4); // 
return True 
myCircularQueue.Rear(); // 
return 4

Обмеження:
1 <= stamp.length <= target.length <= 1000
stamp і target складаються з малих англійських літер.
"""


def moves_to_stamp(stamp, target):
    n, m = len(target), len(stamp)

    if 1 <= n <= m <= 1000:
        raise ValueError("Incorrect len of stamp or target")

    stamped_positions = []

    def can_stamp(i):
        # Допоміжна функція для перевірки можливості застосування штампа в певній позиції
        return any(target[i + j] == '?' or target[i + j] == stamp[j] for j in range(m))

    def do_stamp(i):
        # Допоміжна функція для застосування штампа в певній позиції
        stamped_positions.append(i)
        for j in range(m):
            target_list[i + j] = '?'  # Замінюємо символи на '?'

    target_list = list(target)
    total_moves = 0

    # Продовжуємо наносити штампи до тих пір, поки загальна кількість рухів менша за 10 разів довжину цільового рядка
    while total_moves < 10 * n:
        stamped = False
        for i in range(n - m + 1):
            if can_stamp(i):
                do_stamp(i)
                stamped = True
                total_moves += 1

        if not stamped:
            break
        elif target_list == ['?'] * n:
            return stamped_positions

    return []


# Тестимо:
# stamp = "abc"
# target = "ababc"
# result = moves_to_stamp(stamp.lower(), target.lower())
# print(result)

# ______________________________________________________________________________________________________________________

"""
7. Максимум плаваючого вікна
Вам надано масив цілих чисел nums, є ковзаюче вікно розміром k, яке рухається з самого лівого краю масиву до самого 
правого. Ви можете побачити лише k чисел у вікні. Щоразу ковзне вікно переміщується на одну позицію праворуч.

Поверніть максимальне розсувне вікно.
Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3 Output: [3,3,5,5,6,7] 
Пояснення: Window position Max --------------- ----- 
[1 3 -1] -3 5 3 6 7 3 1 
[3 -1 -3] 5 3 6 7 3 1 3 
[-1 -3 5] 3 6 7 5 1 3 -1 
[-3 5 3] 6 7 5 1 3 -1 -3 
[5 3 6] 7 6 1 3 -1 -3 5 
[3 6 7] 7

Example 2:

Input: nums = [1], k = 1 Output: [1]

Обмеження:
1 <= nums.length <= 100 000
-10 000 <= nums[i] <= 10 000
1 <= k <= nums.length
"""


def maxSlidingWindow(nums, k):
    if not (1 <= len(nums) <= 100000 and all(-10000 <= x <= 10000 for x in nums) and 1 <= k <= len(nums)):
        raise ValueError("Not valid nums and k")

    result = []
    max_heap = []

    # Ініціалізуємо купільник для перших k елементів
    for i in range(k):
        heapq.heappush(max_heap, -nums[i])  # Використовуємо від'ємні значення для отримання максимального елемента
    result.append(-max_heap[0])  # Додаємо максимальний елемент у результат для першого вікна

    for i in range(k, len(nums)):
        # Видаляємо з купільника елемент, який виходить з вікна
        max_heap.remove(-nums[i - k])  # Використовуємо від'ємні значення для видалення
        heapq.heapify(max_heap)  # Перебудовуємо купільник

        # Додаємо новий елемент у вікно
        heapq.heappush(max_heap, -nums[i])  # Використовуємо від'ємні значення для отримання максимального елемента

        result.append(-max_heap[0])  # Додаємо максимальний елемент у результат для поточного вікна

    return result


# Тестуємо
# nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
# k1 = 3
# print(maxSlidingWindow(nums1, k1))
#
# nums2 = [1]
# k2 = 1
# print(maxSlidingWindow(nums2, k2))

# ______________________________________________________________________________________________________________________

"""
8. Обмежена сума підпослідовності
Дано цілий масив nums і ціле k, повернути максимальну суму непорожньої підпослідовності цього масиву так, що для 
кожних двох послідовних цілих чисел у підпослідовності, nums[i] і nums[j], де i < j, умова j - i <= k виконується.

Підпослідовність масиву отримується видаленням деякої кількості елементів (може бути нулем) із масиву, залишаючи решту 
елементів у початковому порядку.

Example 1:
Input: nums = [10,2,-10,5,20], k = 2 
Output: 37 
Пояснення: Підпослідовність це [10, 2, 5, 20].

Example 2:
Input: nums = [-1,-2,-3], k = 1 
Output: -1 
Пояснення: Підпослідовність має бути не пустою, щоб ми могли обрати максимальне число.

Example 3:
Input: nums = [10,-2,-10,-5,20], k = 2 
Output: 23 
Пояснення: Підпослідовність це [10, -2, -5, 20].

Обмеження:
1 <= k <= nums.length <= 100 000
-10 000 <= nums[i] <= 10 000
"""


def subset_sum(nums, k):
    if not (1 <= k <= len(nums) <= 100000 and all(-10000 <= x <= 10000 for x in nums)):
        raise ValueError("Not valid nums and k")

    n = len(nums)
    dp = [0] * n  # Створюємо масив для зберігання максимальних сум

    for i in range(n):
        # Обчислюємо максимальну суму для поточного елемента
        dp[i] = max(nums[i], max(dp[max(0, i - k):i], default=0) + nums[i])

    return max(dp)


# Тестуємо
# nums1 = [10, 2, -10, 5, 20]
# k1 = 2
# print(subset_sum(nums1, k1))
#
# nums2 = [-1, -2, -3]
# k2 = 1
# print(subset_sum(nums2, k2))
#
# nums3 = [10, -2, -10, -5, 20]
# k3 = 2
# print(subset_sum(nums3, k3))


