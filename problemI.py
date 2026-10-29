
def divisors_count(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0: 
            if i * i == n: 
                count += 1 
            else:
                count+= 2 
        i += 1
    return count
def main():
    x = int(input())
    if x < 0: 
        return 0
    i = 1 
    divisors = []
    while i*i <= x:
        if x % i == 0:
            divisors.append(i)
        i+= 1
    for j in divisors:
        if j**(divisors_count(j)) == x:
            print(j)
            return
        
    print("-1")

if __name__ == '__main__':
    main()