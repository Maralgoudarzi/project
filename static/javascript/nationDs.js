var chart = c3.generate({
    bindto:'#chart2',
    data: {
        // iris data from R
        columns: [
            ['Egypt', 9], 
            ['Iran', 6],
            [ 'Iraq', 22],
            ['Jordan', 172],
            ['KW', 179],
            ['Lebanon', 17],
            ['Lybia', 6],
            ['Morocco', 4],
            ['Palestine', 28],
            [ 'SaudiArabia', 11],
            ['Syria', 7],
            ['Tunis', 12],
            ['USA', 6],
            ['Venzuela', 1],
        ],
        type : 'pie',
       
    }
});