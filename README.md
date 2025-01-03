## TM Digital Robot Extension for NVIDIA Omniverse Isaac Sim

## Introduction

**_Important:_** This extension is in **beta testing** and **not for production use**.

TM Digital Robot Extension is a simulation tool that enables developers to control virtual robots using TMSimulation(TMflow). It simplifies robot motion and vision application learning in Isaac Sim's virtual environment, eliminating the need for a physical robot. Pre-built Motion and Vision interfaces handle complex communication between TMRobot and Isaac Sim, streamlining integration tasks.

![](images/sample.png)

<!-- ## Communication Architecture

-   TBD -->

## Release Notes

Refer to the [Release Notes](RELEASE_NOTE.md) for details.

## Prerequisites

-   TMSimulator 2.22 installed on Windows 10 for TMFlow
-   Python 3.10 installed on the PC running Isaac Sim
-   Visual Studio Code installed on the PC running Isaac Sim
-   Ensure the PC running Isaac Sim and TMSimulator are on the same network and using a **wired connection**. A wireless connection is not recommended due to potential instability and delays.

**Note**: TMSimulator runs only on Windows 10. Isaac Sim runs on Windows 10/11 or Ubuntu 22.04.

## Setup Guide

The TM Digital Robot Extension for Isaac Sim requires the following **3 steps** to be completed:

-   Step1: Install Isaac Sim
    -   [For Windows](./docs/INSTALL_WINDOWS.md)
    -   [For Ubuntu](./docs/INSTALL_UBUNTU.md)
-   [Step2: Install TM Digital Robot Extension](./docs/INSTALL_EXTENSION.md)
-   [Step3: Setup TMSimulator](./docs/SETUP_TMSIMULATOR.md)

## Play with Sample Cases

Now you can run the sample cases to synchronize motion between TMRobot and Isaac Sim, please follow the steps below:

-   [Case 1: Motion Synchronization](./docs/CASE01.md)
-   [Case 2: Digital I/O with Surface Gripper](./docs/CASE02.md)

## Isaac Sim Installation Troubleshooting

If you encounter issues installing Isaac Sim, refer to the official link below for more information.

-   Hardware requirements: [Isaac Sim Hardware Requirements](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/requirements.html#system-requirements)
-   Detailed installation instructions: [Isaac Sim Python Environment Installation](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install_python.html).
-   Startup issues: [Isaac Sim Known Issues](https://docs.omniverse.nvidia.com/isaacsim/latest/known_issues.html).

## References

-   [Omniverse IsaacSim Documentation](https://docs.omniverse.nvidia.com/isaacsim/latest/index.html)
