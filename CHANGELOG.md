# Changelog

All notable changes to this Chess project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.6] - 2024-08-21

### Added

- Added tests for the `Piece` class.
- Added `valid_move` method to the `Piece` base class for its subclasses.

### Changed

- Moved the `within_bounds` method from `Piece` to `Board`, relocating its tests accordingly.
- Refactored the `Piece` class to be abstract, adjusting its attributes and methods to align with this.
- Modified the `Board` class to adhere to SOLID principles, adding a `place_piece` method to handle piece placement on the board.
- Shifted the responsibility of placing pieces during board initialization to a new `BoardInitializer` class, further aligning with SOLID principles. This clarified the responsibilities within `Board`.
- Made changes to `Chess` due to the refactoring in `Board`.

### Removed

- Deleted several piece tests to rewrite them.

## [0.1.5] - 2024-08-20

### Added

- Added a `valid_move` method for the `Pawn`, `Bishop`, `King`, and `Queen` pieces, verifying their characteristic movement capabilities.
- Added unit tests for the `King` and `Queen` pieces.

### Changed

- Refactored the codebase to separate each chess piece into individual files. Previously, all pieces were contained in `pieces.py`; now, each piece, including the superclass `Piece`, has its own file. The same structure was applied to their respective tests, separating them into individual files.
- Organized the pieces and their tests into `pieces` and `pieces_t` directories, respectively.

## [0.1.4] - 2024-08-18

### Added

- Added basic logic for the `Rook` piece's movement.
- Added unit tests to verify the `Rook` piece's movement logic.

### Fixed

- Fixed issues with existing chess tests.
- Fixed the `Chess` class to correctly initialize the turn as `WHITE`.

### Changed

- Made minor readability improvements in the `Client` class.

## [0.1.3] - 2024-08-16

### Added

- Added tests for the `Board` class.

### Fixed

- The positions of the Kings and Queens were fixed, as they were previously reversed.

## [0.1.2] - 2024-08-16

### Added

- Added a `ValueError` in the `move` method for cases where no piece is found in the selected starting position.

### Changed

- Updated the `Pawn`, `Rook`, `Knight`, `Bishop`, `Queen`, and `King` subclasses to correctly inherit attributes from the `Piece` superclass.

### Fixed

- Fixed the `move` method in the `Chess` class to correctly move pieces on the board. Previously, the method failed to perform the move.

## [0.1.1] - 2024-08-15

### Added

- Added placeholders for remaining pieces.
- Added subclasses `Knight`, `Bishop`, `Queen`, and `King`.
- Updated the `Board` class to initialize the positions of all pieces on the board.

### Changed

- Improved the initialization process for piece placement on the board.

## [0.1.0] - 2024-08-15

### Added

- Added the `game` folder to contain all game-related modules.
- Added the `board` module to contain the `Board` class.
- Added the `Board` class to manage the game board. It creates an 8x8 board and initializes the rooks' positions. The `get_piece` method retrieves a piece's position on the board.
- Added the `chess` module to contain the `Chess` class.
- Added the `Chess` class to manage basic chess game flow. It initializes the game board and tracks turns. The `move` method is used to move pieces on the board, and the `change_turn` method advances turns.
- Added the `client` module to play the game through the console, allowing players to input coordinates to move pieces.
- Added the `pieces` module to contain the `Piece` superclass and its subclasses `Pawn` and `Rook`. This module handles the functionality of the chess pieces.
- Added the `tests` folder to contain all testing files.
- Added configuration files for CircleCI, CodeClimate, coverage, and Docker.
- Added `.gitignore`.
- Added `CHANGELOG.md`.
- Added `README.md`.

## [0.0.0] - yyyy-mm-dd

### Added
### Changed
### Removed
### Fixes