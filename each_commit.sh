#!/usr/bin/env bash
date=$(git show -s --format=%ct)000
data=$(grep -ie download -e stars README.md | grep -Eo '[0-9,]+' | sed 's/,//g' | tr '\n' ' ')
read total month stars <<<"${data}"
[ -n "${total}" ] && echo "[${date}, ${total}]," >> data_total.json
[ -n "${month}" ] && echo "[${date}, ${month}]," >> data_month.json
exit 0
