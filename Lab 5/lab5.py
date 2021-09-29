############################################################
# CS115 Lab 5
# Name: Tyler Seliber
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
############################################################

def dotProduct(L, K):
    '''Output dot product of lists L and K'''
    pass

# Test code:
print('Testing dotProduct()')
print('dotProduct([5, 3], [6, 4]) should be 42: ' + str(dotProduct([5, 3], [6, 4])))
print()

def removeAll(e, L):
    '''Remove all elements 'e' from list 'L' '''
    pass

# Test code:
print('Testing removeAll()')
print('removeAll(42, [55, 77, 42, 11, 42, 88]) should be [55, 77, 11, 88]:' + str(removeAll(42, [55, 77, 42, 11, 42, 88])))
print('removeAll(42, [55, [77, 42], [11, 42], 88]) should be [55, [77, 42], [11, 42], 88]:' + str(removeAll(42, [55, [77, 42], [11, 42], 88])))
print('removeAll([77, 42], [55, [77, 42], [11, 42], 88 ]) should be [55, [11, 42], 88]:' + str(removeAll([77, 42], [55, [77, 42], [11, 42], 88])))
print()


def geometricSeq(n, f, b):
    
    pass

# Test code:
print('Testing geometricSeq()')
print('geometricSeq(1, 2, 5) should be 5: ' + str(geometricSeq(1, 2, 5)))
print('geometricSeq(3, 3, 1) should be 9: ' + str(geometricSeq(3, 3, 1)))
print('geometricSeq(3, 2, 10) should be 40: ' + str(geometricSeq(3, 2, 10)))
print()

def deepReverse(L):
    '''Returns reversal of list L'''
    pass

# Test code:
print('Testing deepReverse()')
print('deepReverse([1, 2, 3]) should be [3, 2, 1]: ' + str(deepReverse([1, 2, 3])))
print('deepReverse([1, [2, 3], 4]) should be [4, [3, 2], 1]: ' + str(deepReverse([1, [2, 3], 4])))
print('deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]]) should be [[[8, [7, 6], 5], [4, 3], 2], 1]: ' + str(deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]])))
print()