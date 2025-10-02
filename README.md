# Rotation

You can find a basic introduction to **rotation matrices** in my other repositories:  
> https://github.com/JINANJINO/Warping  

This repository explains how to represent rotations using **Euler angles** and **quaternions**.

---

## 1. Euler Angles

Euler angles are a set of three parameters describing the orientation of a rigid body in three-dimensional space relative to a fixed coordinate system. Introduced by **Leonhard Euler** in the 18th century, they are widely used in **engineering, robotics, aerospace,** and **computer graphics**.

A rotation in 3D can be expressed as a sequence of three elemental rotations about coordinate axes.  
The choice of axes and the order of rotations defines the **convention** (e.g., Z-Y-X, Z-Y-Z, X-Y-Z), which may vary depending on application requirements.

<p align="center">
  <img width="283" height="178" alt="Euler angles illustration" src="https://github.com/user-attachments/assets/27cdc521-332f-4aeb-9be9-72244e6535c3" />
</p>

Mathematically, Euler angles $$(\phi, \theta, \psi)$$ are defined as:

- **Roll (\(\phi\))**: rotation about the final **x-axis**  
- **Pitch (\(\theta\))**: rotation about the new **y-axis**  
- **Yaw (\(\psi\))**: rotation about the fixed **z-axis**  

---

### 1.1 Fundamental Rotation Matrices

**Rotation about the x-axis by angle $$\(\alpha\)$$:**

$$
R_x(\alpha) =
\begin{bmatrix}
1 & 0 & 0 \\
0 & \cos\alpha & -\sin\alpha \\
0 & \sin\alpha & \cos\alpha
\end{bmatrix}
$$

**Rotation about the y-axis by angle $$\(\beta\)$$:**

$$
R_y(\beta) =
\begin{bmatrix}
\cos\beta & 0 & \sin\beta \\
0 & 1 & 0 \\
-\sin\beta & 0 & \cos\beta
\end{bmatrix}
$$

**Rotation about the z-axis by angle $$\(\gamma\)$$:**

$$
R_z(\gamma) =
\begin{bmatrix}
\cos\gamma & -\sin\gamma & 0 \\
\sin\gamma & \cos\gamma & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

---

### 1.2 Euler Angle Rotation Matrix (X–Y–Z Convention) 

When using the **extrinsic** (world-fixed) \(X \rightarrow Y \rightarrow Z\) convention, the rotations are applied **about the fixed world axes** in the specified order.  

For a point \(\mathbf{p}\):

1. Rotate about the X-axis:  
$$\[
\mathbf{p}' = R_x(\alpha) \mathbf{p}
\]$$

2. Then rotate the result about the Y-axis:  
$$\[
\mathbf{p}'' = R_y(\beta) \mathbf{p}' = R_y(\beta) R_x(\alpha) \mathbf{p}
\]$$

3. Finally, rotate about the Z-axis:  
$$\[
\mathbf{p}''' = R_z(\gamma) \mathbf{p}'' = R_z(\gamma) R_y(\beta) R_x(\alpha) \mathbf{p}
\]$$

Hence, the **overall rotation matrix** for extrinsic $$X–Y–Z$$ rotations is:

$$\[
R_{\text{extrinsic}}(\alpha,\beta,\gamma) = R_z(\gamma) \, R_y(\beta) \, R_x(\alpha)=
\begin{bmatrix}
\cos\beta \cos\gamma & \sin\alpha \sin\beta \cos\gamma - \cos\alpha \sin\gamma & \cos\alpha \sin\beta \cos\gamma + \sin\alpha \sin\gamma \\
\cos\beta \sin\gamma & \sin\alpha \sin\beta \sin\gamma + \cos\alpha \cos\gamma & \cos\alpha \sin\beta \sin\gamma - \sin\alpha \cos\gamma \\
-\sin\beta & \sin\alpha \cos\beta & \cos\alpha \cos\beta
\end{bmatrix}
\]$$

> **Note:**  
> - The previously presented matrix  
> $$\(\mathbf{R} = R_x(\alpha) R_y(\beta) R_z(\gamma)\)$$  
> corresponds instead to an **intrinsic rotation** (rotations about the moving object's axes, $$Z–Y–X$$ sequence).  
> - Extrinsic rotations are applied **in reverse multiplication order** compared to intrinsic rotations.



---

### 1.3 Limitations of Euler Angles

- **Gimbal Lock:** occurs when two rotation axes align, leading to a loss of one degree of freedom.  
- **Non-uniqueness:** multiple sets of Euler angles can represent the same orientation.  

For applications requiring **robust interpolation** or **singularity-free representation**, **quaternions** or **rotation matrices** are preferred.

<p align="center">
  <img width="850" height="329" alt="Euler angles rotation visualization" src="https://github.com/user-attachments/assets/a767d7ef-0e07-4445-8579-ccc91a8e6388" />
</p>

---
## 2. Quaternions and Rodrigues' Rotation Formula

Quaternions provide a **compact, singularity-free representation** of 3D rotations.  
Interestingly, there is a direct connection between **unit quaternions** and **Rodrigues' Rotation Formula**, which makes quaternions particularly intuitive for representing rotations about an arbitrary axis.

---

### 2.1 Quaternion Definition

A quaternion is defined as:

$$
q = w + xi + yj + zk
$$

or equivalently as a 4-dimensional vector:

$$
q =
\begin{bmatrix}
w \\
x \\
y \\
z
\end{bmatrix},
$$

where $$\(w, x, y, z \in \mathbb{R}\)$$ and $$\(i, j, k\)$$ are the imaginary units.

For a rotation by angle $$\(\theta\)$$ about a unit axis $$\(\mathbf{u} = [u_x, u_y, u_z]^T\)$$, the corresponding **unit quaternion** is:

$$
q =\begin{bmatrix}w \\x \\y \\z\end{bmatrix}=
\begin{bmatrix}
\cos(\theta/2) \\
u_x \sin(\theta/2) \\
u_y \sin(\theta/2) \\
u_z \sin(\theta/2)
\end{bmatrix}.
$$

---

### 2.2 Quaternion Rotation of a Vector

If a vector $$\(\mathbf{v}\)$$ is represented as a **pure quaternion** $$\(v_q = 0 + v_x i + v_y j + v_z k\)$$,  
then the rotated vector $$\(\mathbf{v}_{\text{rot}}\)$$ is obtained via quaternion multiplication:

$$
v' = q \otimes v_q \otimes q^*
$$

where $$\(q^*\)$$ is the **conjugate** of $$\(q\)$$, and $$\(\otimes\)$$ denotes quaternion multiplication.

---

### 2.3 Connection to Rodrigues' Rotation Formula

Expanding the quaternion multiplication above leads to:

$$
\mathbf{v}_{\text{rot}} = \mathbf{v}\cos\theta + (\mathbf{u} \times \mathbf{v})\sin\theta + \mathbf{u} (\mathbf{u} \cdot \mathbf{v})(1 - \cos\theta)
$$

which is **exactly Rodrigues' Rotation Formula**.  
Thus, **unit quaternions are a direct generalization of Rodrigues’ method**, providing a numerically stable and algebraically convenient way to rotate vectors about an arbitrary axis.

---

### 2.4 Quaternion to Rotation Matrix

A unit quaternion $$\(q = [w, x, y, z]^T\)$$ can be converted to a $$\(3 \times 3\)$$ rotation matrix as:

$$
R(q) =
\begin{bmatrix}
1-2(y^2+z^2) & 2(xy - wz) & 2(xz + wy) \\
2(xy + wz) & 1-2(x^2+z^2) & 2(yz - wx) \\
2(xz - wy) & 2(yz + wx) & 1-2(x^2 + y^2)
\end{bmatrix}.
$$

---

### 2.5 Advantages

- **No Gimbal Lock:** unlike Euler angles, quaternions avoid singularities.  
- **Efficient Interpolation:** ideal for smooth rotation interpolation (slerp).  
- **Connection to Rodrigues:** quaternions generalize Rodrigues’ formula to a fully algebraic representation.  
- **Compact Representation:** only 4 parameters vs. 9 for rotation matrices.

> **Note :** https://www.youtube.com/watch?v=d4EgbgTm0Bg
---
## 3. 2D Square Transformation Demo

This repository includes an **interactive Python demonstration** of 2D rigid-body transformations, illustrating **active vs. passive transformations**. It complements the rotation and coordinate transformation concepts introduced above.

### 3.1 Overview

- **Active Transformation:** the object moves (translation and rotation) in a fixed world frame.  
- **Passive Transformation:** the viewer (or reference frame) moves, giving the perception that the object is moving.

### 3.2 Code Snippet for Active Transformation

```python
def redraw():
    global theta, tx, ty

    point1 = [square_local[0][0]*np.cos(theta) - square_local[0][1]*np.sin(theta) + tx,
              square_local[0][0]*np.sin(theta) + square_local[0][1]*np.cos(theta) + ty]
    point2 = [square_local[1][0]*np.cos(theta) - square_local[1][1]*np.sin(theta) + tx,
              square_local[1][0]*np.sin(theta) + square_local[1][1]*np.cos(theta) + ty]
    point3 = [square_local[2][0]*np.cos(theta) - square_local[2][1]*np.sin(theta) + tx,
              square_local[2][0]*np.sin(theta) + square_local[2][1]*np.cos(theta) + ty]
    point4 = [square_local[3][0]*np.cos(theta) - square_local[3][1]*np.sin(theta) + tx,
              square_local[3][0]*np.sin(theta) + square_local[3][1]*np.cos(theta) + ty]

    Pw = [point1, point2, point3, point4]
    P = np.vstack([Pw, Pw[0]])  # close poly
    poly.set_data(P[:,0], P[:,1])
    title.set_text(f"theta={np.degrees(theta):.1f} deg  t=({tx:.2f},{ty:.2f})")
    plt.draw()
```

### 3.3 Interactive Controls

The demonstration provides real-time interaction to manipulate the square object within the 2D plane. Each key corresponds to a specific **translation** or **rotation** operation:

| Key         | Action |
|-------------|--------|
| `Arrow Up`    | Translate the object upward along the positive y-axis |
| `Arrow Down`  | Translate the object downward along the negative y-axis |
| `Arrow Left`  | Translate the object left along the negative x-axis |
| `Arrow Right` | Translate the object right along the positive x-axis |
| `W`           | Rotate the object counterclockwise by a small increment (+θ) |
| `E`           | Rotate the object clockwise by a small increment (-θ) |
| `R`           | Reset the object’s pose to the initial state (θ=0, x=0, y=0) |
| `H`           | Toggle visibility of the help text overlay |

**Implementation Details:**  

- Each vertex of the square is recalculated at each step using the 2D rotation matrix and translation vector:

$$
\mathbf{p}' = R(\theta) \mathbf{p}_{\text{local}} + \mathbf{t},
$$

where $$\(R(\theta)\)$$ is the 2D rotation matrix, $$\(\mathbf{p}_{\text{local}}\)$$ is the vertex coordinate in the local object frame, and $$\(\mathbf{t} = [t_x, t_y]^T\)$$ is the translation vector.

- The updated coordinates are plotted immediately to provide **real-time visual feedback**.

This setup allows users to **intuitively explore the effects of rotations and translations**, reinforcing the theoretical concepts of **active transformations** in a 2D plane.


[Screencast from 10-02-2025 11:28:26 PM.webm](https://github.com/user-attachments/assets/4cb45f96-e08b-4f70-8b2f-911bf1b93c50)

---

# Coordinate Transformation: 
## 1. World and Object Coordinates

Consider a square object defined in the **world frame**:

$$
\mathbf{P}_{\text{world}} =
\begin{bmatrix}
-0.5 & -0.5 \\
0.5 & -0.5 \\
0.5 & 0.5 \\
-0.5 & 0.5
\end{bmatrix}.
$$

Each row represents the $$\(x, y)$$ coordinates of a vertex in the world frame.  
The goal is to transform these points into a **viewer frame** that can move and rotate relative to the world.

---

## 2. 2D Coordinate Transformation

A **2D rigid-body transformation** consists of a rotation $$\(\theta\)$$ and a translation $$\(\mathbf{t} = [t_x, t_y]^T\)$$.  
The transformation from **world coordinates** $$\(\mathbf{p}_w\)$$ to **viewer coordinates** $$\(\mathbf{p}_v\)$$ is:

$$
\mathbf{p}_v = 
R(\theta) \, (\mathbf{p}_w - \mathbf{t}),
$$

where $$\(R(\theta)\)$$ is the **2D rotation matrix**:

$$
R(\theta) =
\begin{bmatrix}
\cos\theta & \sin\theta \\
-\sin\theta & \cos\theta
\end{bmatrix}.
$$

- $$\(\mathbf{t}\)$$ is the **translation of the viewer** in the world frame.  
- $$\(\theta\)$$ is the **rotation of the viewer frame** relative to the world frame.  

> In the code, each vertex of the square is transformed individually using this formula, and the resulting coordinates are plotted in real time.

---

## 3. Extrinsic vs. Intrinsic Rotations

Rotations can be interpreted in two different conventions:

1. **Extrinsic Rotation:**  
   - The axes of rotation are fixed in the **world frame**.  
   - Each successive rotation is applied **about the world axes**, regardless of previous rotations.
   - Example: $$\( \mathbf{p}' = R_z(\theta_z) R_y(\theta_y) R_x(\theta_x) \mathbf{p} \)$$  
     Here, rotations are applied **in world coordinates**.

2. **Intrinsic Rotation:**  
   - The axes of rotation are attached to the **moving frame** (object).  
   - Each successive rotation is applied **about the current, rotated axes**.
   - Example: $$\( \mathbf{p}' = R_x(\theta_x) R_y(\theta_y) R_z(\theta_z) \mathbf{p} \)$$  
     Here, rotations are applied **in the object’s local frame**.

In the context of this viewer example:

- The **viewer moving and rotating** is equivalent to a **passive transformation**, often treated as an **extrinsic rotation**: the world appears to rotate relative to the viewer.  
- Conversely, **rotating the object itself** in a fixed world frame is treated as an **intrinsic rotation**.

The repository also demonstrates **2D coordinate transformations** from the perspective of a **viewer frame**, distinguishing between **active (object moves)** and **passive (viewer moves)** transformations.

---
## 4. Coordinate Transformation: Passive vs. Active

### 4.1 Passive Transformation (Viewer Frame Moves)

In a passive transformation, the object remains stationary in the world frame, while the **viewer or reference frame moves**. This can be mathematically expressed as:

$$
\mathbf{p}_v = R(\theta_v) (\mathbf{p}_w - \mathbf{t}_v),
$$

where:  

- $$\(\mathbf{p}_w\)$$ is the point in the world frame.  
- $$\(\mathbf{p}_v\)$$ is the transformed point in the viewer frame.  
- $$\(R(\theta_v)\)$$ is the 2D rotation of the viewer frame.  
- $$\(\mathbf{t}_v = [t_x, t_y]^T\)$$ is the translation of the viewer frame.

This approach illustrates **extrinsic rotation**, where the world appears to rotate relative to a fixed observer.

### 4.2 Active Transformation (Object Moves)

Conversely, in an active transformation, the **object itself moves** within a fixed world frame:

$$
\mathbf{p}_w' = R(\theta) \mathbf{p}_{\text{local}} + \mathbf{t},
$$

where the translation and rotation are applied **directly to the object’s local coordinates**.  

This corresponds to **intrinsic rotation**, as the rotations are performed in the object’s own frame.

### 4.3 Key Comparison

| Transformation Type | Moving Entity | Interpretation | Rotation Convention |
|--------------------|---------------|----------------|-------------------|
| Passive             | Viewer/Frame  | World appears to move relative to the observer | Extrinsic |
| Active              | Object        | Object moves in world coordinates | Intrinsic |

- The **interactive controls** for the viewer vs. object are identical in terms of key mappings but produce conceptually different results.
- These visualizations help reinforce the understanding of **coordinate frames, rotation order, and reference frames** in 2D transformations.

---

By combining **interactive controls** with **coordinate transformations**, users can experiment with both **active object movement** and **passive frame movement**, gaining an intuitive grasp of 2D rigid-body motion.
