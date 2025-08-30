# operator bitwise, biner, dan binary

a = 9
b = 5

#bitwise or(|)
print("bitwise or")
c = a | b
print('nilai: ',a,' , binary:', format(a, '05b'))
print('nilai: ',b,' , binary:', format(b, '05b'))
print('nilai: ',c,' , binary:', format(c, '05b'))

#bitwise and(&)
print("bitwise and")
c = a & b
print('nilai: ',a,' , binary:', format(a, '05b'))
print('nilai: ',b,' , binary:', format(b, '05b'))
print('nilai: ',c,' , binary:', format(c, '05b'))

#bitwise xor(^)
print("bitwise xor")
c = a ^ b
print('nilai: ',a,' , binary:', format(a, '05b'))
print('nilai: ',b,' , binary:', format(b, '05b'))
print('nilai: ',c,' , binary:', format(c, '05b'))

#bitwise not(~)
print("bitwise not")
a = -1
c = ~a
print('nilai: ',a,' , binary:', format(a, '05b'))
print('nilai: ',c,' , binary:', format(c, '05b'))

#nilai biner
a = 0b10101010
b = 0b11111111
print('nilai: ',a)
print('nilai: ',b)
print('nilai :', a^b, 'binary :', format(a^b, '08b'))

#shifting
#shift right
print("shift right")
a = 10
b = 2
c = a >> 1

print('nilai : ',a, 'binary :', format(a, '08b'))
print('nilai : ',b, 'binary :', format(b, '08b'))
print('nilai : ',c, 'binary :', format(c, '08b'))

#shift left
print("shift left")
c = a << 1
print('nilai : ',c, 'binary :', format(c, '08b'))