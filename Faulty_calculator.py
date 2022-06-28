{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red109\green109\blue109;\red32\green32\blue32;\red117\green114\blue185;
\red153\green168\blue186;\red88\green118\blue71;\red191\green100\blue38;\red86\green132\blue173;}
{\*\expandedcolortbl;;\csgenericrgb\c42745\c42745\c42745;\csgenericrgb\c12549\c12549\c12549;\csgenericrgb\c45882\c44706\c72549;
\csgenericrgb\c60000\c65882\c72941;\csgenericrgb\c34510\c46275\c27843;\csgenericrgb\c74902\c39216\c14902;\csgenericrgb\c33725\c51765\c67843;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28300\viewh17140\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs26 \cf2 \cb3 # !/usr/bin/env python3\
\cf4 print\cf5 (\cf6 "Enter first number"\cf5 )\
n1 = \cf4 int\cf5 (\cf4 input\cf5 ())\
\cf4 print\cf5 (\cf6 "Enter second number"\cf5 )\
n2 = \cf4 int\cf5 (\cf4 input\cf5 ())\
\cf4 print\cf5 (\cf6 "Choose the arithmetic operation you would like to perform\cf7 \\n\cf6  a. Add \cf7 \\n\cf6  b. Subtract \cf7 \\n\cf6  c. Multiple \cf7 \\n\cf6  d. Divide"\cf5 )\
opt = \cf4 str\cf5 (\cf4 input\cf5 ())\
\cf7 if \cf5 opt == \cf6 'a'\cf5 :\
    \cf7 if \cf5 n1 != \cf8 56 \cf7 and \cf5 n2 != \cf8 9\cf5 :\
        res = n1 + n2\
        \cf4 print\cf5 (res)\
    \cf7 else\cf5 :\
        \cf4 print\cf5 (\cf6 "Denied!! you are caught!!"\cf5 )\
\cf7 elif \cf5 opt == \cf6 'b'\cf5 :\
    res = n1 - n2\
    \cf4 print\cf5 (res)\
\cf7 elif \cf5 opt == \cf6 'c'\cf5 :\
    \cf7 if \cf5 n1 != \cf8 45 \cf7 and \cf5 n2 != \cf8 3\cf5 :\
        res = n1 * n2\
        \cf4 print\cf5 (res)\
    \cf7 else\cf5 :\
        \cf4 print\cf5 (\cf6 "Denied!! you are caught!!"\cf5 )\
\cf7 elif \cf5 opt == \cf6 'd'\cf5 :\
    \cf7 if \cf5 n1 != \cf8 56 \cf7 and \cf5 n2 != \cf8 6\cf5 :\
        res = n1 /n2\
        \cf4 print\cf5 (res)\
    \cf7 else\cf5 :\
        \cf4 print\cf5 (\cf6 "Denied!! you are caught!!"\cf5 )\
\cf7 else\cf5 :\
    \cf4 print\cf5 (\cf6 "Choose a valid option"\cf5 )\
\
\
}