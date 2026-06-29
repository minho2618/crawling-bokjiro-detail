# crawling-bokjiro-detail

이 프로젝트는 Selenium을 사용하여 복지로(Bokjiro) 웹사이트의 상세 정보를 크롤링하기 위한 프로젝트입니다.

## 시작하기

본 프로젝트는 의존성 관리 및 가상환경 구축을 위해 [uv](https://github.com/astral-sh/uv)를 사용합니다.

### 1. 가상환경 활성화
가상환경은 프로젝트 내 `.venv` 폴더에 생성되어 있습니다. 먼저 가상환경을 활성화합니다.

**Windows (PowerShell):**
```powershell
.venv\Scripts\activate
```

### 2. 패키지 설치 확인 (선택 사항)
패키지는 이미 `uv`를 통해 설치되어 있습니다. (Selenium, Webdriver Manager 등)
만약 다른 환경에서 패키지를 다시 설치해야 한다면 아래 명령어를 사용하세요.

```powershell
uv pip install -r requirements.txt  # (추후 requirements.txt가 생성될 경우)
# 또는
uv pip install selenium webdriver-manager
```

### 3. 크롤러 실행
스크립트를 실행하려면 다음 명령어를 입력하세요:

```powershell
python main.py
```

*또는 가상환경을 직접 활성화하지 않고 `uv run`을 사용해서 곧바로 실행할 수도 있습니다:*
```powershell
uv run main.py
```

## 주요 파일 설명
- `main.py`: 크롤링을 수행하는 메인 스크립트 파일입니다.
- `.gitignore`: Git 버전 관리 시 무시할 파일(가상환경, 임시 파일, 설정 파일 등)을 정의합니다.
