/* A Bison parser, made by GNU Bison 3.4.1.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2019 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

#ifndef YY_YY_SNAZZLE_TAB_H_INCLUDED
# define YY_YY_SNAZZLE_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    code0 = 258,
    code1 = 259,
    code2 = 260,
    code3 = 261,
    code4 = 262,
    code5 = 263,
    code6 = 264,
    code7 = 265,
    code8 = 266,
    code10 = 267,
    code11 = 268,
    code12 = 269,
    code13 = 270,
    code14 = 271,
    code15 = 272,
    code16 = 273,
    code17 = 274,
    code18 = 275,
    code19 = 276,
    code20 = 277,
    code21 = 278,
    code22 = 279,
    code23 = 280,
    code24 = 281,
    code25 = 282,
    code26 = 283,
    code27 = 284,
    code28 = 285,
    code29 = 286,
    code30 = 287,
    code31 = 288,
    code32 = 289,
    code33 = 290,
    code34 = 291,
    code35 = 292,
    code36 = 293,
    code37 = 294,
    code38 = 295,
    code39 = 296,
    code40 = 297,
    code41 = 298,
    code42 = 299,
    code49 = 300
  };
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 12 "snazzle.y"

  int ival;

#line 107 "snazzle.tab.h"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_SNAZZLE_TAB_H_INCLUDED  */
