#!/usr/bin/env bash
rm -f *.json
echo "dataTotal = [" >> data_total.json
echo "dataMonth = [" >> data_month.json
cp each_commit.sh _each_commit.sh
git rebase --exec "bash _each_commit.sh" 56867ce &>/dev/null
echo "[null, null]]" >> data_total.json
echo "[null, null]]" >> data_month.json
rm _each_commit.sh
