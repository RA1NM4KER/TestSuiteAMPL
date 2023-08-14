# TestSuiteAMPL

## Cloning
1. `clone https://github.com/RA1NM4KER/TestSuiteAMPL.git` into the directory/folder which holds your alan folder.
2. Navigate to directory `cd TestSuiteAMPL`
3. Run a script `python3 test.py xxx`

---

## Testing Scanner
1. **Comments**
	`python3 test.py comments`
	- nested comments
	- error messages; testing position
	- curly brackets inside string literals
	- block comments with error; testing position
	
2. **String Literals**
	`python3 test.py strings`
	- escape codes 
	- multi line string literal error
	- illegal escape codes
	- " at end
	- empty string
	- "untidy"strings"
	
3. **Error handling**
	`python3 test.py errors`
	- illegal characters
	- numbers too long
	- identifiers too long
	- error precedence
	- string not closed
	- comment not closed; normal and nested testing position
	
4. **All available**
	`python3 test.py all`
	- tests all above, and more.
	
--- 