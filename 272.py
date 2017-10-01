# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):

        self.pred, self.succ = [], []
        self.initialize(root, target)
        res = []

        if self.succ and self.pred and self.succ[-1].val == self.pred[-1].val:
            _ = self.next_pred()

        while k:
            if not self.succ:
                res.append(self.next_pred())
            elif not self.pred:
                res.append(self.next_succ())
            else:
                succ_diff, pred_diff = abs(self.succ[-1].val * 1.0 - target), abs(self.pred[-1].val * 1.0 - target)
                res.append(self.next_pred() if succ_diff > pred_diff else self.next_succ())
            k -= 1
        return res


    def initialize(self, root, target):
        while root:
            if root.val == target:
                self.pred.append(root)
                self.succ.append(root)
                break
            elif root.val > target:
                self.succ.append(root)
                root = root.left
            else:
                self.pred.append(root)
                root = root.right

    def next_pred(self):
        curr = self.pred.pop()
        ret = curr.val
        curr = curr.left
        # update the predecessors
        while curr:
            self.pred.append(curr)
            curr = curr.right
        return ret

    def next_succ(self):
        curr = self.succ.pop()
        ret = curr.val
        curr = curr.right
        # update the successors
        while curr:
            self.succ.append(curr)
            curr = curr.left
        return ret
