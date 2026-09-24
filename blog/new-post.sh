#!/usr/bin/env bash
# 用法: ./new-post.sh <分类目录名> <文章标题> [英文slug]
# 示例: ./new-post.sh java "Java 日期时间用法"
set -euo pipefail
cd "$(dirname "$0")"

CAT="${1:?用法: ./new-post.sh <分类目录名> <文章标题> [英文slug]}"
TITLE="${2:?缺少标题}"
SLUG="${3:-}"
DATE=$(date +%F)

if [ -z "$SLUG" ]; then
  if [[ "$TITLE" =~ ^[A-Za-z0-9\ _-]+$ ]]; then
    SLUG=$(echo "$TITLE" | tr 'A-Z ' 'a-z-' | tr -s '-')
  else
    SLUG="$DATE"
  fi
fi

FILE="docs/$CAT/$SLUG.md"
mkdir -p "docs/$CAT"

cat > "$FILE" <<EOF
---
title: $TITLE
date: $DATE
tags: []
---

# $TITLE

EOF

if [ -f "docs/$CAT/index.md" ]; then
  LINK="- [$TITLE](/$CAT/$SLUG) — $DATE"
  sed -i "/<!-- POSTS -->/a\\
$LINK" "docs/$CAT/index.md"
fi

echo "已创建: $FILE"
echo "本地预览: npm run docs:dev"
