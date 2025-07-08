# Week 1 - 알고리즘 & Python 기초

## ✅ 오늘 배운 내용 요약 (2025.07.08)

### 📌 백준 문제 풀이
- [x] 스택 구현 (10828)
- [x] 큐 구현 (18258)

### 📚 Python 문법 및 표준 입출력
- `input()`보다 `sys.stdin.readline()`이 훨씬 빠르다.
- 출력은 `print()` 대신 리스트에 `append()` 후 마지막에 `"\n".join()`으로 출력하면 시간 절약 가능.

### 🧠 자료구조 최적화 팁
- 스택/큐 구현 시 리스트보다는 `collections.deque`를 사용하는 게 효율적이다.
  - `list.pop(0)`은 O(N), `deque.popleft()`는 O(1)
  - `if queue:` 조건문은 큐가 비어있지 않을 때 True

### 💡 Git 사용법
- `git clone <url>`로 내 컴퓨터로 복사
- `cd`로 원하는 폴더 이동
- `git add`, `commit`, `push`로 변경사항 GitHub에 업로드

### ❗ 오류 및 해결
- `strip()` 오타: `satrip()` → `strip()` 으로 수정
- 출력이 안 됐던 이유: `print("\n".join(output))` 빠뜨림
- `RuntimeError`는 보통 오타/빈 입력 처리 문제로 발생

---

## 🗂️ 폴더 구성
- `10828_stack.py` : 스택 직접 구현
- `18258_queue.py` : `deque` 이용한 큐 구현
