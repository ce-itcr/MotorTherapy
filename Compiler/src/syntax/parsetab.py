
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'statementsASIGNWORD BALLOON BEGIN COMMA DEC DIVIDE DO DOW END ENDDO EQUAL FOR FORASIGNWORD FOREND GAME ID INC INT LBRACE LPAREN LSPAREN MAIN MINUS MULTI NUMBER OBJECT PLUS RANDOM RBRACE RPAREN RSPAREN SEMCOL SPIDERWEB STRING TEXT TIMES USING\n    statements : var_assign statements\n               | var_define statements\n               | For statements\n               | Dow statements\n               | Random statements\n               | empty\n    \n    Random : RANDOM LPAREN ID COMMA atomic_variable COMMA atomic_variable RPAREN SEMCOL\n    \n    atomic_variable : NUMBER\n                    | ID\n    \n    var_assign : TYPE ID LSPAREN NUMBER RSPAREN SEMCOL\n               | TYPE ID SEMCOL\n    \n    var_define : ID EQUAL ATOMIC SEMCOL\n               | ID LSPAREN NUMBER RSPAREN EQUAL ATOMIC SEMCOL\n               | TYPE ID EQUAL ATOMIC SEMCOL\n    \n    ForRandom : RANDOM LPAREN ID COMMA atomic_variable RPAREN SEMCOL\n              | RANDOM LPAREN NUMBER COMMA atomic_variable RPAREN SEMCOL\n              | RANDOM LPAREN ID COMMA atomic_variable COMMA atomic_variable RPAREN SEMCOL\n    \n    BalloonFor : BALLOON LPAREN ID COMMA ID RPAREN SEMCOL\n               | BALLOON LPAREN ID COMMA NUMBER RPAREN SEMCOL\n               | BALLOON LPAREN NUMBER COMMA ID RPAREN SEMCOL\n               | BALLOON LPAREN NUMBER COMMA NUMBER RPAREN SEMCOL\n    \n    IncFor : INC LPAREN ID COMMA atomic_variable RPAREN SEMCOL\n    \n    DecFor : DEC LPAREN ID COMMA atomic_variable RPAREN SEMCOL\n    \n    Body : IncFor Body\n         | DecFor Body\n         | BalloonFor Body\n         | ForRandom Body\n         | empty\n    \n    For : FOR NUMBER TIMES USING ID Body FOREND SEMCOL\n    \n    Dow : DOW LPAREN ID RPAREN Body ENDDO SEMCOL\n        | DOW LPAREN NUMBER RPAREN Body ENDDO SEMCOL\n    \n    empty :\n    \n    TYPE : INT\n         | STRING LPAREN NUMBER RPAREN\n    \n    ATOMIC : NUMBER\n           | TEXT\n    '
    
_lr_action_items = {'ID':([0,2,3,4,5,6,8,13,24,25,28,41,43,46,47,49,66,74,75,76,77,79,80,82,89,91,92,93,94,95,96,97,107,114,],[9,9,9,9,9,9,20,-33,35,37,-11,-12,51,63,-34,-14,-10,83,84,85,87,63,-13,-30,-31,-29,63,63,101,104,63,63,-7,63,]),'FOR':([0,2,3,4,5,6,28,41,49,66,80,82,89,91,107,],[10,10,10,10,10,10,-11,-12,-14,-10,-13,-30,-31,-29,-7,]),'DOW':([0,2,3,4,5,6,28,41,49,66,80,82,89,91,107,],[11,11,11,11,11,11,-11,-12,-14,-10,-13,-30,-31,-29,-7,]),'RANDOM':([0,2,3,4,5,6,28,41,44,45,49,51,53,54,55,56,66,80,82,89,91,107,117,118,119,120,121,122,124,125,127,],[12,12,12,12,12,12,-11,-12,61,61,-14,61,61,61,61,61,-10,-13,-30,-31,-29,-7,-22,-23,-18,-19,-21,-20,-15,-16,-17,]),'$end':([0,1,2,3,4,5,6,7,15,16,17,18,19,28,41,49,66,80,82,89,91,107,],[-32,0,-32,-32,-32,-32,-32,-6,-1,-2,-3,-4,-5,-11,-12,-14,-10,-13,-30,-31,-29,-7,]),'INT':([0,2,3,4,5,6,28,41,49,66,80,82,89,91,107,],[13,13,13,13,13,13,-11,-12,-14,-10,-13,-30,-31,-29,-7,]),'STRING':([0,2,3,4,5,6,28,41,49,66,80,82,89,91,107,],[14,14,14,14,14,14,-11,-12,-14,-10,-13,-30,-31,-29,-7,]),'EQUAL':([9,20,42,],[21,29,50,]),'LSPAREN':([9,20,],[22,27,]),'NUMBER':([10,21,22,24,26,27,29,46,50,76,77,79,92,93,94,95,96,97,114,],[23,31,33,36,38,39,31,65,31,86,88,65,65,65,102,103,65,65,65,]),'LPAREN':([11,12,14,58,59,60,61,],[24,25,26,74,75,76,77,]),'SEMCOL':([20,30,31,32,40,48,67,69,78,81,98,108,109,110,111,112,113,115,116,126,],[28,41,-35,-36,49,66,80,82,89,91,107,117,118,119,120,121,122,124,125,127,]),'TEXT':([21,29,50,],[32,32,32,]),'TIMES':([23,],[34,]),'RSPAREN':([33,39,],[42,48,]),'USING':([34,],[43,]),'RPAREN':([35,36,38,63,65,90,99,100,101,102,103,104,105,106,123,],[44,45,47,-9,-8,98,108,109,110,111,112,113,115,116,126,]),'COMMA':([37,63,64,65,83,84,85,86,87,88,105,],[46,-9,79,-8,92,93,94,95,96,97,114,]),'INC':([44,45,51,53,54,55,56,117,118,119,120,121,122,124,125,127,],[58,58,58,58,58,58,58,-22,-23,-18,-19,-21,-20,-15,-16,-17,]),'DEC':([44,45,51,53,54,55,56,117,118,119,120,121,122,124,125,127,],[59,59,59,59,59,59,59,-22,-23,-18,-19,-21,-20,-15,-16,-17,]),'BALLOON':([44,45,51,53,54,55,56,117,118,119,120,121,122,124,125,127,],[60,60,60,60,60,60,60,-22,-23,-18,-19,-21,-20,-15,-16,-17,]),'ENDDO':([44,45,52,53,54,55,56,57,62,70,71,72,73,117,118,119,120,121,122,124,125,127,],[-32,-32,69,-32,-32,-32,-32,-28,78,-24,-25,-26,-27,-22,-23,-18,-19,-21,-20,-15,-16,-17,]),'FOREND':([51,53,54,55,56,57,68,70,71,72,73,117,118,119,120,121,122,124,125,127,],[-32,-32,-32,-32,-32,-28,81,-24,-25,-26,-27,-22,-23,-18,-19,-21,-20,-15,-16,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,2,3,4,5,6,],[1,15,16,17,18,19,]),'var_assign':([0,2,3,4,5,6,],[2,2,2,2,2,2,]),'var_define':([0,2,3,4,5,6,],[3,3,3,3,3,3,]),'For':([0,2,3,4,5,6,],[4,4,4,4,4,4,]),'Dow':([0,2,3,4,5,6,],[5,5,5,5,5,5,]),'Random':([0,2,3,4,5,6,],[6,6,6,6,6,6,]),'empty':([0,2,3,4,5,6,44,45,51,53,54,55,56,],[7,7,7,7,7,7,57,57,57,57,57,57,57,]),'TYPE':([0,2,3,4,5,6,],[8,8,8,8,8,8,]),'ATOMIC':([21,29,50,],[30,40,67,]),'Body':([44,45,51,53,54,55,56,],[52,62,68,70,71,72,73,]),'IncFor':([44,45,51,53,54,55,56,],[53,53,53,53,53,53,53,]),'DecFor':([44,45,51,53,54,55,56,],[54,54,54,54,54,54,54,]),'BalloonFor':([44,45,51,53,54,55,56,],[55,55,55,55,55,55,55,]),'ForRandom':([44,45,51,53,54,55,56,],[56,56,56,56,56,56,56,]),'atomic_variable':([46,79,92,93,96,97,114,],[64,90,99,100,105,106,123,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> var_assign statements','statements',2,'p_statements_test','Statements.py',5),
  ('statements -> var_define statements','statements',2,'p_statements_test','Statements.py',6),
  ('statements -> For statements','statements',2,'p_statements_test','Statements.py',7),
  ('statements -> Dow statements','statements',2,'p_statements_test','Statements.py',8),
  ('statements -> Random statements','statements',2,'p_statements_test','Statements.py',9),
  ('statements -> empty','statements',1,'p_statements_test','Statements.py',10),
  ('Random -> RANDOM LPAREN ID COMMA atomic_variable COMMA atomic_variable RPAREN SEMCOL','Random',9,'p_Random','Syntax.py',18),
  ('atomic_variable -> NUMBER','atomic_variable',1,'p_num_variable','Syntax.py',34),
  ('atomic_variable -> ID','atomic_variable',1,'p_num_variable','Syntax.py',35),
  ('var_assign -> TYPE ID LSPAREN NUMBER RSPAREN SEMCOL','var_assign',6,'p_var_assign','Syntax.py',42),
  ('var_assign -> TYPE ID SEMCOL','var_assign',3,'p_var_assign','Syntax.py',43),
  ('var_define -> ID EQUAL ATOMIC SEMCOL','var_define',4,'p_var_define','Syntax.py',63),
  ('var_define -> ID LSPAREN NUMBER RSPAREN EQUAL ATOMIC SEMCOL','var_define',7,'p_var_define','Syntax.py',64),
  ('var_define -> TYPE ID EQUAL ATOMIC SEMCOL','var_define',5,'p_var_define','Syntax.py',65),
  ('ForRandom -> RANDOM LPAREN ID COMMA atomic_variable RPAREN SEMCOL','ForRandom',7,'p_ForRandom','Syntax.py',127),
  ('ForRandom -> RANDOM LPAREN NUMBER COMMA atomic_variable RPAREN SEMCOL','ForRandom',7,'p_ForRandom','Syntax.py',128),
  ('ForRandom -> RANDOM LPAREN ID COMMA atomic_variable COMMA atomic_variable RPAREN SEMCOL','ForRandom',9,'p_ForRandom','Syntax.py',129),
  ('BalloonFor -> BALLOON LPAREN ID COMMA ID RPAREN SEMCOL','BalloonFor',7,'p_BalloonFor','Syntax.py',154),
  ('BalloonFor -> BALLOON LPAREN ID COMMA NUMBER RPAREN SEMCOL','BalloonFor',7,'p_BalloonFor','Syntax.py',155),
  ('BalloonFor -> BALLOON LPAREN NUMBER COMMA ID RPAREN SEMCOL','BalloonFor',7,'p_BalloonFor','Syntax.py',156),
  ('BalloonFor -> BALLOON LPAREN NUMBER COMMA NUMBER RPAREN SEMCOL','BalloonFor',7,'p_BalloonFor','Syntax.py',157),
  ('IncFor -> INC LPAREN ID COMMA atomic_variable RPAREN SEMCOL','IncFor',7,'p_IncFor','Syntax.py',175),
  ('DecFor -> DEC LPAREN ID COMMA atomic_variable RPAREN SEMCOL','DecFor',7,'p_DecFor','Syntax.py',197),
  ('Body -> IncFor Body','Body',2,'p_Body','Syntax.py',216),
  ('Body -> DecFor Body','Body',2,'p_Body','Syntax.py',217),
  ('Body -> BalloonFor Body','Body',2,'p_Body','Syntax.py',218),
  ('Body -> ForRandom Body','Body',2,'p_Body','Syntax.py',219),
  ('Body -> empty','Body',1,'p_Body','Syntax.py',220),
  ('For -> FOR NUMBER TIMES USING ID Body FOREND SEMCOL','For',8,'p_For','Syntax.py',226),
  ('Dow -> DOW LPAREN ID RPAREN Body ENDDO SEMCOL','Dow',7,'p_Dow','Syntax.py',245),
  ('Dow -> DOW LPAREN NUMBER RPAREN Body ENDDO SEMCOL','Dow',7,'p_Dow','Syntax.py',246),
  ('empty -> <empty>','empty',0,'p_empty','Syntax.py',260),
  ('TYPE -> INT','TYPE',1,'p_type','Syntax.py',266),
  ('TYPE -> STRING LPAREN NUMBER RPAREN','TYPE',4,'p_type','Syntax.py',267),
  ('ATOMIC -> NUMBER','ATOMIC',1,'p_atomic','Syntax.py',276),
  ('ATOMIC -> TEXT','ATOMIC',1,'p_atomic','Syntax.py',277),
]
