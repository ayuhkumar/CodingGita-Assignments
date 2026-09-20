
# Git Cherry-Pick — Assignment

# Q1. Theory — Understanding Cherry-Pick

Answer the following questions:

1. What is `git cherry-pick`?
2. What is the difference between **cherry-pick** and **merge**?
3. Does cherry-pick move the original commit? Explain.
4. Why does cherry-pick create a new commit?
5. What is the purpose of the following commands?

   * `git cherry-pick --continue`
   * `git cherry-pick --abort`
   * `git cherry-pick --skip`
6. What is the difference between:

   ```bash
   git cherry-pick <start_commit>..<end_commit>
   ```

   and

   ```bash
   git cherry-pick <start_commit>^..<end_commit>
   ```

---

# Answer

1. What is git cherry-pick?
- It copies a specific commit from one branch to another.
- Useful when we need only one particular change.

2. Cherry-pick vs Merge

Cherry-pick:
- Copies selected commit(s).
- Does not combine the whole branch.

Merge:
- Combines the changes of two branches.
- Usually brings all commits from the other branch.

3. Does cherry-pick move the original commit?
- No.
- The original commit stays in its original branch.
- Cherry-pick creates a copy of that change on the current branch.

4. Why does cherry-pick create a new commit?
- Because the commit is applied to a different branch/history.
- Git creates a new commit with a new commit ID (hash).

5. Cherry-pick commands

git cherry-pick --continue
- Continues cherry-pick after resolving a conflict.

git cherry-pick --abort
- Cancels the cherry-pick.
- Returns the branch to its previous state.

git cherry-pick --skip
- Skips the current commit.
- Continues with the next commit.

6. Difference between:

git cherry-pick <start_commit>..<end_commit>
- Cherry-picks commits AFTER start_commit up to end_commit.
- start_commit is NOT included.

git cherry-pick <start_commit>^..<end_commit>
- Cherry-picks from start_commit up to end_commit.
- start_commit IS included.

Example:
A -> B -> C -> D

git cherry-pick B..D
- Picks C and D.

git cherry-pick B^..D
- Picks B, C and D.

Remember:
..     = start commit excluded
^..    = start commit included








# Q2. Practical — Cherry-Pick a Specific Commit

## Scenario

You are developing a **Student Management System**.

Create a new Git repository and create a file:

```text
Student.txt
```

Add:

```text
Student Management System
```

Commit it with a meaningful commit message.

### Tasks

1. Initialize the Git repository.
2. Create and commit `Student.txt`.
3. Create a new branch for student information.
4. Add information about **Rahul** and commit it.
5. Add information about **Amit** and commit it.
6. Switch back to `main`.
7. Find the commit ID of the **Amit** commit.
8. Cherry-pick only the **Amit** commit into `main`.
9. Display the commit history using:

```bash
git log --oneline --graph --all
```

### Expected Concept

The final history should show a **new cherry-picked commit on `main`**, while the original commit remains on the student-information branch.

---

# Answer
<img width="753" height="265" alt="image" src="https://github.com/user-attachments/assets/ee281af1-6fc1-4532-ab04-ef9c11924c36" />



# Q3. Practical — Cherry-Pick Multiple Commits

Create your own project scenario.

Examples:

* E-commerce website
* Library Management System
* Hospital Management System
* College Management System
* Food Delivery Application

### Tasks

1. Create a Git repository.
2. Create a `main` branch with an initial commit.
3. Create a meaningful feature branch.
4. Make at least **3 commits** on the feature branch.
5. Switch back to `main`.
6. Cherry-pick **any two specific commits** from the feature branch.

Use:

```bash
git cherry-pick <commit_id1> <commit_id2>
```

7. Display the history:

```bash
git log --oneline --graph --all
```

### Requirement

Do **not** use generic commit messages such as:

```text
commit 1
commit 2
commit 3
```

Use meaningful messages such as:

```text
Add product search
Add product details
Fix product price
```

---


# Answer
<img width="890" height="266" alt="image" src="https://github.com/user-attachments/assets/92af690f-1d2f-4e26-a0cf-7f9442a6f403" />


# Q4. Practical — Cherry-Pick Commit Range

Create a repository with at least **4 commits**:

```text
A → B → C → D
```

Use meaningful commit messages instead of A, B, C, and D.

For example:

```text
Create homepage
Add navigation bar
Add login page
Fix login validation
```

### Task 1 — Excluding Starting Commit

Cherry-pick a range using:

```bash
git cherry-pick <start_commit>..<end_commit>
```

Identify which commits are selected.

---

### Task 2 — Including Starting Commit

Now use:

```bash
git cherry-pick <start_commit>^..<end_commit>
```

Identify which commits are selected.

### Answer

Explain the difference between:

```bash
git cherry-pick <start_commit>..<end_commit>
```

and:

```bash
git cherry-pick <start_commit>^..<end_commit>
```

---

# Answer
<img width="755" height="203" alt="image" src="https://github.com/user-attachments/assets/11dfc214-b031-4c96-bf38-668407396899" />
<img width="785" height="341" alt="image" src="https://github.com/user-attachments/assets/a6a74f3d-d9e3-4d54-83db-8c6427988604" />
<img width="765" height="352" alt="image" src="https://github.com/user-attachments/assets/92257452-d7c9-45ae-881e-d3d341c618de" />
Difference:

git cherry-pick <start_commit>..<end_commit>
Start commit is NOT included.
Picks commits after start up to end.

Example:
B..D → picks C and D.

git cherry-pick <start_commit>^..<end_commit>
Start commit IS included.
Picks start commit up to end.

Example:
B^..D → picks B, C and D.

Remember:
.. = start excluded
^.. = start included

# Q5. Practical — Resolve a Cherry-Pick Conflict

Create a simple project with two branches:

```text
main
feature
```

### Tasks

1. Create a file called:

```text
Student.txt
```

2. Add a student name on the `feature` branch.
3. Commit the change.
4. Switch to `main`.
5. Modify the **same line** in `Student.txt`.
6. Commit the change.
7. Try to cherry-pick the commit from `feature`.

Example:

```bash
git cherry-pick <feature_commit_id>
```

8. Resolve the conflict manually.
9. Stage the resolved file:

```bash
git add Student.txt
```

10. Continue the cherry-pick:

```bash
git cherry-pick --continue
```

11. Check the final history:

```bash
git log --oneline --graph --all
```

---

# Answer

<img width="841" height="917" alt="image" src="https://github.com/user-attachments/assets/c096e8f1-3272-44ce-9ae5-78e3b79b9946" />
<img width="868" height="908" alt="image" src="https://github.com/user-attachments/assets/f3ef967b-f1e0-447e-b2dd-c9e232a38fd1" />
<img width="717" height="255" alt="image" src="https://github.com/user-attachments/assets/eae33aa4-f084-43e8-8bd6-2cc12c7aae86" />


# Q6. Short Practical + Theoretical Questions 

Perform the following commands and explain what each one does:

### 1. Find commit history

```bash
git log --oneline
```

### 2. Cherry-pick one commit

```bash
git cherry-pick <commit_id>
```

### 3. Cherry-pick multiple commits

```bash
git cherry-pick <commit_id1> <commit_id2>
```

### 4. Cherry-pick a range

```bash
git cherry-pick <start_commit>..<end_commit>
```

### 5. Cherry-pick a range including the starting commit

```bash
git cherry-pick <start_commit>^..<end_commit>
```

### 6. Continue after resolving a conflict

```bash
git cherry-pick --continue
```

### 7. Cancel cherry-pick

```bash
git cherry-pick --abort
```

### 8. Skip the current commit

```bash
git cherry-pick --skip
```

---

# Answer
1. Find commit history

Command:
git log --oneline

- Shows the commit history in short form.
- Shows commit ID and commit message.


2. Cherry-pick one commit

Command:
git cherry-pick <commit_id>

- Applies the changes of one specific commit to the current branch.
- Creates a new commit.


3. Cherry-pick multiple commits

Command:
git cherry-pick <commit_id1> <commit_id2>

- Applies changes from multiple selected commits.
- Creates new commits on the current branch.


4. Cherry-pick a range

Command:
git cherry-pick <start_commit>..<end_commit>

- Cherry-picks commits after the start commit up to the end commit.
- Start commit is NOT included.


5. Cherry-pick a range including the starting commit

Command:
git cherry-pick <start_commit>^..<end_commit>

- Cherry-picks from the start commit up to the end commit.
- Start commit IS included.


6. Continue after resolving a conflict

Command:
git cherry-pick --continue

- Continues the cherry-pick after resolving a conflict.
- Used after staging the resolved files.


7. Cancel cherry-pick

Command:
git cherry-pick --abort

- Cancels the current cherry-pick.
- Returns the branch to its previous state.


8. Skip the current commit

Command:
git cherry-pick --skip

- Skips the current commit.
- Continues with the next commit.



