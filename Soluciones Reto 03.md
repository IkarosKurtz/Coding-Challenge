# SOLUCIONES DEL RETO 3
## Kana and Dragon Quest game

**❗ Publicado el 23/06/22**

**Problem**
Kana was just an ordinary high school girl before a talent scout discovered her. Then, she became an idol. But different from the stereotype, she is also a gameholic.
One day Kana gets interested in a new adventure game called Dragon Quest. In this game, her quest is to beat a dragon.

The dragon has a hit point of x initially. When its hit point goes to 0 or under 0, it will be defeated. In order to defeat the dragon, Kana can cast the two following types of spells.


-Void Absorption-

Assume that the dragon's current hit point is h, after casting this spell its hit point will become [h/2]+10. Here [h/2] denotes h divided by two, rounded down.

-Lightning Strike-

This spell will decrease the dragon's hit point by 10. Assume that the dragon's current hit point is h, after casting this spell its hit point will be lowered to h−10.

Due to some reasons Kana can only cast no more than n Void Absorptions and m Lightning Strikes. She can cast the spells in any order and doesn't have to cast all the spells. Kana isn't good at math, so you are going to help her to find out whether it is possible to defeat the dragon.

**Input:**

The first line contains a single integer t (1 ≤ t ≤ 1000)  — the number of test cases.

The next t lines describe test cases. For each test case the only line contains three integers x, n, m (1 ≤ x ≤ 10^5, 0 ≤ n, m ≤ 30)  — the dragon's initial hit point, the maximum number of Void Absorptions and Lightning Strikes Kana can cast respectively.

**Output:**

If it is possible to defeat the dragon, print "YES" (without quotes). Otherwise, print "NO" (without quotes).

You can print each letter in any case (upper or lower).

## Soluciones

Los enlaces son de diferentes repositorios de participantes de este reto.

Python:

* [https://github.com/IkarosKurtz/Kana-and-Dragon-Quest-game](https://github.com/IkarosKurtz/Kana-and-Dragon-Quest-game) por IkarosKurtz