#RESOLUTION OF 32x32 TILES
LEVEL_MAP = [
    '  N                                                                     N  ',
    '  N                        $                                            N  ',
    'S NF          P +       S  Q F  Q      S F                              N  ',
    'TTTH  $     KXXXXM    ITTTTTTTTTTH   ITTTTTH                            N  ',
    'CCCCTHQ             S LCCCCCCCCCCR   LCCCCCR                            N  ',
    'CCCCCCH         F ITTTCCCCCCCCCCCR   JBBBBBG    $                       N  ',
    'CCCCCCCH      ITTTCCCCCCCCCCCCCCCR    D   D                             N  ',
    'CCCCCCCR FS F LCCCCCCCCCCCCCCCCCCR  FQQ S QQ  F Q S QS EF F QS  F F  Q SN  ',
    'CCCCCCCCTTTTTTCCCCCCCCCCCCCCCCCCCCTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT',
] # SHOULD BE 9 TILES HIGH

TILE_SIZE = 16
#SCREEN_WIDTH = len(LEVEL_MAP[0])*TILE_SIZE
#SCREEN_HEIGHT = len(LEVEL_MAP)*TILE_SIZE

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 144