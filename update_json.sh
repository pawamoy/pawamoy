#!/usr/bin/env bash
rm -f *.json
echo "dataTotal = [" >> data_total.json
echo "dataMonth = [" >> data_month.json
git rebase --exec "bash each_commit.sh" 56867ce &>/dev/null
echo "[null, null]]" >> data_total.json
echo "[null, null]]" >> data_month.json