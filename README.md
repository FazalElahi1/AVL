
# 🌳 AVL Tree Implementation in Python

![C++](https://img.shields.io/badge/Language-C++-blue.svg)
![Data Structure](https://img.shields.io/badge/Data%20Structure-AVL%20Tree-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📌 Overview

This project is an implementation of an **AVL Tree**, a self-balancing Binary Search Tree (BST).
It ensures that the tree remains balanced after every insertion and deletion, maintaining **O(log n)** time complexity for core operations.

An AVL tree automatically performs **rotations** when imbalance occurs, making it efficient for searching, insertion, and deletion operations.

---

## 🚀 Features

* 🔍 Search operation (O(log n))
* ➕ Insert node with automatic balancing
* ❌ Delete node with rebalancing
* 🔄 Left and Right rotations
* ⚖️ Self-balancing mechanism using height factor
* 🌲 Inorder, Preorder, Postorder traversal (if implemented)

---

## 🧠 How AVL Tree Works

An AVL tree maintains a **balance factor**:

```
Balance Factor = Height(Left Subtree) - Height(Right Subtree)
```

Each node must satisfy:

```
-1 ≤ Balance Factor ≤ 1
```

If imbalance occurs, the tree performs:

* 🔁 Left Rotation
* 🔁 Right Rotation
* 🔁 Left-Right Rotation
* 🔁 Right-Left Rotation

---

## 🛠️ Tech Stack

* Language: **C++**
* Concept: **Data Structures & Algorithms**
* Focus: **Self-Balancing Binary Search Tree**

---

## 📂 Project Structure

```
AVL/
│── AVLTree.py      # AVL tree implementation
│── README.md       # Documentation
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/FazalElahi1/AVL.git
cd AVL
```

### 2. Compile the code

```bash
g++ main.cpp -o avl
```

### 3. Run the program

```bash
./avl
```

---

## 📊 Example Output

```
Inserted: 10
Inserted: 20
Inserted: 30

Tree balanced using rotation

Inorder Traversal:
10 20 30
```

---

## 📚 Learning Outcomes

This project helps understand:

* Binary Search Trees (BST)
* Tree balancing techniques
* Recursive algorithms
* Rotation logic in AVL trees
* Time complexity optimization

---

## 💡 Future Improvements

* GUI visualization of AVL Tree
* File-based input/output
* Performance comparison with BST
* STL-style generic implementation (templates)

---

## 👨‍💻 Author

**Fazal Elahi**
📌 Passionate about Data Structures, Machine Learning, and Software Development

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to fork it!

---
