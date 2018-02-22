# Math - E - 156 - Lecture 3

- Monday 7:40 - 8:40 EST - Homework 
- Tuesday 7:30 - 8:30 EST - 



# Definitions

- **Density Function:** 
- **Exponential Random Variable:** 
- **Probability Distributions:** Sets of related random variables.
- **Parametric Distributions:**  Distributions that can be indexed using parameters

#  Probability Distributions

**Definition:** Sets of related random variables.   

- This implies are thinking about a whole family of random variables that share some common characteristics


- Instead of thinking about random variable X or Y we are thingking about **all** exponential random variables exponential random variables.
- Typically members of a probability distribution will have densities that have a standard algebriac form, but certain valies have to be specified 

**Example**

- If X is an exponential random variable, then it has a density function. 

$$
f_X(x)  =  \lambda e^-\lambda, \ \ \lambda > 0, \ x > 0
$$

- This describes a family of density functions, which are indexed by $$ \lambda $$

***Example 2***

If we pick a value $$ \lambda = 3 $$, then we have the density function.
$$
f_X(x) = 3 e^{-3x}, x > 0
$$
For each value of $$\lambda$$, we will get a different density function. 



## Binomial Distribution 

**Example**

Lets consider Tom Brady, star quarterback of the champion New England Patriots pro football team.

- Tom Completes 60% of his passes, so we can say that the probablity of Tom completing a single pass is 60%.
- What is the probability if Tom throws 5 passes, he will complete exactly 3 of them?

Solution:

1. Assume each pass is completed with a 60% probability
2. Consider one possible sequence of passes such that out of 5 attempts 3 are completed. 
   1. Use $$ C $$ to denote a completed pass, and $$ I $$ to denote an incomplete pass. 
   2. $$ [C, I, C, C, I] $$
   3. So Tom threw a complete, incomplete, complete, complete, and incomplete passes
3. What is the probability of this sequence?
   1. Since we are assuming that each pass is independent of the others we can decompose the probability of this sequence into the product of the individual passes

$$
\begin{eqnarray*}
\Pr([C, I, C, C, I]) & = & \Pr(C) * \Pr(I) * \Pr(C) * \Pr(C) * \Pr(I) \\
& = &  (0.60) X (0.40) X (0.60)  X (0.60)  X (0.40)  \\
& = & 0.01944
\end{eqnarray*}
$$

4. If we have 5 passes, and 3 of them are completions, then we will have 3 factors of Pr(C) = 0.6 and 2 factors of Pr(I) = 0.4, and since the order in which we multiply these factors doesn't influence the final result, we will always end up with the same result. 
5. How many differenct sequences of 5 passes with 3 completions do we have?
   1. There are 10 possible such sequences
6. We know that each individual sequence has a probabiulity 0.01944
   1. The probability of 3 completions out of 5 pass attempts is:
      1. $$\Pr(X = 3) = 10 X 0.01944 - 0.1944$$



### General Theory 

General Theory that will calculate the probability given three input values:

- The number of pass attempts, denote $$n$$
- The number of pass completetions, denoted $$k$$
- The probability of an individual pass completion, denoted $$p$$

Using this notation, we found that for n = 5, k = 3, and p = 0.6, the probability was 0.1944

But ultimately we wanted to be able to do this calulation for any values of n, k, and p. 

**Two Conclusions**

1. Every sequence of $n$ passes, with $k$ completions will result in the same probability.  
2. There are potentially a lot of the sequences, and it would be good if we could come up with some way to count them systematically

We need a way to systemattically count all the sequences of 5 passes with 3 completions

### Binomial Co-Efficient

Goal:  To develop a method for counting the number of ways of choosing k objects from a total of n objects. 
$$
{{N}\choose{K}}
$$
**Combinitorics**

K objects

-  There will be $k$ positions available for the first object, and for each of these choices there will be $k -1$ for the second, and for each of these sequnces there will be $k - 2$ choices for the third object, and so on. 

- Theus the total number of sequences will be:

- $$
  k * (k - 1) *  (k - 2) * ... * 3 * 2 * 1 = k!
  $$





- When we take $k$ objects and list them in a specific order, this is called a permutation
  - [[3, 1, 2]] and [[2, 3, 1]] are permutations of these set of objects {1,2,3}
  - The permutations of [[3, 1, 2]] and [[2, 3, 1] are distinct because they are listed in different orders
- $k!$ = ( Total number of permutations of k objects )



### Permutations

- Consist of re-orderings of $k$ objects, hence they must have length $k$ and every item in the list must be distinct
- We know that there are 60 possible sequences of choices that will place 3 copies of C into a sequence with 5 positions, and there are 6 permutations for each set of three indices so we have 
- Number of passing sequences = $\frac{60}{6}$ = 10
- Number of passing sequences = (number of sequences of choices)  /  (Number of permutations)

$$
\begin{eqnarray*}
{5 \choose 3} & = & \frac{5 \times 4 \times 3}{3!} \\
& = & \frac{60}{6} \\
& = & 10
\end{eqnarray*}
$$

Then we have:
$$
\begin{eqnarray*}
{n \choose k} & = & \frac{n!}{k! \ \cdot \ (n - k)! } \\
\end{eqnarray*}
$$
**Example**

Let's calculate the expected value of a binomial distribution with parameters n and p:
$$
\begin{eqnarray*}
E[X] & = & \sum_{x \in \Omega x} \ x \ \cdot \ \Pr(X = x) \\
& = & \sum^{n}_{x=0} \ x \ \cdot \ {n \choose x} p^x (1-p)^{n-x} \\
& = &  \sum^{n}_{x=0} \ x \ \cdot \ \frac{n!}{x! (n - x)!}p^x(1-p)^{n - x} \\
& = & \sum^{n}_{x=1} \ \frac{n!}{ (x - 1)! (n - x)! }p^x (1 - p)^{n - x}
\end{eqnarray*}
$$
Minute 00:44:66

Variance is:
$$
\begin{eqnarray*}
\hbox{Var[X]} & = & E[X^2] - (E[X])^2 \\
& = & (n^2p^2 + np - np^2) - (np) \\
& = & np - np^2 \\
& = & np(1 - p)
\end{eqnarray*}
$$
**Example**
$$
\begin{eqnarray*}
\Pr(X = k) & = & {n \choose k}p^k(1-p)^{n-k} \\
E[X] & = & np \\
Var[X] & = & np(1 - p) \\
\end{eqnarray*}
$$


# Transformations of a Random Variable

**Example**

Suppose X is an exponential random variable with parameter $\lambda = 1$, so that the density function for X is:
$$
f_X(x) = e^{-x}, \ x > 0
$$
Now suppose that $g(x) = x^2$, so that $Y = X^2$. What is the density function $ f_Y(y) $?



**Example**
$$
\begin{eqnarray*}
F_Y(9) & = & Pr(Y \leq 9) \\
& = & Pr(X^2 \leq 9) \\
& = & Pr(X \leq 3) \\
& = & F_Y(3)
\end{eqnarray*}
$$



# General Normal Random Variable

**Example**

$\sigma$ - Standard Deviation

$\mu$ - mean



Let Z denote a standard normal random variable, let $\mu$ and $\sigma$  be constants, with $\mu$ > 0, and define a new, transformed random variable $X$ by:
$$
\begin{eqnarray*}
X & = & \sigma \ \cdot \ Z + \mu
\end{eqnarray*}
$$
We can think f this as the function $$ g(Z) = \sigma Z + \mu $$; notice that g(z) is strictly increasing function, because  $$ \sigma > 0 $$ 



I start with creating a structure for my writing.  I immediatly start writing an outline of topics I need to cover.   I then start to write questions for each section on things I want to answer about each topic.   I then look for evidence of each question.   Then I start to answer those questions to those topics, and then perhaps fill in some of the answers with evidence/quotes to support what ever I am writing about.



I then let the thoughts sit for at least 1/2 a day and then I come back to the project. 

Then revise, write, come up with a main idea, then revise.

I wish I could do better at word usage, and cohesiveness in my writing.





# Python For Sport Scientists: Descriptive Statistics

## *Learn how to start analyzing athlete-related datasets by using easy-to-reason-about Python code*

- https://towardsdatascience.com/python-for-sport-scientists-descriptive-statistics-96ed7e66ab3c
- https://towardsdatascience.com/data-visualization-exploration-using-pandas-only-beginner-a0a52eb723d5
- https://towardsdatascience.com/data-visualization-hackathon-style-c6dcaabbf626
- https://www.youtube.com/watch?v=hVimVzgtD6w


