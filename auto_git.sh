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
git commit -m "$msg"
git push