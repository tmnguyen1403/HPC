## Execution time table
| N  | std::sort | odd_even_transposition_sort 4thread | 8thread | 12thread |
| -- | --------- | ----------------------------------- | ------- | -------- |
| 123'000 | 0.01s | 34.21s | 68.18s | 74.08s |
| 123'000'000 | 3.13s | forever | forever| forever |
## Test with schedule odd_even_transposition_sort
| N  | Schedule | 4thread | 8thread | 12thread |
| -- | -------- |--------- | ------- | -------- |
| 123'000 | dynamic, 5000 | 35.65s | 53.60s | 83.69s s|
| 123'000 | static, 5000 | 38.09s | 80.06s | 88.43 s|
| 123'000 | dynamic, 20'000 | 43.92s | 125.02 | 205.54 s|
| 123'000 | static, 20'000 | 46.67s | 130.30s | 200.20 s|

