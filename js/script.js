/**
 * Jincheon Chopyeong Book Village - Exhibition Guide Interaction
 * Features: Web Speech API TTS, Bilingual Toggle, Font Scaling, Keyboard Nav
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Language Toggle
  const langToggleBtn = document.getElementById('langToggleBtn');
  const currentLang = localStorage.getItem('chopyeong_guide_lang') || 'en';
  
  function applyLanguage(lang) {
    if (lang === 'ko') {
      document.body.classList.add('show-korean');
      if (langToggleBtn) {
        langToggleBtn.textContent = 'EN English';
        langToggleBtn.setAttribute('title', 'Switch to English');
      }
    } else {
      document.body.classList.remove('show-korean');
      if (langToggleBtn) {
        langToggleBtn.textContent = 'KO 한국어';
        langToggleBtn.setAttribute('title', '한국어 원문 보기');
      }
    }
    localStorage.setItem('chopyeong_guide_lang', lang);
  }

  if (langToggleBtn) {
    applyLanguage(currentLang);
    langToggleBtn.addEventListener('click', () => {
      const isKo = document.body.classList.contains('show-korean');
      applyLanguage(isKo ? 'en' : 'ko');
      // If TTS is playing when toggling, stop speech
      stopSpeech();
    });
  }

  // 2. Font Size Scaling
  const fontToggleBtn = document.getElementById('fontToggleBtn');
  const savedFontSize = localStorage.getItem('chopyeong_guide_font') || 'default';
  
  if (savedFontSize === 'large') {
    document.body.classList.add('font-large');
    if (fontToggleBtn) fontToggleBtn.classList.add('active');
  }

  if (fontToggleBtn) {
    fontToggleBtn.addEventListener('click', () => {
      const isLarge = document.body.classList.toggle('font-large');
      fontToggleBtn.classList.toggle('active', isLarge);
      localStorage.setItem('chopyeong_guide_font', isLarge ? 'large' : 'default');
    });
  }

  // 3. Audio Guide (TTS using Web Speech API)
  const audioGuideBtn = document.getElementById('audioGuideBtn');
  let synth = window.speechSynthesis;
  let isSpeaking = false;
  let currentUtterance = null;

  function stopSpeech() {
    if (synth && synth.speaking) {
      synth.cancel();
    }
    isSpeaking = false;
    if (audioGuideBtn) {
      audioGuideBtn.classList.remove('playing');
      audioGuideBtn.innerHTML = `
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
        <span>Audio Guide</span>
      `;
    }
  }

  function playSpeech() {
    if (!synth) {
      alert('Your browser does not support audio speech synthesis.');
      return;
    }

    // Determine current language text
    const isKoreanMode = document.body.classList.contains('show-korean');
    const targetContainer = isKoreanMode 
      ? document.querySelector('.lang-content-ko') 
      : document.querySelector('.lang-content-en');

    if (!targetContainer) return;

    // Extract text content cleanly
    const titleEl = document.querySelector('.exhibit-title');
    const titleText = titleEl ? titleEl.textContent.trim() : '';
    const bodyText = targetContainer.innerText.replace(/\n+/g, '. ');
    const fullText = `${titleText}. ${bodyText}`;

    synth.cancel(); // Stop any pending speech

    const utterance = new SpeechSynthesisUtterance(fullText);
    utterance.lang = isKoreanMode ? 'ko-KR' : 'en-US';
    utterance.rate = 0.95; // Calm, deliberate pace for exhibition
    utterance.pitch = 1.0;

    // Pick a natural English/Korean voice if available
    const voices = synth.getVoices();
    if (isKoreanMode) {
      const koVoice = voices.find(v => v.lang.startsWith('ko'));
      if (koVoice) utterance.voice = koVoice;
    } else {
      const enVoice = voices.find(v => (v.name.includes('Google') || v.name.includes('Natural') || v.name.includes('Samantha') || v.name.includes('Daniel') || v.name.includes('David')) && v.lang.startsWith('en'));
      if (enVoice) utterance.voice = enVoice;
    }

    utterance.onend = () => {
      stopSpeech();
    };

    utterance.onerror = () => {
      stopSpeech();
    };

    currentUtterance = utterance;
    synth.speak(utterance);
    isSpeaking = true;

    if (audioGuideBtn) {
      audioGuideBtn.classList.add('playing');
      audioGuideBtn.innerHTML = `
        <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>
        <span>Pause Audio</span>
      `;
    }
  }

  if (audioGuideBtn) {
    audioGuideBtn.addEventListener('click', () => {
      if (isSpeaking) {
        stopSpeech();
      } else {
        playSpeech();
      }
    });

    // Handle voice list async loading in Chrome
    if (speechSynthesis.onvoiceschanged !== undefined) {
      speechSynthesis.onvoiceschanged = () => {};
    }
  }

  // Stop speech on page unload
  window.addEventListener('beforeunload', () => {
    stopSpeech();
  });

  // 4. Keyboard Shortcuts for Navigation
  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') {
      const prevBtn = document.querySelector('.nav-link-btn.prev-btn:not(.disabled)');
      if (prevBtn) prevBtn.click();
    } else if (e.key === 'ArrowRight') {
      const nextBtn = document.querySelector('.nav-link-btn.next-btn:not(.disabled)');
      if (nextBtn) nextBtn.click();
    } else if (e.key === 'Escape') {
      stopSpeech();
      const homeBtn = document.querySelector('.nav-link-btn.home-btn');
      if (homeBtn) homeBtn.click();
    }
  });
});
