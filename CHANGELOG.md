# Changelog

All notable changes to this Chess project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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