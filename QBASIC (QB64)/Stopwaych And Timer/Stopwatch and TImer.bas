'WORKS ONLY IN QBASIC
ENK$ = CHR$(13): UPK$ = CHR$(0) + CHR$(72)
DW$ = CHR$(0) + CHR$(80): SGH$ = CHR$(16)
CLS
A1:
COLOR 30: LOCATE 1, 30: PRINT "MADE BY SHUBHAM ANAND"
COLOR 27: LOCATE 2, 25: PRINT "TIMER AND STOPWATCH PROGRAM"
COLOR 10: LOCATE 3, 1: PRINT "  TIMER"
COLOR 4: LOCATE 4, 1: PRINT "  STOPWATCH"
COLOR 1: LOCATE 5, 1: PRINT "  EXIT"

1 DO
    LOCATE 3, 1: COLOR 15: PRINT SGH$
    C$ = INKEY$
    IF C$ = DW$ THEN LOCATE 3, 1: PRINT "  ": GOTO 2
    IF C$ = ENK$ THEN GOTO B1
LOOP
2 DO
    LOCATE 4, 1: COLOR 15: PRINT SGH$
    C$ = INKEY$
    IF C$ = DW$ THEN LOCATE 4, 1: PRINT " ": GOTO 3
    IF C$ = UPK$ THEN LOCATE 4, 1: PRINT " ": GOTO 1
    IF C$ = ENK$ THEN GOTO A
LOOP

3 IF H = 1 THEN H = 0: GOTO 1
DO
    LOCATE 5, 1: COLOR 15: PRINT SGH$
    C$ = INKEY$
    IF C$ = UPK$ THEN LOCATE 5, 1: PRINT " ": GOTO 2
    IF C$ = ENK$ THEN GOTO H
LOOP
B1: SOUND 500, 1: CLS: LOCATE 1, 30: COLOR 21: PRINT "TIMER PROGRAM"
LOCATE 3, 1: COLOR 2: PRINT "INSTRUCTIONS-";
COLOR 3: PRINT "IF YOU WANT TO ENTER MINUTES AND SECONDS ENTER IT SEPERATELY"
COLOR 14: LOCATE 4, 1: INPUT "MINUTES="; MIN
COLOR 6: LOCATE 5, 1: INPUT "SECONDS="; SEC
NT = (60 * MIN) + SEC
SOUND 500, 1: LOCATE 4, 1: PRINT SPACE$(15): LOCATE 5, 1: PRINT SPACE$(15)
COLOR 4: LOCATE 14, 1: PRINT "TOTAL TIME=";
COLOR 15: PRINT MIN; "minutes"; ":"; SEC; "seconds"
LOCATE 11, 1
COLOR 12: PRINT "TOTAL TIME COVERED="
X = MIN: Y = SEC: MIN = 0: SEC = 0
FOR CT = 1 TO NT
    SLEEP (1): SEC = SEC + 1: Y = Y - 1
    IF SEC = 60 THEN MIN = MIN + 1: SEC = 0
    IF Y = 0 THEN X = X - 1: Y = 60
    LOCATE 11, 22: COLOR 2: PRINT MIN;
    COLOR 15: PRINT "minutes";
    COLOR 14: PRINT ":";
    COLOR 3: PRINT SEC;
    COLOR 15: PRINT "seconds"
    COLOR 13: PRINT "TIME LEFT="; X; "Minutes :"; Y; "Seconds"
    IF CT = NT THEN GOTO V
    COLOR 8: PRINT "1)stop";
    COLOR 31: PRINT "_"
    asd$ = INKEY$
    IF asd$ = "1" THEN GOTO b45
NEXT CT
V:
LOCATE 12, 1: PRINT SPACE$(35)
SOUND 1000, 18.2
LOCATE 15, 12: COLOR 26, A: PRINT "COM";
COLOR 30: PRINT "PLE";
COLOR 22: PRINT "TED"
FG$ = ""
WHILE FG$ = ""
    LOCATE 16, 1: COLOR 15
    PRINT "PRESS ANY KEY TO CONTINUE";
    FG$ = INKEY$
    SOUND 6000, 5
    FG$ = INKEY$
    SOUND 30000, 2
WEND
SOUND 3000, 1: CLS: GOTO A1
b45: COLOR 15: LOCATE 12, 1: PRINT SPACE$(35)
LOCATE 16, 1: SOUND 1000, 18.2: INPUT "PRESS ENTER TO CONTINUE"; GFTFFYYFT
CLS: H = 1: GOTO A1
A: SOUND 500, 1: CLS: COLOR 30: LOCATE 1, 30: PRINT "STOPWATCH PROGRAM"
B: F2$ = ""
WHILE F2$ = ""
    COLOR 15: LOCATE 3, 5: PRINT "PRESS ANY KEY TO START STOPWATCH";
    COLOR 31: PRINT "_"
    F2$ = INKEY$
WEND
LOCATE 3, 5: PRINT SPACE$(33)
SOUND 500, 1
S = 0: M = 0: H = 0
COLOR 4: LOCATE 6, 1: PRINT "1)Pause "
COLOR 11: PRINT "2)Restart"
COLOR 3: PRINT "3)Stop"
COLOR 5: PRINT "ENTER COMMAND";
COLOR 31: PRINT "_"
DO
    COM$ = INKEY$
    IF COM$ = "1" THEN SOUND 1000, 1: GOTO E
    IF COM$ = "2" THEN SOUND 1400, 18: GOTO A
    IF COM$ = "3" THEN GOTO G
    Z:
    IF S = 60 OR M = 60 THEN GOTO Z1
    SLEEP (1): S = S + 1
    IF V = 21 THEN LOCATE 11, 1: PRINT SPACE$(33)
    Z1: IF S = 60 THEN
        M = M + 1: S = 0: SOUND 10000, 18.2
    END IF
    IF M = 60 THEN
        H = H + 1: M = 0: SOUND 10000, 18.2
    END IF
    LOCATE 5, 25: COLOR 3: PRINT H;
    COLOR 9: PRINT "hours";
    COLOR 4: PRINT " :";
    COLOR 2: PRINT M;
    COLOR 15: PRINT "minutes";
    COLOR 4: PRINT " :";
    COLOR 14: PRINT S;
    COLOR 15: PRINT "seconds"
LOOP
E:
COLOR 4: LOCATE 6, 1: PRINT "1)Resume"
DO
    S$ = INKEY$
    IF S$ = "1" THEN
        COLOR 4: LOCATE 6, 1: PRINT "1)Pause "
        SOUND 1000, 18: GOTO Z
    END IF
    IF S$ = "2" THEN SOUND 14000, 18: GOTO A
    IF S$ = "3" THEN GOTO G
LOOP
G: SOUND 500, 10: COLOR 15: LOCATE 17, 14: PRINT " "
LOCATE 12, 1: INPUT "PRESS ENTER TO CONTINUE"; XYDF
CLS: H = 1: GOTO A1
H: SOUND 500, 15: CLS: COLOR 26: LOCATE 12, 24: PRINT "THANK ";
COLOR 24: PRINT "YOU ";
COLOR 30: PRINT "FOR ";
COLOR 27: PRINT "USING ";
COLOR 21: PRINT "THE  ";
COLOR 22: PRINT "PROGRAM"
SLEEP (3): SYSTEM



