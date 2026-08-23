### Assignment 1: Branching Commands & Naming

**Objective:** Revise branching commands and naming conventions.

**Tasks:**
1. Write the modern and older command for the following:

| Action                         | Modern Command | Older Command |
|--------------------------------|----------------|---------------|
| Switch to a branch             |                |               |
| Create + Switch to new branch  |                |               |
| Merge a feature branch         |                |               |
| Delete a merged branch         |                |               |

2. Write 4 **good** branch names and 4 **bad** branch names.
3. What is the recommended naming convention for feature branches?

<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/e95686d8-17a0-4cc6-bed2-5f81433a2a1b" />

### Assignment 2: Local Merge vs Pull Request

**Objective:** Understand the difference between the two methods.

**Tasks:**
1. Create a comparison table between **Local Merge** and **GitHub Pull Request** (at least 5 points).
2. When should you use Local Merge?
3. When should you use a Pull Request?
4. Why is Pull Request preferred in team/professional projects?
<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/308ce73b-8e5a-43a7-8353-248007fdaabe" />






### Assignment 3: Practical Local Merge

**Objective:** Practice the complete local merge workflow.

**Tasks:**
1. Make sure you are on `main`.
2. Create a branch named `feature/about-page`.
3. Create a file `about.txt` and add some content.
4. Stage and commit with a meaningful message.
5. Switch to `main` and merge the branch.
6. Delete the feature branch.
7. Verify with `git branch` and `git log --oneline`.

<img width="1165" height="1003" alt="Screenshot 2026-08-17 181428" src="https://github.com/user-attachments/assets/627f4903-e4ad-4b74-87d6-74770e2d7c55" />
<img width="778" height="435" alt="Screenshot 2026-08-17 181354" src="https://github.com/user-attachments/assets/8a5d6459-6cd2-4466-84dd-88d6d4a41bce" />




### Assignment 4:  Create & Merge Pull Request

**Objective:** Perform the professional Pull Request workflow.

**Tasks:**
1. Create a new branch `feature/services-page`.
2. Add a file `services.txt` with any content.
3. Commit the changes.
4. Push the branch using:
   ```bash
   git push -u origin feature/services-page
   ```
5. Go to GitHub and create a Pull Request.
6. Merge the Pull Request.
7. Delete the branch on GitHub.
8. Update your local main:
   ```bash
   git switch main
   git pull origin main
   git branch -d feature/services-page
   ```

<img width="1920" height="1020" alt="Screenshot 2026-08-17 182944" src="https://github.com/user-attachments/assets/e7bbe73c-46e6-469c-87d9-31f497ce7d49" />
<img width="1920" height="1020" alt="Screenshot 2026-08-17 182842" src="https://github.com/user-attachments/assets/cd122845-bbe0-43bb-a661-81f53930bc83" />
<img width="1920" height="1020" alt="Screenshot 2026-08-17 182718" src="https://github.com/user-attachments/assets/d76a5a1f-e0ee-4a1d-a9f3-563e72a71813" />


### Assignment 5: Complete Understanding + Reflection

**Objective:** Test deep understanding of Day 9 concepts.

**Tasks:**
1. Write the complete **Local Merge** workflow (step-by-step commands).
2. Write the complete **Pull Request** workflow (step-by-step).
3. Answer the following:
   - Why should we always run `git pull` on main before creating a new feature branch?
   - What happens if you merge a PR on GitHub but forget to run `git pull` locally?
   - Why should feature branches be deleted after merging?
4. Write 4 key takeaways from Day 9.

<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/c8917b20-0b7a-4563-adba-0fbd1d9ccc06" />

<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/dd6822a5-e700-4b7b-bdff-0658fddd0871" />



