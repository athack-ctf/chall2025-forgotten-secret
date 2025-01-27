# Forgotten Secret

> Reconstruction of drawing by following a pen's movement indicated by usb packets to retrieve the flag.

## Type

- [X] **OFF**line
- [ ] **ON**line

## Designer(s)

- Shubair [@HAOlleik](https://github.com/HAOlleik)

## Description

Participants are given a pcap file containing captured usb packets. Their task is to dig into the file, extract specific packets, and reassemble them to reconstruct a hidden image by following a pen's movements. Once reconstructed, the image reveals a hidden flag that completes the challenge. Skills in packet analysis and forensics are essential to uncover the flag within this digital puzzle.

## Category(ies)

- `forensics`
- `IDK`

---

# Project Structure

## 1. HACKME.md

- **[HACKME.md](HACKME.md)**: A teaser or description of the challenge to be shared with participants (in CTFd).

## 2. Source Code

- **[source/README.md](source/README.md)**: Sufficient instructions for building your offline artifacts from source
  code. If your project includes multiple subprojects, please consult us (Anis and Hugo).
- **[source/*](source/)**: Your source code.

## 3. Offline Artifacts

- **[offline-artifacts/*](offline-artifacts/)**: All files (properly named) intended for local download by
  participants (e.g., a binary executable for reverse engineering, a custom-encoded image, etc.). For large files (
  exceeding 100 MB), please consult us (Anis and Hugo).

## 4. Solution

- **[solution/README.md](solution/README.md)**: A detailed writeup of the working solution.
- **[solution/FLAGS.md](solution/FLAGS.md)**: A single markdown file listing all (up-to-date) flags.
- **[solution/*](solution/)**: Any additional files or code necessary for constructing a reproducible solution for the
  challenge (e.g., `PoC.py`, `requirement.txt`, etc.). 
