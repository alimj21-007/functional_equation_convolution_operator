# Changelog — Paper 2: Spectral Framework for Zeta Analysis

This document tracks all major changes to the codebase, documentation, and outputs related to Paper 2.

---

## [v1.0.0] — Initial Release (2025-10-01)

- Created core modules:
  - `kernel.py` — kernel matrix constructor
  - `fredholm_determinant.py` — determinant computation
  - `main.py` — execution script
- Added initial Markdown documentation:
  - `theory.md`
  - `numerics.md`
  - `faq.md`
- Generated baseline plots:
  - `spectral_radius_plot.pdf`
  - `functional_equation_symmetry.pdf`

---

## [v1.1.0] — Symmetry Tests and Visualization (2025-10-10)

- Added symmetry comparison:
  - `functional_equation_symmetry_diff.pdf`
- Improved grid resolution in determinant tests
- Refactored `main.py` for modular execution
- Added CSV output for determinant values

---

## [v1.2.0] — Spectral Radius Enhancements (2025-10-18)

- Added dominant eigenvalue tracking
- Generated dual plots:
  - `spectral_radius_plot.pdf`
  - `spectral_radius_diff_plot.pdf`
- Updated `numerics.md` with spectral radius methodology

---

## [v1.3.0] — Documentation and Outreach (2025-10-25)

- Translated key files to Persian:
  - `faq.md` (bilingual)
  - `theory.md` (partial)
- Added mobile-friendly formatting notes
- Prepared public release bundle

---

## [v1.4.0] — Finalization and Repository Integration (2025-10-30)

- Finalized `changelog.md`
- Validated reproducibility across platforms
- Added README and LICENSE files
- Tagged repository for archival and citation

---

## Upcoming

- Add interactive web visualizations
- Extend framework to L-functions
- Prepare journal submission package
