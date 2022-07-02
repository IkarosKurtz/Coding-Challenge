# Coding-Challenge
## Retos mensuales
![Languages](https://github.com/IkarosKurtz/ICI-Challenge/blob/Master/Imagenes/Challenge.png)

## ✨ Objetivo

La idea principal de este repositorio es el crear diferentes programas con distintas soluciones para mejorar nuestro conocimiento con distintas tecnologías y a su vez forzarnos a probar otras nuevas.

## **📙 Reglas**
* Cada tres a cuatro días se publicará un reto y se podrá resolver en cualquier lenguaje que desee.
* Se publicará una posible solución cuando se publique el siguiente reto.
* El output tiene que ser igual al que se muestra en el ejemplo de cada problema
* El problema tiene que estar en un repositorio creado por ti y este debe tener una explicación de tu programa y una foto de la ejecución [EJEMPLO](https://github.com/IkarosKurtz/Kana-and-Dragon-Quest-game).
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
[**ENLACE A UNA POSIBLE SOLUCION**](https://github.com/IkarosKurtz/Kana-and-Dragon-Quest-game)

### ❗ Fecha de publicación: 27/06/22

**PizzaForces**

Difficulty: easy+(900)

Time limit per test: 2 seconds

memory limit per test: 256 megabytes


PizzaForces is Petya's favorite pizzeria. PizzaForces makes and sells pizzas of three sizes: small pizzas consist of 6 slices, medium ones consist of 8 slices, and large pizzas consist of 10 slices each. Baking them takes 15, 20 and 25minutes, respectively.

Petya's birthday is today, and nn of his friends will come, so he decided to make an order from his favorite pizzeria. Petya wants to order so much pizza that each of his friends gets at least one slice of pizza. The cooking time of the order is the total baking time of all the pizzas in the order.

Your task is to determine the minimum number of minutes that is needed to make pizzas containing at least nn slices in total. For example:

if 12 friends come to Petya's birthday, he has to order pizzas containing at least 12  slices in total. He can order two small pizzas, containing exactly 12.  slices, and the time to bake them is 30 minutes;

if 15 friends come to Petya's birthday, he has to order pizzas containing at least 15 slices in total. He can order a small pizza and a large pizza, containing 16 slices, and the time to bake them is 40 minutes;

if 300 friends come to Petya's birthday, he has to order pizzas containing at least  300  slices in total. He can order 15 small pizzas, 10 medium pizzas and 13 large pizzas, in total they contain 15⋅6+10⋅8+13⋅10=300 slices, and the total time to bake them is 15⋅15+10⋅20+13⋅25=750  minutes;

if only one friend comes to Petya's birthday, he can order a small pizza, and the time to bake it is 15 minutes. 

**Input**

The first line contains a single integer tt (1≤t≤1041≤t≤104) — the number of testcases.

Each testcase consists of a single line that contains a single integer nn (1≤n≤10161≤n≤1016) — the number of Petya's friends.

**Output**
For each testcase, print one integer — the minimum number of minutes that is needed to bake pizzas containing at least n slices in total.

```
input
6 
12
15
300
1
9
9999999999999993 
output
30 
40 
750 
15 
25000000000000000 
15 
```


### ❗ Fecha de publicación: 30/06/22

**The Doors**

Difficulty: easy(800)

**Constrains**

Time limit per test: 1 seconds
memory limit per test: 256 megabytes

**Problem**

Three years have passes and nothing changed. It is still raining in London, and Mr. Black has to close all the doors in his home in order to not be flooded. Once, however, Mr. Black became so nervous that he opened one door, then another, then one more and so on until he opened all the doors in his house.

There are exactly two exits from Mr. Black's house, let's name them left and right exits. There are several doors in each of the exits, so each door in Mr. Black's house is located either in the left or in the right exit. You know where each door is located. Initially all the doors are closed. Mr. Black can exit the house if and only if all doors in at least one of the exits is open. You are given a sequence in which Mr. Black opened the doors, please find the smallest index k such that Mr. Black can exit the house after opening the first k doors.

We have to note that Mr. Black opened each door at most once, and in the end all doors became open.

**Input**

The first line contains integer n (2 ≤ n ≤ 200000) — the number of doors.

The next line contains n integers: the sequence in which Mr. Black opened the doors. The i-th of these integers is equal to 0 in case the i-th opened door is located in the left exit, and it is equal to 1 in case it is in the right exit.

It is guaranteed that there is at least one door located in the left exit and there is at least one door located in the right exit.

**Output**

Print the smallest integer k such that after Mr. Black opened the first k doors, he was able to exit the house. 

Example

#Note
In the first example the first two doors are from the left exit, so when Mr. Black opened both of them only, there were two more closed door in the left exit and one closed door in the right exit. So Mr. Black wasn't able to exit at that moment.

When he opened the third door, all doors from the right exit became open, so Mr. Black was able to exit the house.

In the second example when the first two doors were opened, there was open closed door in each of the exit.

With three doors opened Mr. Black was able to use the left exit. 

```
Input
5
0 0 1 0 0
Output
3
----------------------
Input
4
1 0 0 1
Output
3
```
