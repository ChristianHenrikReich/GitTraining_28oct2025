# Git Course: Code Quality Progression

This repository contains 10 Python files that demonstrate a progression from excellent coding practices to complete anti-patterns. These files are designed for a Git course to help students understand code quality, recognize good vs. bad practices, and learn how to use Git to track and manage code changes over time.

## File Overview

### 📈 Excellent to Good Practices (Files 1-3)

**01_excellent_practices.py** - ⭐⭐⭐⭐⭐
- Comprehensive type hints and documentation
- Proper error handling and logging
- Clean class design with dataclasses and enums
- Separation of concerns
- Comprehensive docstrings
- Professional code structure

**02_very_good_practices.py** - ⭐⭐⭐⭐
- Good class design and structure
- Proper error handling
- Clean function organization
- Good variable naming
- Some minor areas for improvement (could use dataclasses)

**03_good_practices.py** - ⭐⭐⭐
- Solid code structure
- Good error handling
- Clear function organization
- Some missing type hints and documentation

### 📉 Declining Practices (Files 4-6)

**04_decent_practices.py** - ⭐⭐
- Mixed naming conventions
- Some missing best practices
- Decent structure but inconsistent
- Global variables appearing
- Basic functionality works

**05_mediocre_practices.py** - ⭐
- Poor naming conventions
- Heavy use of global variables
- Functions doing too much
- Silent error handling
- Inconsistent code style

**06_below_average.py** - 💔
- Very poor naming (single letters)
- Global variable abuse
- Unclear function purposes
- Poor error handling
- Extremely long functions

### 🚨 Poor to Nightmare (Files 7-10)

**07_poor_practices.py** - 💀
- Massive imports and global pollution
- Terrible variable names
- No separation of concerns
- Side effects everywhere
- Extremely nested code

**08_bad_practices.py** - 💀💀
- Global variable chaos
- Semicolons in Python
- Everything on single lines
- Meaningless function names
- Complete structural breakdown

**09_very_bad_practices.py** - 💀💀💀
- Global namespace pollution
- Self-modifying code
- Dangerous practices
- Random execution
- Complete disregard for conventions

**10_nightmare_antipatterns.py** - ☠️☠️☠️
- Shadows built-in functions
- Infinite recursion potential
- Dynamic code execution
- Self-modifying files
- Complete anti-pattern showcase

## Learning Objectives

### For Git Course Students:

1. **Recognize Code Quality**: Learn to identify good vs. bad coding practices
2. **Track Changes**: Use Git to see how code quality can deteriorate over time
3. **Branching Strategy**: Practice creating branches for code improvements
4. **Code Reviews**: Learn to review and suggest improvements
5. **Refactoring**: Practice improving poor code through Git commits

## Suggested Git Exercises

### Exercise 1: Quality Analysis
```bash
git log --oneline
git diff 01_excellent_practices.py 10_nightmare_antipatterns.py
```

### Exercise 2: Improvement Branch
```bash
git checkout -b improve-file-6
# Make improvements to 06_below_average.py
git add 06_below_average.py
git commit -m "Improve variable naming and structure in file 6"
```

### Exercise 3: Code Review
```bash
git checkout -b code-review
# Add comments and suggestions to poor files
git add .
git commit -m "Add code review comments to identify issues"
```

### Exercise 4: Refactoring Journey
```bash
git checkout -b refactor-progression
# Gradually improve files 7-10, one commit per improvement
git commit -m "Fix naming conventions in file 7"
git commit -m "Remove global variables from file 7"
git commit -m "Add proper error handling to file 7"
```

## Code Quality Checklist

Use this checklist when examining the files:

### ✅ Good Practices to Look For:
- [ ] Meaningful variable and function names
- [ ] Type hints and documentation
- [ ] Proper error handling
- [ ] Single responsibility principle
- [ ] Consistent naming conventions
- [ ] Appropriate use of classes
- [ ] No global variable abuse
- [ ] Clean imports and organization

### ❌ Anti-patterns to Avoid:
- [ ] Single-letter variable names
- [ ] Functions doing too much
- [ ] Global variable abuse
- [ ] Silent error handling (bare except)
- [ ] Inconsistent naming
- [ ] No documentation
- [ ] Side effects in functions
- [ ] Deeply nested code

## Advanced Git Concepts to Practice

1. **Blame Analysis**: Use `git blame` to see "who wrote what"
2. **Bisect**: Find where code quality started declining
3. **Revert**: Practice reverting bad commits
4. **Cherry-pick**: Select good improvements from different branches
5. **Interactive Rebase**: Clean up commit history

## Course Progression Suggestions

1. **Week 1**: Analyze files 1-3, identify good practices
2. **Week 2**: Compare files 4-6, spot declining quality
3. **Week 3**: Examine files 7-10, identify anti-patterns
4. **Week 4**: Practice refactoring and improvement
5. **Week 5**: Team code reviews and Git collaboration

## Warning ⚠️

Files 8-10 contain intentionally terrible code with anti-patterns that should **NEVER** be used in real projects. They are educational examples of what to avoid.

## Contributing

When contributing improvements:
1. Create a descriptive branch name
2. Make small, focused commits
3. Write clear commit messages
4. Add comments explaining why changes improve the code

## License

This educational repository is provided for learning purposes. Feel free to use it in educational settings.