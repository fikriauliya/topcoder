# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

# Better solution: http://vexorian.blogspot.sg/2014/03/srm-611-python-review.html
class LCMSetEasy:
    def gen_primes(self):
        D = {}
        q = 2
        while True:
            if q not in D:
                yield q
                D[q * q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            q += 1

    def factorize(self, x):
        primes = self.gen_primes()
        p = next(primes)
        res = dict()
        if x== 1:
            res[1] = 1
            return res
        else:
            while x > 1:
                if x % p == 0:
                    res.setdefault(p, 0)
                    res[p] += 1
                    x /= p
                else:
                    p = next(primes)
            return res

    def include(self, S, x):
        fact = self.factorize(x)
        for i in xrange(len(S)):
            fact_s = self.factorize(S[i])
            if set(fact_s.keys()).issubset(set(fact.keys())):
                for k in fact_s.keys():
                   if fact[k] == fact_s[k]:
                       fact[k] = 0

        if all([b == 0 for b in fact.values()]):
            return "Possible"
        else:
            return "Impossible"

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(S, x, __expected):
    startTime = time.time()
    instance = LCMSetEasy()
    exception = None
    try:
        __result = instance.include(S, x);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("LCMSetEasy (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("LCMSetEasy.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            S = []
            for i in range(0, int(f.readline())):
                S.append(int(f.readline().rstrip()))
            S = tuple(S)
            x = int(f.readline().rstrip())
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(S, x, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1399868789
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
