#!/usr/bin/env bash
exec > charts.html
echo '<div id="containerMonth"></div>'
echo '<div id="containerTotal"></div>'
echo '<script src="https://code.highcharts.com/highcharts.js"></script><script>'
bash update_json.sh
cat *.json
echo 'dataMonth.pop();'
echo 'dataTotal.pop();'
cat chart.js
echo '</script>'
rm -f *.json
