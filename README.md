# 🥁 Alpine Beats

Create awesome beats with an Alesis SR-16 inspired drum machine built with Alpine.js!

[GitHub Pages Live Preview](https://wclaytor.github.io/alpine-beats/index.html)

## Features

- **16-Step Sequencer**: Classic 16-step pattern programming
- **8 Drum Tracks**: Kick, Snare, Closed Hi-Hat, Open Hi-Hat, Clap, Rim, Tom Hi, Tom Lo
- **Adjustable Tempo**: 60-200 BPM with real-time adjustment
- **Web Audio API**: Synthesized drum sounds generated in real-time
- **Progressive Web App**: Installable and works offline
- **Responsive Design**: Works on desktop and mobile devices

## Getting Started

### Quick Start

1. Open `index.html` in a modern web browser
2. Click instrument buttons to preview sounds
3. Click on the pads to create your beat pattern
4. Press the Play button to start the sequencer
5. Adjust the tempo slider to change the speed

### Local Development

Simply serve the files using any static web server:

```bash
# Using Python
python3 -m http.server 8000

# Using Node.js
npx serve

# Using PHP
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

## Usage

### Creating Patterns

- **Click** on any pad to toggle it on/off (active pads are highlighted)
- **Click** instrument buttons to preview drum sounds
- Active steps will be highlighted when the sequencer reaches them
- Create complex rhythms by combining different drum sounds

### Controls

- **Play/Stop Button**: Start or stop the sequencer
- **Clear Button**: Reset all patterns to empty
- **Tempo Slider**: Adjust playback speed (60-200 BPM)

### Demo Pattern

The app loads with a simple demo pattern to get you started:
- Kick drum on beats 1, 5, 9, and 13
- Snare on beats 4 and 12
- Hi-hats on every other step

## Inspired by Alesis SR-16

This drum machine takes inspiration from the legendary [Alesis SR-16](https://www.alesisdrums.com/multipads-and-drum-machines/sr-16/), a classic drum machine known for its realistic sounds and intuitive pattern programming.

## Technical Details

- **Framework**: Alpine.js 3.x (loaded from CDN)
- **Audio**: Web Audio API for sound synthesis
- **Architecture**: True single-page PWA - all code, styles, and PWA assets contained in `index.html`
- **Service Worker**: Inlined for offline functionality
- **Manifest**: Dynamically generated and inlined
- **No Build Step**: Pure HTML, CSS, and JavaScript - no external files required

## Browser Compatibility

Works in all modern browsers that support:
- Web Audio API
- Service Workers
- ES6 JavaScript
- CSS Grid and Flexbox

## License

MIT

## Acknowledgments

Built with ❤️ using Alpine.js and inspired by the Alesis SR-16 drum machine.

