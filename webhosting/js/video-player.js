/**
 * YouTube 스타일 비디오 플레이어 스크립트 (재생 기능 전용)
 */

document.addEventListener('DOMContentLoaded', () => {
  const playerWrapper = document.getElementById('playerWrapper');
  const video = document.getElementById('mainVideo');
  const bigCenterPlay = document.getElementById('bigCenterPlay');
  const playPauseBtn = document.getElementById('playPauseBtn');
  const playIcon = document.getElementById('playIcon');
  const pauseIcon = document.getElementById('pauseIcon');
  const centerIndicator = document.getElementById('centerIndicator');
  const centerIcon = document.getElementById('centerIcon');
  
  const progressContainer = document.getElementById('progressContainer');
  const currentBar = document.getElementById('currentBar');
  const bufferBar = document.getElementById('bufferBar');
  const timeTooltip = document.getElementById('timeTooltip');
  const currentTimeEl = document.getElementById('currentTime');
  const durationTimeEl = document.getElementById('durationTime');

  const muteBtn = document.getElementById('muteBtn');
  const volumeHighIcon = document.getElementById('volumeHighIcon');
  const volumeMutedIcon = document.getElementById('volumeMutedIcon');
  const volumeGroup = document.querySelector('.volume-group');
  const volumeSliderContainer = document.querySelector('.volume-slider-container');
  const volumeSlider = document.getElementById('volumeSlider');

  const fullscreenBtn = document.getElementById('fullscreenBtn');
  const fsEnterIcon = document.getElementById('fsEnterIcon');
  const fsExitIcon = document.getElementById('fsExitIcon');

  const leftRipple = document.getElementById('leftRipple');
  const rightRipple = document.getElementById('rightRipple');
  const toastEl = document.getElementById('playerToast');

  let controlsTimeout = null;
  let isDraggingProgress = false;
  let lastTapTime = 0;
  let tapTimeout = null;

  // 1. 시간 포맷 함수 (mm:ss 또는 hh:mm:ss)
  function formatTime(seconds) {
    if (isNaN(seconds) || seconds < 0) return '0:00';
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds % 3600) / 60);
    const s = Math.floor(seconds % 60);

    const sStr = s < 10 ? `0${s}` : `${s}`;
    if (h > 0) {
      const mStr = m < 10 ? `0${m}` : `${m}`;
      return `${h}:${mStr}:${sStr}`;
    }
    return `${m}:${sStr}`;
  }

  // 2. 토스트 알림
  function showToast(text, duration = 1500) {
    if (!toastEl) return;
    toastEl.textContent = text;
    toastEl.classList.add('show');
    clearTimeout(toastEl._timer);
    toastEl._timer = setTimeout(() => {
      toastEl.classList.remove('show');
    }, duration);
  }

  // 3. 중앙 재생/일시정지 리플 인디케이터
  function triggerCenterIndicator(type) {
    if (!centerIndicator || !centerIcon) return;
    if (type === 'play') {
      centerIcon.innerHTML = '<path d="M8 5v14l11-7z"></path>';
    } else {
      centerIcon.innerHTML = '<rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect>';
    }
    centerIndicator.classList.remove('animate');
    void centerIndicator.offsetWidth;
    centerIndicator.classList.add('animate');
    setTimeout(() => {
      centerIndicator.classList.remove('animate');
    }, 350);
  }

  // 4. 재생 / 일시정지 (소리와 함께 정상 재생)
  function togglePlay() {
    if (video.paused || video.ended) {
      video.muted = false;
      if (video.volume === 0) {
        updateVolume(1);
      }
      video.play().catch(err => {
        console.log('Play interrupted, attempting fallback:', err);
        video.muted = true;
        video.play();
      });
    } else {
      video.pause();
    }
  }

  function updatePlayState() {
    if (video.paused) {
      playerWrapper.classList.remove('playing');
      playerWrapper.classList.add('paused');
      playIcon.style.display = 'block';
      pauseIcon.style.display = 'none';
      showControls();
    } else {
      playerWrapper.classList.add('playing');
      playerWrapper.classList.remove('paused');
      playIcon.style.display = 'none';
      pauseIcon.style.display = 'block';
      resetControlsTimeout();
    }
  }

  playPauseBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    togglePlay();
    triggerCenterIndicator(video.paused ? 'pause' : 'play');
  });

  if (bigCenterPlay) {
    bigCenterPlay.addEventListener('click', (e) => {
      e.stopPropagation();
      togglePlay();
    });
  }

  // 5. 비디오 상태 이벤트
  video.addEventListener('play', updatePlayState);
  video.addEventListener('pause', updatePlayState);
  video.addEventListener('waiting', () => playerWrapper.classList.add('loading'));
  video.addEventListener('canplay', () => playerWrapper.classList.remove('loading'));

  video.addEventListener('loadedmetadata', () => {
    durationTimeEl.textContent = formatTime(video.duration);
    currentTimeEl.textContent = formatTime(video.currentTime);
  });

  video.addEventListener('timeupdate', () => {
    if (!isDraggingProgress && video.duration) {
      const percent = (video.currentTime / video.duration) * 100;
      currentBar.style.width = `${percent}%`;
      currentTimeEl.textContent = formatTime(video.currentTime);
    }
  });

  video.addEventListener('progress', () => {
    if (video.duration > 0 && video.buffered.length > 0) {
      for (let i = 0; i < video.buffered.length; i++) {
        if (video.buffered.start(video.buffered.length - 1 - i) < video.currentTime) {
          const bufferEnd = video.buffered.end(video.buffered.length - 1 - i);
          const percent = (bufferEnd / video.duration) * 100;
          bufferBar.style.width = `${percent}%`;
          break;
        }
      }
    }
  });

  // 6. 타임라인 Seekbar
  function getProgressPercent(e) {
    const rect = progressContainer.getBoundingClientRect();
    const clientX = e.touches ? e.touches[0].clientX : e.clientX;
    let pos = (clientX - rect.left) / rect.width;
    return Math.min(Math.max(pos, 0), 1);
  }

  function seekToPosition(percent) {
    if (video.duration) {
      video.currentTime = percent * video.duration;
      currentBar.style.width = `${percent * 100}%`;
      currentTimeEl.textContent = formatTime(video.currentTime);
    }
  }

  progressContainer.addEventListener('mousedown', (e) => {
    isDraggingProgress = true;
    progressContainer.classList.add('dragging');
    seekToPosition(getProgressPercent(e));
  });

  progressContainer.addEventListener('mousemove', (e) => {
    const pos = getProgressPercent(e);
    if (video.duration) {
      timeTooltip.textContent = formatTime(pos * video.duration);
      timeTooltip.style.left = `${pos * 100}%`;
    }
    if (isDraggingProgress) {
      seekToPosition(pos);
    }
  });

  document.addEventListener('mouseup', () => {
    if (isDraggingProgress) {
      isDraggingProgress = false;
      progressContainer.classList.remove('dragging');
    }
  });

  progressContainer.addEventListener('touchstart', (e) => {
    isDraggingProgress = true;
    progressContainer.classList.add('dragging');
    seekToPosition(getProgressPercent(e));
  }, { passive: true });

  progressContainer.addEventListener('touchmove', (e) => {
    if (isDraggingProgress) {
      seekToPosition(getProgressPercent(e));
    }
  }, { passive: true });

  progressContainer.addEventListener('touchend', () => {
    isDraggingProgress = false;
    progressContainer.classList.remove('dragging');
  });

  // 7. 음량 및 음소거
  function updateVolume(val) {
    val = Math.max(0, Math.min(1, val));
    video.volume = val;
    video.muted = (val === 0);
    volumeSlider.value = val;

    // 볼륨 양에 맞춰 슬라이더 바 채움 비율(0% ~ 100%) 반영
    const percent = Math.round(val * 100);
    volumeSlider.style.setProperty('--volume-percent', `${percent}%`);

    if (video.muted || val === 0) {
      volumeHighIcon.style.display = 'none';
      volumeMutedIcon.style.display = 'block';
    } else {
      volumeHighIcon.style.display = 'block';
      volumeMutedIcon.style.display = 'none';
    }
  }

  volumeSlider.addEventListener('input', (e) => {
    updateVolume(parseFloat(e.target.value));
  });

  volumeSlider.addEventListener('change', (e) => {
    updateVolume(parseFloat(e.target.value));
  });

  // 유튜브 모바일 스타일 원클릭 음소거 토글
  function toggleMute() {
    if (video.muted || video.volume === 0) {
      video.muted = false;
      const targetVol = parseFloat(volumeSlider.value) > 0 ? parseFloat(volumeSlider.value) : 1;
      updateVolume(targetVol);
      showToast('🔊 소리 켬');
    } else {
      video.muted = true;
      updateVolume(0);
      showToast('🔇 음소거');
    }
  }

  muteBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    toggleMute();
  });

  // 모바일 터치 기기(아이폰/스마트폰) 감지 시 볼륨 슬라이더 즉시 완전 숨김 (유튜브 모바일 표준)
  function hideVolumeSliderOnMobile() {
    const isMobileDevice = ('ontouchstart' in window) || (navigator.maxTouchPoints > 0) || (window.innerWidth <= 820);
    if (isMobileDevice && volumeSliderContainer) {
      volumeSliderContainer.style.setProperty('display', 'none', 'important');
    }
  }
  hideVolumeSliderOnMobile();
  window.addEventListener('resize', hideVolumeSliderOnMobile);
  window.addEventListener('orientationchange', hideVolumeSliderOnMobile);

  // 초기 상태: 일시정지 상태 및 볼륨 100% 설정
  updatePlayState();
  video.muted = false;
  updateVolume(1);

  // 8. 전체화면
  function toggleFullscreen() {
    if (!document.fullscreenElement && !document.webkitFullscreenElement) {
      if (playerWrapper.requestFullscreen) {
        playerWrapper.requestFullscreen();
      } else if (playerWrapper.webkitRequestFullscreen) {
        playerWrapper.webkitRequestFullscreen();
      } else if (video.webkitEnterFullscreen) {
        video.webkitEnterFullscreen();
      }
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
      }
    }
  }

  fullscreenBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    toggleFullscreen();
  });

  function updateFullscreenIcons() {
    const isFs = !!(document.fullscreenElement || document.webkitFullscreenElement);
    fsEnterIcon.style.display = isFs ? 'none' : 'block';
    fsExitIcon.style.display = isFs ? 'block' : 'none';
  }

  document.addEventListener('fullscreenchange', updateFullscreenIcons);
  document.addEventListener('webkitfullscreenchange', updateFullscreenIcons);

  // 9. 화면 클릭 및 더블 탭 스킵
  function triggerSkipRipple(side) {
    const ripple = side === 'left' ? leftRipple : rightRipple;
    if (!ripple) return;
    ripple.classList.add('show');
    clearTimeout(ripple._timer);
    ripple._timer = setTimeout(() => ripple.classList.remove('show'), 400);
  }

  function skipTime(seconds) {
    video.currentTime = Math.min(Math.max(video.currentTime + seconds, 0), video.duration || 0);
    showToast(`${seconds > 0 ? '+' : ''}${seconds}초`);
  }

  const clickOverlay = document.getElementById('playerClickOverlay');
  clickOverlay.addEventListener('click', (e) => {
    const now = Date.now();
    const rect = clickOverlay.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    const isLeftHalf = clickX < rect.width / 2;

    if (now - lastTapTime < 300) {
      clearTimeout(tapTimeout);
      if (isLeftHalf) {
        skipTime(-10);
        triggerSkipRipple('left');
      } else {
        skipTime(10);
        triggerSkipRipple('right');
      }
      lastTapTime = 0;
    } else {
      lastTapTime = now;
      tapTimeout = setTimeout(() => {
        togglePlay();
        triggerCenterIndicator(video.paused ? 'pause' : 'play');
      }, 300);
    }
  });

  // 10. 컨트롤 바 2.5초 자동 숨김
  function showControls() {
    playerWrapper.classList.remove('hide-controls');
  }

  function resetControlsTimeout() {
    showControls();
    clearTimeout(controlsTimeout);
    if (!video.paused) {
      controlsTimeout = setTimeout(() => {
        if (!isDraggingProgress) {
          playerWrapper.classList.add('hide-controls');
        }
      }, 2500);
    }
  }

  playerWrapper.addEventListener('mousemove', resetControlsTimeout);
  playerWrapper.addEventListener('touchstart', resetControlsTimeout, { passive: true });
  playerWrapper.addEventListener('mouseleave', () => {
    if (!video.paused && !isDraggingProgress) {
      playerWrapper.classList.add('hide-controls');
    }
  });

  // 11. 유튜브 단축키
  document.addEventListener('keydown', (e) => {
    switch (e.key) {
      case ' ':
      case 'k':
      case 'K':
        e.preventDefault();
        togglePlay();
        triggerCenterIndicator(video.paused ? 'pause' : 'play');
        break;
      case 'j':
      case 'J':
        e.preventDefault();
        skipTime(-10);
        triggerSkipRipple('left');
        break;
      case 'l':
      case 'L':
        e.preventDefault();
        skipTime(10);
        triggerSkipRipple('right');
        break;
      case 'ArrowLeft':
        e.preventDefault();
        skipTime(-5);
        triggerSkipRipple('left');
        break;
      case 'ArrowRight':
        e.preventDefault();
        skipTime(5);
        triggerSkipRipple('right');
        break;
      case 'ArrowUp':
        e.preventDefault();
        const nextUpVol = Math.min((parseFloat(volumeSlider.value) || 0) + 0.05, 1);
        updateVolume(nextUpVol);
        showToast(`볼륨: ${Math.round(nextUpVol * 100)}%`);
        break;
      case 'ArrowDown':
        e.preventDefault();
        const nextDownVol = Math.max((parseFloat(volumeSlider.value) || 0) - 0.05, 0);
        updateVolume(nextDownVol);
        showToast(`볼륨: ${Math.round(nextDownVol * 100)}%`);
        break;
      case 'm':
      case 'M':
        e.preventDefault();
        muteBtn.click();
        break;
      case 'f':
      case 'F':
        e.preventDefault();
        toggleFullscreen();
        break;
      default:
        if (e.key >= '0' && e.key <= '9' && video.duration) {
          e.preventDefault();
          seekToPosition(parseInt(e.key, 10) * 0.1);
        }
        break;
    }
  });
});
