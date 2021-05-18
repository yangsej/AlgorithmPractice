def toPostorder(preorder, inorder, answers):
    N = len(preorder)
    if N == 0:
        return
    elif N == 1:
        answers.append(preorder[0])
        return
    elif N == 2:
        answers.append(preorder[1])
        answers.append(preorder[0])
        return
    else:
        root_idx = inorder.index(preorder[0])

        left_in = inorder[:root_idx]
        left_pre = preorder[1:1 + len(left_in)]
        toPostorder(left_pre, left_in, answers)

        right_in = inorder[root_idx + 1:]
        right_pre = preorder[len(left_pre) + 1:]

        toPostorder(right_pre, right_in, answers)

        answers.append(preorder[0])


T = int(input())
for t in range(T):
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    answers = []
    toPostorder(preorder, inorder, answers)
    print(" ".join(map(str, answers)))
