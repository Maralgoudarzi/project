var chart = c3.generate({
    bindto:'#chart1',
    data: {
        // iris data from R
        columns: [
            ['F', 175], 
            ['M', 305],
            
        ],
        type : 'pie',
       
    }
});