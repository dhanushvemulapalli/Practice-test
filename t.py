class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(1)
curr = head 
for i in range(2,6):
    curr.next = Node(i)
    curr = curr.next

# curr = head
# while curr:
#     print(curr.data, end = "->")
#     curr = curr.next

count = 0
curr = head
while curr:
    count += 1
    curr = curr.next
# print(count)
idx = count//2 
curr = head
for i in range(idx):
    curr = curr.next

print(curr.data)

sptr =head
fptr = head
while fptr and fptr.next:
    sptr = sptr.next
    fptr = fptr.next.next

print(sptr.data)
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)

# print(head.data)
# print(head.next.data)
# print(head.next.next.data)
# print(head.next.next.next.data)
# print(head.next.next.next.next.data)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

# print("Binary Tree Before Mirroring")
# # print(root.data)
# # print(root.left.data)
# # print(root.right.data)
# # print(root.left.left.data)
# # print(root.left.right.data)
# # print(root.right.left.data)
# # print(root.right.right.data)

# def print_tree(root):
#     if root is None :
#         return
#     print_tree(root.left)
    
#     print(root.data, end = "   ")

#     print_tree(root.right)


# print_tree(root)

# def mirror(root):
#     if root is None:
#         return
#     mirror(root.left)
#     mirror(root.right)
#     root.left, root.right = root.right, root.left
# mirror(root)

# print("\nBinary Tree After Mirroring")
# print_tree(root)