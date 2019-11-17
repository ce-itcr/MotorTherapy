
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ASIGNWORD BALLOON BEGIN COMMA DEC DIVIDE DO DOW END ENDDO EQUAL FOR FORASIGNWORD FOREND GAME ID INC INT LBRACE LPAREN LSPAREN MAIN MINUS MULTI NUMBER OBJECT PLUS RANDOM RBRACE RPAREN RSPAREN SEMCOL SPIDERWEB STRING TEXT TIMES USING\n    For : FOR NUMBER TIMES USING NUMBER\n    \n    Dow : DOW '(' ID ')'\n        | DOW '(' NUMBER ')'\n    var : var_assign : ID EQUAL NUMBER\n                  | ID EQUAL TEXT\n                  | 'i' 'n' 't' ID EQUAL NUMBER\n                  | 's' 't' 'r' 'i' 'n' 'g' '(' NUMBER ')' ID '[' NUMBER ']'\n                  | 'i' 'n' 't' ID '[' NUMBER ']'\n    \n    empty :\n    "
    
_lr_action_items = {'FOR':([0,],[2,]),'$end':([1,6,],[0,-1,]),'NUMBER':([2,5,],[3,6,]),'TIMES':([3,],[4,]),'USING':([4,],[5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'For':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> For","S'",1,None,None,None),
  ('For -> FOR NUMBER TIMES USING NUMBER','For',5,'p_For','Lexical.py',40),
  ('Dow -> DOW ( ID )','Dow',4,'p_Dow','Lexical.py',49),
  ('Dow -> DOW ( NUMBER )','Dow',4,'p_Dow','Lexical.py',50),
  ('var -> <empty>','var',0,'p_var','Lexical.py',60),
  ('var_assign -> ID EQUAL NUMBER','var_assign',3,'p_var_assign','Lexical.py',63),
  ('var_assign -> ID EQUAL TEXT','var_assign',3,'p_var_assign','Lexical.py',64),
  ('var_assign -> i n t ID EQUAL NUMBER','var_assign',6,'p_var_assign','Lexical.py',65),
  ('var_assign -> s t r i n g ( NUMBER ) ID [ NUMBER ]','var_assign',13,'p_var_assign','Lexical.py',66),
  ('var_assign -> i n t ID [ NUMBER ]','var_assign',7,'p_var_assign','Lexical.py',67),
  ('empty -> <empty>','empty',0,'p_empty','Lexical.py',78),
]