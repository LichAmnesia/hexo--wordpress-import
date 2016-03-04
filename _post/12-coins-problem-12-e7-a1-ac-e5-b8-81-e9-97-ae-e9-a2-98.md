---
title: 12 coins problem (12硬币问题)
id: 431
categories:
  - Mathmatic
  - 数学
date: 2014-02-20 20:40:37
tags:
---

<span style="font-size: 13px; line-height: 1.6em;">这个问题最初表述为：</span>

	你有一个天平秤和12个硬币，其中1个是假的。假冒重量比其他硬币少或者多。你能确定假币是哪一枚，并判断它是重还是轻？

	较难并且较为普遍的问题是：

	对于一些给定的n&gt;1，有（3^ N - 3）/2个硬币，其中1是假冒的。假冒重量比其他硬币少或者多。你能用天平秤，确定伪造硬币，并判断它是重还是轻？

* * *

## 
	**The solution for 3 coins**

	对于&nbsp;n&nbsp;= 2, 总共3个硬币,称重步骤如下:

<pre class="brush:other">
    1 against 2
    1 against 3</pre>

	对于每一次称重都有三种结果：倾向left(l)，倾向right(r)，或者balance(b)。如下表格给出了对于每种结果的答案:

<pre class="brush:other">
   l l     1 too heavy
   l b     2 too light
   l r     (not possible)
   b l     3 too light
   b b     no fake coin
   b r     3 too heavy
   r l     (not possible)
   r b     2 too heavy
   r r     1 too light</pre>

	&nbsp;

	其中 l r 以及 r l 是永远不会出现的结果。

* * *

## 
	**The solution for 12 coins**

	现在，对于n&nbsp;= 3,我们替换原先一个硬币c换成3c-2,3c-1以及3c。按照上面所说的方法:

<pre class="brush:other">
   1 2 3  against  4 5 6
   1 2 3  against  7 8 9</pre>

	这样两次之后，我们就知道哪一个集合({1,2,3}, {4,5,6} ,{7,8,9})里面有那个假冒的硬币，并且可以知道假冒的硬币是重了还是轻了。再通过一次称重操作，我们就可以确定哪一个是假冒的硬币，只要每一个集合取一个放在左边，每一个集合取一个放在右边:

<pre class="brush:other">
   1 4 7  against  2 5 8</pre>

	但是这样只能解出1到9的结果，总共有12 (= (3^3 - 3)/2)个。考虑到结果集合里不会出现 &ldquo;l r&rdquo; 以及&ldquo;r l&rdquo;(上面的两个123的称重方法)。可以利用这个条件，把10，11, 12，放进式子里:

<pre class="brush:other">
   1 2 3 10  against  4 5 6 11
   1 2 3 11  against  7 8 9 10
   1 4 7 10  against  2 5 8 12</pre>

	这样如果不是如下情况的话，假冒的就是在1-9，否则就是在10-12里面的。根据结果分析得出:

<pre class="brush:other">
   l r l       10 too heavy
   l r b       11 too light
   l r r     (not possible)
   b b l       12 too light
   b b b       no fake coin
   b b r       12 too heavy
   r l l     (not possible)
   r l b       11 too heavy
   r l r       10 too light</pre>

* * *

### 
	**Intermezzo**

	另外的一种解决的方案:

<pre class="brush:other">
   1 4 6 10  against  5 7 9 12
   2 5 4 11  against  6 8 7 10
   3 6 5 12  against  4 9 8 11</pre>

	对于这个方案，&ldquo;l l l&rdquo;与&ldquo;r r r&rdquo;并不可能。

	&nbsp;

	&nbsp;

	&nbsp;

	<u>可以考虑这个问题，有多少不同方案？可以确定假冒的硬币，并且确定是重了还是轻了</u>

	&nbsp;

	&nbsp;

	&nbsp;

* * *

## 
	**The solution for 39 (and more) coins**

	现在我们可以考虑一下如何解决_n_&nbsp;= 4的情况。同理，我们替换原先一个硬币c换成3c-2,3c-1以及3c。这样可以解决36的硬币，现在还差3个。现在我们还是按照上面的两种结果是不可能的&ldquo;l r r&rdquo;与&ldquo;r l l&rdquo;，于是我们又按照上次的方法来加入三个硬币:

<pre class="brush:other">
 ........... 37  against ........... 38
 ........... 38  against ........... 37
 ........... 38  against ........... 37
 1 4 7 .. 34 38  against 2 5 8 .. 35 39</pre>

	如此推断，对于任意的n &gt; 1，我们都能用n次称重找到那个假冒的硬币。

	&nbsp;

	&nbsp;