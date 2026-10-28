/**
 * 진천 초평책마을 완위각 QR 웹페이지 공통 스크립트
 * 모바일 최적화 및 이미지 라이트박스(확대 보기) 기능
 */
document.addEventListener('DOMContentLoaded', () => {
  // 라이트박스 모달 동적 생성
  const modal = document.createElement('div');
  modal.className = 'image-modal';
  modal.id = 'imageModal';
  modal.setAttribute('role', 'dialog');
  modal.setAttribute('aria-modal', 'true');
  modal.innerHTML = `
    <button class="image-modal-close" aria-label="닫기">&times;</button>
    <img class="image-modal-content" id="modalImg" alt="확대 이미지" />
  `;
  document.body.appendChild(modal);

  const modalImg = document.getElementById('modalImg');
  const closeBtn = modal.querySelector('.image-modal-close');

  const openModal = (src, alt) => {
    modalImg.src = src;
    modalImg.alt = alt || '확대 이미지';
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  const closeModal = () => {
    modal.classList.remove('active');
    document.body.style.overflow = '';
    setTimeout(() => {
      modalImg.src = '';
    }, 250);
  };

  // 줌 가능한 이미지 클릭/터치 이벤트 리스너
  document.querySelectorAll('.zoomable-img').forEach(img => {
    img.addEventListener('click', () => {
      // 고화질 원본 우선, 없으면 현재 src
      const fullSrc = img.getAttribute('data-full') || img.currentSrc || img.src;
      openModal(fullSrc, img.alt);
    });
  });

  // 닫기 이벤트들
  closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal || e.target === modalImg) {
      closeModal();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeModal();
    }
  });
});
