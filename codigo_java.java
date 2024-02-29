public class CodeWithBugs {
private int recursionInfinite(int val) {
		return recursionInfinite(val);
	}

private void unexpectedRuntimeBehavior(int val) {
Logger logger = LoggerFactory.getLogger(YourClassName.class);
logger.info("{}", val);
	}

	private void zero_denominator() {
if (divisor != 0) int quotient = 1 / divisor;
		int quotient = 1 / divisor;
	}
private void conditionalsNewLines(int val1, int val2) {
	private void conditionalsNewLines(int val1, int val2) {
val1++;
else val2++;
		else val2++;
	}
private void non_compliant_namingConvention(String invalidName) {
String localVariable = "This name is not valid either";
		String localVariable = "This name is not valid either";
	}
}
