# Release Notes

## [2.22.9] - 2025-01-24

-   Fixed error message: "Can't execute command: 'ChangeSetting'" on Isaac Sim startup
-   Forced recovery of the default position of the eye-in-hand camera upon activation
-   Added `change_scene_camera_position` function in `extension.py` to change the scene camera position

## [2.22.8] - 2025-01-21

-   Fixed external camera path from body to base
-   Enabled Extension to connect to both of TMSimulator and TMFlow

## [2.22.7] - 2025-01-17

-   Add documentation: Case 3 Collaboration Accessories
-   Add documentation: Case 4 FOV Settings of External Camera
-   Refine the README.md document structure

## [2.22.6] - 2025-01-13

-   Resolve the issue where the calibration board disappears when viewed through the EXT camera.
-   Add a disk light to illuminate the front tier of the EXT camera.

## [2.22.5] - 2025-01-10

-   Update virtual camera parameters according to the specification of focal length and sensor size
-   Add 10cm pin for up-looking calibration
-   Hiding known issue of warnings in the console

## [2.22.4] - 2025-01-03

-   Add small calibration board attached to the robot flange for up-looking calibration
-   Add two sample cases in README.md and improve document structure

## [2.22.3] - 2024-12-27

-   Add Reset button for resetting the extension as needed
-   Update Third Party License
-   Update README.md

## [2.22.2] - 2024-12-20

-   Add a hint message if the connected robot model differs from the one set in the TM Digital Robot Extension.
-   Adjust the motion queue size based on the number of connected robots.
-   Update the timing for setting DI for gripper suck and release.
-   Update README.md

## [2.22.1] - 2024-12-13

-   Initial version of TM Digital Robot Extension
