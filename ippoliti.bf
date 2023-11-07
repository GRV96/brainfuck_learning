#!/usr/bin/beef

Challenge by Giuliano Ippoliti
https://www(dot)linkedin(dot)com/pulse/brainfck(hyphen)password(hyphen)challenge(hyphen)giuliano(hyphen)ippoliti

To solve the challenge you have to find the only 8 character input
string which causes the program to print «!» instead of «!!»

c: character input
m: minus
p: plus

++++++++[
	>++++++++++[
		>++++++++++<-] (8; 0; 100) position 1

	>>,<[
	(0; 0; 0; pc) p1
	(8; 0; 100; c) position 2

		->-<]
		(0; 0; m100; m100)
		(8; 0; 0; c minus 100) position 2

	><<+>>[
	(0; p1; 0; 0) p1
	(8; 1; 0; c minus 100) position 3

		>+<<]
		(0; 0; 0; 0; p1) m1
		(8; 1; 0; c minus 100; 1) position 2

	<[
	(0; 0; 0; 0; 0) m1
	(8; 1; 0; c minus 100; 1) position 1

		>]
		(0; 0; 0; 0; 0) p1
		(8; 1; 0; c minus 100; 1) position 2

	>[
	(0; 0; 0; 0; 0) p1
	(8; 1; 0; c minus 100; 1) position 3

		-]
		(0; 0; 0; m(c m100); 0)
		(8; 1; 0; 0; 1) position 3

	<<[
	(0; 0; 0; 0; 0) m2
	(8; 1; 0; 0; 1) position 1

		-]
		(0; m1; 0; 0; 0)
		(8; 0; 0; 0; 1) position 1

	+<-]
	(m1; p1; 0; 0; 0) m1
	(7; 1; 0; 0; 1) position 0

The following code prints "!!"

(0; 0; 0; 0; 0) position 0
>>+>>[
(0; 0; p1; 0; 0) p4
(0; 0; 1; 0; 0) position 4

	The first exclamation mark is printed only if position 4 is non-zero
	>+++++++++++++++++++++++++++++++++.<<]
	(0; 0; 0; 0; 0; p33) m1
	(0; 0; 1; 0; 33) position 3

<[
(0; 0; 0; 0; 0; 0) m1
(0; 0; 1; 0; 33) position 2

	>]
	(0; 0; 0; 0; 0; 0) p1
	(0; 0; 0; 0; 0) position 0

+++++++++++++++++++++++++++++++++.
(0; 0; 0; 0; 0; 0)
(0; 0; 0; 0; 0) position 0
