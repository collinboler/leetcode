class Spreadsheet {
    HashMap<String, Integer> map;
    public Spreadsheet(int rows) {
        map = new HashMap<>();
        // initialize

    
    for (char c = 'A'; c <= 'Z'; c++) {
        for (int i = 1; i <= rows; i++) {
            StringBuilder sb = new StringBuilder();
            sb.append(String.valueOf(c)); 
            sb.append(String.valueOf(i));
            map.put(sb.toString(), 0); // initalize to 0
        }
    }
    }
    

    public void setCell(String cell, int value) {
        map.put(cell, value);
    }
    
    public void resetCell(String cell) {
        map.put(cell, 0);
    }
    
    public int get(String key) {
        if (map.get(key) != null) return map.get(key);
        return 0;
    }
    public int getValue(String formula) {
    int value1 = 0;
    int value2 = 0;
    StringBuilder sb = new StringBuilder();
    int i = 1;
    // first var
    while(i < formula.length() && formula.charAt(i) != '+') {
        sb.append(formula.charAt(i));
        i++;
    }
    i++;
    
    String val1 = sb.toString();
    if (Character.isLetter(formula.charAt(1))) {
        System.out.println(formula.charAt(1));
        System.out.println("val1:" + val1);
        value1 = map.get(val1);
    }
    else value1 = Integer.parseInt(val1);
    // second var
    StringBuilder sb2 = new StringBuilder();
    boolean varTwoL = false;
    System.out.println("yo: " + formula.charAt(i));
    if (Character.isLetter(formula.charAt(i))) varTwoL = true;
    System.out.println(varTwoL);
    while(i < formula.length()) {
        sb2.append(formula.charAt(i));
        i++;
    }
    String val2 = sb2.toString();
    if (varTwoL) value2 = map.get(val2);
    else {
        value2 = Integer.parseInt(val2);

    }
    return value1 + value2;

    // =A10+123
    // =123+B10
    // =123+123
    // letter case
    
    }
}

/**
 * Your Spreadsheet object will be instantiated and called as such:
 * Spreadsheet obj = new Spreadsheet(rows);
 * obj.setCell(cell,value);
 * obj.resetCell(cell);
 * int param_3 = obj.getValue(formula);
 */