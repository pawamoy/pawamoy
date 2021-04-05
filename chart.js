subtitle = {
    text: document.ontouchstart === undefined ?
        'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
}
plotOptions = {
    area: {
        fillColor: {
            linearGradient: {x1: 0, y1: 0, x2: 0, y2: 1},
            stops: [
                [0, Highcharts.getOptions().colors[0]],
                [1, Highcharts.color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
            ]
        },
        marker: {radius: 2},
        lineWidth: 1,
        states: {hover: {lineWidth: 1}},
        threshold: null
    }
}

Highcharts.chart('containerMonth', {
    chart: {zoomType: 'x'},
    title: {text: 'Ego'},
    subtitle: subtitle,
    xAxis: {type: 'datetime'},
    yAxis: {title: {text: 'Number'}},
    legend: {enabled: false},
    plotOptions: plotOptions,
    series: [{
        type: 'area',
        name: 'Downloads per month',
        data: dataMonth
    }]
});

Highcharts.chart('containerTotal', {
    chart: {zoomType: 'x'},
    title: {text: 'Ego'},
    subtitle: subtitle,
    xAxis: {type: 'datetime'},
    yAxis: {title: {text: 'Number'}},
    legend: {enabled: false},
    plotOptions: plotOptions,
    series: [{
        type: 'area',
        name: 'Total downloads',
        data: dataTotal
    }]
});