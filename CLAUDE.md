# Claude Instructions - Alpine Beats Drum Machine

## 🎯 Project Context and Purpose

Alpine Beats is a fully functional web-based drum machine inspired by the legendary Alesis SR-16. This project demonstrates professional Alpine.js development for creating an interactive music application with real-time audio synthesis, sequencer programming, and PWA capabilities.

**Project Domain**: Music Production / Audio Application
**Tech Stack**: Alpine.js 3.x, Web Audio API, Progressive Web App, Pure HTML/CSS/JavaScript

This application showcases:
- Real-time audio synthesis using Web Audio API
- Interactive 16-step sequencer with 8 drum tracks
- Reactive state management with Alpine.js
- Progressive Web App with offline capabilities
- No build process - pure standalone HTML application

## 🥁 When Working on Alpine Beats

### ✅ Current Features (Implemented):
- **16-Step Sequencer**: Classic 16-step pattern programming
- **8 Drum Tracks**: Kick, Snare, Closed Hi-Hat, Open Hi-Hat, Clap, Rim, Tom Hi, Tom Lo
- **Each Track Has**: Name (desktop), emoji icon (mobile), 16 step slots, synthesized sound
- **Adjustable Tempo**: 60-200 BPM with real-time slider adjustment
- **Controls**: Play/Stop button, Clear button, Tempo slider
- **Visual Feedback**: Active steps highlighted, current playback position shown with red border
- **Sound Preview**: Click track label button to preview drum sounds
- **Demo Pattern**: Auto-loads with kick (1,5,9,13), snare (4,12), hi-hats (every other step)
- **Web Audio API**: All 8 drum sounds synthesized in real-time (oscillators + noise)
- **Progressive Web App**: Installable, works offline, dynamic manifest and service worker
- **Responsive Design**: Works on desktop (full names) and mobile (emoji icons)
- **True Single-File**: Everything inline in index.html (no external .js, .css, or PWA files)

### ✅ Focus Areas for Enhancements:
- Enhancing drum sequencer functionality (swing, pattern length, sub-steps)
- Improving Web Audio API sound synthesis (effects, filters, better sounds)
- Adding new drum sounds or effects (reverb, delay, compression)
- Enhancing user interface interactions (drag patterns, copy/paste)
- Performance optimization for audio playback
- PWA features and offline capabilities
- Mobile/touch interface improvements
- Pattern save/load functionality
- MIDI support
- Pattern export (audio or MIDI)

### ⚠️ Project Constraints (Critical - Never Violate):
- **No build process**: Must remain a pure HTML/CSS/JavaScript application
- **No external audio files**: All sounds generated via Web Audio API synthesis
- **No external dependencies**: Alpine.js from CDN only, everything else inline
- **Offline capable**: Must work via Service Worker after first load
- **Performance critical**: Audio timing must be precise (no latency/jitter)
- **Mobile friendly**: Touch interactions must be responsive
- **Single-file architecture**: Keep everything in index.html

## 📋 Alpine Beats Architecture

### Core Structure
```
Alpine Beats
├── index.html          # Complete standalone application - ALL code, styles, and PWA assets inline
├── README.md          # User documentation
├── AGENTS.md          # AI agents role-based development guide
├── CLAUDE.md          # This file - Claude-specific instructions
├── LICENSE.md         # MIT License
├── docs/              # Additional role documentation and feature guides
└── .github/           # GitHub configuration and Copilot instructions
```

**Key Architecture Points:**
- **True Single-File App**: index.html contains everything - HTML, CSS, JavaScript, Alpine.js initialization
- **No External Files**: Alpine.js loaded from CDN (https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js)
- **Dynamic PWA**: Service Worker and Manifest are dynamically generated at runtime using Blob URLs and data URLs
- **Inline Everything**: No separate .js, .css, sw.js, or manifest.json files required
- **Offline Capable**: Service Worker is registered from inline code, caches CDN Alpine.js and the page itself

### Alpine.js State Management Pattern
```javascript
function drumMachine() {
    return {
        // === DRUM TRACKS STATE ===
        tracks: [
            { name: 'Kick', icon: '🦶', steps: Array(16).fill(false), sound: null },
            { name: 'Snare', icon: '🥁', steps: Array(16).fill(false), sound: null },
            { name: 'Closed HH', icon: '🔒', steps: Array(16).fill(false), sound: null },
            { name: 'Open HH', icon: '🔓', steps: Array(16).fill(false), sound: null },
            { name: 'Clap', icon: '👏', steps: Array(16).fill(false), sound: null },
            { name: 'Rim', icon: '⭕', steps: Array(16).fill(false), sound: null },
            { name: 'Tom Hi', icon: '⬆️', steps: Array(16).fill(false), sound: null },
            { name: 'Tom Lo', icon: '⬇️', steps: Array(16).fill(false), sound: null }
            // Each track has name (desktop), icon (mobile), 16 steps, and sound function
        ],
        
        // === SEQUENCER STATE ===
        tempo: 120,
        isPlaying: false,
        currentStep: -1,
        intervalId: null,
        audioContext: null,
        
        // === LIFECYCLE ===
        init() {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            this.generateDrumSounds();
            this.loadDemoPattern(); // Loads demo beat: kick on 1,5,9,13; snare on 4,12; hi-hats on every other step
        },
        
        // === AUDIO SYNTHESIS ===
        playKick() {
            // Oscillator-based kick: 150Hz exponential decay to 0.01 over 0.5s
        },
        
        playSnare() {
            // Hybrid: oscillator (200Hz) + white noise, both with 0.2s envelope
        },
        
        // === SEQUENCER LOGIC ===
        step() {
            if (!this.isPlaying) return;
            
            this.currentStep = (this.currentStep + 1) % 16;
            
            // Play sounds for active steps
            this.tracks.forEach(track => {
                if (track.steps[this.currentStep] && track.sound) {
                    track.sound();
                }
            });
            
            // Precise timing using setTimeout (16th notes)
            const stepDuration = (60 / this.tempo) * 1000 / 4;
            this.intervalId = setTimeout(() => this.step(), stepDuration);
        }
    }
}
```

## 🎨 Alpine Beats UI Patterns

### Sequencer Grid Pattern
```html
<div class="sequencer">
    <template x-for="(track, trackIndex) in tracks" :key="trackIndex">
        <div class="track">
            <!-- Track label is a button for sound preview -->
            <button class="track-label" @click="previewSound(trackIndex)">
                <span class="track-name" x-text="track.name"></span>
                <span class="track-icon" x-text="track.icon"></span>
            </button>
            <div class="steps">
                <template x-for="(step, stepIndex) in track.steps" :key="stepIndex">
                    <div 
                        class="step" 
                        :class="{ 
                            'active': step, 
                            'current': currentStep === stepIndex 
                        }"
                        @click="toggleStep(trackIndex, stepIndex)"
                    ></div>
                </template>
            </div>
        </div>
    </template>
</div>
```

**Key Pattern Notes:**
- Track labels show full name on desktop (>768px), emoji icon only on mobile (≤768px)
- Clicking track label previews the drum sound
- Clicking step pads toggles them on/off
- `current` class highlights the playback position
- `active` class shows programmed steps

### Audio Preview Pattern
```javascript
// Click interaction for sound preview (works on mobile and desktop)
previewSound(trackIndex) {
    if (this.tracks[trackIndex].sound) {
        this.tracks[trackIndex].sound();
    }
}
```

**Note**: The original implementation mentioned hover (`@mouseenter`), but the current version uses click (`@click`) on track labels for better mobile compatibility.

### Tempo Control Pattern
```html
<div class="tempo-control">
    <label>Tempo: <span x-text="tempo"></span> BPM</label>
    <input type="range" min="60" max="200" x-model="tempo" @input="updateTempo()">
</div>
```

## 🔊 Web Audio API Integration

### Critical Audio Patterns

**1. Audio Context Initialization**
```javascript
init() {
    // ALWAYS check for vendor prefixes for Safari compatibility
    this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
    this.generateDrumSounds(); // Assign sound functions to tracks
    this.loadDemoPattern(); // Load the demo beat
}
```

**2. Oscillator-Based Sounds (Kick, Rim, Toms)**
```javascript
playKick() {
    const now = this.audioContext.currentTime;
    const osc = this.audioContext.createOscillator();
    const gain = this.audioContext.createGain();
    
    // Frequency envelope for punch: 150Hz decaying to near-zero
    osc.frequency.setValueAtTime(150, now);
    osc.frequency.exponentialRampToValueAtTime(0.01, now + 0.5);
    
    // Amplitude envelope: exponential decay for natural sound
    gain.gain.setValueAtTime(1, now);
    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.5);
    
    osc.connect(gain);
    gain.connect(this.audioContext.destination);
    
    osc.start(now);
    osc.stop(now + 0.5); // CRITICAL: Always stop to prevent memory leaks
}
```

**3. Noise-Based Sounds (Snare, Hi-hats, Clap)**
```javascript
playSnare() {
    const now = this.audioContext.currentTime;
    
    // Tone component (oscillator)
    const osc = this.audioContext.createOscillator();
    const oscGain = this.audioContext.createGain();
    osc.frequency.setValueAtTime(200, now);
    oscGain.gain.setValueAtTime(0.3, now);
    oscGain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
    osc.connect(oscGain);
    
    // Noise component (white noise buffer)
    const bufferSize = this.audioContext.sampleRate * 0.2;
    const buffer = this.audioContext.createBuffer(1, bufferSize, this.audioContext.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
        data[i] = Math.random() * 2 - 1; // White noise: -1 to 1
    }
    
    const noise = this.audioContext.createBufferSource();
    noise.buffer = buffer;
    const noiseGain = this.audioContext.createGain();
    noiseGain.gain.setValueAtTime(0.5, now);
    noiseGain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
    noise.connect(noiseGain);
    
    // Connect both to destination
    oscGain.connect(this.audioContext.destination);
    noiseGain.connect(this.audioContext.destination);
    
    osc.start(now);
    osc.stop(now + 0.2);
    noise.start(now);
}
```

**4. Filtered Noise (Hi-hats)**
```javascript
playClosedHihat() {
    const now = this.audioContext.currentTime;
    const bufferSize = this.audioContext.sampleRate * 0.05; // Short duration
    const buffer = this.audioContext.createBuffer(1, bufferSize, this.audioContext.sampleRate);
    const data = buffer.getChannelData(0);
    
    for (let i = 0; i < bufferSize; i++) {
        data[i] = Math.random() * 2 - 1;
    }
    
    const noise = this.audioContext.createBufferSource();
    noise.buffer = buffer;
    
    // High-frequency bandpass filter for metallic hi-hat sound
    const bandpass = this.audioContext.createBiquadFilter();
    bandpass.type = 'bandpass';
    bandpass.frequency.value = 10000; // High frequency
    
    const gain = this.audioContext.createGain();
    gain.gain.setValueAtTime(0.3, now);
    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.05);
    
    noise.connect(bandpass);
    bandpass.connect(gain);
    gain.connect(this.audioContext.destination);
    
    noise.start(now);
}
```

**5. Multi-Layer Sounds (Clap - 3 noise bursts)**
```javascript
playClap() {
    const now = this.audioContext.currentTime;
    
    // Create 3 noise bursts with slight delay for realistic clap
    for (let i = 0; i < 3; i++) {
        const time = now + (i * 0.03); // 30ms between bursts
        const bufferSize = this.audioContext.sampleRate * 0.05;
        const buffer = this.audioContext.createBuffer(1, bufferSize, this.audioContext.sampleRate);
        const data = buffer.getChannelData(0);
        
        for (let j = 0; j < bufferSize; j++) {
            data[j] = Math.random() * 2 - 1;
        }
        
        const noise = this.audioContext.createBufferSource();
        noise.buffer = buffer;
        
        const bandpass = this.audioContext.createBiquadFilter();
        bandpass.type = 'bandpass';
        bandpass.frequency.value = 1500; // Mid-frequency for hand clap
        
        const gain = this.audioContext.createGain();
        gain.gain.setValueAtTime(0.3, time);
        gain.gain.exponentialRampToValueAtTime(0.01, time + 0.05);
        
        noise.connect(bandpass);
        bandpass.connect(gain);
        gain.connect(this.audioContext.destination);
        
        noise.start(time);
    }
}
```

### Current Drum Sounds Implementation

| Drum | Type | Frequency/Filter | Duration | Notes |
|------|------|------------------|----------|-------|
| **Kick** | Oscillator | 150Hz → 0.01Hz | 0.5s | Deep bass punch with exponential pitch decay |
| **Snare** | Osc + Noise | 200Hz osc + white noise + bandpass | 0.2s | Hybrid of tone and noise for realistic snare |
| **Closed HH** | Filtered Noise | 10kHz bandpass | 0.05s | Short, bright metallic sound |
| **Open HH** | Filtered Noise | 8kHz bandpass | 0.3s | Longer decay for open hi-hat sizzle |
| **Clap** | 3x Noise Bursts | 1.5kHz bandpass, 30ms apart | 0.05s each | Layered bursts simulate hand clap |
| **Rim** | Oscillator | 800Hz → 400Hz | 0.1s | Short, bright rim shot |
| **Tom Hi** | Oscillator | 300Hz → 100Hz | 0.3s | High tom with pitch sweep |
| **Tom Lo** | Oscillator | 180Hz → 60Hz | 0.4s | Low tom with longer decay |

## ⚠️ Critical Alpine Beats Rules

### ALWAYS Follow:

1. **Audio Timing Precision**: Use `audioContext.currentTime` for scheduling, never `Date.now()` or `performance.now()`
2. **Exponential Ramps**: Use `exponentialRampToValueAtTime()` for natural-sounding envelopes (never linear for audio)
3. **Stop Oscillators**: Always call `osc.stop()` to prevent memory leaks
4. **No Audio Files**: All sounds must be synthesized via Web Audio API
5. **Touch Events**: Support both mouse and touch events for mobile compatibility
6. **Tempo Changes**: Tempo adjustments take effect on next step to avoid glitches

### Performance Guidelines:
- Minimize DOM updates during sequencer playback
- Use `:class` bindings for visual feedback (not direct DOM manipulation)
- Reuse audio nodes where possible to reduce GC pressure
- Use `setTimeout` over `setInterval` for precise timing control
- Test on mobile devices for touch latency

### PWA Best Practices:
- Service Worker must cache all essential assets
- App must work completely offline after first load
- Manifest must include proper icons and theme colors
- Support installation on home screen

## 📱 Progressive Web App Implementation

Alpine Beats uses a **unique inline PWA approach** where all PWA assets are generated dynamically at runtime:

### Dynamic Icon Generation
```javascript
// SVG drum icon as data URL
const svgIcon = `data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 192 192'%3E%3Crect width='192' height='192' fill='%231a1a1a'/%3E%3Ctext x='96' y='96' text-anchor='middle' dominant-baseline='middle' font-size='120' fill='%234ecdc4'%3E🥁%3C/text%3E%3C/svg%3E`;

// Convert to PNG at runtime for better compatibility
function svgToPng(svgDataUrl, size) {
    return new Promise((resolve, reject) => {
        const img = new Image();
        img.onload = function() {
            const canvas = document.createElement('canvas');
            canvas.width = size;
            canvas.height = size;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(img, 0, 0, size, size);
            resolve(canvas.toDataURL('image/png'));
        };
        img.src = svgDataUrl;
    });
}
```

### Dynamic Manifest
```javascript
const manifest = {
    name: 'Alpine Beats',
    short_name: 'Alpine Beats',
    description: 'Create awesome beats with an Alesis SR-16 inspired drum machine',
    display: 'standalone',
    theme_color: '#1a1a1a',
    background_color: '#1a1a1a',
    start_url: window.location.href,
    scope: window.location.origin + window.location.pathname,
    icons: [{ src: pngDataUrl, sizes: '192x192', type: 'image/png', purpose: 'any maskable' }]
};

// Set manifest as data URL
const b64manifest = btoa(JSON.stringify(manifest));
const link = document.createElement('link');
link.rel = 'manifest';
link.href = "data:application/json;base64," + b64manifest;
document.head.appendChild(link);
```

### Inline Service Worker
```javascript
// Service Worker code as string
const swCode = `
    const CACHE_NAME = 'alpine-beats-v2';
    const urlsToCache = [
        '/',
        'https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js'
    ];
    // ... install, fetch, activate handlers
`;

// Register from Blob URL
const blob = new Blob([swCode], { type: 'application/javascript' });
const swUrl = URL.createObjectURL(blob);
navigator.serviceWorker.register(swUrl);
```

### iOS Startup Image
```javascript
function createStartupImage(bgColor) {
    const canvas = document.createElement('canvas');
    canvas.width = window.screen.width * window.devicePixelRatio;
    canvas.height = window.screen.height * window.devicePixelRatio;
    const ctx = canvas.getContext('2d');
    
    ctx.fillStyle = bgColor;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Draw drum emoji in center
    ctx.font = `${canvas.width * 0.2}px Arial`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillStyle = '#4ecdc4';
    ctx.fillText('🥁', canvas.width / 2, canvas.height / 2);
    
    return canvas.toDataURL('image/png');
}
```

**Why This Approach:**
- ✅ **True single-file distribution**: No need to deploy multiple files
- ✅ **Works on any static host**: GitHub Pages, Netlify, S3, local file system
- ✅ **No build process**: Pure runtime generation
- ✅ **Full PWA features**: Installable, offline, startup images
- ✅ **Cross-platform**: Works on iOS, Android, desktop

---

## 🏗️ Role-Based Development Methodology

This project uses a professional role-based development approach with five specialized roles that collaborate to create exceptional Alpine.js applications. Each role has specific expertise and responsibilities for Alpine Beats development.

### **🎯 Product-Owner Role**
**Focus**: User experience, feature prioritization, musical workflow
**Key Responsibilities**: Defines drum machine features, user stories for musicians, success criteria for beat creation
**Expertise**: Music production workflows, user experience for musicians, creative tool design

**Alpine Beats Context**: 
- Understands drummer workflows and pattern programming
- Prioritizes features that enhance creative expression
- Ensures the interface supports rapid beat creation
- Defines success metrics (beats per minute created, learning curve, creative potential)

### **🏗️ Architect Role** 
**Focus**: Audio architecture, timing precision, performance optimization
**Key Responsibilities**: Web Audio API architecture, sequencer timing strategy, memory management
**Expertise**: Web Audio API, real-time audio systems, performance optimization, browser compatibility

**Alpine Beats Context**:
- Designs audio synthesis architecture for realistic drum sounds
- Ensures precise timing for the sequencer (no jitter or latency)
- Optimizes memory usage for continuous audio playback
- Plans for future features (recording, export, MIDI support)

### **🎨 Designer Role**
**Focus**: Interface design, visual feedback, accessibility
**Key Responsibilities**: Sequencer grid layout, visual feedback for active steps, mobile touch optimization
**Expertise**: Music software UI/UX, visual rhythm representation, accessibility for musicians

**Alpine Beats Context**:
- Creates intuitive grid-based sequencer interface
- Designs clear visual feedback for active steps and playback position
- Ensures touch targets are appropriate for finger tapping on mobile
- Maintains visual hierarchy (controls, tracks, steps)

### **💻 Developer Role**
**Focus**: Alpine.js implementation, audio synthesis, sequencer logic
**Key Responsibilities**: Implementing Web Audio API sounds, sequencer timing, state management
**Expertise**: Alpine.js reactive patterns, Web Audio API, JavaScript timing, PWA implementation

**Alpine Beats Context**:
- Implements drum sound synthesis using Web Audio API
- Creates precise sequencer timing using setTimeout
- Manages Alpine.js state for tracks, steps, and playback
- Ensures PWA works offline with Service Worker

### **🧪 QA-Engineer Role**
**Focus**: Audio quality, timing accuracy, cross-browser compatibility
**Key Responsibilities**: Testing audio synthesis quality, timing precision, mobile performance
**Expertise**: Audio quality testing, timing measurement, browser compatibility, mobile testing

**Alpine Beats Context**:
- Validates audio synthesis sounds realistic across browsers
- Measures sequencer timing accuracy (must be within 1-2ms)
- Tests touch interactions on various mobile devices
- Ensures PWA installation works on iOS and Android

## 🔄 Role Collaboration Patterns

### **Multi-Role Response Pattern**
When users request drum machine features, respond as multiple roles:

```markdown
**🎯 Product-Owner Analysis**: 
[Musical workflow value, user story, acceptance criteria for beat creation]

**🏗️ Architect Blueprint**: 
[Audio architecture approach, timing strategy, Web Audio API patterns]

**🎨 Designer Specifications**: 
[UI/UX for new feature, visual feedback, mobile considerations]

**💻 Developer Implementation**: 
[Complete Alpine.js and Web Audio API code with best practices]

**🧪 QA-Engineer Validation**: 
[Audio quality testing, timing validation, cross-browser checklist]
```

### **Role Detection Keywords**
- **Product-Owner**: "feature", "workflow", "musician needs", "user story", "beat creation"
- **Architect**: "audio architecture", "timing", "performance", "Web Audio API", "sequencer design"
- **Designer**: "UI", "grid", "visual feedback", "mobile", "touch", "accessibility"
- **Developer**: "implement", "Alpine.js", "code", "synthesis", "sequencer logic"
- **QA-Engineer**: "test", "audio quality", "timing accuracy", "mobile testing", "browser compatibility"

## 💡 Common Alpine Beats Development Patterns

### **Adding New Drum Sound Pattern**
1. **Product-Owner**: Define what drum sound is needed and why (user value)
2. **Architect**: Design Web Audio API synthesis approach (oscillators, filters, envelopes)
3. **Designer**: Specify track label, emoji icon, visual identity
4. **Developer**: Implement sound synthesis function and integrate into tracks array
5. **QA-Engineer**: Validate sound quality, mixing balance, browser compatibility

**Implementation Steps:**
```javascript
// 1. Add track to tracks array in drumMachine()
tracks: [
    // ... existing tracks
    { name: 'Cowbell', icon: '🔔', steps: Array(16).fill(false), sound: null }
],

// 2. Add sound assignment in generateDrumSounds()
this.tracks[8].sound = () => this.playCowbell();

// 3. Implement sound synthesis function
playCowbell() {
    const now = this.audioContext.currentTime;
    const osc1 = this.audioContext.createOscillator();
    const osc2 = this.audioContext.createOscillator();
    const gain = this.audioContext.createGain();
    
    osc1.frequency.value = 540;
    osc2.frequency.value = 800;
    
    gain.gain.setValueAtTime(0.5, now);
    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
    
    osc1.connect(gain);
    osc2.connect(gain);
    gain.connect(this.audioContext.destination);
    
    osc1.start(now);
    osc2.start(now);
    osc1.stop(now + 0.3);
    osc2.stop(now + 0.3);
}
```

### **Sequencer Enhancement Pattern**
1. **Product-Owner**: Define sequencer feature (swing, sub-steps, pattern length)
2. **Architect**: Design timing calculation changes, state management impact
3. **Designer**: Design UI controls and visual representation
4. **Developer**: Implement timing logic and Alpine.js state updates
5. **QA-Engineer**: Validate timing precision, edge cases, mobile performance

### **Audio Effect Pattern**
1. **Product-Owner**: Define effect value (reverb, filter, distortion)
2. **Architect**: Design Web Audio API effect chain architecture
3. **Designer**: Design control interface (knobs, sliders, presets)
4. **Developer**: Implement audio nodes, connections, parameter controls
5. **QA-Engineer**: Test effect quality, parameter ranges, CPU usage

### **Mobile Optimization Pattern**
1. **Product-Owner**: Define mobile use cases and priorities
2. **Architect**: Plan touch event handling, performance requirements
3. **Designer**: Optimize layout for small screens, larger touch targets
4. **Developer**: Implement touch events, responsive CSS, mobile-specific features
5. **QA-Engineer**: Test on various mobile devices, validate touch responsiveness

**Current Mobile Implementation:**
```css
/* Desktop: Show full track names */
.track-name { display: inline; }
.track-icon { display: none; }

/* Mobile (≤768px): Show emoji icons only */
@media (max-width: 768px) {
    .track-name { display: none; }
    .track-icon { display: inline; }
    
    .track-label {
        width: 50px;
        font-size: 1.2em;
        padding: 6px;
    }
}
```

**Mobile-Friendly Features:**
- Track labels reduced to 50px width showing emoji only
- Step pads are 32x32px with touch-friendly spacing
- Click-based interactions (no hover required)
- Responsive controls wrap on small screens
- Larger font sizes for readability

## 🔄 Application Lifecycle and Flow

### Initialization Sequence (on page load)
1. **HTML/CSS Loaded**: Page structure and styles rendered
2. **PWA Setup Executes**: 
   - SVG icon converted to PNG
   - Manifest generated with icons
   - Service Worker registered from Blob URL
   - iOS startup image created
3. **Alpine.js Loads**: CDN script loads and initializes
4. **drumMachine() init()**:
   - Web Audio Context created
   - `generateDrumSounds()` assigns sound functions to tracks
   - `loadDemoPattern()` sets up kick, snare, hi-hat pattern
5. **Ready**: User can interact with the sequencer

### User Interaction Flows

**Creating a Beat:**
1. User clicks track label → `previewSound(trackIndex)` plays sound
2. User clicks step pad → `toggleStep(trackIndex, stepIndex)` toggles step on/off
3. Active steps get `.active` class and cyan highlight
4. Repeat to build pattern across all 16 steps and 8 tracks

**Playing the Sequencer:**
1. User clicks Play button → `togglePlay()` → `play()`
2. `play()` sets `isPlaying = true`, resets `currentStep = -1`, calls `step()`
3. `step()` function:
   - Increments `currentStep` (0-15 in a loop)
   - Checks each track's current step
   - If step is active AND track has sound, plays sound via `track.sound()`
   - Calculates next step timing: `(60 / tempo) * 1000 / 4` milliseconds (16th notes)
   - Schedules itself again via `setTimeout()`
4. Visual feedback: `.current` class highlights playback position
5. Loop continues until user clicks Stop

**Adjusting Tempo:**
1. User moves tempo slider → `@input` triggers `updateTempo()`
2. `tempo` value updates reactively (Alpine.js x-model)
3. Next `step()` call uses new tempo for scheduling
4. No interruption to playback - change is smooth

**Clearing Pattern:**
1. User clicks Clear button → `clear()`
2. All tracks' steps reset to `false`
3. Sequencer stops via `stop()`
4. Visual: All active step highlights removed

### Audio Timing Precision

**Why setTimeout Instead of setInterval:**
```javascript
// ❌ setInterval can drift and accumulate timing errors
setInterval(() => this.step(), stepDuration); // BAD

// ✅ setTimeout recalculates each step for precise timing
const stepDuration = (60 / this.tempo) * 1000 / 4;
this.intervalId = setTimeout(() => this.step(), stepDuration); // GOOD
```

**Tempo Calculation:**
- 60 seconds / tempo = seconds per beat
- × 1000 = milliseconds per beat
- ÷ 4 = milliseconds per 16th note (because 16 steps = 4 beats = 16 16th notes)
- Example: 120 BPM → (60/120) × 1000 ÷ 4 = 125ms per step

**Audio Scheduling:**
```javascript
const now = this.audioContext.currentTime; // High-precision audio timeline
osc.start(now); // Start immediately
osc.stop(now + 0.5); // Stop 500ms later
```
- Uses `audioContext.currentTime` (not `Date.now()`) for sub-millisecond precision
- Schedules all events relative to audio clock, not JavaScript clock
- Prevents drift and jitter

## ✅ Success Criteria

### **Technical Excellence**
- Single HTML file architecture (no build process required)
- All drum sounds synthesized via Web Audio API (no audio files)
- Sequencer timing precision within 1-2ms accuracy
- Works completely offline via Service Worker
- Responsive design from 320px to 4K displays
- Smooth 60fps UI during sequencer playback
- Fast load time (<1 second on average connection)

### **Audio Quality**
- Realistic drum sounds with natural decay envelopes
- No audio clicks, pops, or artifacts
- Consistent volume across all drum sounds
- Clean mixing when multiple drums play simultaneously
- Works across all modern browsers (Chrome, Firefox, Safari, Edge)

### **Role Collaboration Quality**
- Each role provides domain-specific expertise
- Audio architecture decisions are technically sound
- Musical workflow is intuitive for users
- Implementation follows Alpine.js best practices
- Testing covers audio quality and timing accuracy

### **Musical Functionality**
- Easy to create beats quickly (intuitive workflow)
- Visual feedback clearly shows active steps and playback position
- Tempo adjustment is smooth and immediate
- Sound preview on hover helps with pattern creation
- Demo pattern loads to teach basic usage

---

## 🚀 Getting Started with Alpine Beats Development

When users request Alpine Beats enhancements or ask development questions:

1. **Analyze the request** - Determine which roles are most relevant
2. **Consider audio implications** - Web Audio API changes require careful planning
3. **Adopt role perspective(s)** - Respond with appropriate role expertise
4. **Provide working code** - Include complete, testable implementations
5. **Validate timing** - Ensure any sequencer changes maintain timing precision

### Testing the Application Locally

**Option 1: Python HTTP Server**
```bash
cd /path/to/alpine-beats
python3 -m http.server 8000
# Open http://localhost:8000 in browser
```

**Option 2: Node.js serve**
```bash
npx serve
# Opens automatically in browser
```

**Option 3: PHP Server**
```bash
php -S localhost:8000
```

**Option 4: Direct File**
- Simply open index.html in browser
- PWA features require HTTP/HTTPS (won't work with file://)

## 🔧 Troubleshooting Common Issues

### No Sound on Safari
**Problem**: Safari requires user interaction before audio can play
**Solution**: Already handled - audio context created on page load, sounds play on user clicks

### Service Worker Not Registering
**Problem**: Service Workers require HTTPS or localhost
**Solution**: Test on localhost or deploy to HTTPS host (GitHub Pages works)

### Timing Drift After Long Sessions
**Problem**: Accumulated timing errors from tempo changes
**Solution**: Already handled - each `step()` recalculates timing from current tempo

### Mobile Layout Issues
**Problem**: Track labels too wide on small screens
**Solution**: Already handled - responsive CSS shows emoji icons only on ≤768px

### Memory Leaks from Oscillators
**Problem**: Forgetting to call `osc.stop()` causes memory leaks
**Solution**: All sound functions properly call `stop()` after duration

### Exponential Ramp Errors
**Problem**: `exponentialRampToValueAtTime(0, ...)` throws error (can't ramp to zero)
**Solution**: Use 0.01 instead: `exponentialRampToValueAtTime(0.01, ...)`

### PWA Not Installing
**Problem**: Missing manifest icons or service worker errors
**Solution**: Already handled - dynamic generation with proper MIME types and sizes

### Alpine.js Not Initializing
**Problem**: CDN blocked or timing issues
**Solution**: Use `defer` attribute on Alpine.js script tag (already implemented)

### Common Development Scenarios

**Adding a New Drum Sound (e.g., Cowbell):**
1. **Architect**: Design synthesis (two oscillators at 540Hz and 800Hz with short decay)
2. **Designer**: Choose emoji icon (🔔) and ensure it fits visual style
3. **Developer**: 
   - Add track to array: `{ name: 'Cowbell', icon: '🔔', steps: Array(16).fill(false), sound: null }`
   - Assign in generateDrumSounds(): `this.tracks[8].sound = () => this.playCowbell()`
   - Implement `playCowbell()` function
4. **QA**: Test across browsers, verify it mixes well with other drums

**Adding Swing to Sequencer:**
1. **Product-Owner**: Define swing value (shuffle feel, 50-75% range)
2. **Architect**: Design timing modification (even steps delayed by swing percentage)
3. **Designer**: Design swing control slider
4. **Developer**:
   - Add `swing: 50` to state
   - Modify step timing: `const delay = (stepIndex % 2 === 1) ? (stepDuration * this.swing / 100) : 0`
   - Add UI control
5. **QA**: Validate timing precision with different swing values

**Adding Pattern Save/Load:**
1. **Product-Owner**: Define use case (save patterns to localStorage, share via URL)
2. **Architect**: Design state serialization (JSON format of track steps)
3. **Designer**: Design save/load UI (buttons, pattern list)
4. **Developer**:
   - Implement `savePattern()`: `localStorage.setItem('pattern-' + name, JSON.stringify(pattern))`
   - Implement `loadPattern()`: restore steps from JSON
   - Add UI controls
5. **QA**: Test save/load, browser compatibility, storage limits

**Adding Audio Effect (e.g., Reverb):**
1. **Product-Owner**: Define effect value (adds space/depth to drums)
2. **Architect**: Design ConvolverNode approach or simple delay-based reverb
3. **Designer**: Design reverb control (slider for wet/dry mix)
4. **Developer**:
   - Create master effect chain
   - Add ConvolverNode or delay network
   - Connect all sounds through effect chain
   - Add UI control
5. **QA**: Test CPU usage, effect quality, mobile performance

**Improving Mobile Touch Response:**
1. **Designer**: Analyze current 32x32px step pads, consider increasing to 40x40px
2. **Developer**: 
   - Update `.step` height and max-width in CSS
   - Test touch targets on actual devices
   - Consider adding touch feedback animation
3. **QA**: Test on iOS, Android, tablets, various screen sizes

## 🎨 Visual Design and Styling

### Color Palette
```css
/* Background */
body background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
container background: #2a2a2a;

/* Primary Colors */
--cyan: #4ecdc4;      /* Track labels, text accents */
--purple: #667eea;    /* Buttons, active steps */
--pink: #f5576c;      /* Current step indicator */
--red: #ff6b6b;       /* Heading gradient start */

/* UI Elements */
--dark-bg: #1a1a1a;   /* Track labels, steps */
--border: #333;       /* Step borders */
--text: #fff;         /* Main text */
--text-dim: #888;     /* Subtitle, labels */
```

### Button Gradient Patterns
```css
/* Main controls */
button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

/* Playing state */
button.playing {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

/* Heading */
h1 {
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
```

### Step Pad States
```css
/* Normal state */
.step {
    background: #1a1a1a;
    border: 2px solid #333;
}

/* Active (programmed) step */
.step.active {
    background: #667eea;
    border-color: #667eea;
    box-shadow: 0 0 10px rgba(102, 126, 234, 0.6);
}

/* Current playback position */
.step.current {
    border-color: #f5576c;
    box-shadow: inset 0 0 0 1px #f5576c;
}

/* Active step at current position */
.step.current.active {
    box-shadow: 0 0 15px rgba(245, 87, 108, 0.8), 
                inset 0 0 0 1px #f5576c;
}
```

### Responsive Typography
```css
/* Desktop */
h1 { font-size: 2.5em; }
button { padding: 12px 24px; font-size: 1em; }
.track-label { font-size: 0.75em; }

/* Mobile (≤768px) */
h1 { font-size: 1.8em; }
button { padding: 10px 20px; font-size: 0.9em; }
.track-label { font-size: 1.2em; } /* Larger for emoji */
```

## 🎵 Alpine Beats Best Practices

### Code Organization
- Keep audio synthesis functions separate and well-named
- Use clear variable names for audio nodes (`osc`, `gain`, `filter`, `bandpass`)
- Comment complex Web Audio API chains
- Group related functionality (synthesis, sequencer, UI)
- Each drum sound should be its own function (e.g., `playKick()`, `playSnare()`)

### Alpine.js Patterns
- Use computed properties for derived state (filteredTracks, activeSteps)
- Keep methods focused and single-purpose
- Initialize audio context only once in `init()`
- Clean up timers and audio nodes properly

### Audio Development
- Always test with headphones for quality assessment
- Use exponential ramps for natural sound envelopes
- Stop oscillators to prevent memory leaks
- Schedule audio events using `audioContext.currentTime`

### Testing Strategy
- Test timing accuracy by recording output and measuring
- Validate audio quality on different devices and browsers
- Test touch interactions on actual mobile devices
- Verify PWA installation and offline functionality

---

This role-based approach ensures Alpine Beats development maintains high standards for both technical implementation and musical functionality, creating an exceptional web-based drum machine that musicians will love to use.

*Use these instructions to provide expert-level Alpine.js development assistance for the Alpine Beats drum machine, combining audio engineering excellence with proven software development methodology.*
