# CM4: Understanding Spark’s State Duration in Stream-Stream Outer Joins

![alt text](<Screenshot 2025-03-28 at 00.22.27.png>)


## Given:
- **Stream 1 Watermark**: 1 hour  
- **Stream 2 Watermark**: 2 hours  

### Join Condition:
- `Stream 2 time ≥ Stream 1 time AND Stream 2 time ≤ Stream 1 time + 1 hour`

### Types of Joins:
1. **Left Outer Join**: Keep all records from Stream 1; match with Stream 2 if possible, otherwise NULL.  
2. **Right Outer Join**: Keep all records from Stream 2; match with Stream 1 if possible, otherwise NULL.
3. **Full Outer Join**: Keeps all records from both streams. If no match is found, the missing side is filled with NULL.



---

## 1. Left Outer Join: Keeping Stream 1

### State Duration
- **Stream 1 (Left Side)**:  
    Spark must retain events from Stream 1 long enough to allow Stream 2 records to match.  
    - Join condition allows a match for up to 1 hour after Stream 1’s time.  
    - Stream 2 has a 2-hour watermark, so late-arriving events must still be considered.  
    **Total State Duration for Stream 1** = 1 hour (join condition) + 2 hours (watermark of Stream 2) = **3 hours**.

- **Stream 2 (Right Side)**:  
    Since Stream 2 only contributes when it matches Stream 1, there is no need to store unmatched records.  
    Stream 2 follows its own watermark limit.  
    **Total State Duration for Stream 2** = 2 hours (watermark limit).

### Summary for Left Outer Join:
| Stream       | State Duration                                   |
|--------------|--------------------------------------------------|
| Stream 1 (Left) | 3 hours (1-hour join condition + 2-hour watermark) |
| Stream 2 (Right) | 2 hours (watermark limit)                     |

---

## 2. Right Outer Join: Keeping Stream 2

### State Duration
- **Stream 2 (Right Side)**:  
    Spark must retain events from Stream 2 long enough to allow Stream 1 records to match.  
    - Join condition allows Stream 1 to match up to 1 hour before Stream 2.  
    - Stream 1 has a 1-hour watermark, meaning older events are discarded sooner.  
    **Total State Duration for Stream 2** = 1 hour (join condition) + 1 hour (watermark of Stream 1) = **2 hours**.

- **Stream 1 (Left Side)**:  
    Since Stream 1 only contributes when it matches Stream 2, there is no need to store unmatched records.  
    Stream 1 follows its own watermark limit.  
    **Total State Duration for Stream 1** = 1 hour (watermark limit).

### Summary for Right Outer Join:
| Stream       | State Duration                                   |
|--------------|--------------------------------------------------|
| Stream 1 (Left) | 1 hour (watermark limit)                       |
| Stream 2 (Right) | 2 hours (1-hour join condition + 1-hour watermark) |

---

## 3. Full Outer Join: Keeping All Records

### State Duration

- **Stream 1 (Left Side)**:  
    Stream 1 must be retained until it has a chance to match with Stream 2 events.  
    - The join condition allows Stream 2 to match up to 1 hour after Stream 1’s time.  
    - Additionally, Stream 2’s watermark is 2 hours, meaning late-arriving Stream 2 events could still match with Stream 1.  
    **Total State Duration for Stream 1** = 1 hour (join condition) + 2 hours (watermark of Stream 2) = **3 hours**.

- **Stream 2 (Right Side)**:  
    Stream 2 must be retained until it has a chance to match with Stream 1 events.  
    - The join condition allows Stream 1 to match up to 1 hour before Stream 2’s time.  
    - However, Stream 1’s watermark is only 1 hour, meaning older Stream 1 events are discarded sooner.  
    **Total State Duration for Stream 2** = 1 hour (join condition) + 1 hour (watermark of Stream 1) = **2 hours**.

### Summary for Full Outer Join:
| Stream       | State Duration                                   |
|--------------|--------------------------------------------------|
| Stream 1 (Left) | 3 hours (1-hour join condition + 2-hour watermark) |
| Stream 2 (Right) | 2 hours (1-hour join condition + 1-hour watermark) |

---
## Final Summary Table

| Join Type         | Stream 1 State Duration                     | Stream 2 State Duration                     |
|-------------------|---------------------------------------------|---------------------------------------------|
| Left Outer Join   | 3 hours (1 hour join + 2-hour watermark)    | 2 hours (watermark limit)                   |
| Right Outer Join  | 1 hour (watermark limit)                    | 2 hours (1 hour join + 1-hour watermark)    |
| Full Outer Join   | 3 hours (1 hour join + 2-hour watermark)    | 2 hours (1 hour join + 1-hour watermark)    |


## Key Insights:
- **Left Outer Join** → Stream 1 must be retained longer because it keeps unmatched records.  
- **Right Outer Join** → Stream 2 must be retained longer because it keeps unmatched records.  
- **Full Outer Join**: A Full Outer Join retains the most state compared to Left and Right Outer Joins because both sides must keep unmatched records.

    - **Stream 1 Retention**:  
    Stream 1 must be retained longer due to Stream 2's longer watermark (2 hours), allowing late-arriving matches to occur.  

    - **Stream 2 Retention**:  
    Stream 2 must be retained for 2 hours because Stream 1 can arrive up to 1 hour earlier, and Stream 1’s watermark is only 1 hour.  

    - **Comparison with Left Outer Join**:  
    While Stream 1’s retention remains unchanged, a Full Outer Join increases Stream 2’s retention by 1 hour compared to a Left Outer Join.
