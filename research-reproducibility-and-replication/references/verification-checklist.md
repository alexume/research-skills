# Clean-Room Verification Checklist

## Isolation

- Use a fresh checkout or clean package copy.
- Do not read undeclared files from the author's working directory.
- Restore dependencies from documented metadata.
- Record operating system, locale, software versions, and hardware constraints.

## Execution

- Follow only the README.
- Start from the documented entry point.
- Record each command, exit status, warning, error, and elapsed time.
- Identify network, licensed, manual, and restricted-data steps.
- Confirm all required intermediate and final outputs are regenerated.

## Comparison

- Compare key estimates, sample sizes, uncertainty measures, tables, figures, and appendix values with the manuscript.
- Use hashes for byte-stable artifacts.
- Define numeric tolerances before comparison and justify nonzero tolerances.
- Visually inspect figures when image hashes are expected to vary by platform.
- Trace each discrepancy to environment, data, code, randomness, rendering, or manuscript inconsistency.

## Decision

- `pass`: documented execution reproduces all reported results within declared tolerances.
- `conditional pass`: bounded, disclosed exceptions do not affect central claims and have an assigned correction.
- `fail`: execution is incomplete, central outputs differ, required inputs are undocumented, or verification depends on undeclared author knowledge.

The verification report must distinguish package limitations from verification failures and name every unresolved discrepancy.
