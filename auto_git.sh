#!/usr/bin/env bash
set -e

msg="$*"

if [ -z "$msg" ]; then
  read -r -p "请输入提交名称: " msg
fi

git add -- \
  .gitignore \
  auto_git.sh \
  光伏原理 \
  光电子学 \
  半导体物理 \
  单片机 \
  电子材料 \
  纳米材料 \
  集成电路制造

if git diff --cached --quiet; then
  echo "没有需要提交的改动。"
  exit 0
fi

git commit -m "$msg"

if git remote get-url origin >/dev/null 2>&1; then
  git push
else
  echo "未配置远程仓库，已完成本地提交。"
fi
