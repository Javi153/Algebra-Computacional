def fft_in_place(p, xi):
    n = len(p)//2
    d = 1
    while n >= 1:
        for i in range(d):
            for j in range(n):
                x = p[2*n*i+j]
                y = p[2*n*i+j+n]
                p[2*n*i+j] = x+y
                p[2*n*i+j+n] = x-y
        for i in range(d):
            for j in range(n):
                p[2*n*i+j+n] *= xi**(j*d)
        n //= 2
        d *= 2

def ifft_in_place(p, xi):
    d = len(p)//2
    n = 1
    while d >= 1:
        for i in range(d):
            for j in range(n):
                p[2*n*i+j+n] /= xi**(j*d)
        for i in range(d):
            for j in range(n):
                x = p[2*n*i+j]
                y = p[2*n*i+j+n]
                p[2*n*i+j] = 0.5*(x+y)
                p[2*n*i+j+n] = 0.5*(x-y)
        n *= 2
        d //= 2
