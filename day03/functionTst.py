# 函数
# 斐波那切数列 即任意两个数的和都是后一个数
fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])

print(fibs)


def fibsfun(num):
    'hahahahhah'
    fibs = [0, 1]
    for i in range(num):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs


# 定义一个函数，没有任何的返回值
def noreturn():
    print("hahah")
    return


x = noreturn()
print(x)

num = input("input num:\n")
print(fibsfun(int(num)))

print(callable(fibsfun)) # 使用callable判断是否可调用

print(fibsfun.__doc__)

help(fibsfun)



'''
给定一个正整数，实现一个方法来求出离该整数最近的大于自身的“换位数”。
    什么是换位数呢？就是把一个整数各个数位的数字进行全排列，从而得到新的整数。例如53241和23541。
    小灰也不知道这种经过换位的整数应该如何称呼，所以姑且称其为“换位数”。
    题目要求写一个方法来寻找最近的且大于自身的换位数。比如下面这样：
    输入12345，返回12354
    输入12354，返回12435
    输入12435，返回12453
'''
def findNearestNumber(nums):
    # 复制一份，避免修改原列表
    numsCopy = nums[:]
    # 查找逆序开始点
    index = findTransferPoint(numsCopy)
    # 交换逆序开始点前一个点和逆序中最小的整数
    exchangeHead(numsCopy, index)
    reverse(numsCopy, index)
    return numsCopy;

def findTransferPoint(nums):
    for i in list(reversed(range(0, len(nums)))):
        if nums[i] > nums[i - 1]:
            return i;
    else:
        return 0


def exchangeHead(nums, index):
    for i in list(reversed(range(index, len(nums)))):
        if nums[i] > nums[index-1]:
            nums[index-1], nums[i] = nums[i], nums[index-1]
            break

def reverse(nums, index):
    for i, j in zip(range(index, len(nums)),list(reversed(range(0, len(nums))))):
        if i < j:
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break
        else:
            break

print(findNearestNumber([1,2,0,5,1,2,4,3])) # 输出12051324
