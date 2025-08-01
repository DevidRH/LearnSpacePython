#ANCHOR - Nested Tuple Indexing
"""
Using nested indexing print the following items from clubs tuple.

The name of first player from Arsenal

The year that Manchester United FC founded.

Squad number of Dembele

The tuple representing the 2nd player in Real Madrid CF

Output

Lacazette
1878
7
(9, 'Benzema')

"""

clubs = (
          ("FC Barcelona", "Spain", 1899,
            [
                (3, "Pique"),
                (5, "Busquets"),
                (7, "Dembele"),
            ]
         ),
         ("Real Madrid CF", "Spain", 1902,
            [
                (7, "Hazard"),
                (9, "Benzema"),
                (10, "Modric"),
            ]
         ),
         ("Manchester United FC", "England", 1878,
            [
                (6, "Pogba"),
                (7, "Ronaldo"),
                (14, "Lingard"),
            ]
         ),
         ("Arsenal FC", "England", 1886,
            [
                (7, "Lacazette"),
                (14, "Aubameyang"),
                (16, "Holding"),
            ]
         ),
        )

arsenal_player = clubs[3][3][0]
print(arsenal_player)

manchester_year = clubs[2][2]
print(manchester_year)

squad_number = clubs[0][3][2][0]
print(squad_number)

realmadrid_player = clubs[1][3][1]
print(realmadrid_player)