
## Question 1:

Explain the following in your own words:

1. What is the difference between a **Branch** and a **Tag** in Git?
2. What is the difference between a **Lightweight Tag** and an **Annotated Tag**?
3. Why should we prefer Annotated tags in professional/collaborative projects?
4. What is Semantic Versioning? Explain with examples of `v1.0.0`, `v1.1.0`, and `v1.1.1`.

---

# Answer
1. Branch vs Tag

Branch:
- Used for ongoing development.
- Moves forward when new commits are added.
- Example: main

Tag:
- Marks a specific commit.
- Usually used for releases/versions.
- Normally stays fixed.
- Example: v1.0.0


2. Lightweight Tag vs Annotated Tag

Lightweight Tag:
- Simple pointer to a commit.
- No extra information.
- Example: git tag v1.0.0

Annotated Tag:
- Contains extra details like author, date and message.
- Can also be signed.
- Example: git tag -a v1.0.0 -m "Release 1.0.0"


3. Why use Annotated Tags?

- Gives more information about a release.
- Shows who created it and when.
- Can contain a release message.
- Better for team/professional projects.
- Can be digitally signed.


4. Semantic Versioning

Format:
MAJOR.MINOR.PATCH

Examples:
- v1.0.0 -> First stable release.
- v1.1.0 -> New feature added.
- v1.1.1 -> Bug fix.

Remember:
MAJOR -> Breaking changes
MINOR -> New features
PATCH -> Bug fixes



## Question 2:

Perform the following tasks in your repository and submit screenshots:

1. Create at least 4 commits on the `main` branch.
2. Create two **Lightweight tags** on any two commits (as personal bookmarks).
3. Create three **Annotated tags** with proper Semantic Versioning:
   - `v1.0.0`
   - `v1.1.0`
   - `v1.1.1`
4. Push all annotated tags to GitHub.
5. Create **GitHub Releases** for `v1.0.0` and `v1.1.0`.

# Answer
<img width="1026" height="201" alt="image" src="https://github.com/user-attachments/assets/7b590ce2-ada5-4471-9308-58b4d6f23d0c" />
<img width="1017" height="287" alt="image" src="https://github.com/user-attachments/assets/379e19d9-d00d-4d38-9d25-1d9da965ec69" />
<img width="1090" height="402" alt="image" src="https://github.com/user-attachments/assets/956f1069-ef53-4251-b8fb-c2ecb8f8c455" />
<img width="1403" height="752" alt="image" src="https://github.com/user-attachments/assets/a0ce2a5d-16dc-4813-832b-b38f74453810" />
<img width="1405" height="746" alt="image" src="https://github.com/user-attachments/assets/24952c48-37d0-4fb6-b7bc-1a9002b9ccc1" />

## Question 3:

**Scenario:**

You are working on a project. Initially you were working alone, so you created lightweight tags as personal bookmarks. Later, two more developers joined the project. Now you need to follow professional standards.

### Part A: Lightweight Tags

1. Create a new repository.
2. Make at least **3 commits** on the `main` branch.
3. Create **Lightweight tags** on these commits as personal bookmarks.  
   Example names:
   - `v0.1.0-light`
   - `v0.1.1-bugFix`
   - `temp-trial`

4. Run the following command and take a screenshot:
   ```bash
   git tag
   ```

---
# Answer Part-A
<img width="828" height="130" alt="image" src="https://github.com/user-attachments/assets/0c4dc486-c48b-4aa7-9585-f0112a04b113" />

### Part B: Annotated Tags

Now imagine 2-3 developers have joined your project. From now on, use only **Annotated tags**.

### Steps:

1. Create three branches:
   ```bash
   git branch feature/major-update
   git branch feature/minor-update
   git branch bugfix/login-issue
   ```

2. **Major Update (v1.0.0)**
   - Switch to `feature/major-update`
   - Make **3 commits** (example: Authentication, Home Page, Payment Gateway)
   - Merge the branch into `main` using `pull request`
   - Create an **Annotated tag** on the merge commit:
     ```bash
     git tag -a v1.0.0 -m "First stable release - Auth, Home Page & Payment Gateway"
     ```

3. **Minor Update (v1.1.0)**
   - Switch to `feature/minor-update`
   - Make **2 commits** (example: Dark Mode feature)
   - Merge into `main` using `pull request`
   - Create Annotated tag:
     ```bash
     git tag -a v1.1.0 -m "Minor release - Added Dark Mode"
     ```

4. **Bug Fix (v1.1.1)**
   - Switch to `bugfix/login-issue`
   - Make **1 commit** (example: Fixed login redirect)
   - Merge into `main` using `pull request`
   - Create Annotated tag:
     ```bash
     git tag -a v1.1.1 -m "Patch release - Fixed login redirect issue"
     ```

---

### Part C: Push to GitHub

1. Push the `main` branch:
   ```bash
   git push origin main
   ```

2. Push all the annotated tags:
   ```bash
   git push origin v1.0.0
   git push origin v1.1.0
   git push origin v1.1.1
   ```

   **OR**

   ```bash
   git push origin --tags
   ```

---

### Part D: Create GitHub Releases

1. Go to your repository on GitHub.
2. Click on **Releases** → **Draft a new release**.
3. Create releases for the following tags:

   | Tag     | Release Title                        |
   |---------|--------------------------------------|
   | v1.0.0  | v1.0.0 – First Stable Release        |
   | v1.1.0  | v1.1.0 – Dark Mode Added             |
   | v1.1.1  | v1.1.1 – Login Bug Fix               |

4. Add a short description for each release.

---

## Submission Requirements

Submit the following:

1. Screenshot of `git tag` command (showing all tags)
2. Screenshot of `git show v1.0.0`
3. Screenshot of `git log --oneline --decorate --graph --all`
4. Link to your GitHub repository
5. Screenshots of the three GitHub Releases you created

---
# Part - B,C,D

<img width="988" height="237" alt="image" src="https://github.com/user-attachments/assets/ecbb35c2-eba2-482f-9420-da2cf7f880ad" />
<img width="1002" height="457" alt="image" src="https://github.com/user-attachments/assets/93acab62-9547-46ef-8c4a-33505ca6e940" />

<img width="1257" height="495" alt="image" src="https://github.com/user-attachments/assets/f654877b-97a9-4127-8dde-502f858ad232" />

https://github.com/ayuhkumar/git-tags-assignment2
<img width="1405" height="761" alt="image" src="https://github.com/user-attachments/assets/95bc2fb3-8cf0-4828-8747-294479caa3c8" />

<img width="1392" height="751" alt="image" src="https://github.com/user-attachments/assets/5e5ee95f-113f-4423-b402-5593e4f310df" />
<img width="1393" height="760" alt="image" src="https://github.com/user-attachments/assets/7fadf2a6-b359-4190-8408-58c74aa3e808" />































