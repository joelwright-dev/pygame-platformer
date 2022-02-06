import os, pygame
from support import import_level

# #RESOLUTION OF 32x32 TILES
# LEVEL_MAP = [
#     '  N                                                                     N  ',
#     '  N                        $                                            N  ',
#     'S NF          P +       S  Q F  Q      S F                              N  ',
#     'TTTH  $     KXXXXM    ITTTTTTTTTTH   ITTTTTH                            N  ',
#     'CCCCTHQ             S LCCCCCCCCCCR   LCCCCCR                            N  ',
#     'CCCCCCH         F ITTTCCCCCCCCCCCR   JBBBBBG    $                       N  ',
#     'CCCCCCCH      ITTTCCCCCCCCCCCCCCCR    D   D                         %   N  ',
#     'CCCCCCCR FS F LCCCCCCCCCCCCCCCCCCR  FQQ S QQ  F Q S QS EF F QS  F F  Q SN  ',
#     'CCCCCCCCTTTTTTCCCCCCCCCCCCCCCCCCCCTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT',
# ] # SHOULD BE 9 TILES HIGH

imported_levels = import_level('levels')

levels = []

for level_data in imported_levels:
    level_list = []
    with open(level_data, 'r') as l:
        rows = l.readlines()
        for row in rows:
            row = row.replace("\n", "")
            level_list.append(row)
    levels.append(level_list)

TILE_SIZE = 16
#SCREEN_WIDTH = len(LEVEL_MAP[0])*TILE_SIZE
#SCREEN_HEIGHT = len(LEVEL_MAP)*TILE_SIZE

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 144