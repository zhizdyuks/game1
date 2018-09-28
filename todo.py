"""
TODO

IDEA:
Rogue-lite 2D top-down space shooter game

Features:
1) Rogue-lite concept:
    -health do not regenerate between levels
    -after death all credits and uprades reset
    -at star player have to choose from __3 types__(to be detailed) of space-ships
    -each run player earns game-points which DON NOT reset
    -game-points unlocks __upgrades__(to be detailed) after death or end of the run
    
2)Multiple level space shooter

3)Player have a space-system map with a starting point and end point

4)Map has a tree-like structure making player to choose the path

5)Map paths contains:
    -10 levels in total
    -standart enemies levels
    -event levels
    -elite enemies levels
    -trade events
    -1 BOSS envet
    -random events (to be detailed)

6)Standart enemies level:
    -one or multiple enemies
    -each enemy got 1 types of attack or 1 type of skill or both
    -enemy strength scales depending on progress
    
    Standart ememies level if defeated rewards player with ability or upgraded ability + credits
    
7)Event leves:
    -standart enemies level
    -buff or heal option event:
        player has option to get healed (% of PLAYER_MAX_HP) or upgrade STAT or upgrade ABILITY_LVL
    -decision events:
        player has option to heat healed, upgrade STATs, ABILITY_LVL, PLAYER_MAX_HP,
        earn CREDITS and/or get DEBUFFED (lose HP, PLAYER_MAX_HP etc)
        
    _....(to be detailed)
    
8)Elite enemies:
    -Powerfull enemy
    -Have:
        -Strong attack and def OR
        -Strong attack and heal
        -Can spawn minions (optional)
    
    Elite enemy events if defeated rewards player with (rare ability or ability upgrade) + ship uprade + credits
    
    
9)Trade events:
    -provide choise of buying next items for credits:
        abilities
        ship upgrades
        temporary buffs
        






_____________________________________________________________
CONCEPT

IDE:
-Game is developing in Processing 3.4 and provided libs

Graphic style:
- no style yet, for developing concerns used grayscale colors and primitive forms 
  like triangles circles rectangles etc. (to be changed)

Animation:
Hud and menu items shold be animated to provide better UX




STRUCTURE:
    OOP and stuff

===>PLAYER
1)movements
2)fire
3)...


===>HUD

_______________
|===        |  | 
|           |__|
|              |
|              |
|              |
|   _ _ _ _    |
___|_|_|_|_|_____
1) 4 active skill-boxes (center alligned in the bottom of the window)
2) tactics map
3) health





_______________________
LEVEL DESIGN:
    Space plane with enemies and random obstacles (asteroids etc.)
    ...
    
