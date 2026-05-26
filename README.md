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

---

*Documentation by Luca — digital preservation hobbyist, legacy dependency recovery, rare software archival.*
