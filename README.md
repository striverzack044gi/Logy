# Logy AI

Logy is a personal AI system designed to provide a private,
modular and extensible AI experience.

## Main Goals

- Personal AI Brain
- Local Memory
- Reasoning System
- Knowledge Base
- Web Search
- Voice Input
- Voice Output
- Vision
- File Reading
- Calculator
- Security
- Android Application
- Custom API

## Architecture

Logy is divided into multiple independent modules.

### Brain

Controls Logy's thinking and response generation.

### Memory

Stores personal conversation memory locally.

### API

Provides communication between the Android application
and Logy's backend.

### Tools

Contains utilities such as:

- Web Search
- Calculator
- File Reader

### Voice

Handles:

- Speech-to-Text
- Text-to-Speech
- Voice configuration

### Vision

Responsible for image understanding.

### Knowledge

Stores and manages Logy's knowledge base.

### Security

Contains security-related functions.

### Config

Contains project configuration.

## Privacy

Logy's personal runtime data is intended to remain on
the user's device.

Runtime data inside the `data/` directory is excluded
from Git tracking.

## Running

Install dependencies:

```bash
pip install -r requirements.txt# Logy
