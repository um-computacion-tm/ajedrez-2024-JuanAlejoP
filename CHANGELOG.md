# Changelog

All notable changes to this Chess project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.2] - 2024-09-08

### Added

- Added detailed tutorial and Docker setup instructions to the README, including images and explanations on how to play the game, configure colors, and handle game end conditions.
- Added Docker build and run instructions with details on ensuring colorama works correctly during execution.

## [1.0.1] - 2024-09-08

### Added

- Added documentation to all project files and tests, following the Google Docstrings style.

### Fixed

- Fixed the command in the Dockerfile to execute the project correctly.

## [1.0.0] - 2024-09-04

### Added

- Added tests for new features and adjusted existing tests to match the updated turn display format.

### Changed

- Fixed the starting positions of the kings and queens. Kings now start at e1 and e8, and queens start at d1 and d8, respectively.
- Added validation to ensure pieces of a specific colour can only move during their turn. White pieces can only move on white's turn, and black pieces can only move on black's turn.
- Implemented game termination conditions: the game ends when a king is captured, when all pieces of a colour are gone, or when both players agree to a draw.
- Improved the error message for empty move input to clarify the requirement for proper move notation (e.g., e4 e5).
- Refactored code for better clarity and consistency in style.
- Changed designation from 'WHITE' and 'BLACK' to 'BLANCAS' and 'NEGRAS' for identifying pieces and turns in the code and during gameplay.
- Enhanced turn display to show the current king's representation alongside the turn indicator (e.g., 'TURNO: BLANCAS' now also shows the white king).

### Fixed

- Corrected the representation and positioning of kings and queens.
- Fixed issues related to move validation and game termination conditions.

## [0.2.5] - 2024-09-01

### Changed

- Adjusted piece symbol handling to return a single symbol, removing color dependency.
- Refactored the `Board` class to display pieces with their colored symbols using the `coloured_symbol` method.
- Updated `ConsoleIO` and `Game` classes to handle color customization and board output with the new symbol handling.
- Removed the `colours` module and `ColourScheme` class as part of the refactoring.
- Refactored tests to accommodate the changes in symbol representation for pieces.
- Ensured all pieces and the board use the `coloured_symbol` method for consistent terminal representation.

### Removed

- Removed the `colours` module and `ColourScheme` class.

### Fixed

- Fixed symbol representation issues to ensure all pieces display correctly.

## [0.2.4] - 2028-08-30

### Added

- Added `is_knight_move` method to the `Knight` class.

### Changed

- Refactored knights movement logic into separated methods to solve CodeClimate issues.

## [0.2.3] - 2024-08-30

### Changed

- Refactored pieces movement logic to its previous state, since more CodeClimate issues were found in version [0.2.2].

### Removed

- Removed the `MovementValidator` class.

## [0.2.2] - 2024-08-30

### Added

- Added the `MovementValidator` class to manage piece movement validations and comply to CodeClimate issues.

### Changed

- Refactored all pieces movement logic (except `king`'s) to solve CodeClimate issues.

## [0.2.1] - 2024-08-30

### Changed

- Refactored `is_path_blocked` method to solve CodeClimate issues.

## [0.2.0] - 2024-08-29

### Added

- Added `is_occupied` method to the `Board` class to check if a square is occupied.
- Added `is_path_blocked` method to the `Board` class to verify if the path a piece wants to traverse is clear or blocked, validating the move accordingly.
- Added `move_piece` method to the `Board` class to ensure pieces do not move off the board and, if valid, move the piece.
- Added `__str__` method to handle the board's terminal representation.
- Added board as a property for the `Chess` class.
- Added `is_valid_move` method to the `Chess` class to validate moves based on the rules for each piece through their `move` methods, or `is_valid_pawn_move` for pawns.
- Added `is_valid_pawn_move` to the `Chess` class to validate pawn movements and handle captures correctly.
- Added `ConsoleIO` and `Game` classes.
- Added `colours` module and `ColourScheme` class for future UI customization options.
- Added `symbol` method to return the Unicode representation of pieces based on their color (white or black).
- Added tests for all pieces, `board`, `chess`, `client`, and `console_io` modules.

### Changed

- Refactored all code to better adhere to SOLID principles.
- Added validation for invalid moves based on the piece type using the `is_valid_move` method.
- Introduced a check to prevent pieces, except knights, from moving if their path is blocked by another piece using the `is_path_blocked` method.
- Added validation to prevent capturing a piece of the same color.
- Refactored movement logic by delegating position updates to the `move_piece` method in the `Board` class.
- Refactored chess code for greater clarity and efficiency.
- Separated input/output logic into a new `ConsoleIO` class, adhering to SOLID principles.
- Refactored the game loop into a `Game` class, improving maintainability and facilitating future extensions.
- Updated the `Chess` class usage in the client to align with the new `Game` and `ConsoleIO` structure.
- Adjusted exception handling and user interaction to be managed by `ConsoleIO`, simplifying the main game logic.
- Updated `Piece` class by changing `valid_move` to `move` to better reflect movement logic and added `symbol` for piece representation.
- Refactored all pieces by replacing `valid_move` method with a `move` method for handling movement.

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

- Added `valid_move` method for the `Pawn`, `Bishop`, `King`, and `Queen` pieces, verifying their characteristic movement capabilities.
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

- Fixed the positions of the Kings and Queens, which were previously reversed.

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