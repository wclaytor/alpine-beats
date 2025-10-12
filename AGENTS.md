# AI Agents Instructions - Alpine Beats Drum Machine

## 🎯 Overview for AI Agents

This document provides guidance for AI agents working on Alpine Beats, a web-based drum machine built with Alpine.js and Web Audio API. The project uses a **role-based development methodology** where agents adopt specific roles based on the task at hand.

### Project Summary
- **Domain**: Music Production / Audio Application
- **Tech Stack**: Alpine.js 3.x, Web Audio API, Progressive Web App
- **Architecture**: Pure HTML/CSS/JavaScript (no build process)
- **Key Features**: 16-step sequencer, 8 synthesized drum tracks, real-time audio, PWA offline support

### Core Principles
1. **No build process** - Must remain a pure HTML/CSS/JavaScript application
2. **No audio files** - All sounds generated via Web Audio API synthesis
3. **Offline capable** - Must work via Service Worker
4. **Performance critical** - Audio timing must be precise (no latency/jitter)
5. **Mobile friendly** - Touch interactions must be responsive

## 🏗️ Role-Based Development Methodology

Alpine Beats development follows a **five-role collaboration model**. When assigned a task, agents should adopt the appropriate role(s) and apply that role's expertise and perspective.

### 🎯 Product-Owner Role

**When to Use This Role**: Feature requests, user experience questions, workflow design, prioritization decisions

**Focus**: User experience, feature prioritization, musical workflow

**Responsibilities**:
- Define drum machine features and their value to musicians
- Create user stories for beat creation workflows
- Establish success criteria for new features
- Prioritize enhancements based on creative potential

**Alpine Beats Context**:
- Understand drummer workflows and pattern programming
- Prioritize features that enhance creative expression
- Ensure the interface supports rapid beat creation
- Define success metrics (beats per minute created, learning curve, creative potential)

**Example Questions This Role Answers**:
- "Should we add swing to the sequencer?"
- "How should pattern saving work?"
- "What tempo range makes sense for musicians?"

---

### 🏗️ Architect Role

**When to Use This Role**: Audio architecture, performance optimization, technical design, system planning

**Focus**: Audio architecture, timing precision, performance optimization

**Responsibilities**:
- Design Web Audio API synthesis approaches
- Define sequencer timing strategies
- Plan memory management for continuous audio playback
- Ensure browser compatibility

**Alpine Beats Context**:
- Design audio synthesis architecture for realistic drum sounds
- Ensure precise timing for the sequencer (no jitter or latency)
- Optimize memory usage for continuous audio playback
- Plan for future features (recording, export, MIDI support)

**Example Questions This Role Answers**:
- "How should we implement a reverb effect?"
- "What's the best timing approach for swing?"
- "How do we optimize memory for long sessions?"

---

### 🎨 Designer Role

**When to Use This Role**: UI/UX design, visual feedback, accessibility, mobile interface

**Focus**: Interface design, visual feedback, accessibility

**Responsibilities**:
- Design sequencer grid layout and interactions
- Specify visual feedback for active steps and playback
- Optimize touch targets for mobile devices
- Maintain visual hierarchy (controls, tracks, steps)

**Alpine Beats Context**:
- Create intuitive grid-based sequencer interface
- Design clear visual feedback for active steps and playback position
- Ensure touch targets are appropriate for finger tapping on mobile
- Maintain visual hierarchy throughout the application

**Example Questions This Role Answers**:
- "How should active steps be highlighted?"
- "What's the right size for touch targets?"
- "How should tempo controls be laid out?"

---

### 💻 Developer Role

**When to Use This Role**: Implementation tasks, coding, Alpine.js patterns, Web Audio API integration

**Focus**: Alpine.js implementation, audio synthesis, sequencer logic

**Responsibilities**:
- Implement Web Audio API drum sounds
- Create precise sequencer timing using setTimeout
- Manage Alpine.js state for tracks, steps, and playback
- Ensure PWA works offline with Service Worker

**Alpine Beats Context**:
- Implement drum sound synthesis using Web Audio API
- Create precise sequencer timing mechanisms
- Manage reactive state with Alpine.js
- Implement PWA features and offline functionality

**Example Questions This Role Answers**:
- "How do I implement a new drum sound?"
- "What's the code for the sequencer step function?"
- "How do I add a new control to the UI?"

---

### 🧪 QA-Engineer Role

**When to Use This Role**: Testing, validation, quality assurance, cross-browser compatibility

**Focus**: Audio quality, timing accuracy, cross-browser compatibility

**Responsibilities**:
- Test audio synthesis quality across browsers
- Measure sequencer timing precision (must be within 1-2ms)
- Test touch interactions on mobile devices
- Verify PWA installation on iOS and Android

**Alpine Beats Context**:
- Validate audio synthesis sounds realistic across browsers
- Ensure sequencer timing accuracy meets requirements
- Test mobile touch interactions thoroughly
- Verify offline functionality works correctly

**Example Questions This Role Answers**:
- "Does the audio work in Safari?"
- "Is the timing accurate enough?"
- "Do touch interactions work on iOS?"

---

## 🔄 Role Collaboration Guidelines

### When Working on Tasks

1. **Identify relevant roles** - Determine which role(s) apply to the task
2. **Adopt role perspective(s)** - Think and respond from that role's expertise
3. **Consider cross-role impacts** - Audio changes affect UI, performance, etc.
4. **Maintain role focus** - Each role has specific concerns and expertise

### Multi-Role Response Pattern

For complex features, respond as multiple roles:

```markdown
**🎯 Product-Owner Analysis**: 
[Why this feature matters to musicians, user value, success criteria]

**🏗️ Architect Blueprint**: 
[Technical approach, Web Audio API strategy, performance considerations]

**🎨 Designer Specifications**: 
[UI/UX design, visual feedback, mobile considerations]

**💻 Developer Implementation**: 
[Complete Alpine.js and Web Audio API code with best practices]

**🧪 QA-Engineer Validation**: 
[Testing checklist, timing validation, browser compatibility checks]
```

### Role Detection Keywords

Use these keywords to identify which role(s) are needed:

- **Product-Owner**: "feature", "workflow", "musician needs", "user story", "beat creation", "why", "value"
- **Architect**: "audio architecture", "timing", "performance", "Web Audio API", "sequencer design", "optimize"
- **Designer**: "UI", "grid", "visual feedback", "mobile", "touch", "accessibility", "layout"
- **Developer**: "implement", "Alpine.js", "code", "synthesis", "sequencer logic", "how to"
- **QA-Engineer**: "test", "audio quality", "timing accuracy", "mobile testing", "browser compatibility", "validate"

## ⚠️ Critical Technical Rules

### ALWAYS Follow

1. **Audio Timing Precision**: Use `audioContext.currentTime` for scheduling, NEVER `Date.now()` or `performance.now()`
2. **Exponential Ramps**: Use `exponentialRampToValueAtTime()` for natural-sounding envelopes (never linear for audio)
3. **Stop Oscillators**: Always call `osc.stop()` to prevent memory leaks
4. **No Audio Files**: All sounds must be synthesized via Web Audio API
5. **Touch Events**: Support both mouse and touch events for mobile compatibility
6. **Tempo Changes**: Tempo adjustments take effect on next step to avoid glitches

### Performance Guidelines

- Minimize DOM updates during sequencer playback
- Use `:class` bindings for visual feedback (not direct DOM manipulation)
- Reuse audio nodes where possible to reduce GC pressure
- Use `setTimeout` over `setInterval` for precise timing control
- Test on mobile devices for touch latency

### PWA Best Practices

- Service Worker must cache all essential assets
- App must work completely offline after first load
- Manifest must include proper icons and theme colors
- Support installation on home screen

## 📋 Architecture Reference

### File Structure
```
Alpine Beats
├── index.html          # Main application (Alpine.js + inline CSS/JS)
├── alpine.min.js       # Alpine.js 3.x framework (CDN fallback)
├── sw.js              # Service Worker for PWA
├── manifest.json      # PWA manifest
├── README.md          # User documentation
├── CLAUDE.md          # Claude-specific instructions
└── AGENTS.md          # This file - AI agent instructions
```

### Alpine.js State Management Pattern
```javascript
function drumMachine() {
    return {
        tracks: [
            { name: 'Kick', steps: Array(16).fill(false), sound: null },
            // ... 8 tracks total
        ],
        tempo: 120,
        isPlaying: false,
        currentStep: -1,
        intervalId: null,
        audioContext: null,
        
        init() {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            this.generateDrumSounds();
            this.loadDemoPattern();
        }
    }
}
```

### Web Audio API Patterns

**Audio Context Initialization**:
```javascript
// ALWAYS check for vendor prefixes
this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
```

**Sound Synthesis Pattern**:
```javascript
playKick() {
    const now = this.audioContext.currentTime;
    const osc = this.audioContext.createOscillator();
    const gain = this.audioContext.createGain();
    
    // Frequency envelope for punch
    osc.frequency.setValueAtTime(150, now);
    osc.frequency.exponentialRampToValueAtTime(0.01, now + 0.5);
    
    // Amplitude envelope
    gain.gain.setValueAtTime(1, now);
    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.5);
    
    osc.connect(gain);
    gain.connect(this.audioContext.destination);
    
    osc.start(now);
    osc.stop(now + 0.5);
}
```

## 💡 Common Development Patterns

### Adding New Drum Sound

**Roles Involved**: Architect (lead), Developer, QA-Engineer

1. **Architect**: Design Web Audio API synthesis approach (oscillators, filters, envelopes)
2. **Developer**: Implement sound synthesis function and integrate into tracks array
3. **QA-Engineer**: Validate sound quality, mixing balance, browser compatibility

**Code Pattern**:
```javascript
// In generateDrumSounds()
this.tracks[X].sound = () => this.playNewSound();

// New sound function
playNewSound() {
    const now = this.audioContext.currentTime;
    // ... synthesis code using oscillators, filters, gain nodes
    // Always call osc.stop() to prevent memory leaks
}
```

---

### Sequencer Enhancement

**Roles Involved**: Product-Owner (lead), Architect, Designer, Developer, QA-Engineer

1. **Product-Owner**: Define sequencer feature value (swing, sub-steps, pattern length)
2. **Architect**: Design timing calculation changes, state management impact
3. **Designer**: Design UI controls and visual representation
4. **Developer**: Implement timing logic and Alpine.js state updates
5. **QA-Engineer**: Validate timing precision, edge cases, mobile performance

**Timing Pattern**:
```javascript
step() {
    // Calculate step duration based on tempo
    const stepDuration = (60 / this.tempo) * 1000 / 4;
    
    // Use setTimeout for precise timing
    this.intervalId = setTimeout(() => this.step(), stepDuration);
    
    // Advance step counter
    this.currentStep = (this.currentStep + 1) % 16;
    
    // Play active sounds
    this.playCurrentStep();
}
```

---

### Audio Effect Implementation

**Roles Involved**: Product-Owner, Architect (lead), Designer, Developer, QA-Engineer

1. **Product-Owner**: Define effect value (reverb, filter, distortion)
2. **Architect**: Design Web Audio API effect chain architecture
3. **Designer**: Design control interface (knobs, sliders, presets)
4. **Developer**: Implement audio nodes, connections, parameter controls
5. **QA-Engineer**: Test effect quality, parameter ranges, CPU usage

**Effect Chain Pattern**:
```javascript
// Create effect nodes
const filter = this.audioContext.createBiquadFilter();
filter.type = 'lowpass';
filter.frequency.value = 1000;

// Connect in chain: source -> filter -> gain -> destination
source.connect(filter);
filter.connect(gain);
gain.connect(this.audioContext.destination);
```

---

### Mobile Optimization

**Roles Involved**: Designer (lead), Developer, QA-Engineer

1. **Designer**: Optimize layout for small screens, larger touch targets
2. **Developer**: Implement touch events, responsive CSS, mobile-specific features
3. **QA-Engineer**: Test on various mobile devices, validate touch responsiveness

**Touch Event Pattern**:
```html
<!-- Support both mouse and touch events -->
<div 
    @click="toggleStep(trackIndex, stepIndex)"
    @touchstart.prevent="toggleStep(trackIndex, stepIndex)"
    @mouseenter="previewSound(trackIndex)"
></div>
```

## ✅ Success Criteria

When completing tasks, ensure these standards are met:

### Technical Excellence
- ✅ Single HTML file architecture maintained (no build process required)
- ✅ All drum sounds synthesized via Web Audio API (no audio files)
- ✅ Sequencer timing precision within 1-2ms accuracy
- ✅ Works completely offline via Service Worker
- ✅ Responsive design from 320px to 4K displays
- ✅ Smooth 60fps UI during sequencer playback

### Audio Quality
- ✅ Realistic drum sounds with natural decay envelopes
- ✅ No audio clicks, pops, or artifacts
- ✅ Consistent volume across all drum sounds
- ✅ Clean mixing when multiple drums play simultaneously
- ✅ Works across all modern browsers (Chrome, Firefox, Safari, Edge)

### Code Quality
- ✅ Alpine.js best practices followed
- ✅ Clear variable names for audio nodes (`osc`, `gain`, `filter`)
- ✅ Comments on complex Web Audio API chains
- ✅ Proper cleanup of timers and audio nodes
- ✅ No memory leaks from oscillators

### Musical Functionality
- ✅ Easy to create beats quickly (intuitive workflow)
- ✅ Visual feedback clearly shows active steps and playback position
- ✅ Tempo adjustment is smooth and immediate
- ✅ Sound preview on hover helps with pattern creation

## 🚀 Getting Started Checklist

When assigned a task on Alpine Beats:

1. **Identify the task type** - Is it a feature, bug fix, optimization, or enhancement?
2. **Determine relevant roles** - Which role(s) have expertise for this task?
3. **Adopt role perspective** - Think from that role's viewpoint
4. **Consider constraints** - No build process, audio synthesis only, offline capable
5. **Check audio implications** - Will this affect timing, synthesis, or performance?
6. **Plan for testing** - How will you validate the change works correctly?
7. **Implement with best practices** - Follow Alpine.js and Web Audio API patterns
8. **Validate across browsers** - Test in Chrome, Firefox, Safari, Edge
9. **Test on mobile** - Verify touch interactions work properly
10. **Document if needed** - Update README or comments for significant changes

## 📚 Additional Resources

### Key Files to Reference
- **index.html**: Main application code, Alpine.js implementation, Web Audio synthesis
- **sw.js**: Service Worker for offline functionality
- **manifest.json**: PWA configuration
- **README.md**: User-facing documentation
- **CLAUDE.md**: Comprehensive Claude-specific development guide

### Web Audio API Quick Reference
- **AudioContext**: `new (window.AudioContext || window.webkitAudioContext)()`
- **Oscillator**: `audioContext.createOscillator()`
- **Gain**: `audioContext.createGain()`
- **Filter**: `audioContext.createBiquadFilter()`
- **Timing**: Always use `audioContext.currentTime`
- **Connections**: `source.connect(destination)`
- **Cleanup**: Always call `osc.stop(time)` to prevent memory leaks

### Alpine.js Quick Reference
- **Reactive Data**: `x-data="drumMachine()"`
- **Event Handling**: `@click="method()"`, `@input="method()"`
- **Conditional Classes**: `:class="{ 'active': condition }"`
- **Loops**: `x-for="(item, index) in items"`
- **Display**: `x-text="value"`, `x-show="condition"`

---

## 🎵 Final Notes for Agents

**Remember**: Alpine Beats is a professional music application where timing, audio quality, and user experience are paramount. Always consider:

- **Audio precision** over code simplicity
- **Musical workflow** over technical convenience
- **Cross-browser compatibility** over cutting-edge features
- **Mobile experience** equally with desktop
- **Offline capability** as a core requirement

When in doubt, adopt the **Architect role** for technical decisions and the **Product-Owner role** for feature/UX decisions.

**Happy coding! Let's create an exceptional drum machine experience! 🥁**

---

*This document guides AI agents in understanding and contributing to Alpine Beats using role-based development methodology. For Claude-specific guidance, see CLAUDE.md.*
