### PROBLEM

Let $z_1, z_2, z_3$ be distinct complex numbers representing the vertices of an equilateral triangle in the complex plane. Let $G$ be the centroid of this triangle.

A complex number $z$ satisfies the condition that the squared distances from $z$ to $z_1, z_2, z_3$ are in arithmetic progression in the specified order: $|z-z_1|^2$, $|z-z_2|^2$, $|z-z_3|^2$.

**(a)** Prove that the locus of $z$ is a straight line passing through the centroid $G$ of the triangle $z_1z_2z_3$. Describe this line geometrically relative to the triangle $z_1z_2z_3$.

**(b)** If, in addition to the arithmetic progression condition, $z$ also lies on the circumcircle of the triangle $z_1z_2z_3$, find the complex numbers representing these possible values of $z$ in terms of $z_1, z_2, z_3$.

### STEP-BY-STEP SOLUTION

**Part (a): Locus of $z$**

The condition that $|z-z_1|^2, |z-z_2|^2, |z-z_3|^2$ are in arithmetic progression means:
$2|z-z_2|^2 = |z-z_1|^2 + |z-z_3|^2$

Let $G$ be the centroid of the equilateral triangle $z_1z_2z_3$. We know $G = \frac{z_1+z_2+z_3}{3}$.
To simplify calculations, we can translate the entire system so that the centroid $G$ is at the origin. Let $z' = z-G$, $z_1' = z_1-G$, $z_2' = z_2-G$, $z_3' = z_3-G$.
Then $z_1'+z_2'+z_3' = (z_1-G)+(z_2-G)+(z_3-G) = (z_1+z_2+z_3) - 3G = 3G - 3G = 0$.
The condition becomes:
$2|z'-(z_2-G)|^2 = |z'-(z_1-G)|^2 + |z'-(z_3-G)|^2$
$2|z'-z_2'|^2 = |z'-z_1'|^2 + |z'-z_3'|^2$

Expand the squared moduli using $|w|^2 = w\bar{w}$:
$2(z'-z_2')(\bar{z}'-\bar{z_2'}) = (z'-z_1')(\bar{z}'-\bar{z_1'}) + (z'-z_3')(\bar{z}'-\bar{z_3'})$
$2(z'\bar{z}' - z'\bar{z_2'} - \bar{z}'z_2' + z_2'\bar{z_2'}) = (z'\bar{z}' - z'\bar{z_1'} - \bar{z}'z_1' + z_1'\bar{z_1'}) + (z'\bar{z}' - z'\bar{z_3'} - \bar{z}'z_3' + z_3'\bar{z_3'})$
$2|z'|^2 - 2z'\bar{z_2'} - 2\bar{z}'z_2' + 2|z_2'|^2 = 2|z'|^2 - z'(\bar{z_1'}+\bar{z_3'}) - \bar{z}'(z_1'+z_3') + |z_1'|^2 + |z_3'|^2$

Since $z_1', z_2', z_3'$ are the vertices of an equilateral triangle centered at the origin, their moduli are equal to the circumradius $R$: $|z_1'|=|z_2'|=|z_3'|=R$. Thus, $|z_1'|^2=|z_2'|^2=|z_3'|^2=R^2$.
Also, since $z_1'+z_2'+z_3'=0$, we have $z_1'+z_3' = -z_2'$ and $\bar{z_1'}+\bar{z_3'} = -\bar{z_2'}$.

Substitute these into the equation:
$2|z'|^2 - 2z'\bar{z_2'} - 2\bar{z}'z_2' + 2R^2 = 2|z'|^2 - z'(-\bar{z_2'}) - \bar{z}'(-z_2') + R^2 + R^2$
$2|z'|^2 - 2z'\bar{z_2'} - 2\bar{z}'z_2' + 2R^2 = 2|z'|^2 + z'\bar{z_2'} + \bar{z}'z_2' + 2R^2$
$-2z'\bar{z_2'} - 2\bar{z}'z_2' = z'\bar{z_2'} + \bar{z}'z_2'$
$3z'\bar{z_2'} + 3\bar{z}'z_2' = 0$
$z'\bar{z_2'} + \bar{z}'z_2' = 0$

This equation implies that $2\text{Re}(z'\bar{z_2'}) = 0$, so $z'\bar{z_2'}$ is purely imaginary.
Let $z' = x+iy$ and $z_2' = x_2'+iy_2'$. Then $\bar{z_2'} = x_2'-iy_2'$.
$z'\bar{z_2'} = (x+iy)(x_2'-iy_2') = (xx_2'+yy_2') + i(yx_2'-xy_2')$.
For this to be purely imaginary, the real part must be zero: $xx_2'+yy_2' = 0$.
This is the dot product of the position vectors of $z'$ and $z_2'$ being zero. Geometrically, this means the vector from the origin to $z'$ is perpendicular to the vector from the origin to $z_2'$.

Therefore, the locus of $z'$ is a straight line passing through the origin (which is the centroid $G$).
Translating back, the locus of $z$ is a straight line passing through the centroid $G$ and perpendicular to the line segment $Gz_2$.

**Geometric Description of the Line:**
In an equilateral triangle, the line segment from a vertex to the centroid (e.g., $Gz_2$) lies on the altitude from that vertex to the opposite side. This altitude is perpendicular to the opposite side.
So, the line containing $Gz_2$ is perpendicular to the side $z_1z_3$.
The locus of $z$ is a line passing through $G$ and perpendicular to $Gz_2$.
Therefore, the locus of $z$ is a straight line passing through the centroid $G$ and **parallel to the side $z_1z_3$**.

**Part (b): Intersection with the Circumcircle**

The circumcircle of the triangle $z_1z_2z_3$ has its center at the centroid $G$ and its radius is $R = |z_1-G| = |z_2-G| = |z_3-G|$.
In the translated coordinate system where $G$ is the origin, the circumcircle is $|z'|=R$.
From part (a), the locus of $z'$ is the line $z'\bar{z_2'} + \bar{z}'z_2' = 0$.
We need to find the points $z'$ that satisfy both conditions:
1. $|z'|=R$
2. $z'\bar{z_2'} + \bar{z}'z_2' = 0$

From condition (2), $z'\bar{z_2'}$ is purely imaginary. Let $z'\bar{z_2'} = ik$ for some real $k$.
Then $z' = \frac{ik}{\bar{z_2'}} = \frac{ik z_2'}{|z_2'|^2} = \frac{ik z_2'}{R^2}$.
Now substitute this into condition (1):
$|z'| = \left|\frac{ik z_2'}{R^2}\right| = \frac{|i||k||z_2'|}{R^2} = \frac{1 \cdot |k| \cdot R}{R^2} = \frac{|k|}{R}$.
Since $|z'|=R$, we have $\frac{|k|}{R}=R$, which implies $|k|=R^2$. So $k = \pm R^2$.

Substituting $k = R^2$ into the expression for $z'$:
$z' = \frac{i R^2 z_2'}{R^2} = i z_2'$
Substituting $k = -R^2$ into the expression for $z'$:
$z' = \frac{-i R^2 z_2'}{R^2} = -i z_2'$

So, in the translated system, the two possible values for $z'$ are $i z_2'$ and $-i z_2'$.
These represent rotations of $z_2'$ by $\pm \frac{\pi}{2}$ about the origin $G$.

Now, translate back to the original coordinate system.
$z' = z-G$ and $z_2' = z_2-G$.
The possible values of $z$ are:
$z-G = i(z_2-G) \implies z = G + i(z_2-G)$
$z-G = -i(z_2-G) \implies z = G - i(z_2-G)$

In terms of $z_1, z_2, z_3$:
$G = \frac{z_1+z_2+z_3}{3}$.
The two possible values for $z$ are:
$z = \frac{z_1+z_2+z_3}{3} + i\left(z_2 - \frac{z_1+z_2+z_3}{3}\right)$
$z = \frac{z_1+z_2+z_3}{3} - i\left(z_2 - \frac{z_1+z_2+z_3}{3}\right)$

Simplifying the term in the parenthesis:
$z_2 - \frac{z_1+z_2+z_3}{3} = \frac{3z_2 - (z_1+z_2+z_3)}{3} = \frac{-z_1+2z_2-z_3}{3}$.

So the two possible values of $z$ are:
$z = \frac{z_1+z_2+z_3}{3} + i\frac{-z_1+2z_2-z_3}{3}$
$z = \frac{z_1+z_2+z_3}{3} - i\frac{-z_1+2z_2-z_3}{3}$

These are the two points on the circumcircle of the triangle $z_1z_2z_3$ that lie on the line passing through $G$ and parallel to the side $z_1z_3$. These points are obtained by rotating the vertex $z_2$ by $\pm \pi/2$ about the centroid $G$.

The final answers are $\boxed{z = \frac{z_1+z_2+z_3}{3} \pm i\left(\frac{2z_2-z_1-z_3}{3}\right)}$.
----------------------------------------------