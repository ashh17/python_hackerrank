# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
m = int(m)
n = int(n)
z = int((m-3)/2)
y = int(n/2)
c = '.|.'
if n % 2 != 0 and m == 3*n:
    for i in range(y):
        print((c*i).rjust(z, '-')+c+(c*i).ljust(z, '-'))

    print('WELCOME'.center(m, '-'))

    for i in range(y-1, -1, -1):
        print((c*i).rjust(z, '-')+c+(c*i).ljust(z, '-'))


# other useful solution
#N, M = map(int, input().split())
# for i in xrange(1, N, 2):
#    print str('.|.' * i).center(M, '-')
# print 'WELCOME'.center(M, '-')
# for i in xrange(N-2, -1, -2):
#    print str('.|.' * i).center(M, '-')
