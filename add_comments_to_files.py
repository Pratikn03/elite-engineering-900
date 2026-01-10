#!/usr/bin/env python3
"""
Script to add detailed instructional comments to all 900 problem Python files.
Each file will have comprehensive comments explaining what to implement.
"""

import csv
import os
from pathlib import Path


def get_problem_template(problem_data):
    """
    Generate detailed comments template for a problem file.
    
    Args:
        problem_data: dict with problem information from CSV
    
    Returns:
        str: Python file content with detailed comments
    """
    title = problem_data['problem_title']
    category = problem_data['category'].replace('_', ' ').title()
    link = problem_data['suggested_link']
    
    # Determine difficulty and pattern based on category
    patterns = {
        'arrays_strings': 'Array/String Manipulation',
        'backtracking': 'Backtracking/Recursion',
        'binary_search': 'Binary Search',
        'dynamic_programming': 'Dynamic Programming',
        'graphs': 'Graph Traversal/Search',
        'hashmap_set': 'HashMap/HashSet',
        'heaps_greedy_unionfind': 'Heap/Greedy/Union-Find',
        'linked_list': 'Linked List',
        'sliding_window': 'Sliding Window',
        'stack_queue': 'Stack/Queue',
        'trees': 'Tree Traversal',
        'two_pointers': 'Two Pointers'
    }
    
    pattern = patterns.get(problem_data['category'], 'Problem Solving')
    
    template = f'''"""
{title}
{'=' * len(title)}

LeetCode: {link}
Category: {category}
Pattern: {pattern}

PROBLEM DESCRIPTION:
-------------------
Visit the LeetCode link above to read the full problem statement.
Make sure you understand:
  - What are the inputs?
  - What should the output be?
  - What are the constraints?
  - What are the edge cases?

APPROACH TO SOLVE:
-----------------
1. READ the problem carefully on LeetCode
2. UNDERSTAND the examples provided
3. IDENTIFY the pattern (this is a {pattern} problem)
4. THINK about edge cases:
   - Empty inputs?
   - Single element?
   - Duplicates?
   - Negative numbers (if applicable)?
   - Maximum size inputs?

5. PLAN your approach:
   - What data structures do you need?
   - What algorithm will you use?
   - What's the time complexity?
   - What's the space complexity?

6. IMPLEMENT step by step:
   - Start with a simple brute force if needed
   - Then optimize
   - Add comments as you code
   - Use meaningful variable names

7. TEST your solution:
   - Run through the examples
   - Test edge cases
   - Verify time/space complexity

HINTS:
------
- Check the README.md in this directory for detailed hints
- Category: {category} - review similar problems in this folder
- Think about the {pattern} pattern

YOUR SOLUTION BELOW:
-------------------
"""

def solve():
    """
    TODO: Implement your solution here.
    
    Steps to follow:
    1. Define your function signature based on the problem
    2. Add input validation if needed
    3. Implement your core logic
    4. Return the expected output
    
    Remember:
    - Use descriptive variable names
    - Add comments for complex logic
    - Consider edge cases
    - Think about time/space complexity
    """
    pass


# TODO: Add test cases here
if __name__ == "__main__":
    """
    Test your solution with various test cases.
    
    Example format:
    test_cases = [
        (input1, input2, expected_output),
        # Add more test cases
    ]
    
    for inputs in test_cases:
        result = solve(*inputs[:-1])
        expected = inputs[-1]
        print(f"Input: {{inputs[:-1]}}")
        print(f"Expected: {{expected}}")
        print(f"Got: {{result}}")
        print(f"Status: {{'PASS' if result == expected else 'FAIL'}}")
        print("-" * 50)
    """
    
    # TODO: Uncomment and modify the test code above
    print("Problem: {title}")
    print("Visit: {link}")
    print("Start coding your solution in the solve() function above!")
'''
    
    return template


def add_comments_to_file(file_path, problem_data):
    """
    Add detailed comments to a Python file if it's mostly empty.
    
    Args:
        file_path: Path to the Python file
        problem_data: dict with problem information
    
    Returns:
        bool: True if file was updated, False if skipped
    """
    try:
        # Read existing file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Only update if file is minimal (just placeholder comment)
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # If file has more than 5 substantial lines, skip it
        if len(lines) > 5:
            return False
        
        # If file already has detailed comments, skip
        if '"""' in content and len(content) > 200:
            return False
        
        # Generate new content with detailed comments
        new_content = get_problem_template(problem_data)
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"    Error: {e}")
        return False


def process_all_files(csv_path, base_path):
    """
    Process all Python files and add detailed comments.
    
    Args:
        csv_path: Path to the CSV index file
        base_path: Base directory of the repository
    
    Returns:
        dict: Statistics about the operation
    """
    stats = {
        'total': 0,
        'updated': 0,
        'skipped': 0,
        'errors': 0
    }
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            stats['total'] += 1
            file_path = os.path.join(base_path, row['file_path'])
            
            # Check if file exists
            if not os.path.exists(file_path):
                print(f"⚠️  File not found: {row['problem_title']}")
                stats['skipped'] += 1
                continue
            
            # Try to add comments
            try:
                updated = add_comments_to_file(file_path, row)
                
                if updated:
                    print(f"✅ Updated: {row['problem_title']}")
                    stats['updated'] += 1
                else:
                    print(f"⏭️  Skipped (has content): {row['problem_title']}")
                    stats['skipped'] += 1
                    
            except Exception as e:
                print(f"❌ Error: {row['problem_title']} - {e}")
                stats['errors'] += 1
    
    return stats


def main():
    """Main execution function."""
    print("=" * 70)
    print("🚀 Add Detailed Comments to All 900 Problem Files")
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
    response = input("Add detailed comments to all Python files? (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("❌ Cancelled by user")
        return
    
    print()
    print("🔨 Adding comments to files...")
    print("-" * 70)
    
    # Process all files
    stats = process_all_files(csv_path, base_path)
    
    # Print summary
    print()
    print("=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    print(f"Total problems:     {stats['total']}")
    print(f"✅ Updated:         {stats['updated']}")
    print(f"⏭️  Skipped:         {stats['skipped']}")
    print(f"❌ Errors:          {stats['errors']}")
    print("=" * 70)
    print()
    
    if stats['updated'] > 0:
        print("✨ Success! Python files now have detailed instructional comments.")
        print("📝 Each file explains what to implement and how to approach it.")
    else:
        print("ℹ️  No files were updated (they may already have content).")


if __name__ == "__main__":
    main()
