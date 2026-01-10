#!/usr/bin/env python3
"""
Script to generate README.md files for all 900 problems.
Each README provides problem explanation, approach hints, and learning guide.
NO SOLUTIONS INCLUDED - designed for self-study.
"""

import csv
import os
from pathlib import Path


def create_readme_content(problem_data):
    """
    Generate README.md content for a problem.
    
    Args:
        problem_data: dict with keys: id, track, category, problem_title, 
                      file_path, suggested_link, fallback_search
    
    Returns:
        str: Formatted README content
    """
    title = problem_data['problem_title']
    category = problem_data['category'].replace('_', ' ').title()
    link = problem_data['suggested_link']
    search = problem_data['fallback_search']
    
    content = f"""# {title}

## 📋 Problem Information

- **ID**: #{problem_data['id']}
- **Track**: {problem_data['track'].replace('_', ' ').title()}
- **Category**: {category}
- **LeetCode Link**: [{link}]({link})
- **Backup Search**: [Google Search]({search})

---

## 📝 Problem Statement

> **Note**: Visit the LeetCode link above to read the full problem description, 
> constraints, and see detailed examples.

### Quick Overview
{title} - Solve this problem using techniques from **{category}**.

---

## 🎯 Learning Objectives

After solving this problem, you should understand:
- [ ] Core pattern recognition for {category.lower()} problems
- [ ] Time and space complexity trade-offs
- [ ] Edge cases specific to this problem type
- [ ] Common pitfalls and how to avoid them

---

## 💡 Approach Hints

### Think About These Questions First:
1. **What is the core pattern here?**
   - Is this a simulation? Transformation? Search? Optimization?
   
2. **What data structures might help?**
   - Array? HashMap? Stack? Queue? Set? Tree? Graph?
   
3. **What's the brute force approach?**
   - Start with the simplest solution (even if inefficient)
   - Then optimize step by step
   
4. **What are the constraints?**
   - Input size limits?
   - Special cases (empty input, duplicates, negatives)?
   - Performance requirements?

---

## 🔍 Step-by-Step Guide

### Phase 1: Understand
- [ ] Read the problem statement carefully
- [ ] Identify inputs and outputs
- [ ] Work through examples manually
- [ ] List all constraints

### Phase 2: Plan
- [ ] Identify the pattern (from {category})
- [ ] Think about edge cases
- [ ] Sketch your approach on paper
- [ ] Estimate time/space complexity

### Phase 3: Implement
- [ ] Start with a simple test case
- [ ] Write clean, readable code
- [ ] Add comments for complex logic
- [ ] Handle edge cases

### Phase 4: Test
- [ ] Test with provided examples
- [ ] Test edge cases
- [ ] Test with large inputs (if applicable)
- [ ] Verify complexity matches your estimate

### Phase 5: Optimize
- [ ] Can you reduce time complexity?
- [ ] Can you reduce space complexity?
- [ ] Is there a trade-off worth making?

---

## ✅ Verification Checklist

Before marking this problem as complete:
- [ ] Solution handles all examples correctly
- [ ] Solution handles edge cases
- [ ] Code is clean and well-documented
- [ ] You understand the time complexity
- [ ] You understand the space complexity
- [ ] You can explain your approach out loud
- [ ] You've tested with custom test cases

---

## 🎓 Key Concepts for {category}

Make sure you're comfortable with these concepts:
- Pattern recognition specific to {category.lower()}
- Common algorithms used in {category.lower()}
- Typical time/space complexity patterns
- Edge cases that frequently appear

---

## 📚 Related Problems

After solving this, try related problems in:
- Same category: `{problem_data['category']}/`
- Other {category.lower()} variations
- Problems that combine {category.lower()} with other patterns

---

## 🔄 Review Schedule

- [ ] **First Review**: 1 day after solving
- [ ] **Second Review**: 3 days after solving
- [ ] **Third Review**: 1 week after solving
- [ ] **Final Review**: 1 month after solving

---

## 📝 Personal Notes

### What I Learned:
<!-- Add your insights here -->

### Mistakes I Made:
<!-- Track common errors to avoid repeating them -->

### Time Spent:
<!-- Track your progress -->

### Difficulty Rating (Personal):
<!-- Easy / Medium / Hard - How hard was it for YOU? -->

---

## 🔗 Resources

- [LeetCode Discussion]({link}discuss/)
- [Solution Patterns for {category}](../README.md)
- [Google Search for Hints]({search})

---

**Remember**: The goal is understanding, not just solving. Take your time! 🚀
"""
    
    return content


def generate_all_readmes(csv_path, base_path):
    """
    Read CSV and generate README.md for each problem.
    
    Args:
        csv_path: Path to all_900_problems_index.csv
        base_path: Base directory path for the repo
    """
    stats = {
        'total': 0,
        'created': 0,
        'skipped': 0,
        'errors': 0
    }
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            stats['total'] += 1
            
            # Get the directory where the problem file exists
            problem_file_path = row['file_path']
            problem_dir = os.path.dirname(problem_file_path)
            
            # Create README path
            readme_path = os.path.join(base_path, problem_dir, 'README.md')
            
            # Check if README already exists
            if os.path.exists(readme_path):
                print(f"⏭️  Skipped (exists): {row['problem_title']}")
                stats['skipped'] += 1
                continue
            
            try:
                # Create directory if it doesn't exist
                os.makedirs(os.path.dirname(readme_path), exist_ok=True)
                
                # Generate and write README
                content = create_readme_content(row)
                with open(readme_path, 'w', encoding='utf-8') as readme_file:
                    readme_file.write(content)
                
                print(f"✅ Created: {row['problem_title']}")
                stats['created'] += 1
                
            except Exception as e:
                print(f"❌ Error creating README for {row['problem_title']}: {e}")
                stats['errors'] += 1
    
    return stats


def main():
    """Main execution function."""
    print("=" * 70)
    print("🚀 README.md Generator for Elite Engineering 900")
    print("=" * 70)
    print()
    
    # Set paths
    base_path = Path(__file__).parent
    csv_path = base_path / 'all_900_problems_index.csv'
    
    # Verify CSV exists
    if not csv_path.exists():
        print(f"❌ Error: CSV file not found at {csv_path}")
        return
    
    print(f"📁 Base directory: {base_path}")
    print(f"📄 CSV file: {csv_path}")
    print()
    
    # Ask for confirmation
    response = input("Generate README.md files for all 900 problems? (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("❌ Cancelled by user")
        return
    
    print()
    print("🔨 Generating README files...")
    print("-" * 70)
    
    # Generate READMEs
    stats = generate_all_readmes(csv_path, base_path)
    
    # Print summary
    print()
    print("=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    print(f"Total problems:     {stats['total']}")
    print(f"✅ Created:         {stats['created']}")
    print(f"⏭️  Skipped:         {stats['skipped']}")
    print(f"❌ Errors:          {stats['errors']}")
    print("=" * 70)
    print()
    
    if stats['created'] > 0:
        print("✨ Success! README.md files have been generated.")
        print("📚 Each problem directory now has a self-study guide.")
    else:
        print("ℹ️  No new README files were created.")


if __name__ == "__main__":
    main()
