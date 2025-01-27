# cloud_tasks_probation

Welcome to the tasks! This guide will help you follow the Git workflow to keep everything organized and ensure smooth collaboration.

## Table of Contents
- [Workflow Overview](#workflow-overview)
- [Setup Instructions](#setup-instructions)
- [Creating a New Feature](#creating-a-new-feature)
- [Directory Structure](#directory-structure)
- [Submitting Your Work](#submitting-your-work)
- [Pull Request Workflow](#pull-request-workflow)

---

## Workflow Overview

To maintain an organized codebase, we follow a Git branching strategy where each team member will work in their own directory. The general steps are:

1. **Create a feature branch** from the `main` branch (e.g., `feature/username`).
2. **Work on your code** in your own directory (e.g., `username/`).
3. **Make commits** to your feature branch.
4. **Push your branch** to GitHub.
5. **Create a Pull Request** (PR) to merge your changes into `main`.
6. **Review and merge** PR after review.
7. **Pull the latest changes** from `main` to keep your local repository up-to-date.

---

## Setup Instructions

1. **Clone the repository** to your local machine:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Make sure you're on the `main` branch**:

    ```bash
    git checkout main
    ```

3. **Pull the latest changes** from `main`:

    ```bash
    git pull origin main
    ```

---

## Creating a New Feature

1. **Create a new branch** from `main` for your feature:

    ```bash
    git checkout -b feature/username
    ```

   Replace `username` with your GitHub username or a descriptive name for your feature.

2. **Work on your code** in your **specific directory** (`username/`). For example:

    ```text
    ├── username/
    │   ├── index.html
    │   ├── portfolio.css
    │   └── portfolio.js
    ```

3. **Make commits** to your feature branch:

    ```bash
    git add .
    git commit -m "Added new portfolio page"
    ```

4. **Push your branch** to GitHub:

    ```bash
    git push origin feature/username
    ```

---

## Directory Structure

Each team member has their own directory where they will work. The structure will look something like this:

