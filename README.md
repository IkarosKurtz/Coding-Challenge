# ICI-Challenge
## Proyecto de retos ICI mensuales.
![Languages](https://github.com/IkarosKurtz/ICI-Challenge/blob/Master/Imagenes/Challenge.png)

## ✨ Objetivo

La idea principal de este repositorio es el crear diferentes programas con distintas soluciones para mejorar nuestro conocimiento con distintas tecnologías y así forzarnos a probar otras nuevas.

## **📙 Reglas**
* Cada tres a cuatro días se publicará un reto y se podrá resolver en cualquier lenguaje que desee.
* Se publicará una posible solución cuando se publique el siguiente reto.
* Se recomienda que el output se igual al que se pide, pero no es obligatorio.
* El repositorio en el cual resolviste el reto debe tener una explicación de tu programa y una foto de la ejecución.
* Divertirse.

## **🔴 Lista de retos**
### Fecha de publicación: 16/06/2022

**PARKWAY WALK**

Difficulty: easy(800)

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


### Fecha de publicación: 20/06/22

**Where's the Bishop?**

Difficulty: easy(800)

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
