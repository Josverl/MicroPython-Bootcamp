# MicroPython-Bootcamp

The goal of this repo is to hold the materials for a MicroPython IoT Bootcamp.

This Bootcamp has the following main goals:

* Transfer knowledge and information to create rapid prototypes
* Show the art of the possible using simple devices 
* Learn to use these devices in combination with simple and more complex cloud services Using both Micosoft and other technologies
* Allow the participant use the knowledge during provided Labs
* Allow the participants to use this knowledge to envision possibilitiues for the use of IoT in production environments.
* Take the solutions (both Software and Devices) back to their workplace or home to continue learning and expirimentation.

Hardware
--------
The plan is to use ESP32 based hardware with SPI RAM to allow effective protytyping withouth the need to write highly optimised code.

Firmware
--------
The bootcamp will use [MicroPython](http://micropython.org/)

and specifically the  firmware developped by 
[loboris / MicroPython_ESP32_psRAM_LoBo](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo) 

IDE Tooling
-----------
The Labs will make use of a fork of ESPlorer: [Josverl/ESPlorer](https://github.com/Josverl/ESPlorer) which is a simple IDE and this fork has specific support for MicroPython.

## Project Structure
Code, Documentation and required binaries are located in the following structure:

    ├───Documentation
    ├───MCU                         Software to be loaded on the ESP32
    │   ├───Demo-1 Description      Software and descriptions 
    │   ├───Demo-2 Description          for the different Demos
    │   ├───Firmware                The ESP32 Firmware to be used
    │   ├───Lab-1 Description       Lab code and Decumentation
    │   ├───Lab-2 Description
    │   ├───Lab-x
    │   └───Libs                    MicroPython Libraries
    └───PC                          Software to be loaded on the MCU
        ├───IDE
        ├───Prerequisites
        └───Python

## Contributions
Please refer to [Contributing.md](Documentation/CONTRIBUTING.md)

## License
This project has adopted the [Microsoft Open Source Code of Conduct] (https://opensource.microsoft.com/codeofconduct/). For more information, see the [Code of Conduct FAQ] (https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com] (mailto:opencode@microsoft.com) with any additional questions or comments.

The MIT License (MIT)

Copyright (c) 2018 Microsoft

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
