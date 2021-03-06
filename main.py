import random
import string
from typing import List, Tuple, Optional, Iterator, Generator
from collections import deque, defaultdict
import hashlib
import operator
from collections import Counter
import math
import sys


def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


def linear_search(numbers: List[int], value: int) -> int:
    for i in range(len(numbers)):
        if numbers[i] == value:
            return i
    return -1


def binary_search(numbers: List[int], value: int) -> int:
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return - 1


def binary_search_2(numbers: List[int], value: int) -> int:
    def _binary_search(numbers: List[int], value: int,
                       left: int, right: int) -> int:
        if left > right:
            return - 1

        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(numbers, value, mid + 1, right)
        else:
            _binary_search(numbers, value, left, mid - 1)

    _binary_search(numbers, value, 0, len(numbers)-1)


# class Node(object):
#     def __init__(self, data, next_node=None):
#         self.data = data
#         self.next = next_node


class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


class HashTable(object):
    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for i in range(self.size)]

    def hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def print(self) -> None:
        for index in range(self.size):
            print(index, end=" ")
            for data in self.table[index]:
                print("-->", end=" ")
                print(data, end=" ")

            print()

    def get(self, key):
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    def __setitem__(self, key, value) -> None:
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)


def getPair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)


def getPair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_numbers = sum(numbers)
    # if sum_numbers % 2 != 0:
    #     return
    # half_sum = int(sum_numbers / 2)
    half_sum, remainder = divmod(sum_numbers, 2)
    if remainder != 0:
        return
    cache = set()
    for num in numbers:
        cache.add(num)
        val = half_sum - num
        if val in cache:
            return val, num


class Stack(object):

    def __init__(self) -> None:
        self.stack = []

    def push(self, data) -> None:
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()


def validate_format(chars: str) -> bool:
    lookup = {"{": "}", "[": "]", "(": ")"}
    stack = []
    for c in chars:
        if c in lookup.keys():
            stack.append(lookup[c])
        if c in lookup.values():
            if not stack:
                return False
            if c != stack.pop():
                return False
    if stack:
        return False
    return True


class Que(object):

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)


def reverse(queue):
    new_queue = deque()
    while queue:
        new_queue.append(queue.pop())

    return new_queue


class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


def find_pair(pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
    cache = {}
    for pair in pairs:
        first, second = pair[0], pair[1]
        value = cache.get(second)
        if not value:
            cache[first] = second
        elif value == first:
            yield pair


def find_max_value(value: str):
    cache = []
    for a in value:
        if a.isalpha():
            cache.append(a.lower())
    List = Counter(cache).most_common()
    print(cache)
    return List[0]


def count_chars_v1(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    # l = []
    # for char in strings:
    #     if not char.isspace():
    #         l.append((char, strings.count(char)))
    ln = [(c, strings.count(c)) for c in strings if not c.isspace()]
    return max(ln, key=operator.itemgetter(1))


def count_chars_v2(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = {}
    for char in strings:
        if not char.isspace():
            d[char] = d.get(char, 0) + 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


def count_chars_v3(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = Counter()
    for char in strings:
        print(d)
        if not char.isspace():
            d[char] += 1
    max_key = max(d, key=d.get)
    print(d)
    return max_key, d[max_key]


def memoize(f):
    cache = {}

    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return _wrapper


# @memoize
def long_func(num: int) -> int:
    r = 0
    for i in range(10000000):
        r += num * i
    return r


def min_count_remove(x: List[int], y: List[int]) -> None:
    # count_x = {}
    # count_y = {}
    # for i in x:
    #     count_x[i] = count_x.get(i, 0) + 1
    # for i in y:
    #     count_y[i] = count_y.get(i, 0) + 1
    counter_x = Counter(x)
    counter_y = Counter(y)

    for key_x, value_x in counter_x.items():
        value_y = counter_y.get(key_x)
        if value_y:
            if value_x < value_y:
                x[:] = [i for i in x if i != key_x]
            elif value_x > value_y:
                y[:] = [i for i in y if i != key_x]


def remove_zero(numbers: List[int]) -> None:
    if numbers and numbers[0] == 0:
        numbers.pop(0)
        remove_zero(numbers)


def list_to_int(numbers: List[int]) -> int:
    sum_numbers = 0
    for i, num in enumerate(reversed(numbers)):
        sum_numbers += num * (10 ** i)
    return sum_numbers


def list_to_int_plus_one(numbers: List[int]) -> int:
    i = len(numbers) - 1
    numbers[i] += 1
    while 0 < i:
        if numbers[i] != 10:
            remove_zero(numbers)
            break

        numbers[i] = 0
        numbers[i-1] += 1
        i -= 1
    else:
        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)
    return list_to_int(numbers)


def snake_string_v1(chars: str) -> List[List[str]]:
    result = [[], [], []]
    result_indexes = {0, 1, 2}
    insert_index = 1
    for i, s in enumerate(chars):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(" ")
    return result


def snake_string_v2(chars: str, depth: int) -> List[List[str]]:
    result = [[] for _ in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = int(depth / 2)

    # def pos(i):
    #     return i + 1

    # def neg(i):
    #     return i - 1
    op = operator.neg

    for s in chars:
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(" ")
        if insert_index <= 0:
            op = operator.pos
        if insert_index >= depth - 1:
            op = operator.neg
        insert_index += op(1)
    return result


def get_max_sequence_sum(numbers: List[int]) -> int:
    result_sequence, sum_sequence = 0, 0
    for num in numbers:
        # temp_sum_sequence = sum_sequence + num
        # if num < temp_sum_sequence:
        #     sum_sequence = temp_sum_sequence
        # else:
        #     sum_sequence = num
        sum_sequence = max(num, sum_sequence + num)

        # if result_sequence < sum_sequence:
        #     result_sequence = sum_sequence
        result_sequence = max(result_sequence, sum_sequence)
    return result_sequence


def find_max_circular_sequence(numbers: List[int]) -> int:
    max_sequence_sum = get_max_sequence_sum(numbers)
    invert_numbers = []
    all_sum = 0
    for num in numbers:
        all_sum += num
        invert_numbers.append(-num)
    max_wrap_sequence = all_sum-(-get_max_sequence_sum(invert_numbers))
    return max(max_sequence_sum, max_wrap_sequence)


def delete_duplicate_v1(numbers: List[int]) -> None:
    tmp = []
    for num in numbers:
        if num not in tmp:
            tmp.append(num)
    numbers[:] = tmp
    print(numbers)


def delete_duplicate_v2(numbers: List[int]) -> None:
    tmp = [numbers[0]]
    i, len_num = 0, len(numbers) - 1
    while i < len_num:
        if numbers[i] != numbers[i + 1]:
            tmp.append(numbers[i + 1])
        i += 1
    numbers[:] = tmp
    print(numbers)


def delete_duplicate_v3(numbers: List[int]) -> None:
    i, len_numbers = 0, len(numbers) - 1
    while i < len_numbers - 1:
        if numbers[i] == numbers[i + 1]:
            numbers.remove((numbers[i]))
            i -= 1
        i += 1


def delete_duplicate_v4(numbers: List[int]) -> None:
    i = len(numbers) - 1
    while i > 0:
        if numbers[i] == numbers[i - 1]:
            numbers.pop(i)
        i -= 1


def all_perms(elements: List[int]) -> Iterator[List[int]]:

    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


def is_palindrome(strings: str) -> bool:
    len_strings = len(strings)
    if not len_strings:
        return False
    if len_strings == 1:
        return True
    start, end = 0, len_strings-1
    while start < end:
        if strings[start] != strings[end]:
            return False
        start += 1
        end -= 1
    return True


def find_palindrome(strings: str, left: int, right: int):
    # result = []
    while 0 <= left and right <= len(strings) - 1:
        if strings[left] != strings[right]:
            break
        yield strings[left: right + 1]
        left -= 1
        right += 1


def find__all_palindrome(strings: str):
    # result = []
    len_strings = len(strings)
    if not len_strings:
        yield
    if len_strings == 1:
        yield strings

    for i in range(1, len_strings - 1):
        yield from find_palindrome(strings, i - 1, i + 1)
        yield from find_palindrome(strings, i - 1, i)


def order_even_odd_last(numbers: List[int]) -> None:
    even_list = []
    odd_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    numbers[:] = even_list+odd_list


def order_even_odd_last_v2(numbers: List[int]) -> None:
    i, j = 0, len(numbers) - 1
    while i < j:
        if numbers[i] % 2 == 0:
            i += 1
        else:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j -= 1


def order_change_index_v1(chars: List[str], indexes: List[int]) -> str:
    tmp = [None] * len(chars)
    for i, index in enumerate(indexes):
        tmp[index] = chars[i]
    return "".join(tmp)


def order_change_index_v2(chars: List[str], indexes: List[int]) -> str:
    i, len_indexes = 0, len(indexes) - 1
    while i < len_indexes:
        while i != indexes[i]:
            index = indexes[i]
            chars[index], chars[i] = chars[i], chars[index]
            indexes[index], indexes[i] = indexes[i], indexes[index]
        i += 1
    return "".join(chars)


NUM_ALPHABET_MAPPING = {
    0: "+",
    1: "@",
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ",
}


def phone_mnemonic_v1(phone_numbers: str) -> List[str]:
    phone_number = [int(s) for s in phone_numbers.replace("-", "")]
    candidate = []
    tmp = [""] * len(phone_number)

    def find_candidate_alphabet(digit: int = 0) -> None:
        if digit == len(phone_number):
            candidate.append("".join(tmp))
        else:
            for char in NUM_ALPHABET_MAPPING[phone_number[digit]]:
                tmp[digit] = char
                find_candidate_alphabet(digit + 1)
    find_candidate_alphabet()
    return candidate


def generate_prime_v1(number: int) -> List[int]:
    primes = []

    for x in range(2, number + 1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            primes.append(x)
    return primes


def generate_prime_v2(number: int) -> List[int]:
    primes = []
    cache = {}
    for x in range(2, number + 1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        primes.append(x)
        cache[x] = True
        for y in range(x ** 2, number + 1, x):
            cache[y] = False
    return primes


def generate_prime_v3(number: int) -> Generator[int, None, None]:
    cache = {}
    for x in range(2, number + 1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue
        yield x
        cache[x] = True
        for y in range(x ** 2, number + 1, x):
            cache[y] = False


def is_prime_v1(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_prime_v2(num: int) -> bool:
    if num <= 1:
        return False
    # for i in range(2, math.floor(math.sqrt(num)) + 1):
    #     if num % i == 0:
    #         return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def is_prime_v3(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, math.floor(math.sqrt(num) + 1), 2):
        if num % i == 0:
            return False
    return True


def is_prime_v4(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, math.floor(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def taxi_cab_number(max_answer_num: int, match_answer_num: int = 2) -> List[Tuple[int, List[Tuple[int, int]]]]:
    result = []
    got_answer_count = 0
    answer = 1
    while got_answer_count < max_answer_num:
        match_answer_count = 0
        memo = defaultdict(list)

        max_param = int(pow(answer, 1.0 / 3)) + 1

        for x in range(1, max_param):
            for y in range(x + 1, max_param):
                if x ** 3 + y ** 3 == answer:
                    match_answer_count += 1
                    memo[answer].append((x, y))
        if match_answer_count == max_answer_num:
            result.append((answer, memo[answer]))
            got_answer_count += 1
        answer += 1
    return result


def felmer_last_theorem_v1(max_num: int, square_num: int) -> List[Tuple[int, int]]:
    result = []
    if square_num < 2:
        return result
    max_z = int(pow((max_num-1)**2+max_num**2, 1.0/square_num))
    for x in range(1, max_num + 1):
        for y in range(x + 1, max_num + 1):
            for z in range(y + 1, max_z):
                if pow(x, square_num) + pow(y, square_num) == pow(z, square_num):
                    result.append((x, y, z))
    return result


def felmer_last_theorem_v2(max_num: int, square_num: int) -> List[Tuple[int, int]]:
    result = []
    if square_num < 2:
        return result
    for x in range(1, max_num + 1):
        for y in range(x + 1, max_num + 1):
            pow_sum = pow(x, square_num)+pow(y, square_num)
            if pow_sum > sys.maxsize:
                raise ValueError(x, y, z, square_num, pow_sum)
            z = pow(pow_sum, 1.0 / square_num)
            if not z.is_integer():
                continue
            z = int(z)
            z_pow = pow(z, square_num)
            if z_pow == pow_sum:
                result.append((x, y, z))
    return result


def ceaser_cipher(text: str, shift: int) -> str:
    result = ""
    len_alphabet = ord("Z")-ord("A")+1
    for char in text:
        # if char.isupper():
        #     alphabet = string.ascii_uppercase
        # elif char.islower():
        #     alphabet = string.ascii_lowercase
        # else:
        #     result += char
        #     continue
        # index = (alphabet.index(char)+shift) % len(alphabet)
        # result += alphabet[index]
        if char.isupper():
            result += chr((ord(char)+shift-ord("A")) % len_alphabet+ord("A"))
        elif char.islower():
            result += chr((ord(char)+shift-ord("a")) % len_alphabet+ord("a"))
        else:
            result += char

    return result


def caeser_cipher_hack(text: str) -> Generator[Tuple[int, str], None, None]:
    len_alphabet = ord("Z") - ord("A") + 1
    # len_alphabet = len(string.ascii_uppercase)
    for candidate_shift in range(1, len_alphabet + 1):
        reverted = ""
        for char in text:
            # if char.isupper():
            #     alphabet = string.ascii_uppercase
            # elif char.islower():
            #     alphabet = string.ascii_lowercase
            # else:
            #     reverted += char
            #     continue
            # index = alphabet.index(char) - candidate_shift
            # if index < 0:
            #     index += len_alphabet
            # reverted += alphabet[index]
            if char.isupper():
                index = ord(char) - candidate_shift
                if index < ord("A"):
                    index += chr(index)
                reverted += chr(index)
            elif char.islower():
                index = ord(char) - candidate_shift
                if index < ord("a"):
                    index += len_alphabet
                reverted += chr(index)
            else:
                reverted += char
        yield candidate_shift, reverted


def hanoi(disk: int, src: str, dest: str, support: str):
    if disk < 1:
        return

    hanoi(disk-1, src, support, dest)
    print(f'move {disk} from {src} to {dest}')
    hanoi(disk-1, support, dest, src)


def get_hanoi_movement(disk: int, src: str, dest: str, support: str) -> List[Tuple[int, str]]:
    result = []

    def _hanoi(disk: int, src: str, dest: str, support: str):
        if disk < 1:
            return

        _hanoi(disk-1, src, support, dest)
        result.append((disk, src, dest))
        _hanoi(disk - 1, support, dest, src)
    _hanoi(disk, src, dest, support)
    return result


def generate_pascal_triangle(depth: int) -> List[List[int]]:
    data = [[1] * (i + 1) for i in range(depth)]
    for line in range(2, depth):
        for i in range(1, line):
            data[line][i] = data[line - 1][i - 1] + data[line - 1][i]
    return data


def print_pascal(data: List[int]) -> None:
    max_digit = len(str(max(data[-1])))
    width = max_digit+(max_digit % 2)+2
    for i, line in enumerate(data):
        numbers = "".join([str(i).center(width, " ") for i in line])
        print((" " * int(width/2))*(len(data)-i), numbers)


def generate_triangle_list(depth: int, max_num: int) -> List[List[int]]:
    return [[random.randint(0, max_num) for _ in range(i)]for i in range(1, depth+1)]


def print_triangle(data: List[List[int]]) -> None:
    max_digit = len(str(max([max(l) for l in data])))
    width = max_digit + (max_digit % 2) + 2
    for index, line in enumerate(data):
        numbers = "".join([str(i).center(width, " ") for i in line])
        print(" " * int(width/2)*(len(data)-index), numbers)


def sum_min_path(triangle: List[List[int]]) -> Optional[int]:
    tree_sum = triangle[:]
    j, len_triangle = 1, len(triangle)
    if not len_triangle:
        return
    while j < len_triangle:
        line = triangle[j]
        line_path_sum = []
        for i, value in enumerate(line):
            if i == 0:
                sum_value = line[i]+tree_sum[j-1][0]
            elif i == len(line) - 1:
                sum_value = line[i]+tree_sum[j-1][i-1]
            else:
                min_path = min(tree_sum[j-1][i-1], min([tree_sum[j-1][i]]))
                sum_value = line[i]+min_path
            line_path_sum.append(sum_value)
        tree_sum[j] = line_path_sum
        j += 1
    return (min(tree_sum[-1]))


if __name__ == '__main__':
    data = generate_triangle_list(5, 9)
    print_triangle(data)
    print('min_path -->>', sum_min_path(data))
