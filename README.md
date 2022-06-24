# ICI-Challenge
## Proyecto de retos ICI mensuales.
![Languages](https://github.com/IkarosKurtz/ICI-Challenge/blob/Master/Imagenes/Challenge.png)

## ✨ Objetivo

La idea principal de este repositorio es el crear diferentes programas con distintas soluciones para mejorar nuestro conocimiento con distintas tecnologías y a su vez forzarnos a probar otras nuevas.

## **📙 Reglas**
* Cada tres a cuatro días se publicará un reto y se podrá resolver en cualquier lenguaje que desee.
* Se publicará una posible solución cuando se publique el siguiente reto.
* Se recomienda que el output se igual al que se pide, pero no es obligatorio.
* El repositorio en el cual resolviste el reto debe tener una explicación de tu programa y una foto de la ejecución.
* Divertirse.

## **🔴 Lista de retos**
### ❗ Fecha de publicación: 16/06/2022

**PARKWAY WALK**

Difficulty: easy(800) 🟢

**Problem:**

You are walking through a parkway near your house. The parkway has n+1 benches in a row numbered from 1 to n+1 from left to right. The distance between the bench i and i+1 is ai meters.

Initially, you have m units of energy. To walk 1 meter of distance, you spend 1 unit of your energy. You can't walk if you have no energy. Also, you can restore your energy by sitting on benches (and this is the only way to restore the energy). When you are sitting, you can restore any integer amount of energy you want (if you sit longer, you restore more energy). Note that the amount of your energy can exceed m

Your task is to find the minimum amount of energy you have to restore (by sitting on benches) to reach the bench n+1 from the bench 1 (and end your walk).

You have to answer t independent test cases.

**Input:**

The first line of the input contains one integer t (1 ≤ t ≤ 100) — the number of test cases. Then t test cases follow.

The first line of the test case contains two integers n and m (1 ≤ n ≤ 100; 1 ≤ m ≤ 10^4).

The second line of the test case contains n integers a1, a2, …, an (1 ≤ ai ≤ 100), where ai is the distance between benches i and i+1.

**Output:**

For each test case, print one integer — the minimum amount of energy you have to restore (by sitting on benches) to reach the bench n+1 from the bench 1 (and end your walk) in the corresponding test case.
```
Input:
3
3 1
1 2 1
4 5
3 3 5 2
5 16
1 2 3 4 5
Output:
3
8
0
```
#Note:
In the first test case of the example, you can walk to the bench 2, spending 1 unit of energy, then restore 2 units of energy on the second bench, walk to the bench 3, spending 2 units of energy, restore 1 unit of energy and go to the bench 4.

In the third test case of the example, you have enough energy to just go to the bench 6 without sitting at all.

[**ENLACE A UNA POSIBLE SOLUCION**](https://github.com/IkarosKurtz/ICI-Challenge/blob/Master/Posibles%20Soluciónes/Parkway%20Walk.py)

### ❗ Fecha de publicación: 20/06/22

**Where's the Bishop?**

Difficulty: easy(800) 🟢

Constrains:

time limit per test: 1 second
memory limit per test: 256 megabytes

**Problem:**

Mihai has an 8×8 chessboard whose rows are numbered from 1 to 8 from top to bottom and whose columns are numbered from 1 to 8 from left to right.

Mihai has placed exactly one bishop on the chessboard. The bishop is not placed on the edges of the board. (In other words, the row and column of the bishop are between 2 and 7, inclusive.)

The bishop attacks in all directions diagonally, and there is no limit to the distance which the bishop can attack. Note that the cell on which the bishop is placed is also considered attacked.

Mihai has marked all squares the bishop attacks, but forgot where the bishop was! Help Mihai find the position of the bishop. 

![Reto 2](https://github.com/IkarosKurtz/ICI-Challenge/blob/Master/Imagenes/Reto2.png)

**Input:**

The first line of the input contains a single integer t (1 ≤ t ≤ 36) — the number of test cases. The description of test cases follows. There is an empty line before each test case.

Each test case consists of 8 lines, each containing 8 characters. Each of these characters is either '#' or '.', denoting a square under attack and a square not under attack, respectively.

**Output:**

For each test case, output two integers r and c(2 ≤ r, c ≤ 7) — the row and column of the bishop.

The input is generated in such a way that there is always exactly one possible location of the bishop that is not on the edge of the board.
```
Input:
3

.....#..
#...#...
.#.#....
..#.....
.#.#....
#...#...
.....#..
......#.

#.#.....
.#......
#.#.....
...#....
....#...
.....#..
......#.
.......#

.#.....#
..#...#.
...#.#..
....#...
...#.#..
..#...#.
.#.....#
#.......
Output:
4 3
2 2
4 5
```
[**ENLACE A UNA POSIBLE SOLUCION**](https://github.com/IkarosKurtz/ICI-Challenge/blob/Master/Posibles%20Soluciónes/Where's%20the%20Bishop.cpp)

### ❗ Fecha de publicación: 23/06/22

**Kana and Dragon Quest game**

Difficulty: easy+(900) 🟢

Constrains:
time limit per test: 1 second
memory limit per test: 256 megabytes

**Problem:**

Kana was just an ordinary high school girl before a talent scout discovered her. Then, she became an idol. But different from the stereotype, she is also a gameholic.
One day Kana gets interested in a new adventure game called Dragon Quest. In this game, her quest is to beat a dragon.

The dragon has a hit point of x initially. When its hit point goes to 0 or under 0, it will be defeated. In order to defeat the dragon, Kana can cast the two following types of spells.


-Void Absorption ⚫-

Assume that the dragon's current hit point is h, after casting this spell its hit point will become [h/2]+10. Here [h/2] denotes h divided by two, rounded down.

-Lightning Strike ⚡-

This spell will decrease the dragon's hit point by 10. Assume that the dragon's current hit point is h, after casting this spell its hit point will be lowered to h−10.

Due to some reasons Kana can only cast no more than n Void Absorptions and m Lightning Strikes. She can cast the spells in any order and doesn't have to cast all the spells. Kana isn't good at math, so you are going to help her to find out whether it is possible to defeat the dragon.

**Input:**

The first line contains a single integer t (1 ≤ t ≤ 1000)  — the number of test cases.

The next t lines describe test cases. For each test case the only line contains three integers x, n, m (1 ≤ x ≤ 10^5, 0 ≤ n, m ≤ 30)  — the dragon's initial hit point, the maximum number of Void Absorptions and Lightning Strikes Kana can cast respectively.

**Output:**

If it is possible to defeat the dragon, print "YES" (without quotes). Otherwise, print "NO" (without quotes).

You can print each letter in any case (upper or lower).

Example:

#Note: One possible casting sequence of the first test case is shown below:

-Void Absorption [100/2]+10=60.

-Lightning Strike 60−10=50.

-Void Absorption [50/2]+10=35.

-Void Absorption [35/2]+10=27.

-Lightning Strike 27−10=17.

-Lightning Strike 17−10=7.

-Lightning Strike 7−10=−3.
```
Input:
7
100 3 4
189 3 4
64 2 3
63 2 3
30 27 7
10 9 1
69117 21 2

Output:
YES
NO
NO
YES
YES
YES
YES
```
