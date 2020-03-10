%{

#include <stdio.h>
#include "snazzle.tab.h"
using namespace std;
%}

%%
[\t]
[\n]
[\r]
[ ]
\[ {return code2;}
\] {return code3;}
\{ {return code4;}
\} {return code5;}
\( {return code6;}
\) {return code7;}
; {return code8;}
, {return code10;}
\<{2} {return code11;}
\>{2} {return code12;}
# {return code13;}
\+ {return code14;}
\- {return code15;}
\* {return code16;}
\/ {return code17;}
% {return code18;}
\< {return code19;}
\<\= {return code20;}
\= {return code21;}
\>\= {return code22;}
\> {return code23;}
\=\= {return code24;}
\&{2} {return code25;}
\|{2} {return code26;}
! {return code27;}
!\= {return code28;}
\+{2} {return code31;}
\-{2} {return code30;}
void {return code32;}
int {return code33;}
char {return code34;}
while {return code35;}
if {return code36;}
else {return code37;}
printf {return code38;}
scanf {return code39;}
return {return code40;}
for {return code41;}
main {return code42;}
_*|[A-Z]+|[a-z]+[0-9]* {return code0;}
[0-9] {return code1;}
. {return code49;}
%%

int yywrap()
{
return 1;
}


