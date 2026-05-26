# Case Study: Pirates of the Caribbean Online — Server Source Code & Dependency Recovery

**Category:** Fan Server Preservation / Legacy Dependency Matching  
**Status:** Functional — tested on Windows and Apple Silicon (M1) with known issues documented  
**Year Found:** 2024  

---

## What This Is

Pirates of the Caribbean Online (POTCO) was a Disney MMO that shut down in 2013. A small community of developers attempted to revive it through fan servers. This case study documents the recovery of:

- Full server source code for a POTCO fan server revival (Pirates Online Retribution — POR)
- The specific Astron server framework version required to run it
- The specific Panda3D build required to compile and run the client correctly

These three components must match exactly. Using the wrong version of either Astron or Panda3D causes the server or client to fail silently or crash.

---

## How To Run It
- Copy and paste the Panda3D-1.10.0 folder into C:\Panda3D-1.10.0
- Add C:\Panda3D-1.10.0\bin and C:\Panda3D-1.10.0\python to your windows PATH **Make sure that the Python included is the default one. This game doesn't work on Python 3 ANDIT NEEDS TO BE THE VERSION INCLUDED WITH THE Panda3D-1.10.0 FOLDER, AS THIS VERSION OF Panda3D HAS VERY SPECIFIC POTCO RELATED FILES!**
- Move the retribution-src folder into the C:\retribution-src
- Download msvcr120.dll and paste in SysWOW64 and System32 (I'll include it eventually. *If you want to download it from elsewhere, search of it on Google.* **Astron and the server will NOT work without this DLL file.**)
- Go to the retribution-src\win32 and run *astron.bat* then *ud.bat* and finally *ai.bat* **IN THAT EXACT ORDER**
- Go back to the retribution-src folder and run *client.bat* and choose localhost.
- Wait for the game to initialize and create a character.

Your command line should look similar. Though the client still has rendering issues on M-series Macs (as you can see in the red sky at the top), it is rendering correctly on WIndows PCs.
![Image Alt](https://github.com/TheAlepou/retribution-src/blob/master/Screenshot.png)

The game should look like this.
![Image Alt](https://github.com/TheAlepou/retribution-src/blob/master/Game_Screenshot.png)

---
## Known Bugs and Old README.md
- This version of Panda3D sometimes can corrupt itself, leaving you with errors. If there are any errors regarding Panda3D, simply delete the old copy from the C:\ drive and CTRL + C and CTRL + V the original one from the retribution-src folder into the C:\ drive. *Don't overwrite the old Panda3D. Delete it and copy and paste the original.*
- The original person who made this code public recommendeds to run the game with MongoDB for an unknown reason. Refer to the [orginal README.md](https://github.com/TheAlepou/retribution-src/blob/master/README_old.md) on how to do that.
- The [original README](https://github.com/TheAlepou/retribution-src/blob/master/README_old.md) had more bugs I have not encountered myself yet. Which is why i haven't listed them.

---

## Why This Was Hard to Find

The repository containing all three components had:

- **Zero stars**
- **Zero forks**
- No documentation linking it to POTCO or POR by name in a searchable way
- No cross-references from any known POTCO preservation community thread

It was effectively invisible to standard search. Discovery required several days of iterative searching across GitHub, archived forum threads, and dead-linked community pages before the repository surfaced.

This was not a well-known leak. At time of discovery, I was verifiably the first person to find it based on engagement metrics.

---

## The Dependency Problem

POTCO's fan server stack is built on:

- **Panda3D** — a game engine originally developed by Disney, later open-sourced. The fan server requires a *specific legacy build*, not the current release. The current release is incompatible.
- **Astron** — a distributed server framework designed for Panda3D MMOs. Again, a specific legacy version is required.

The version pinning is strict. This is not documented anywhere in an accessible, consolidated form. Matching the correct Astron version to the correct Panda3D build to the correct server source required cross-referencing fragments of information from multiple dead or semi-active community sources.

---

## Current Status & Known Issues

| Platform | Status | Notes |
|----------|--------|-------|
| Windows | Functional | Standard setup, no major issues |
| Apple Silicon (M1 Mac) | Functional with visual bug | Color rendering is distorted — likely a Panda3D rendering pipeline issue on ARM architecture. Root cause unresolved. |

The M1 color distortion is an open problem. It does not prevent the server from running but affects visual fidelity. This is worth investigating for anyone working on ARM compatibility for legacy Panda3D builds.

---

## What This Demonstrates

- Ability to locate zero-visibility repositories through iterative, non-standard search methodology
- Understanding of legacy dependency trees and version pinning in game engine stacks
- Ability to get legacy MMO server infrastructure running across multiple platforms
- Identification and documentation of platform-specific bugs for future contributors

---

## Related Finds

- **Toontown Open Level Editor** — fan server level editor, source code located and archived. Source https://github.com/TheAlepou/OpenLevelEditor
- **Toontown Stride source code** — full server source located. Source: https://github.com/TheAlepou/ToontownStride
- **Cog Invasion Online (CIO)** — source code + resources + specific Panda3D version located. CIO is a first-person shooter mod of Toontown capable of loading Half-Life BSP maps. BSP map import pipeline currently unresolved. Source: https://github.com/TheAlepou/cio-src https://github.com/TheAlepou/Open-CIO-Panda3D https://github.com/Cog-Invasion-Online https://github.com/Cog-Invasion-Online/cio-resources
- **libpirates:** source code for a DLL file. Possibly useful. Source: https://github.com/TheAlepou/libpirates-src

---

*Documentation by Luca — digital preservation hobbyist, legacy dependency recovery, rare software archival.*
