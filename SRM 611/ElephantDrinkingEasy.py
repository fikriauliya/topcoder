# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

# Brute force every possible combination. Exceeding time limits! Java version is still ok
# Much better solution: http://vexorian.blogspot.sg/2014/03/srm-611-python-review.html
class ElephantDrinkingEasy:
    def maxElephants(self, map):
        n = len(map)
        sim = [[map[i][j] for j in xrange(n)] for i in xrange(n)]
        size = n * n

        def rec(sim, ctr, allocated):
            if ctr == size:
                return allocated
            else:
                i = ctr / n
                j = ctr % n

                # Don't drink
                r1 = rec(sim, ctr + 1, allocated)
                r2, r3, r4, r5 = 0, 0, 0, 0

                orig_sim = [[sim[k][l] for l in xrange(n)] for k in xrange(n)]

                if sim[i][j] == 'Y':
                    # Drink from left
                    if not any((sim[i][k] == '#' for k in xrange(j))):
                        for k in xrange(j + 1): sim[i][k] = '#'
                        r2 = rec(sim, ctr + 1, allocated + 1)
                        for k in xrange(j + 1): sim[i][k] = orig_sim[i][k]

                    # Drink from right
                    if not any((sim[i][k] == '#' for k in xrange(j + 1, n))):
                        for k in xrange(j, n): sim[i][k] = '#'
                        r3 = rec(sim, ctr + 1, allocated + 1)
                        for k in xrange(j, n): sim[i][k] = orig_sim[i][k]

                    # Drink from top
                    if not any((sim[k][j] == '#' for k in xrange(i))):
                        for k in xrange(i + 1): sim[k][j] = '#'
                        r4 = rec(sim, ctr + 1, allocated + 1)
                        for k in xrange(i + 1): sim[k][j] = orig_sim[k][j]

                    # Drink from bottom
                    if not any((sim[k][j] == '#' for k in xrange(i + 1, n))):
                        for k in xrange(i, n): sim[k][j] = '#'
                        r5 = rec(sim, ctr + 1, allocated + 1)
                        for k in xrange(i, n): sim[k][j] = orig_sim[k][j]
                return max(r1, r2, r3, r4, r5)
        return rec(sim, 0, 0)

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

def do_test(map, __expected):
    startTime = time.time()
    instance = ElephantDrinkingEasy()
    exception = None
    try:
        __result = instance.maxElephants(map);
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
    sys.stdout.write("ElephantDrinkingEasy (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("ElephantDrinkingEasy.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            map = []
            for i in range(0, int(f.readline())):
                map.append(f.readline().rstrip())
            map = tuple(map)
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(map, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1399871872
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
