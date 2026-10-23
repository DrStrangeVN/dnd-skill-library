# Check Rules — Excel & Financial Checker

## 1. Formula integrity
- Scan formula errors.
- Compare formula pattern by row/column blocks.
- Detect hardcoded constants interrupting a formula series.
- Validate totals/subtotals against components.
- Validate cross-sheet period/category references.
- Recompute affected totals after any correction.

## 2. Reconciliation
Preferred hierarchy:
1. Exact identity/reconciliation from workbook logic.
2. Neighboring formula pattern.
3. Cross-sheet matching.
4. Historical pattern inside workbook.
5. Heuristic anomaly only — flag, do not auto-fix.

## 3. Duplicates
Classify:
- Exact duplicate row.
- Duplicate unique key.
- Potential duplicate (same person/vendor/date/amount, different transaction ID).
Never delete a potential duplicate automatically unless evidence is conclusive.

## 4. Anomalies
Flag candidates such as:
- abrupt period-over-period change;
- unusually high/low amount relative to peers;
- zero where surrounding periods are non-zero;
- negative values inconsistent with row meaning;
- date outside reporting period;
- text in numeric calculation area.
Anomaly ≠ error. Use `Needs Review` unless reconciliation proves it wrong.

## 5. Formatting quality
- Preserve house style first.
- Normalize inconsistent number/date/% formats.
- Autofit with sensible width caps.
- Keep headers distinct and readable.
- Avoid excessive colors.

## 6. Confidence
- High: mathematically provable or exact formula pattern.
- Medium: strongly supported but has an alternative explanation.
- Low: anomaly/heuristic only.
Only High-confidence issues are auto-fixed by default.
