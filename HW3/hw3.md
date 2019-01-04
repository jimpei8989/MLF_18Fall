# MLF - HW3

###### By: B06902029

### Problem 1.

<img src="CourseraResult.png" style="zoom: 25%">

### Problem 2.

##### PLA

$$
\mathbf w_{t + 1} \leftarrow \mathbf w_t + [\![y_n \ne \text{sign}(\mathbf w_t^T \mathbf x_n)]\!] (y_n \mathbf x_n)
$$

##### SGD

$$
\mathbf w_{t + 1} \leftarrow \mathbf w_t + \eta (-\nabla \text{err}(\mathbf w))
$$

### Problem 3.

<h3 style="page-break-before: always">Problem 4.</h3>

<img src="ExpResult/Ein_2000.png" style="zoom: 20%">

#### My findings

1. The $E_{in}$ of Fixed rate Gradient Descent is monotonic while $E_{in}$ of SGD is not.
2. Generally speaking, the $E_{in}$ of Fixed rate Gradient Descent is smaller than the $E_{in}$ of SGD.
3. I think both *(1)* and *(2)* result from the fact that Fixed rate Gradient Descent takes much more computational resource ($O(N)$ time to update $\mathbf w_{t + 1}$ with all the testdata) than SGD takes ($O(1)$ time to update $\mathbf w_{t + 1}$ with one testdata).

<h3 style="page-break-before: always">Problem 5.</h3>

<img src="ExpResult/Eout_2000.png" style="zoom: 20%">

#### My findings

1. The $E_{out}$ of both the two versions for Gradient Descent are highly correlated with the $E_{in}$ but bigger than $E_{in}$. It is not a new news because we have the same finding in PLA/pocket algorithm we've learned.

2. I also conduct an experiment by increasing $T$ from $2000$ to $10000$. And I get the following two figures.

   |                       $E_{in}$                        |                       $E_{out}$                        |
   | :---------------------------------------------------: | :----------------------------------------------------: |
   | <img src="ExpResult/Ein_10000.png" style="zoom: 10%"> | <img src="ExpResult/Eout_10000.png" style="zoom: 10%"> |

   1. Both $E_{in}$ and $E_{out}$ of Fixed rate Gradient Descent converges to around $0.20$.
   2. The $E_{in}$ and $E_{out}$ of SGD finally start to fall. And the curve seems to be periodic, I think the period interval might be the size of train data ($1000$).