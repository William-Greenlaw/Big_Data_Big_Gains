def apply_golden_range(f: go.FigureWidget) -> go.FigureWidget:
    '''
    If a line chart's axis doesn't start at 0, make 33% of the
    plot's y-axis space blank space. If the new minimum y-axis value
    becomes negative to fit the golden ratio and the old minimum y-axis
    value wasn't, then set y-axis minimum to 0. 
    
    This logic supports a design
    decision where if the chart's minimum is great than 0, the function
    assumes it does not make sense to use y values less than 0. For example, 
    in the case of lifting weights, one can lift little enough volume to 
    make setting a "golden range" require negative y-axis labelling, but
    entertaining negative numbers doesn't make sense since one cannot lift
    negative weight. In that case, setting the y-axis to 0 makes the best 
    use of space to ameliorate concerns with truncating y-axis ranges.
    
    Math:
    
    For a "golden range", the distance between the minimum data point 
    and the minimum y-axis value is one third the height of the entire
    plotting area, which is distance between the maximum y-axis value 
    and the minimum y-axis value:
    
    (min_data - min_y_range) = (max_y_range - min_y_range) / 3
    
    *transform equation*
    
    min_y_range =  (3 * min_data - max_y_range) / 2
    
    See discussion of fair y-axis ranges here: https://www.chezvoila.com/blog/yaxis
    
    This function relies on plotly automatically choosing the maximum y-axis value
    of a figure and simply changes the minimum y-axis value to make it conform
    to the golden ratio.
    '''
    
    if f.layout.yaxis.range[0] != 0:
        # get minimum y-axis data point of all the traces in the figure
        min_data = min([min(trace.y) for trace in f.data])
        
        # get current minimum and maxiumum y-axis range
        max_y_range = f.layout.yaxis.range[1]
        original_y_min = f.layout.yaxis.range[0]
        
        # get minimum y-axis range value to conform to golden ratio
        min_y_range = (3 * min_data - max_y_range) / 2
        
        # If the new minimum y-axis value is negative and the old minimum y-axis
        # value wasn't, then set y-axis minimum to 0
        if min_y_range < 0 and original_y_min > 0:
            min_y_range = 0
        
        # set new y-axis range
        f.layout.yaxis.range = [min_y_range, max_y_range]
    
    return f