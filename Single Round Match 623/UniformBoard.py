# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class UniformBoard:
    def getBoard(self, board, K):
        count = {}
        ss = "AP."
        height = len(board)
        width = len(board[0])

        for s in ss:
            count[s] = [[0 for _ in xrange(width + 1)] for _ in xrange(height + 1)]
            for i in xrange(1, height + 1):
                for j in xrange(1, width + 1):
                    count[s][i][j] = count[s][i-1][j] + count[s][i][j-1] - count[s][i-1][j-1]
                    if board[i-1][j-1] == s:
                        count[s][i][j] = 1 + count[s][i][j]

            # print(count[s])

        def rectangle(c, x0, y0, x1, y1):
            # print(x0, y0, x1, y1)
            return count[c][y1][x1] - count[c][y0][x1] - count[c][y1][x0] + count[c][y0][x0]

        sumApples = rectangle('A', 0, 0, width, height)
        sumEmpties = rectangle('.', 0, 0, width, height)

        res = 0
        # print(height + " x " + width)
        for y0 in xrange(height):
            for x0 in xrange(width):
                for y1 in xrange(y0 + 1, height + 1):
                    for x1 in xrange(x0 + 1, width + 1):
                        countEmpties = rectangle('.', x0, y0, x1, y1)
                        countPears = rectangle('P', x0, y0, x1, y1)
                        rectangleArea = (y1 - y0) * (x1 - x0)

                        if (sumApples >= rectangleArea) and (countPears == 0 or sumEmpties > 0):
                            if countEmpties + 2 * countPears <= K:
                                res = max(res, rectangleArea)

        return res

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

def do_test(board, K, __expected):
    startTime = time.time()
    instance = UniformBoard()
    exception = None
    try:
        __result = instance.getBoard(board, K);
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
    sys.stdout.write("UniformBoard (300 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("UniformBoard.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            board = []
            for i in range(0, int(f.readline())):
                board.append(f.readline().rstrip())
            board = tuple(board)
            K = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(board, K, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1402381114
    PT, TT = (T / 60.0, 75.0)
    points = 300 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
