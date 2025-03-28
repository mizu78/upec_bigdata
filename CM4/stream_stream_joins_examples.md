# Example: Left Outer Join with Watermarks

## Setup

- **Stream 1 (Orders) Watermark**: 1 hour  
- **Stream 2 (Payments) Watermark**: 2 hours  

### Join Condition

- `Stream 2 time ≥ Stream 1 time`  
- `Stream 2 time ≤ Stream 1 time + 1 hour`  

**Join Type**: LEFT OUTER JOIN  

- All records from **Stream 1 (Orders)** are kept.  
- If no matching record is found from **Stream 2 (Payments)**, `NULL` is returned.  

---

## Incoming Events

| Event Time | Stream 1 (Orders) | Stream 2 (Payments) |
|------------|--------------------|----------------------|
| 12:00 PM   | Order A           | -                    |
| 12:30 PM   | Order B           | Payment A (12:30 PM) |
| 1:00 PM    | -                 | Payment B (1:00 PM)  |
| 1:30 PM    | Order C           | -                    |
| 2:30 PM    | Order D           | -                    |
| 3:00 PM    | -                 | Payment C (3:00 PM)  |
| 4:00 PM    | Order E (Late)    | -                    |

---

## Join Execution

| Stream 1 (Orders) Time | Stream 2 (Payments) Time | Matched? | Output (Order, Payment)          |
|-------------------------|--------------------------|----------|-----------------------------------|
| 12:00 PM               | -                        | ❌ No    | (Order A, NULL)                  |
| 12:30 PM               | 12:30 PM                 | ✅ Yes   | (Order B, Payment A)             |
| 1:30 PM                | 1:00 PM                  | ✅ Yes   | (Order C, Payment B)             |
| 2:30 PM                | -                        | ❌ No    | (Order D, NULL)                  |
| 4:00 PM                | 3:00 PM                  | ✅ Yes   | (Order E, Payment C)             |

---

## Why Some Orders Have NULL Payments?

- **Order A (12:00 PM)** → No matching payment (Payment must be ≥ 12:00 PM, and no such payment exists).  
- **Order D (2:30 PM)** → No matching payment (No payment between 2:30 PM and 3:30 PM).  
- **Order E (4:00 PM)** → Matches with Payment C (3:00 PM) (within the 1-hour window).  

---

## State Retention Analysis

### Stream 1 (Orders) State Duration:
- Orders must be stored for **1 extra hour** beyond their event time (to match with a payment).  
- Since Stream 2 has a **2-hour watermark**, Orders must be kept for a total of **3 hours**.  

### Stream 2 (Payments) State Duration:
- Payments are stored for up to **2 hours** (due to the watermark).  
- Payments do not need to store unmatched records because this is a **left outer join**.  

**Total duration**: 2 hours.  

---

## Final Takeaways

- All orders are retained, even if there is no matching payment (`NULL` values).  
- Payments expire after **2 hours**, but orders are kept up to **3 hours** to accommodate late matches.  
- Late orders (like **Order E at 4:00 PM**) can still join with earlier payments if within the time condition.  