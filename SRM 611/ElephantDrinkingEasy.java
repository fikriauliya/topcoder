import java.io.*;
import java.util.*;

public class ElephantDrinkingEasy {
	int n;
	
	private int rec(char[][] sim, int ctr, int allocated) {
		if (ctr == n * n) {
			return allocated;
		} else {
			int i = ctr / n;
			int j = ctr % n;
			
			int[] r = new int[5];
			r[0] = rec(sim, ctr + 1, allocated);
			
			if (sim[i][j] == 'Y') {
				char[][] origSim = new char[n][n];
				for (int k=0;k<n;k++) for (int l=0;l<n;l++) origSim[k][l] = sim[k][l];
				
				boolean isValid = true;
				for (int k=0;k<j;k++) if (sim[i][k] == '#') isValid = false;
				if (isValid) {
					for (int k=0;k<=j;k++) sim[i][k] = '#';
					r[1] = rec(sim, ctr + 1, allocated + 1);
					for (int k=0;k<=j;k++) sim[i][k] = origSim[i][k];
				}
				
				isValid = true;
				for (int k=j+1;k<n;k++) if (sim[i][k] == '#') isValid = false;
				if (isValid) {
					for (int k=j;k<n;k++) sim[i][k] = '#';
					r[2] = rec(sim, ctr + 1, allocated + 1);
					for (int k=j;k<n;k++) sim[i][k] = origSim[i][k];
				}
				
				isValid = true;
				for (int k=0;k<i;k++) if (sim[k][j] == '#') isValid = false;
				if (isValid) {
					for (int k=0;k<=i;k++) sim[k][j] = '#';
					r[3] = rec(sim, ctr + 1, allocated + 1);
					for (int k=0;k<=i;k++) sim[k][j] = origSim[k][j];
				}
				
				isValid = true;
				for (int k=i+1;k<n;k++) if (sim[k][j] == '#') isValid = false;
				if (isValid) {
					for (int k=i;k<n;k++) sim[k][j] = '#';
					r[4] = rec(sim, ctr + 1, allocated + 1);
					for (int k=i;k<n;k++) sim[k][j] = origSim[k][j];
				}
			}
			
			int max = 0;
			for (int k=0; k<5; k++) if (r[k] > max) max=r[k];
			return max;
		}
	}
	
	public int maxElephants(String[] map) {
		n = map.length;
		
		char[][] cMap = new char[n][n];
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				cMap[i][j] = map[i].charAt(j);
			}
		}
			
		return rec(cMap, 0, 0);
	}

// CUT begin
	public static void main(String[] args){
		System.err.println("ElephantDrinkingEasy (1000 Points)");
		System.err.println();
		HashSet<Integer> cases = new HashSet<Integer>();
        for (int i = 0; i < args.length; ++i) cases.add(Integer.parseInt(args[i]));
        runTest(cases);
	}

	static void runTest(HashSet<Integer> caseSet) {
	    int cases = 0, passed = 0;
	    while (true) {
	    	String label = Reader.nextLine();
	    	if (label == null || !label.startsWith("--"))
	    		break;

            String[] map = new String[Integer.parseInt(Reader.nextLine())];
            for (int i = 0; i < map.length; ++i)
                map[i] = Reader.nextLine();
            Reader.nextLine();
            int __answer = Integer.parseInt(Reader.nextLine());

            cases++;
            if (caseSet.size() > 0 && !caseSet.contains(cases - 1))
                continue;
    		System.err.print(String.format("  Testcase #%d ... ", cases - 1));

            if (doTest(map, __answer))
                passed++;
	    }
	    if (caseSet.size() > 0) cases = caseSet.size();
        System.err.println(String.format("%nPassed : %d/%d cases", passed, cases));

        int T = (int)(System.currentTimeMillis() / 1000) - 1399879891;
        double PT = T / 60.0, TT = 75.0;
        System.err.println(String.format("Time   : %d minutes %d secs%nScore  : %.2f points", T / 60, T % 60, 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))));
	}

	static boolean doTest(String[] map, int __expected) {
		for (int i = 0; i < map.length; i++) {
			map[i] = new String(map[i]);
		}
		long startTime = System.currentTimeMillis();
		Throwable exception = null;
		ElephantDrinkingEasy instance = new ElephantDrinkingEasy();
		int __result = 0;
		try {
			__result = instance.maxElephants(map);
		}
		catch (Throwable e) { exception = e; }
		double elapsed = (System.currentTimeMillis() - startTime) / 1000.0;

		if (exception != null) {
			System.err.println("RUNTIME ERROR!");
			exception.printStackTrace();
			return false;
		}
		else if (__result == __expected) {
			System.err.println("PASSED! " + String.format("(%.2f seconds)", elapsed));
			return true;
		}
		else {
			System.err.println("FAILED! " + String.format("(%.2f seconds)", elapsed));
			System.err.println("           Expected: " + __expected);
			System.err.println("           Received: " + __result);
			return false;
		}
	}

	static class Reader {
        private static final String dataFileName = "ElephantDrinkingEasy.sample";
	    private static BufferedReader reader;

	    public static String nextLine() {
	        try {
                if (reader == null) {
                    reader = new BufferedReader(new InputStreamReader(new FileInputStream(dataFileName)));
                }
                return reader.readLine();
	        }
	        catch (IOException e) {
	            System.err.println("FATAL!! IOException");
	            e.printStackTrace();
	            System.exit(1);
	        }
	        return "";
	    }
	}
// CUT end
}
