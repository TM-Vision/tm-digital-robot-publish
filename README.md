# TM Digital Robot

## Introduction

TM Digital Robot Extension is a robot simulation tool that allow developers control virtual robot by TMSimulation(TMflow), robot controller. Developers can easily learn how control robot motion and vision applications in the virtual environment of Isaac Sim, without the need for a physical robot. The complex communication between TMRobot and Isaac Sim has been simplified with pre-built Monition and Vision interfaces, allowing developers to avoid handling intricate integration tasks.

![](images/sample.png)

<!-- ## Communication Architecture

-   TBD -->

## Release Notes

-   Please refer to the [Release Notes](RELEASE_NOTE.md) for the details.

## Prerequisites

-   TMSimulator 2.22 installed in Windows 10 where the TMFlow will be running
-   Python 3.10 installed in the PC where Isaac Sim will be running
-   Visual Studio Code installed in the PC where Isaac Sim will be running

**Important**: TMSimulator can be run in Windows 10 only. Isaac Sim can be run in Windows 10/11 or Ubuntu 22.04.

## Installation of Isaac Sim

-   Refer to the [Isaac Sim Setup Guide for Windows](SETUP_WINDOWS.md) for quick installation instructions.
-   Refer to the [Isaac Sim Setup Guide for Ubuntu](SETUP_UBUNTU.md) for quick installation instructions.
-   **Troubleshooting:**

    -   If you want to know more installation details from official documents, please refer to [Isaac Sim Python Environment Installation](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install_python.html)

    -   If you encounter any issues when starting Isaac Sim, please refer to [Isaac Sim Known Issues](https://docs.omniverse.nvidia.com/isaacsim/latest/known_issues.html)

## Installation of TM Digital Robot Extension

-   Start Isaac Sim
-   Click Window -> Extensions from the top menu, an Extensions window will appear
-   Click the hamburger icon on the top right corner, then click Settings, Extensions Search Paths will appear

    ![](images/20241211115451.png)

-   Click the Add button, then input the path of the TM Digital Robot Extension where you have cloned the repository, please make sure the path MUST PLUS **/exts** at the end

    -   Example of setting in Windows

    ![](images/20241211160922.png)

    -   Example of setting in Ubuntu

    ![](images/20241211120042.png)

-   Next, click THIRD PARTY tab, find TM Digital Robot Extension, then toggle the ENABLED and check AUTOLOAD

    ![](images/20241211130628.png)

-   If setup is correct, you will see a new Menu called TMRobot on the top menu, click TM Digital Robot then TM Digital Robot Extension will appear

    ![](images/20241211130926.png)

-   It's the good idea to drag and dock the TM Digital Robot Extension to the right side of the window for easy access

    ![](images/20241211131210.png)

-   Now, you've successfully installed the TM Digital Robot Extension

## Setup TMSimulator

-   Once you have installed the TMSimulator(TMflow), click the TMSimulator icon on the desktop to start the application, then Select Virtual Robot Type window will appear

    ![](images/20241211131907.png)

-   Click one of the robot types you want to simulate

    ![](images/20241211134942.png)

### Setup Communication

-   Click gear icon -> Configuration -> Communication on left menu, then Communication window will appear

-   Click Ethernet Slave tab, then toggle Status as Disable

    ![](images/20241211135513.png)

-   Config Data Table

    -   Step 1. Select Joint_Angle, Ctrl_DI, Ctrl_DO, End_DI, End_DO to the right side of the window, **(IMPORTANT)the sequence of the selected items MUST be the same as the below image**

    -   Step 2. Set Communication Mode as STRING
    -   Step 3. Save the Transmit File Name as digital_robot

        ![](images/20241211135713.png)

    -   Step 4. Go back the Communication window, tick Write Permission and toggle Status to Enable

        ![](images/20241211150426.png)

### Enable Virtual Camera API

-   Click gear icon -> Configuration -> Vision Settings on left menu, then Vision Settings window will appear

-   Click Services

    ![](images/20241211154146.png)

-   Click Virtual Camera API tab, then toggle Status to Enabled

    ![](images/20241211154258.png)

-   Now, you've successfully setup the TMSimulator

<!-- -   Import TMflow sample project **digital_robot_motion_v7.zip** from folder tmflow_sample_project to TMSimulator

-   Play the project, you will see the robot is moving

    ![](images/20241211153813.png) -->

<!-- ## Usage

-   TbD -->
