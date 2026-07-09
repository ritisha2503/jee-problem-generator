### PROBLEM

Let $z_1, z_2, z_3$ be three distinct complex numbers representing the vertices of a non-degenerate triangle $T$ in the complex plane. A complex number $z$ is said to be a **Steiner point** of triangle $T$ if it satisfies the condition:
$$ \sum_{k=1}^3 \frac{z-z_k}{|z-z_k|^2} = 0 $$

**(A)** Prove that there are at most two distinct complex numbers $z$ satisfying this condition. Let these points be $z_A$ and $z_B$.

**(B)** If $T$ is an equilateral triangle with side length $a$, and its centroid is located at the origin, determine the coordinates of $z_A$ and $z_B$.

**(C)** If $T$ is a right-angled isosceles triangle with the right angle at vertex $z_1$, and its circumcenter is located at the origin, find the distance $|z_A - z_B|$ in terms of the length $a$ of the equal sides.

---

### STEP-BY-STEP SOLUTION

**(A) Proof of at most two distinct Steiner points:**

The given condition is $\sum_{k=1}^3 \frac{z-z_k}{|z-z_k|^2} = 0$.
We know that for any complex number $w$, $w/|w|^2 = 1/\bar{w}$.
Applying this to each term, we get:
$$ \sum_{k=1}^3 \frac{1}{\overline{z-z_k}} = 0 $$
$$ \sum_{k=1}^3 \frac{1}{\bar{z}-\bar{z_k}} = 0 $$
Let $w = \bar{z}$. Then the equation becomes:
$$ \frac{1}{w-\bar{z_1}} + \frac{1}{w-\bar{z_2}} + \frac{1}{w-\bar{z_3}} = 0 $$
To solve for $w$, we combine the fractions:
$$ (w-\bar{z_2})(w-\bar{z_3}) + (w-\bar{z_1})(w-\bar{z_3}) + (w-\bar{z_1})(w-\bar{z_2}) = 0 $$
Expanding this, we get a quadratic equation in $w$:
$$ (w^2 - (\bar{z_2}+\bar{z_3})w + \bar{z_2}\bar{z_3}) + (w^2 - (\bar{z_1}+\bar{z_3})w + \bar{z_1}\bar{z_3}) + (w^2 - (\bar{z_1}+\bar{z_2})w + \bar{z_1}\bar{z_2}) = 0 $$
$$ 3w^2 - 2(\bar{z_1}+\bar{z_2}+\bar{z_3})w + (\bar{z_1}\bar{z_2}+\bar{z_2}\bar{z_3}+\bar{z_3}\bar{z_1}) = 0 $$
This is a quadratic equation of the form $Aw^2+Bw+C=0$, where $A=3$, $B=-2(\bar{z_1}+\bar{z_2}+\bar{z_3})$, and $C=(\bar{z_1}\bar{z_2}+\bar{z_2}\bar{z_3}+\bar{z_3}\bar{z_1})$.
A quadratic equation has at most two distinct solutions. Thus, there are at most two distinct values for $w$, and consequently, at most two distinct values for $z = \bar{w}$. These are $z_A$ and $z_B$.

**Algebraic Verification:**
The discriminant of the quadratic equation is $\Delta = B^2 - 4AC$.
$\Delta = 4(\bar{z_1}+\bar{z_2}+\bar{z_3})^2 - 12(\bar{z_1}\bar{z_2}+\bar{z_2}\bar{z_3}+\bar{z_3}\bar{z_1})$
This can be rewritten as:
$\Delta = 2 \left( (\bar{z_1}-\bar{z_2})^2 + (\bar{z_2}-\bar{z_3})^2 + (\bar{z_3}-\bar{z_1})^2 \right)$.
For a non-degenerate triangle, $z_1, z_2, z_3$ are distinct.
The roots $w_{A,B} = \frac{-B \pm \sqrt{\Delta}}{2A}$.
If $\Delta \ne 0$, there are two distinct solutions for $w$, hence two distinct solutions for $z$.
If $\Delta = 0$, there is exactly one solution for $w$, hence one solution for $z$. This happens when $(\bar{z_1}-\bar{z_2})^2 + (\bar{z_2}-\bar{z_3})^2 + (\bar{z_3}-\bar{z_1})^2 = 0$, which is equivalent to $(\bar{z_1}-\bar{z_2}) = \epsilon(\bar{z_2}-\bar{z_3}) = \epsilon^2(\bar{z_3}-\bar{z_1})$ where $\epsilon$ is a cube root of unity. This condition is met if and only if the triangle formed by $\bar{z_1}, \bar{z_2}, \bar{z_3}$ (and thus by $z_1, z_2, z_3$) is equilateral. So, for an equilateral triangle, $z_A$ and $z_B$ coincide.

**(B) Equilateral triangle with centroid at origin:**

If $T$ is an equilateral triangle and its centroid $G$ is at the origin, then $z_1+z_2+z_3 = 0$.
Taking the conjugate, we have $\bar{z_1}+\bar{z_2}+\bar{z_3} = 0$.
For an equilateral triangle with centroid at the origin, we also have the property $z_1z_2+z_2z_3+z_3z_1 = 0$. This can be shown by considering $z_1, z_2, z_3$ as roots of $P(z) = (z-z_1)(z-z_2)(z-z_3) = z^3 - (z_1+z_2+z_3)z^2 + (z_1z_2+z_2z_3+z_3z_1)z - z_1z_2z_3 = 0$. If $z_1+z_2+z_3=0$, then $z^3 + (z_1z_2+z_2z_3+z_3z_1)z - z_1z_2z_3 = 0$. For an equilateral triangle, $z_1, z_2, z_3$ are of the form $R, R\omega, R\omega^2$ (after rotation, if not centered at origin). For $G=0$, $z_1+z_2+z_3=0$. This implies $z_1^2+z_2^2+z_3^2=0$ and $z_1z_2+z_2z_3+z_3z_1=0$.
Taking the conjugate of $z_1z_2+z_2z_3+z_3z_1=0$, we get $\bar{z_1}\bar{z_2}+\bar{z_2}\bar{z_3}+\bar{z_3}\bar{z_1}=0$.

Substituting these into the quadratic equation for $w$:
$$ 3w^2 - 2(0)w + (0) = 0 $$
$$ 3w^2 = 0 \implies w = 0 $$
Since $w = \bar{z}$, we have $\bar{z}=0$, which implies $z=0$.
Thus, for an equilateral triangle with its centroid at the origin, there is only one Steiner point, which is the origin itself.
Therefore, $z_A = 0$ and $z_B = 0$.

**(C) Right-angled isosceles triangle, right angle at $z_1$, circumcenter at origin:**

Let the circumcenter $S$ be at the origin, so $S=0$. This implies $|z_1|=|z_2|=|z_3|=R$ for some radius $R$.
Since the triangle is right-angled at $z_1$, the side opposite to $z_1$, which is $z_2z_3$, must be the diameter of the circumcircle.
Therefore, the midpoint of $z_2z_3$ is the circumcenter.
So, $(z_2+z_3)/2 = S = 0$, which implies $z_2+z_3=0$, or $z_3 = -z_2$.
We can choose specific coordinates for the vertices satisfying these conditions. Let $R$ be the circumradius.
Let $z_1 = R$. Since $z_2, z_3$ are on the circle and $z_3=-z_2$, and the angle at $z_1$ is $90^\circ$, we can set $z_2 = iR$ and $z_3 = -iR$.
(Check: $(z_2-z_1)/(z_3-z_1) = (iR-R)/(-iR-R) = R(i-1)/(-R(i+1)) = (i-1)/-(i+1) = (i-1)^2/(-(i+1)(i-1)) = (-1-2i+1)/-(-1-1) = -2i/2 = -i$, which is purely imaginary, confirming the right angle at $z_1$.)

Now we find the coefficients for the quadratic equation $3w^2 - 2(\bar{z_1}+\bar{z_2}+\bar{z_3})w + (\bar{z_1}\bar{z_2}+\bar{z_2}\bar{z_3}+\bar{z_3}\bar{z_1}) = 0$.
The conjugates are $\bar{z_1}=R$, $\bar{z_2}=-iR$, $\bar{z_3}=iR$.
1.  Sum of conjugates:
    $\bar{z_1}+\bar{z_2}+\bar{z_3} = R + (-iR) + (iR) = R$.
2.  Sum of products of conjugates taken two at a time:
    $\bar{z_1}\bar{z_2} = R(-iR) = -iR^2$.
    $\bar{z_2}\bar{z_3} = (-iR)(iR) = -i^2R^2 = R^2$.
    $\bar{z_3}\bar{z_1} = (iR)R = iR^2$.
    $\bar{z_1}\bar{z_2}+\bar{z_2}\bar{z_3}+\bar{z_3}\bar{z_1} = -iR^2 + R^2 + iR^2 = R^2$.

Substitute these into the quadratic equation:
$$ 3w^2 - 2(R)w + R^2 = 0 $$
Solving for $w$ using the quadratic formula $w = \frac{-B \pm \sqrt{B^2-4AC}}{2A}$:
$$ w = \frac{2R \pm \sqrt{(-2R)^2 - 4(3)(R^2)}}{2(3)} $$
$$ w = \frac{2R \pm \sqrt{4R^2 - 12R^2}}{6} $$
$$ w = \frac{2R \pm \sqrt{-8R^2}}{6} $$
$$ w = \frac{2R \pm iR\sqrt{8}}{6} = \frac{2R \pm 2iR\sqrt{2}}{6} $$
$$ w = \frac{R \pm iR\sqrt{2}}{3} $$
So the two values for $w$ are $w_A = \frac{R(1+i\sqrt{2})}{3}$ and $w_B = \frac{R(1-i\sqrt{2})}{3}$.
The Steiner points $z_A$ and $z_B$ are the conjugates of $w_A$ and $w_B$:
$$ z_A = \overline{w_A} = \frac{R(1-i\sqrt{2})}{3} $$
$$ z_B = \overline{w_B} = \frac{R(1+i\sqrt{2})}{3} $$
We need to find the distance $|z_A - z_B|$:
$$ z_A - z_B = \frac{R(1-i\sqrt{2})}{3} - \frac{R(1+i\sqrt{2})}{3} = \frac{R(1-i\sqrt{2} - 1 - i\sqrt{2})}{3} = \frac{R(-2i\sqrt{2})}{3} $$
$$ |z_A - z_B| = \left| \frac{-2iR\sqrt{2}}{3} \right| = \frac{2R\sqrt{2}}{3} $$
Finally, we need to express this in terms of the side length $a$ of the equal sides.
For a right-angled isosceles triangle with vertices $z_1=R, z_2=iR, z_3=-iR$, the equal sides are $z_1z_2$ and $z_1z_3$.
The length $a = |z_1-z_2| = |R - iR| = |R(1-i)| = R\sqrt{1^2+(-1)^2} = R\sqrt{2}$.
From this, $R = a/\sqrt{2}$.
Substitute $R$ back into the distance formula:
$$ |z_A - z_B| = \frac{2(a/\sqrt{2})\sqrt{2}}{3} = \frac{2a}{3} $$

The final answer is $\boxed{\frac{2a}{3}}$.
----------------------------------------------