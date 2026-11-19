# BST(Binary Search Tree, 이진탐색트리)
# 중위 순회로 자료 정렬하기
# 각 노드 기준으로 left<node<right
# 왼쪽 서브트리 : 현재 노드보다 작은 값
# 오른쪽 서브트리 : 현재 노드보다 큰 값
# 입력 순성에 따라 트리 모양이 달라짐 





# BST 노드 정의
class Node:
    def __init__(self, key):
        self.key = key # 노드가 저장하는 값
        self.left = None # 왼쪽 자식 노드(더 작은 값이 저장)
        self.right = None # 오른쪽 자식 노드(더 큰 값이 저장)


# BST에 자료 삽입
def insert(root, key):
    if root is None:    # 현재 위치가 비워져 있다면
        return Node(key) # 새 노드 생성 후 그 자리에 값 넣고 리턴

    if key < root.key: # 넣을 값이 현재 노드보다 작으면 
        root.left = insert(root.left, key) # 새 노드를 생성

def inorder(root, result):
    if root is None:
        return

    inorder(root.left, result)
    result.append(root.key)
    inorder(root.right, result)



# values = [5, 3, 7, 2, 4, 9]
values = [9,7,5,4,3,1]
root = None
for v in values:
    root = insert(root, v)  # BST에 삽입하고 루트(최상단) 갱신


# BST 정렬 결과 출력
sorted_result = []
inorder(root, sorted_result)
print('순회 결과 : ', sorted_result)