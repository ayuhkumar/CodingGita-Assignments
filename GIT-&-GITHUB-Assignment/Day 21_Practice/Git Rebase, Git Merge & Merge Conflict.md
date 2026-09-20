
## Q1. Rebase, Merge & Merge Conflict 

Answer the following:

1. Define **Git Merge**, **Merge Conflict**, and **Git Rebase**.
2. Explain **Merge vs Rebase** with a suitable diagram.
3. Write three advantages of Git Rebase.
4. Explain why Rebase is useful in real-life projects.
5. Explain the purpose of:

   * `git rebase --continue`
   * `git rebase --abort`
   * `git rebase --skip`

---

# Answer

1. Definitions

Git Merge:

* Combines changes from two branches.
* Creates a merge commit in many cases.

Merge Conflict:

* Happens when Git cannot automatically combine changes.
* We have to resolve the conflict manually.

Git Rebase:

* Moves/replays commits of one branch on top of another branch.
* Keeps the history more linear.

2. Merge vs Rebase

Merge:

main:    A---B---C
\
feature:       D---E

main:    A---B---C---D---E---M

* Combines branches.
* May create a merge commit.

Rebase:

main:    A---B---C

feature:       D---E

After rebase:

main:    A---B---C

feature:           D'---E'

* Moves feature commits on top of main.
* Creates a cleaner, straight history.

3. Three Advantages of Rebase

* Keeps Git history clean and linear.
* Makes project history easier to understand.
* Reduces unnecessary merge commits.

4. Why Rebase is useful in real-life projects?

* Keeps feature branches updated with the latest main branch.
* Makes commit history easier to read.
* Helps developers review changes more easily.
* Useful before merging a feature into the main branch.

5. Rebase Commands

git rebase --continue

* Continues the rebase after resolving a conflict.

git rebase --abort

* Cancels the rebase.
* Returns the branch to its previous state.

git rebase --skip

* Skips the current commit causing the conflict.
* Continues the rebase.

## Q2. Merge and Rebase

### Scenario: E-Commerce Website

You are working on an e-commerce project.

Create the following scenario yourself:

* Create a `main` branch.
* Create a branch named `product-page`.
* Make **two commits** on `product-page` related to the product page.
* Make **two new commits** on `main` related to other website updates.

### Tasks

1. Show the commit history using a diagram similar to:

```text
A---B---C---D  main
     \
      E---F    product-page
```

Use your **own meaningful commit messages** instead of `A, B, C...`.

2. Merge `product-page` into `main`.
3. Show the commit history after the merge (submit the screenshot).
4. Reset/recreate the scenario if required and perform a **rebase of `product-page` onto `main`**.
5. Show the commit history after the rebase(submit the screenshot).
6. Write **two differences** you observed between the merge and rebase results.

 
** Submission ** : GitHub Repo link + Screenshots + Photos of written answers

---
# Answer
<img width="1156" height="257" alt="image" src="https://github.com/user-attachments/assets/5015d095-d06f-42f0-9f24-21f6e787a9bf" />
<img width="992" height="315" alt="image" src="https://github.com/user-attachments/assets/38bb5d31-ef6d-430d-ac4b-67e076cc577d" />
https://github.com/ayuhkumar/git-rebase-assignment-1
### 6. 
Two differences observed between Merge and Rebase
Commit history:
Merge: Creates a merge commit (Merge branch 'product-page').
Rebase: Creates a straight/linear history without a new merge commit.
Commit IDs:
Merge: Original commit IDs remain the same.
Rebase: Commits are re-created, so their commit IDs change.


# Q3. Rebase Conflict

### Scenario: Student Management System

You are developing a student management system.

Create your own Git scenario using:

* `main` branch
* `student-profile` branch

### Tasks

1. Create the `student-profile` branch from `main`.
2. On `student-profile`, make **two commits** related to the student profile.
3. Switch to `main` and make a change to the **same line of the same file**.
4. Switch back to `student-profile`.
5. Rebase `student-profile` onto `main`:

```bash
git rebase main
```

6. Resolve the rebase conflict.
7. Complete the rebase using:

```bash
git add .
git rebase --continue
```

8. Create another small rebase-conflict scenario and demonstrate:

```bash
git rebase --abort
```

Explain what happened to the branch after aborting.

9. Demonstrate:

```bash
git rebase --skip
```

Explain which commit was skipped.

10. Finally, display the commit history using following command and submit the screenshot:

```bash
git log --oneline --graph --all
```

** Submission ** : GitHub Repo link + Screenshots + Photos of written answers.

---

# Answer
https://github.com/ayuhkumar/git-rebase-assignment-2
<img width="1531" height="960" alt="image" src="https://github.com/user-attachments/assets/8f41d219-0e7b-497d-b5c2-8d866467ee35" />
<img width="1502" height="907" alt="image" src="https://github.com/user-attachments/assets/2bf6c4b0-8ed6-4e3e-ae8b-83a587342bed" />

### 8.
git rebase --abort cancelled the rebase process.
The student-profile branch returned to its previous state before the rebase.
The terminal no longer shows REBASE 1/2, meaning the rebase was successfully stopped.
From the git log, student-profile and main are now pointing to the same commit (5d55321).

In short: Rebase was cancelled, and the branch was restored to its previous state.

### 9.
The skipped commit was:
Commit: d4a64b3
Message: Added email in the student-profile.txt file in student-profile Commit->G

It was skipped because Git could not apply this commit during the rebase.
After running git rebase --skip, Git ignored this commit and continued the rebase successfully.

<img width="1237" height="150" alt="image" src="https://github.com/user-attachments/assets/41a94ad1-6161-4b48-8c7f-18bd18546b55" />



<img width="1212" height="317" alt="image" src="https://github.com/user-attachments/assets/b082897e-9868-4093-ac79-9ded77f2d24e" />

<img width="1117" height="246" alt="image" src="https://github.com/user-attachments/assets/ce2a8d2c-2a5d-42e0-9bca-a0773042045b" />









