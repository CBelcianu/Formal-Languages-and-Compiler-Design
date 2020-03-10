## Laboratory  3

### Context-free grammars

#### Construct the grammar corresponding to your mini-language defined in lab 1:

grammar = {*terminals*, *non_terminals*, *starting_symbol*, *production_rules*}

non_terminals = {**program_statement**, **function_call_statement**, **function**, **block**, **lhs**, **rhs**, **assignment**, **statement**, **statement_list**, **keyboard_io_operation**, **if_statement**, **condition**, **while_statement**, **expression**, **for_statement**}

terminals = { 0 `ID`, 1 `STRING`, 1 `NUMBER`, 1 `DIGIT`, 2 `if`, 3 `else`, 4 `while`, 5 `for`, 6 `def`, 7 `input`, 8 `print`  , 9 `range`, 10 `true`, 11 `false`, 12 `and`, 13 `or`, 14 `not`, 15 `EQEQ`, 16 `LTE`, 17 `GTE`, 18 `EQ`, 19 `LT`, 20 `GT`       , 21 `+`, 22 `-`, 23 `*`, 24 `/`, 25 `(`, 26 `)`, 27 `[`, 28 `]`, 29 `,`, 30 `:`, 31 `TAB`, 32 `SPACE`, 33 `;`, 34 `.`, 35 `COMMENT`, 38 `'`, 39 `"`, 40 `in range`, 41 `empty statement`, 44 `new line`, 45 `...` }

starting_symbol = **program_statement**

production_rules = {
- **program_statement** -> function function_call_statement, <br>
- **function_call_statement** -> 0 15 16 `identifier ( )`, <br>
- **function** -> 6 `def` 0 `identifier` 25 `(` 0 `identifier` 29 `,` 0 `identifier` 26 `)` 30`:` block <br>
- **block** -> 31 `tab` statement_list
- **lhs** -> 0 `identifier` <br>
- **rhs** -> 27 `[` rhs 28 `]` 
    - -> expression <br>
- **assignment** -> lhs 18 `=` rhs <br>
- **statement** -> assignment | keyboard_io_operation | epsilon <br>
- **statement_list** -> statement 44 `newline` statement_list | epsilon <br>
- **keyboard_io_operation** -> 7 `input` 25 `(` 1 `string` 26`)` <br>
    - -> 8 `print` 25 `(` 0 `identifier` 26 `)` <br>
    - -> 8 `print` 25 `(` 1 `constant` 26 `)` <br>
- **if_statement** -> 2 `if` condition 30 `:` block 3 `else` block <br>
- **relational_operator** -> 12 `and` 
    - -> 13 `or`
- **condition** -> 14 `not` expression relational_operator expression <br>
- **while_statement** -> 4 `while` condition 30 `:` block <br>
- **arithmetic_operator** -> 21 `+` 
    - -> 22 `-`
    - -> 23 `*` 
    - -> 24 `/`
- **expression** -> 0 `identifier` arithmetic_operator 0 `identifier` <br>
    - -> 1 `integer` arithmetic_operator 1 `integer` <br>
    - -> 0 `identifier` arithmetic_operator 1 `integer` <br>
    - -> 1 `integer` arithmetic_operator 0 `identifier` <br>
    - -> 1 `integer | boolean | string` <br>
- **for_statement** -> 5 `for` 0 `identifier` 40 `in range` 25 `(` 1 `integer` 26 `)` 30 `:` block <br>

}
