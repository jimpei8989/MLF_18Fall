# MLF - HW4

##### By: Wu-Jun Pei (B06902029)

### Problem 1.

<img src="CourseraResult.png" style="zoom: 25%">

### Problem 2.

##### Gradien Descent Update Rule

$$
\mathbf w_{t + 1} \leftarrow \mathbf w_{t} + \eta(-\nabla \text{err})
$$

with $\text{err} = E_{aug}(\mathbf w) = E_{in}(\mathbf w) + \frac \lambda N \mathbf w^T \mathbf w$.
$$
\begin{align*}
\nabla E_{aug}(\mathbf w) &= \nabla E_{in}(\mathbf w) + \frac{2\lambda}{N} \mathbf w
\end{align*}
$$
Substitute it back to the update rule, we can have
$$
\begin{align*}
\mathbf w_{t + 1} 
&	\leftarrow \mathbf w_t - \eta(\nabla E_{in}(\mathbf w_t) + \frac{2\lambda}{N} \mathbf w_t)\\
&=	(1 - \frac{2\lambda \eta}{N})\mathbf w_t + \eta \nabla E_{in}(\mathbf w_t)
\end{align*}
$$

### Problem 3.

-   Consider $h_0$, we can observe that our algorithm will always choose the middle point between the two other point as $b_0$.

    -   $e_1 = (0.5 - 0)^2= 0.25 ​$
    -   $e_2 = (0 - 1)^2 = 1$
    -   $e_3 = (0.5 - 0)^2 = 0.25$

    Thus, we can get $E_{loocv}(h_0) = \frac{0.25 + 1 + 0.25}{3} = 0.5​$

-   Consider $h_1$, the line passing through the other two point will be chosen, and we can get $a_1 = \frac{y_1 - y_2}{x_1 - x_2}$ and $b_1 = \frac{x_1 y_2 - x_2 y_1}{x_1 - x_2}$.

    -   $e_0 = (\frac{-2}{\rho - 1} - 0)^2 =(\frac{2}{\rho - 1})^2$
    -   $e_1 = (1 - 0)^2 = 1​$
    -   $e_2 = (\frac{-2}{-1 - \rho} - 0)^2 = (\frac{2}{\rho + 1})^2​$.

    Thus, we can get $E_{loocv}(h_1) = \frac{(\frac{2}{\rho - 1})^2 + 1+ (\frac{2}{\rho + 1})^2}{3}$.

To make the two models tie,
$$
\begin{align*}
&&E_{loocv}(h_0) &= E_{loocv}(h_1) \\
&&0.5 &= (\frac2{\rho - 1})^2 + (\frac2{\rho + 1})^2 \\
\Rightarrow&& (\rho - 1)^2 (\rho + 1)^2 &= 8((\rho - 1)^2 + (\rho + 1)^2) \\
\Rightarrow&& \rho^4 - 2\rho^2 + 1 &= 8(2\rho^2 + 2) \\
\Rightarrow&& \rho^4 - 18\rho^2 + 81 &= 96 \\
\Rightarrow&& (\rho^2 - 9)^2 &= 96 \\
\Rightarrow&& \rho &= \sqrt{9 + 4 \sqrt 6} 


\end{align*}
$$

### Problem 4.

### Problem 5.

The deterministic noise is
$$
\mu(w) = \int_{x = 0}^{x = 2 \pi} (wx - \sin(ax))^2 dx = 
-\frac{2w \sin(2 \pi a)}{a^2} -
\frac{\cos(2 \pi a)(\sin(2 \pi a) - 8 \pi w)}{2a} +
\frac{8 \pi^3 w^2}{3} +
\pi
$$
by Wolfram Alpha. To minimize the noise, we have to find a $w$ with $\mu'(w) = 0$
$$
\mu'(w) = \frac{-2 \sin(2 \pi a)}{a^2} + \frac{4 \pi \cos(2 \pi a)}{a} + \frac{16 \pi^3 w}{3} = 0
$$
, and we can get
$$
\begin{align*}
w &= \frac{3}{16 \pi^3}(\frac{2 \sin(2 \pi a)}{a^2} - \frac{4 \pi \cos(2 \pi a)}{a}) \\
&= \frac{3\sin(2\pi a) - 6 \pi a \cos(2 \pi a)}{8 \pi^3 a^2}
\end{align*}
$$
Substitue $w$ into $\mu(w)$, and we can get
$$
\begin{align*}
\mu(w)
&= {\frac{-6\sin^2(2 \pi a) + 6 \pi a \sin(4 \pi a)}{8 \pi^3 a^4}} \\
&+ \frac{-\sin(4 \pi a)}{4a} + \frac{3\sin(4\pi a) - 12 \pi a \cos^2(2\pi a)}{4 \pi^2 a^3} \\ 
&+ \frac{3 \sin^2(2 \pi a) - 6 \pi a \sin (4 \pi a) + 12 \pi^2a^2\cos^2(2 \pi a)}{8 \pi^3a^4} \\
&+ \pi \\

\end{align*}
$$
Reference

-   Wolfram Alpha: <https://www.wolframalpha.com>