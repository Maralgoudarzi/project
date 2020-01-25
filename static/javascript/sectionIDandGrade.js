var chart = c3.generate({
    bindto:'#chart3',
    data: {
        columns: [
            ['L', 71,48,8],
            ['M', 128,66,17,]
            
        ],
        type: 'bar'
    },
    axis: {
        x: {
            type: 'category',
            categories: ['A', 'B', 'C', ]
        }
    }
});

    setTimeout(function () {
    chart.load({
        columns: [
            ['H', 84,53,5]
        ]
    });
}, 1000);