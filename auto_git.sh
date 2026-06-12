#!/usr/bin/env bash
set -e
export GIT_SSH_COMMAND="ssh -i ~/.ssh/id_ed25519"

msg="$*"

if [ -z "$msg" ]; then
  read -r -p "请输入提交名称: " msg
fi

git add -- \
  .gitattributes \
  .gitignore \
  auto_git.sh \
  光伏原理 \
  光电子学 \
  半导体物理 \
  单片机 \
  电子材料 \
  纳米材料 \
  集成电路制造 \
  集成电路设计 \
  AGENTS.md \
  AI复习指南.md \
  BSPDN课程设计

if ! git diff --cached --quiet; then
  git commit -m "$msg"
fi

git push
