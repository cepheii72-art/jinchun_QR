# 진천 초평책마을 QR 전시 웹페이지

> **진천 초평책마을(완위각·담헌 이하곤 아카이브)** 전시장 관람객을 위한 모바일 최적화 반응형 QR 웹페이지 및 고성능 미디어 플레이어 프로젝트입니다.

---

## 📌 프로젝트 개요

* **프로젝트명**: 진천 초평책마을 QR 전시 웹 서비스
* **주관/디자인**: 꿈씨디자인 × 디지믹스 (Digimix)
* **목적**: 전시장 내 QR 코드를 관람객의 스마트폰으로 스캔하여 유물 해설, 전시 텍스트, 고화질 아카이브 이미지 및 메인 홍보 영상을 쾌적하게 열람
* **저장소**: [https://github.com/cepheii72-art/jinchun_QR](https://github.com/cepheii72-art/jinchun_QR)

---

## ✨ 주요 특징 및 기능

### 1. 모바일 퍼스트 반응형 전시 웹페이지 (`page1.html` ~ `page9.html`)
* **한국어/영어 병기 및 아카이브 뷰어**: 이하곤 선생의 생애, 완위각 장서, 두타초, 고문헌 해설 수록
* **노치 및 안전영역(Safe Area) 대응**: 최신 아이폰 및 안드로이드 기기의 상/하단 바 완벽 대응
* **웹폰트 최적화**: 전시장 인쇄물과의 통일성을 위한 KoPubWorld 돋움 WOFF2 경량 웹폰트 탑재

### 2. 프리미엄 골드 비디오 플레이어 (`video.html`)
* **완위각 앤틱 골드 테마 디자인**: 게슈탈트 시각 법칙(전경-배경 분리, 대칭성, 근접성)을 적용한 고급스러운 UI
* **Cloudflare R2 글로벌 CDN 스트리밍**:
  * 127MB 고화질 비디오를 Cloudflare R2 무제한 대역폭 CDN에 분산 배치
  * 일반 웹호스팅(카페24 등)의 일일 트래픽 초과 차단 위험 0% 실현
  * HTTP 206 Partial Content 스트리밍 지원으로 버퍼링 없는 고속 로딩
* **모바일 및 아이폰(iOS) 표준 UX 적용**:
  * 기기 볼륨 제약 대응: 모바일 환경에서는 화면 슬라이더를 숨기고 **'유튜브 모바일 스타일 원클릭 음소거(🔊/🔇) 토글'** 제공
  * 단독 골드 원형 재생 버튼 및 화면 터치 시 소리와 함께 즉시 시작
  * 화면 좌/우 더블탭 시 **±10초 부드러운 스킵 리플 애니메이션**
  * PC 환경: 키보드 단축키 지원 (Space/K: 재생·정지, J/L: 10초 스킵, M: 음소거, F: 전체화면)

### 3. 브랜드 아이덴티티 및 아이콘 시스템
* `logo2.png` 좌측의 상징적인 **완위각 전통 한옥 기와집 심볼**을 기반으로 파비콘 및 앱 아이콘 구축
* 라이트/다크 모드 탭 시인성 보장을 위한 골드 라운드 배지 디자인
* 멀티 규격 지원: `favicon.ico`, `favicon.png`, `apple-touch-icon.png` (180×180), `icon-192.png`, `icon-512.png`

---

## 📂 디렉토리 구조

```text
QRwebpage/
├── webhosting/                     # 카페24 등 웹호스팅 배포용 루트 디렉토리
│   ├── page1.html ~ page9.html     # 전시 코너별 모바일 웹페이지
│   ├── video.html                  # 메인 비디오 스트리밍 플레이어 페이지
│   ├── favicon.ico                 # 16/32/48px 멀티사이즈 브라우저 파비콘
│   ├── favicon.png                 # 고해상도 탭 아이콘
│   ├── apple-touch-icon.png        # iOS/사파리 홈 화면 바로가기 아이콘 (180x180)
│   ├── css/
│   │   ├── style.css               # 전시 상세 페이지 공통 스타일시트
│   │   └── video-player.css        # 프리미엄 골드 비디오 플레이어 전용 CSS
│   ├── js/
│   │   ├── main.js                 # 전시 상세 페이지 인터랙션 스크립트
│   │   └── video-player.js         # 비디오 플레이어 제어 스크립트
│   ├── fonts/                      # KoPubWorld 돋움 WOFF2 웹폰트
│   └── images/                     # 전시 유물 이미지, WebP 최적화 에셋, 파비콘 세트
│       └── video_poster.jpg        # 비디오 시작 전 대표 고화질 스틸컷
├── qrimage/                        # 인쇄 및 리플렛용 QR 코드 원본 파일 (EPS, ZIP)
├── .gitignore                      # 대용량 미디어 파일(100MB+) 제외 설정
└── README.md                       # 프로젝트 문서
```

---

## 🚀 배포 가이드 (카페24 웹호스팅 기준)

1. **FTP 접속**: 카페24 호스팅 계정의 `www/` (또는 `html/`) 디렉토리에 접속합니다.
2. **업로드**: `webhosting/` 폴더 안의 모든 파일과 하위 폴더(`css`, `js`, `images`, `fonts`, `.html` 등)를 웹 루트에 업로드합니다.
3. **비디오 파일 안내**:
   * 비디오는 이미 `https://pub-db7a586363374e9981ce418e457ebcbe.r2.dev/jin01.mp4` CDN으로 자동 연결되어 있으므로, 127MB 크기의 비디오 파일을 웹호스팅 FTP에 별도로 올리실 필요가 없습니다.

---

## 🛠 기술 스택

* **Frontend**: HTML5, CSS3 (Custom Properties), Vanilla JavaScript (ES6+)
* **Media Streaming**: Cloudflare R2 Object Storage (Global CDN)
* **Design & Typography**: KoPubWorld Dotum, Custom Wanwigak Gold Theme
* **Encoding & Media**: HandBrake (Web Optimized H.264/AAC), FFmpeg

---

## 📄 라이선스

본 프로젝트의 디자인 및 콘텐츠 자산의 저작권은 **꿈씨디자인**과 **진천 초평책마을**에 있습니다.
