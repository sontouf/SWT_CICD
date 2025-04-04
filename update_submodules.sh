#!/bin/bash
echo "📦 서브모듈 최신 커밋으로 업데이트 중..."

cd "$(dirname "$0")"

# TeamA 최신화
cd SWT_TeamA
git checkout main
git pull origin main
cd ..

# TeamB 최신화
cd SWT_TeamB
git checkout main
git pull origin main
cd ..

# 변경된 submodule 커밋들을 상위에 반영 (선택)
git add SWT_TeamA SWT_TeamB
git commit -m "🔄 Update submodules to latest commit" || echo "No submodule updates to commit."
git push
