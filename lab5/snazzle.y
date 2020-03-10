%{
  #include <cstdio>
  #include <iostream>
  using namespace std;

  extern int yylex();
  extern int yyparse();
  extern FILE *yyin;
 
  void yyerror(const char *s);
%}
%union {
  int ival;
}

%token <ival> code0
%token <ival> code1
%token <ival> code2
%token <ival> code3
%token <ival> code4
%token <ival> code5
%token <ival> code6
%token <ival> code7
%token <ival> code8
%token <ival> code10
%token <ival> code11
%token <ival> code12
%token <ival> code13
%token <ival> code14
%token <ival> code15
%token <ival> code16
%token <ival> code17
%token <ival> code18
%token <ival> code19
%token <ival> code20
%token <ival> code21
%token <ival> code22
%token <ival> code23
%token <ival> code24
%token <ival> code25
%token <ival> code26
%token <ival> code27
%token <ival> code28
%token <ival> code29
%token <ival> code30
%token <ival> code31
%token <ival> code32
%token <ival> code33
%token <ival> code34
%token <ival> code35
%token <ival> code36
%token <ival> code37
%token <ival> code38
%token <ival> code39
%token <ival> code40
%token <ival> code41
%token <ival> code42
%token <ival> code49
%%

program: code33 code42 code6 code7 code4 stmtlist code5 {cout<<"bison found PROGRAM\n";};
stmtlist: auxstmt  {cout<<"bison found STMTLIST\n";};
auxstmt: stmt auxstmt | stmt {cout<<"bison found AUXSTMT\n";}; 
stmt: declstmt | assignstmt | iostmt | whilestmt | forstmt | ifstmt {cout<<"bison found STMT\n";};
declstmt: vardeclstmt | arraydeclstmt {cout<<"bison found DECLSTMT\n";};
vardeclstmt: type code0 code8 {cout<<"bison found VARDECLSTMT\n";};
arraydeclstmt: type code0 code2 code1 code3 code8 {cout<<"bison found ARRAYDECLSTMT\n";};
type: code33 | code34 {cout<<"bison found TYPE\n";};
assignstmt: varassignstmt | arrayassignstmt {cout<<"bison found ASSIGNSTMT\n";};
varassignstmt: code0 code21 expresie code8 {cout<<"bison found VARASSIGNSTMT\n";};
arrayassignstmt: code0 code2 code1 code3 code21 expresie code8 {cout<<"bison found a ARRAYASSIGNSTMT\n";};
iostmt: input | output {cout<<"bison found IOSTMT\n";};
input: code39 code6 code0 code7 code8 {cout<<"bison found INPUT\n";};
output: code38 code6 expresie code7 code8 {cout<<"bison found OUTPUT\n";};
whilestmt: code35 code6 conditie code7 code4 stmtlist code5 {cout<<"bison found WHILESTMT\n";};
ifstmt: code36 code6 conditie code7 code4 stmtlist code5 | code36 code6 conditie code7 code4 stmtlist code5 code37 code4 stmtlist code5 {cout<<"bison found IFSTMT\n";};
forstmt: code41 code6 varassignstmt code8 conditie code8 varmodifystmt code7 code4 stmtlist code5 {cout<<"bison found FORSTMT\n";};
varmodifystmt: varindentstmt | vardecrementstmt {cout<<"bison found VARMODIFYSTMT\n";};
varindentstmt: code0 code31 {cout<<"bison found VARINDENTSTMT\n";};
vardecrementstmt: code0 code30 {cout<<"bison found VARDECREMENTSTMT\n";};
conditie: expresie {cout<<"bison found CONDITION\n";};
expresie: expresie operatie expresie | term {cout<<"bison found EXPRESION\n";};
operatie: code14 | code15 | code16 | code17 | code18 | code26 | code25 {cout<<"bison found OPERATION\n";};
term: code0 | code1 {cout<<"bison found TERM\n";};

%%

int main(int, char**) {
  // Open a file handle to a particular file:
  FILE *myfile = fopen("cmmd.cpp", "r");
  // Make sure it is valid:
  if (!myfile) {
    cout << "I can't open a.snazzle.file!" << endl;
    return -1;
  }
  // Set Flex to read from it instead of defaulting to STDIN:
  yyin = myfile;
  
  // Parse through the input:
  yyparse();
  
}

void yyerror(const char *s) {
  cout << "ERR, parse error!  Message: " << s << endl;
  // might as well halt now:
  exit(-1);
}
