class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def averageOfSubtree(root: TreeNode):
    ans=1
    def gettree(root):
        nonlocal ans
        if root is None:
            return 0,0
        lsum,l=gettree(root.left)
        rsum,r=gettree(root.right)
        tsum=root.val+lsum+rsum
        count=1+l+r
        if tsum//count==root.val:
            ans+=1
        return tsum,count
    gettree(root)
    return ans
c=TreeNode(2)
b=TreeNode(3)
a=TreeNode(1,b,c)
print(averageOfSubtree(a))
