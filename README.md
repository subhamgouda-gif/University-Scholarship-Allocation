# University Scholarship Allocation

A beginner-friendly program that checks scholarship rules and ranks eligible students.

## What it demonstrates

Variables, numeric and string data, tuples, lists of subject marks, loops, conditions, tuple unpacking, comparison operators, and a repeated-character heading pattern. The program uses no imports or user-defined functions.

## Rules used

- Average mark must be at least 85.
- Every subject mark must be at least 70.
- Attendance must be at least 75%.
- Family income must not exceed 250000.
- Rank by higher average, then higher attendance, then lower income, then name alphabetically.

The sample student records are at the top of `main.py`; edit them to try different cases. The rules are sample assumptions and can be changed there too.

## Algorithm

1. Read each sample student record.
2. Check every subject mark, then check average, attendance, and family income.
3. Add qualifying students to a new list.
4. Compare and swap records until the list follows the tie-break ranking.
5. Print the ranked scholarship candidates.

## Pseudocode

```text
FOR each student
    check all subject marks
    IF all scholarship rules pass
        add student to eligible list
FOR each pair in eligible list
    compare ranking rules and swap if needed
print eligible list in rank order
```

## Flowchart

```text
START -> Read student list -> Check subject marks and eligibility
       -> Eligible? --yes--> Add to list
              | no              |
              +-----------------+
       -> Rank eligible students -> Print results -> END
```

## Run

```powershell
python main.py
```

## Live Streamlit deployment

https://university-scholarship-allocation-unzqdqeavixsan4khjprrs.streamlit.app/
