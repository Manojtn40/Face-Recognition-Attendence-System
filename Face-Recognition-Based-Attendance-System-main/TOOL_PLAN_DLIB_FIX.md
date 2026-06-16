# Plan: Fix VSCode "Import \"dlib\" could not be resolved"

## Information gathered
- Repo scripts that import dlib:
  - `get_faces_from_camera_tkinter.py`
  - `attendance_taker.py`
  - `features_extraction_to_csv.py`
- `requirements.txt` exists in repo (nested folder) and pins `dlib==19.17.0`.
- Current issue is IDE/static: VSCode/Pylance cannot resolve `dlib`.

## Plan
1. Add a lightweight Pylance-friendly stub package:
   - Create `dlib.pyi` (or `stubs/dlib/__init__.pyi`) so VSCode recognizes the module.
   - This removes the “could not be resolved” squiggle without requiring dlib to be installed.
2. (Safety) Update runtime imports in the three scripts to produce a clear error if dlib is not installed.
   - Wrap `import dlib` in `try/except ImportError`.
   - If missing, raise a RuntimeError with an install command suggestion.

## Dependent files to edit
- Add: `dlib.pyi` (in repo root)
- Edit:
  - `get_faces_from_camera_tkinter.py`
  - `attendance_taker.py`
  - `features_extraction_to_csv.py`

## Followup steps
- Reload VSCode / Pylance after changes.
- If runtime is needed, install dlib into the same interpreter used by VSCode.

## Notes
- Stub fixes IDE squiggles; runtime still needs real `dlib` installation.

