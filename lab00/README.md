# Welcome to EECS388 lab. 

In this semester, you will develop parts of a self-driving car using small embedded computers, sensors, and actuators. In the process, you will learn the fundamental concepts and practical skills to design and implement an embedded system. 

# Hardware Platforms
We will use two embedded single board computer (SBC) platforms, shown below. 


![HiFive1 Microcontroller](doc/hifive.png "HiFive Microcontroller")
![Raspberry Pi 4](doc/raspberrypi.png "Rasberry Pi 4")


The first is an Arduino compatible SBC featuring a RISC-V architecture microcontroller called HiFive1, which will be responsible for basic control and safety of the car, and the second is a Raspberry Pi 4, which will be responsible for vision-based steering using deep learning.  In the first half of the semester, we will use the HiFive1 while in the second half of the semester, we will use both platforms.

More detailed technical specs can be found in the following links. We will provide additional details of the hardware platforms when necessary for the labs in the future.

SiFive HiFive 1 rev b: [https://www.sifive.com/boards/hifive1-rev-b]
Raspberry Pi 4: [https://www.raspberrypi.org/products/raspberry-pi-4-model-b/specifications/]

# Part 0: git Setup 

## git

Git is a program that allows us to do version control, meaning we can save and track multiple versions of a single project over the course of its development. 

## git vs GitLab 

Git is the program that runs and keeps repositories (version controlled directories) on your local machine. GitLab is an online service that utilizes git to allow for people to collaborate easily by hosting a central repository that multiple people can fork, clone, or change as long as they have an internet connection. In EECS 388, we will be using KU's private GitLab servers.

## git in EECS 388

Project submissions for the labs in EECS 388 will be done with git via GitLab. Git is already setup on EECS machines. For personal setup, please follow the EECS department's tutorial here: http://wiki.eecs.ku.edu/git 

When you sign in to GitLab you will see a repository named with your student ID - in this repository you will be provided the starter code for each lab. Within your repository there will be a branch for each weeks lab that you will need to checkout. 

For example, in the first lab: 

`git checkout lab0` 

When you complete the lab, you submit your work with a final commit message in the format "FINAL COMMIT - LabXX"

## Useful git commands

Cloning (Downloading a git repo) from my gitlab repo:

* `git clone http://git.eecs.ku.edu/eecs388-Fa2020/student-repos/e559s777.git` 

Pushing (Uploading and Updating to a git repo) to gitlab:

* `git push origin labXX`

Staging files: 

* `git add .`

Committing files:

* `git commit -m "Message describing what I have done"`

# Part 1: Setup development environment 
For software development on the microcontroller, we will use Visual Studio Code (VSCode) and PlatformIO IDE combination. VSCode is already installed on your computer but you will need to install the PlatformIO IDE and other extensions. 

(Note that the following installation instructions are based on the PlatformIO IDE for VSCode documentation at: [https://docs.platformio.org/en/latest/ide/vscode.html#installation])
## Task 1.1: Take a look at Visual Studio Code 
Launch the Visual Studio Code program from the command line as follows. 

`$ code`

## Task 1.2: Install PlatformIO extensions
Next, Install the PlatformIO IDE extension for VSCode as follows. 

1. Open VSCode Package Manager
1. Search for official “platformio ide” extension
1. Install PlatformIO IDE


![PlatformIO IDE](doc/ide.png)

After the installation is completed, check if you have both `PlatformIO IDE` and `C/C++` extensions installed as follows. Optionally, installing `vscode-icons` and `vscode-pdf` extensions are also recommended. 

 
![PlatformIO IDE](doc/ide1.png)

## Task 1.3. Connect the board to your PC
Next, connect your board to one of your PC’s USB ports. Once the board is connected to the PC, two yellow power LEDs (3.3V and 1.8V) should be turned on. (See the figure below).

![Hifive](doc/hifive1.png)
 
# Part 2: Run your first program on the HiFive1 board. 
## Task 2.1 Add l1-blinky project folder 
Add the l1-blinky folder in VSCode. 

![add project](doc/addproj0.png)

![add project](doc/addproj1.png)
 
You should be able to see the screen above. 
## Task 2.2. Build and Deploy. 
You are now ready to build the code and deploy it on the target board.

First build the program by clicking the build button in the toolbar as shown below or with `ctrl+alt+b` hotkey. 

If it is successful, you can now upload the compiled program binary to the board by clicking the upload button or with `ctrl+alt+u` hotkey. 

![build](doc/build0.png)
 
If it was successful, you should see the green led on the board is blinking. (orange circle in the figure below)

![led](doc/led.png)
 
## Task 2.3. Debugging (Optional)
The HiFive1 board is already equipped with a hardware debugger support. Thus, you can utilize PlatformIO+VSCode’s debugging capability to debug your code. To use debugging, find the `Debug` menu from the pull down menu or hit `F5` (or `Ctrl+F5`). You should be able to see something like the following screen. Then, you can use the debugger toolbar (right top corner of the screenshot) to navigate the code. 

![debug](doc/debug.png)


# Appendix
## PlatformIO Keybindings

* ctrl+alt+b / cmd-shift-b / ctrl-shift-b Build Project
* cmd-shift-d / ctrl-shift-d Debug project
* ctrl+alt+u Upload Firmware
* ctrl+alt+s Open Serial Port Monitor

## PlatformIO Toolbar

 

1. [PlatformIO Home](https://docs.platformio.org/en/latest/home/index.html#piohome)
1.	PlatformIO: Build
1.	PlatformIO: Upload
1.	[PIO Remote](https://docs.platformio.org/en/latest/plus/pio-remote.html#pioremote)
1.	PlatformIO: Clean
1.	[PIO Unit Testing](https://docs.platformio.org/en/latest/plus/unit-testing.html#unit-testing)
1.	Run a task… (See “Task Runner” below)
1.	[Serial Port Monitor](https://docs.platformio.org/en/latest/userguide/cmd_device.html#cmd-device-monitor)
1.	PIO Terminal

## PlatformIO documentation

[https://docs.platformio.org/en/latest/ide/vscode.html#installation][https://docs.platformio.org/en/latest/ide/vscode.html#installation]
