# Scanner Documentation

##### I. Scanner Implementation

```
The scanner input will be a text file containind the source program, and will produce as output the following:
	- PIF - Program Internal Form
	- ST  - Symbol Table
In addition, the program should be able to determine the lexical errors, specifying the location, and, if possible, the type of the error.

The scanner assignment will be diferentiated based on:
	1. Identifiers:
		a. length at most 8 characters
	2. Symbol Table:
		a. unique for identifiers and constants
	3. Symbol Table Organization:
		c. hashing table
```

The scanner was implemented in Python 3.7



##### II. Data Structures

- Program Internal Form:
  - The PIF is implemented using a list of lists
  - The list of lists has only 2 levels, thus making it act as a matrix
  - Each sublist has only 2 elements making them act as tuples, so the matrix has actually only 2 columns
- Symbol Table
  - The ST was implemented using a hash table
  - The hash table was implemented using a list of lists, and has 10 positions
  - h(x) = x%length
  - Collisions are avoided by finding the first empty cell
- Codification table
  - The Codification table is a dictionary in which the key is a separator/reserved word/operator and the value is an integer number
  - value 0 and 1 are reserved for 'identifier' and 'constant' respectively