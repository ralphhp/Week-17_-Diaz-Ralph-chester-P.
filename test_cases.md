# Test Cases – Simulated Device Monitoring and Alert System

**Tested by:** Ralph Chester Diaz 
**Date of testing:** 10/17/26

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 – View initial readings | Choose `1` | Displays 28, 31, 35, 37, 29 in order | Displays 28, 31, 35, 37, 29 in order | Passed |
| TC02 – Add valid reading | Choose `2`, enter `33` | “Reading added successfully.” | “Reading added successfully.” | Passed |
| TC03 – Non-numeric input | Choose `2`, enter `abc` | Rejected; list remains unchanged | Rejected; list remains unchanged | Passed |
| TC04 – Below valid range | Choose `2`, enter `-5` | Rejected; list remains unchanged | Rejected; list remains unchanged | Passed |
| TC05 – Above valid range | Choose `2`, enter `120` | Rejected; list remains unchanged | Rejected; list remains unchanged | Passed |
| TC06 – Boundary 30 °C | Add `30`, then choose `3` | `30 °C -> WARNING` | `30 °C -> WARNING` | Passed |
| TC07 – Boundary 35 °C | Choose `3` | `35 °C -> WARNING` | `35 °C -> WARNING` | Passed |
| TC08 – Numerical summary | Choose `4` before adding readings | Total 160, average 32.00, minimum 28, maximum 37, status ATTENTION REQUIRED | Total 160, average 32.00, minimum 28, maximum 37, status ATTENTION REQUIRED | Passed |
| TC09 – Invalid menu choice | Enter `9` | Error message appears and menu is shown again | Error message appears and menu is shown again | Passed |
| TC10 – Exit | Choose `5` | Exit message appears and program ends | Exit message appears and program ends | Passed |

## Bugs Found and Fixed
During testing, check that the minimum and maximum are initialized using the first reading rather than zero. This prevents the minimum from incorrectly becoming 0 when all readings are positive. Also verify that the status function checks for a CRITICAL reading before checking for WARNING, because CRITICAL has higher priority.