def bezout(a, b):
    '''An implementation of extended Euclidean algorithm.
    Returns integer x, y and gcd(a, b) for Bezout equation:
        ax + by = gcd(a, b).
    '''
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)


def main():
    primes = [19, 23, 29]
    m = 1
    for i in range(len(primes)):
        m *= primes[i]
    mi = [int(m/primes[i]) for i in range(len(primes))]
    miopp = [int(bezout(mi[i], primes[i])[0]) % primes[i] for i in range(len(primes))]
    print("primes="+str(primes))
    print("m="+str(m))
    print("mi="+str(mi))
    print("miopp="+str(miopp))
    input("Continue?")
    results = []
    results_dict = dict()
    for k in range(primes[2]):
        for j in range(primes[1]):
            for i in range(primes[0]):
                xi = [i, j, k]
                for l in range(3):
                    xi[l] *= mi[l]*miopp[l]
                x = int(sum(xi)) % m
                results.append(x)
                results_dict.update({x: [i, j, k]})
                # print(i, j, k)
                # print(int(x))
    
    results.sort()
                
    print("\n"+"-"*50+'\n')
    print("Sorting...")
    
    print("Sorted:")
    ds = set()
    print(results[0])
    for i in range(1, len(results)):
        print(results[i], end =' ')
        d = results[i] - results[i-1]
        ds.add(d)
        print("d="+str(d))
        
    print("\n"+"-"*50+'\n')
    print("Set of ds (sorted):")
    dsl = list(ds)
    dsl.sort()
    for i in range(len(dsl)):
        print(dsl[i])
    
    print("\n"+"-"*50+'\n')
    print("i, j, k for sorted results:")
    for i in range(len(results)):
        print(results_dict[results[i]])
        print(results[i])
    input("Press any key to continue...")
    

if __name__ == "__main__":
    main()
    